(*
 * Copyright (c) 2019, Facebook, Inc.
 * All rights reserved.
 *
 * This source code is licensed under the MIT license found in the
 * LICENSE file in the "hack" directory of this source tree.
 *
 *)
open Hh_prelude
open SearchUtils
open SearchTypes

(* How many locally changed files are in this env? *)
let count_local_fileinfos ~(sienv : si_env) : int =
  Relative_path.Map.cardinal sienv.lss_fullitems

(* Relative paths sometimes produce doubled-up slashes, as in
 * "/path/to/root//subpath/file".  When we extract the suffix
 * from a relative_path.t, clear out any preceding slash. *)
let strip_first_char char s =
  if String.length s = 0 || not (Char.equal s.[0] char) then
    s
  else
    String.sub s ~pos:1 ~len:(String.length s - 1)

(* Determine a tombstone for a file path *)
let get_tombstone (path : Relative_path.t) : int64 =
  let rel_path_str = Relative_path.suffix path in
  let fixed_path_str = strip_first_char '/' rel_path_str in
  let path_hash = SharedMemHash.hash_string fixed_path_str in
  path_hash

(* This function is used if fast-facts-parser fails to scan the file *)
let convert_fileinfo_to_contents
    ~(ctx : Provider_context.t)
    ~(sienv : SearchUtils.si_env)
    ~(info : FileInfo.t)
    ~(filepath : string) : SearchUtils.si_capture =
  let append_item
      (kind : SearchTypes.si_kind)
      (acc : SearchUtils.si_capture)
      (name : string) =
    let (sif_kind, sif_is_abstract, sif_is_final) =
      (* FFP produces more detailed information about classes
       * than we can get from FileInfo.t objects.  Since this function is only
       * called when a file has been modified locally, it's safe to call
       * decl_provider - this information has already been cached. *)
      if is_si_class kind && sienv.sie_resolve_local_decl then
        match Decl_provider.get_class ctx name with
        | Some cls ->
          let is_final = Decl_provider.Class.final cls in
          let is_abstract = Decl_provider.Class.abstract cls in
          let real_kind = Decl_provider.Class.kind cls in
          let converted_kind =
            match real_kind with
            | Ast_defs.Cclass _ -> SI_Class
            | Ast_defs.Cinterface -> SI_Interface
            | Ast_defs.Ctrait -> SI_Trait
            | Ast_defs.Cenum_class _
            | Ast_defs.Cenum ->
              SI_Enum
          in
          (converted_kind, is_abstract, is_final)
        | None -> (kind, false, false)
      else
        (kind, false, false)
    in
    let item =
      {
        (* Only strip Hack namespaces. XHP must have a preceding colon *)
        sif_name = Utils.strip_ns name;
        sif_kind;
        sif_filepath = filepath;
        sif_is_abstract;
        sif_is_final;
      }
    in
    item :: acc
  in
  let fold_full
      (kind : SearchTypes.si_kind)
      (acc : SearchUtils.si_capture)
      (list : FileInfo.id list) : SearchUtils.si_capture =
    List.fold list ~init:acc ~f:(fun inside_acc (_, name, _) ->
        append_item kind inside_acc name)
  in
  let acc = fold_full SI_Function [] info.FileInfo.funs in
  let acc = fold_full SI_Class acc info.FileInfo.classes in
  let acc = fold_full SI_Typedef acc info.FileInfo.typedefs in
  let acc = fold_full SI_GlobalConstant acc info.FileInfo.consts in
  acc

(* Update files when they were discovered *)
let update_file
    ~(ctx : Provider_context.t)
    ~(sienv : si_env)
    ~(path : Relative_path.t)
    ~(info : FileInfo.t) : si_env =
  let tombstone = get_tombstone path in
  let filepath = Relative_path.suffix path in
  let contents =
    try
      let full_filename = Relative_path.to_absolute path in
      if Sys.file_exists full_filename then
        let popt = Provider_context.get_popt ctx in
        let namespace_map = ParserOptions.auto_namespace_map popt in
        let contents = IndexBuilder.parse_one_file ~namespace_map ~path in
        if List.is_empty contents then
          convert_fileinfo_to_contents ~ctx ~sienv ~info ~filepath
        else
          contents
      else
        convert_fileinfo_to_contents ~ctx ~sienv ~info ~filepath
    with
    | _ -> convert_fileinfo_to_contents ~ctx ~sienv ~info ~filepath
  in
  {
    sienv with
    lss_fullitems =
      Relative_path.Map.add sienv.lss_fullitems ~key:path ~data:contents;
    lss_tombstones = Relative_path.Set.add sienv.lss_tombstones path;
    lss_tombstone_hashes =
      Tombstone_set.add sienv.lss_tombstone_hashes tombstone;
  }

let update_file_from_addenda
    ~(sienv : si_env)
    ~(path : Relative_path.t)
    ~(addenda : SearchTypes.si_addendum list) : si_env =
  let tombstone = get_tombstone path in
  let filepath = Relative_path.suffix path in
  let contents : SearchUtils.si_capture =
    List.map addenda ~f:(fun addendum ->
        {
          sif_name = addendum.sia_name;
          sif_kind = addendum.sia_kind;
          sif_filepath = filepath;
          sif_is_abstract = addendum.sia_is_abstract;
          sif_is_final = addendum.sia_is_final;
        })
  in
  {
    sienv with
    lss_fullitems =
      Relative_path.Map.add sienv.lss_fullitems ~key:path ~data:contents;
    lss_tombstones = Relative_path.Set.add sienv.lss_tombstones path;
    lss_tombstone_hashes =
      Tombstone_set.add sienv.lss_tombstone_hashes tombstone;
  }

(* Remove files from local when they are deleted *)
let remove_file ~(sienv : si_env) ~(path : Relative_path.t) : si_env =
  let tombstone = get_tombstone path in
  {
    sienv with
    lss_fullitems = Relative_path.Map.remove sienv.lss_fullitems path;
    lss_tombstones = Relative_path.Set.add sienv.lss_tombstones path;
    lss_tombstone_hashes =
      Tombstone_set.add sienv.lss_tombstone_hashes tombstone;
  }

(* Exception we use to short-circuit out of a loop if we find enough results.
 * May be worth rewriting this in the future to use `fold_until` rather than
 * exceptions *)
exception BreakOutOfScan of si_item list

(* Search local changes for symbols matching this prefix *)
let search_local_symbols
    ~(sienv : si_env)
    ~(query_text : string)
    ~(max_results : int)
    ~(context : autocomplete_type)
    ~(kind_filter : si_kind option) : si_item list =
  (* case insensitive search, must include namespace, escaped for regex *)
  let query_text_regex_case_insensitive =
    Str.regexp_case_fold (Str.quote query_text)
  in
  (* case insensitive search, break out if max results reached *)
  let check_symbol_and_add_to_accumulator_and_break_if_max_reached
      ~(acc : si_item list)
      ~(symbol : si_fullitem)
      ~(context : autocomplete_type)
      ~(kind_filter : si_kind option)
      ~(path : Relative_path.t) : si_item list =
    let is_valid_match =
      match (context, kind_filter) with
      | (Actype, _) -> SearchTypes.valid_for_actype symbol.SearchUtils.sif_kind
      | (Acnew, _) ->
        SearchTypes.valid_for_acnew symbol.SearchUtils.sif_kind
        && not symbol.SearchUtils.sif_is_abstract
      | (Acid, _) -> SearchTypes.valid_for_acid symbol.SearchUtils.sif_kind
      | (Actrait_only, _) -> is_si_trait symbol.sif_kind
      | (Ac_workspace_symbol, Some kind_match) ->
        equal_si_kind symbol.sif_kind kind_match
      | (Ac_workspace_symbol, None) -> true
    in
    if
      is_valid_match
      && Str.string_partial_match
           query_text_regex_case_insensitive
           symbol.sif_name
           0
    then
      (* Only strip Hack namespaces. XHP must have a preceding colon *)
      let fullname = Utils.strip_ns symbol.sif_name in
      let acc_new =
        {
          si_name = fullname;
          si_kind = symbol.sif_kind;
          si_file = SI_Path path;
          si_fullname = fullname;
        }
        :: acc
      in
      if List.length acc_new >= max_results then
        raise (BreakOutOfScan acc_new)
      else
        acc_new
    else
      acc
  in
  try
    let acc =
      Relative_path.Map.fold
        sienv.lss_fullitems
        ~init:[]
        ~f:(fun path fullitems acc ->
          let matches =
            List.fold fullitems ~init:[] ~f:(fun acc symbol ->
                check_symbol_and_add_to_accumulator_and_break_if_max_reached
                  ~acc
                  ~symbol
                  ~context
                  ~kind_filter
                  ~path)
          in
          List.append acc matches)
    in
    acc
  with
  | BreakOutOfScan acc -> acc

(* Filter the results to extract any dead objects *)
let extract_dead_results ~(sienv : SearchUtils.si_env) ~(results : si_item list)
    : si_item list =
  List.filter results ~f:(fun item ->
      match item.si_file with
      | SearchTypes.SI_Path path ->
        not (Relative_path.Set.mem sienv.lss_tombstones path)
      | SearchTypes.SI_Filehash hash_str ->
        let hash = Int64.of_string hash_str in
        not (Tombstone_set.mem sienv.lss_tombstone_hashes hash))
