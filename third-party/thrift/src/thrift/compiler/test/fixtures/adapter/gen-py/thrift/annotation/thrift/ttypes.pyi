#
# Autogenerated by Thrift
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#  @generated
#

# pyre-unsafe

import typing as __T  # sometimes `t` is used as a field name

from thrift import Thrift
from thrift.protocol.TProtocol import TProtocolBase

__property__ = property  # sometimes `property` is used as a field name


UTF8STRINGS: bool


class Beta:
    thrift_spec: __T.Tuple[__T.Optional[__T.Tuple[int, int, str, __T.Any, __T.Optional[int], int]]]
    thrift_field_annotations: __T.Dict[int, __T.Dict[str, str]]
    thrift_struct_annotations: __T.Dict[str, str]

    def __init__(
        self
    ) -> None:
        ...



    def isUnion(self) -> bool: ...
    def checkRequired(self) -> None: ...
    def read(self, iprot: TProtocolBase) -> None: ...
    @__T.overload
    def readFromJson(self, json: __T.Dict[str, __T.Any], is_text: bool = ..., **kwargs: __T.Any) -> None: ...
    @__T.overload
    def readFromJson(self, json: str, is_text: bool = ..., **kwargs: __T.Any) -> None: ...
    def write(self, oprot: TProtocolBase) -> None: ...
    def __eq__(self, other: __T.Any) -> bool: ...
    def __ne__(self, other: __T.Any) -> bool: ...
    def __dir__(self) -> __T.Sequence[str]: ...
    def _to_python(self) -> "facebook.thrift.annotation.thrift.thrift_types.Beta": ...   # type: ignore
    def _to_py3(self) -> "facebook.thrift.annotation.thrift.types.Beta": ...   # type: ignore
    def _to_py_deprecated(self) -> Beta: ...


class Experimental:
    thrift_spec: __T.Tuple[__T.Optional[__T.Tuple[int, int, str, __T.Any, __T.Optional[int], int]]]
    thrift_field_annotations: __T.Dict[int, __T.Dict[str, str]]
    thrift_struct_annotations: __T.Dict[str, str]

    def __init__(
        self
    ) -> None:
        ...



    def isUnion(self) -> bool: ...
    def checkRequired(self) -> None: ...
    def read(self, iprot: TProtocolBase) -> None: ...
    @__T.overload
    def readFromJson(self, json: __T.Dict[str, __T.Any], is_text: bool = ..., **kwargs: __T.Any) -> None: ...
    @__T.overload
    def readFromJson(self, json: str, is_text: bool = ..., **kwargs: __T.Any) -> None: ...
    def write(self, oprot: TProtocolBase) -> None: ...
    def __eq__(self, other: __T.Any) -> bool: ...
    def __ne__(self, other: __T.Any) -> bool: ...
    def __dir__(self) -> __T.Sequence[str]: ...
    def _to_python(self) -> "facebook.thrift.annotation.thrift.thrift_types.Experimental": ...   # type: ignore
    def _to_py3(self) -> "facebook.thrift.annotation.thrift.types.Experimental": ...   # type: ignore
    def _to_py_deprecated(self) -> Experimental: ...


class Testing:
    thrift_spec: __T.Tuple[__T.Optional[__T.Tuple[int, int, str, __T.Any, __T.Optional[int], int]]]
    thrift_field_annotations: __T.Dict[int, __T.Dict[str, str]]
    thrift_struct_annotations: __T.Dict[str, str]

    def __init__(
        self
    ) -> None:
        ...



    def isUnion(self) -> bool: ...
    def checkRequired(self) -> None: ...
    def read(self, iprot: TProtocolBase) -> None: ...
    @__T.overload
    def readFromJson(self, json: __T.Dict[str, __T.Any], is_text: bool = ..., **kwargs: __T.Any) -> None: ...
    @__T.overload
    def readFromJson(self, json: str, is_text: bool = ..., **kwargs: __T.Any) -> None: ...
    def write(self, oprot: TProtocolBase) -> None: ...
    def __eq__(self, other: __T.Any) -> bool: ...
    def __ne__(self, other: __T.Any) -> bool: ...
    def __dir__(self) -> __T.Sequence[str]: ...
    def _to_python(self) -> "facebook.thrift.annotation.thrift.thrift_types.Testing": ...   # type: ignore
    def _to_py3(self) -> "facebook.thrift.annotation.thrift.types.Testing": ...   # type: ignore
    def _to_py_deprecated(self) -> Testing: ...


class ReserveIds:
    thrift_spec: __T.Tuple[__T.Optional[__T.Tuple[int, int, str, __T.Any, __T.Optional[int], int]]]
    thrift_field_annotations: __T.Dict[int, __T.Dict[str, str]]
    thrift_struct_annotations: __T.Dict[str, str]

    def __init__(
        self,
        ids: __T.Optional[__T.List[int]] = ...,
        id_ranges: __T.Optional[__T.Dict[int, int]] = ...
    ) -> None:
        ...

    @__property__
    def ids(self) -> __T.List[int]: ...
    @ids.setter
    def ids(self, value: __T.Optional[__T.List[int]]) -> None: ...
    @__property__
    def id_ranges(self) -> __T.Dict[int, int]: ...
    @id_ranges.setter
    def id_ranges(self, value: __T.Optional[__T.Dict[int, int]]) -> None: ...


    def isUnion(self) -> bool: ...
    def checkRequired(self) -> None: ...
    def read(self, iprot: TProtocolBase) -> None: ...
    @__T.overload
    def readFromJson(self, json: __T.Dict[str, __T.Any], is_text: bool = ..., **kwargs: __T.Any) -> None: ...
    @__T.overload
    def readFromJson(self, json: str, is_text: bool = ..., **kwargs: __T.Any) -> None: ...
    def write(self, oprot: TProtocolBase) -> None: ...
    def __eq__(self, other: __T.Any) -> bool: ...
    def __ne__(self, other: __T.Any) -> bool: ...
    def __dir__(self) -> __T.Sequence[str]: ...
    def _to_python(self) -> "facebook.thrift.annotation.thrift.thrift_types.ReserveIds": ...   # type: ignore
    def _to_py3(self) -> "facebook.thrift.annotation.thrift.types.ReserveIds": ...   # type: ignore
    def _to_py_deprecated(self) -> ReserveIds: ...


class RequiresBackwardCompatibility:
    thrift_spec: __T.Tuple[__T.Optional[__T.Tuple[int, int, str, __T.Any, __T.Optional[int], int]]]
    thrift_field_annotations: __T.Dict[int, __T.Dict[str, str]]
    thrift_struct_annotations: __T.Dict[str, str]

    def __init__(
        self,
        field_name: bool = ...
    ) -> None:
        ...

    @__property__
    def field_name(self) -> bool: ...
    @field_name.setter
    def field_name(self, value: bool) -> None: ...


    def isUnion(self) -> bool: ...
    def checkRequired(self) -> None: ...
    def read(self, iprot: TProtocolBase) -> None: ...
    @__T.overload
    def readFromJson(self, json: __T.Dict[str, __T.Any], is_text: bool = ..., **kwargs: __T.Any) -> None: ...
    @__T.overload
    def readFromJson(self, json: str, is_text: bool = ..., **kwargs: __T.Any) -> None: ...
    def write(self, oprot: TProtocolBase) -> None: ...
    def __eq__(self, other: __T.Any) -> bool: ...
    def __ne__(self, other: __T.Any) -> bool: ...
    def __dir__(self) -> __T.Sequence[str]: ...
    def _to_python(self) -> "facebook.thrift.annotation.thrift.thrift_types.RequiresBackwardCompatibility": ...   # type: ignore
    def _to_py3(self) -> "facebook.thrift.annotation.thrift.types.RequiresBackwardCompatibility": ...   # type: ignore
    def _to_py_deprecated(self) -> RequiresBackwardCompatibility: ...


class NoTesting:
    thrift_spec: __T.Tuple[__T.Optional[__T.Tuple[int, int, str, __T.Any, __T.Optional[int], int]]]
    thrift_field_annotations: __T.Dict[int, __T.Dict[str, str]]
    thrift_struct_annotations: __T.Dict[str, str]

    def __init__(
        self
    ) -> None:
        ...



    def isUnion(self) -> bool: ...
    def checkRequired(self) -> None: ...
    def read(self, iprot: TProtocolBase) -> None: ...
    @__T.overload
    def readFromJson(self, json: __T.Dict[str, __T.Any], is_text: bool = ..., **kwargs: __T.Any) -> None: ...
    @__T.overload
    def readFromJson(self, json: str, is_text: bool = ..., **kwargs: __T.Any) -> None: ...
    def write(self, oprot: TProtocolBase) -> None: ...
    def __eq__(self, other: __T.Any) -> bool: ...
    def __ne__(self, other: __T.Any) -> bool: ...
    def __dir__(self) -> __T.Sequence[str]: ...
    def _to_python(self) -> "facebook.thrift.annotation.thrift.thrift_types.NoTesting": ...   # type: ignore
    def _to_py3(self) -> "facebook.thrift.annotation.thrift.types.NoTesting": ...   # type: ignore
    def _to_py_deprecated(self) -> NoTesting: ...


class NoExperimental:
    thrift_spec: __T.Tuple[__T.Optional[__T.Tuple[int, int, str, __T.Any, __T.Optional[int], int]]]
    thrift_field_annotations: __T.Dict[int, __T.Dict[str, str]]
    thrift_struct_annotations: __T.Dict[str, str]

    def __init__(
        self
    ) -> None:
        ...



    def isUnion(self) -> bool: ...
    def checkRequired(self) -> None: ...
    def read(self, iprot: TProtocolBase) -> None: ...
    @__T.overload
    def readFromJson(self, json: __T.Dict[str, __T.Any], is_text: bool = ..., **kwargs: __T.Any) -> None: ...
    @__T.overload
    def readFromJson(self, json: str, is_text: bool = ..., **kwargs: __T.Any) -> None: ...
    def write(self, oprot: TProtocolBase) -> None: ...
    def __eq__(self, other: __T.Any) -> bool: ...
    def __ne__(self, other: __T.Any) -> bool: ...
    def __dir__(self) -> __T.Sequence[str]: ...
    def _to_python(self) -> "facebook.thrift.annotation.thrift.thrift_types.NoExperimental": ...   # type: ignore
    def _to_py3(self) -> "facebook.thrift.annotation.thrift.types.NoExperimental": ...   # type: ignore
    def _to_py_deprecated(self) -> NoExperimental: ...


class NoBeta:
    thrift_spec: __T.Tuple[__T.Optional[__T.Tuple[int, int, str, __T.Any, __T.Optional[int], int]]]
    thrift_field_annotations: __T.Dict[int, __T.Dict[str, str]]
    thrift_struct_annotations: __T.Dict[str, str]

    def __init__(
        self
    ) -> None:
        ...



    def isUnion(self) -> bool: ...
    def checkRequired(self) -> None: ...
    def read(self, iprot: TProtocolBase) -> None: ...
    @__T.overload
    def readFromJson(self, json: __T.Dict[str, __T.Any], is_text: bool = ..., **kwargs: __T.Any) -> None: ...
    @__T.overload
    def readFromJson(self, json: str, is_text: bool = ..., **kwargs: __T.Any) -> None: ...
    def write(self, oprot: TProtocolBase) -> None: ...
    def __eq__(self, other: __T.Any) -> bool: ...
    def __ne__(self, other: __T.Any) -> bool: ...
    def __dir__(self) -> __T.Sequence[str]: ...
    def _to_python(self) -> "facebook.thrift.annotation.thrift.thrift_types.NoBeta": ...   # type: ignore
    def _to_py3(self) -> "facebook.thrift.annotation.thrift.types.NoBeta": ...   # type: ignore
    def _to_py_deprecated(self) -> NoBeta: ...


class Released:
    thrift_spec: __T.Tuple[__T.Optional[__T.Tuple[int, int, str, __T.Any, __T.Optional[int], int]]]
    thrift_field_annotations: __T.Dict[int, __T.Dict[str, str]]
    thrift_struct_annotations: __T.Dict[str, str]

    def __init__(
        self
    ) -> None:
        ...



    def isUnion(self) -> bool: ...
    def checkRequired(self) -> None: ...
    def read(self, iprot: TProtocolBase) -> None: ...
    @__T.overload
    def readFromJson(self, json: __T.Dict[str, __T.Any], is_text: bool = ..., **kwargs: __T.Any) -> None: ...
    @__T.overload
    def readFromJson(self, json: str, is_text: bool = ..., **kwargs: __T.Any) -> None: ...
    def write(self, oprot: TProtocolBase) -> None: ...
    def __eq__(self, other: __T.Any) -> bool: ...
    def __ne__(self, other: __T.Any) -> bool: ...
    def __dir__(self) -> __T.Sequence[str]: ...
    def _to_python(self) -> "facebook.thrift.annotation.thrift.thrift_types.Released": ...   # type: ignore
    def _to_py3(self) -> "facebook.thrift.annotation.thrift.types.Released": ...   # type: ignore
    def _to_py_deprecated(self) -> Released: ...


class TerseWrite:
    thrift_spec: __T.Tuple[__T.Optional[__T.Tuple[int, int, str, __T.Any, __T.Optional[int], int]]]
    thrift_field_annotations: __T.Dict[int, __T.Dict[str, str]]
    thrift_struct_annotations: __T.Dict[str, str]

    def __init__(
        self
    ) -> None:
        ...



    def isUnion(self) -> bool: ...
    def checkRequired(self) -> None: ...
    def read(self, iprot: TProtocolBase) -> None: ...
    @__T.overload
    def readFromJson(self, json: __T.Dict[str, __T.Any], is_text: bool = ..., **kwargs: __T.Any) -> None: ...
    @__T.overload
    def readFromJson(self, json: str, is_text: bool = ..., **kwargs: __T.Any) -> None: ...
    def write(self, oprot: TProtocolBase) -> None: ...
    def __eq__(self, other: __T.Any) -> bool: ...
    def __ne__(self, other: __T.Any) -> bool: ...
    def __dir__(self) -> __T.Sequence[str]: ...
    def _to_python(self) -> "facebook.thrift.annotation.thrift.thrift_types.TerseWrite": ...   # type: ignore
    def _to_py3(self) -> "facebook.thrift.annotation.thrift.types.TerseWrite": ...   # type: ignore
    def _to_py_deprecated(self) -> TerseWrite: ...


class Box:
    thrift_spec: __T.Tuple[__T.Optional[__T.Tuple[int, int, str, __T.Any, __T.Optional[int], int]]]
    thrift_field_annotations: __T.Dict[int, __T.Dict[str, str]]
    thrift_struct_annotations: __T.Dict[str, str]

    def __init__(
        self
    ) -> None:
        ...



    def isUnion(self) -> bool: ...
    def checkRequired(self) -> None: ...
    def read(self, iprot: TProtocolBase) -> None: ...
    @__T.overload
    def readFromJson(self, json: __T.Dict[str, __T.Any], is_text: bool = ..., **kwargs: __T.Any) -> None: ...
    @__T.overload
    def readFromJson(self, json: str, is_text: bool = ..., **kwargs: __T.Any) -> None: ...
    def write(self, oprot: TProtocolBase) -> None: ...
    def __eq__(self, other: __T.Any) -> bool: ...
    def __ne__(self, other: __T.Any) -> bool: ...
    def __dir__(self) -> __T.Sequence[str]: ...
    def _to_python(self) -> "facebook.thrift.annotation.thrift.thrift_types.Box": ...   # type: ignore
    def _to_py3(self) -> "facebook.thrift.annotation.thrift.types.Box": ...   # type: ignore
    def _to_py_deprecated(self) -> Box: ...


class Mixin:
    thrift_spec: __T.Tuple[__T.Optional[__T.Tuple[int, int, str, __T.Any, __T.Optional[int], int]]]
    thrift_field_annotations: __T.Dict[int, __T.Dict[str, str]]
    thrift_struct_annotations: __T.Dict[str, str]

    def __init__(
        self
    ) -> None:
        ...



    def isUnion(self) -> bool: ...
    def checkRequired(self) -> None: ...
    def read(self, iprot: TProtocolBase) -> None: ...
    @__T.overload
    def readFromJson(self, json: __T.Dict[str, __T.Any], is_text: bool = ..., **kwargs: __T.Any) -> None: ...
    @__T.overload
    def readFromJson(self, json: str, is_text: bool = ..., **kwargs: __T.Any) -> None: ...
    def write(self, oprot: TProtocolBase) -> None: ...
    def __eq__(self, other: __T.Any) -> bool: ...
    def __ne__(self, other: __T.Any) -> bool: ...
    def __dir__(self) -> __T.Sequence[str]: ...
    def _to_python(self) -> "facebook.thrift.annotation.thrift.thrift_types.Mixin": ...   # type: ignore
    def _to_py3(self) -> "facebook.thrift.annotation.thrift.types.Mixin": ...   # type: ignore
    def _to_py_deprecated(self) -> Mixin: ...


class SerializeInFieldIdOrder:
    thrift_spec: __T.Tuple[__T.Optional[__T.Tuple[int, int, str, __T.Any, __T.Optional[int], int]]]
    thrift_field_annotations: __T.Dict[int, __T.Dict[str, str]]
    thrift_struct_annotations: __T.Dict[str, str]

    def __init__(
        self
    ) -> None:
        ...



    def isUnion(self) -> bool: ...
    def checkRequired(self) -> None: ...
    def read(self, iprot: TProtocolBase) -> None: ...
    @__T.overload
    def readFromJson(self, json: __T.Dict[str, __T.Any], is_text: bool = ..., **kwargs: __T.Any) -> None: ...
    @__T.overload
    def readFromJson(self, json: str, is_text: bool = ..., **kwargs: __T.Any) -> None: ...
    def write(self, oprot: TProtocolBase) -> None: ...
    def __eq__(self, other: __T.Any) -> bool: ...
    def __ne__(self, other: __T.Any) -> bool: ...
    def __dir__(self) -> __T.Sequence[str]: ...
    def _to_python(self) -> "facebook.thrift.annotation.thrift.thrift_types.SerializeInFieldIdOrder": ...   # type: ignore
    def _to_py3(self) -> "facebook.thrift.annotation.thrift.types.SerializeInFieldIdOrder": ...   # type: ignore
    def _to_py_deprecated(self) -> SerializeInFieldIdOrder: ...


class BitmaskEnum:
    thrift_spec: __T.Tuple[__T.Optional[__T.Tuple[int, int, str, __T.Any, __T.Optional[int], int]]]
    thrift_field_annotations: __T.Dict[int, __T.Dict[str, str]]
    thrift_struct_annotations: __T.Dict[str, str]

    def __init__(
        self
    ) -> None:
        ...



    def isUnion(self) -> bool: ...
    def checkRequired(self) -> None: ...
    def read(self, iprot: TProtocolBase) -> None: ...
    @__T.overload
    def readFromJson(self, json: __T.Dict[str, __T.Any], is_text: bool = ..., **kwargs: __T.Any) -> None: ...
    @__T.overload
    def readFromJson(self, json: str, is_text: bool = ..., **kwargs: __T.Any) -> None: ...
    def write(self, oprot: TProtocolBase) -> None: ...
    def __eq__(self, other: __T.Any) -> bool: ...
    def __ne__(self, other: __T.Any) -> bool: ...
    def __dir__(self) -> __T.Sequence[str]: ...
    def _to_python(self) -> "facebook.thrift.annotation.thrift.thrift_types.BitmaskEnum": ...   # type: ignore
    def _to_py3(self) -> "facebook.thrift.annotation.thrift.types.BitmaskEnum": ...   # type: ignore
    def _to_py_deprecated(self) -> BitmaskEnum: ...


class ExceptionMessage:
    thrift_spec: __T.Tuple[__T.Optional[__T.Tuple[int, int, str, __T.Any, __T.Optional[int], int]]]
    thrift_field_annotations: __T.Dict[int, __T.Dict[str, str]]
    thrift_struct_annotations: __T.Dict[str, str]

    def __init__(
        self,
        field: __T.Optional[str] = ...
    ) -> None:
        ...

    @__property__
    def field(self) -> str: ...
    @field.setter
    def field(self, value: __T.Optional[str]) -> None: ...


    def isUnion(self) -> bool: ...
    def checkRequired(self) -> None: ...
    def read(self, iprot: TProtocolBase) -> None: ...
    @__T.overload
    def readFromJson(self, json: __T.Dict[str, __T.Any], is_text: bool = ..., **kwargs: __T.Any) -> None: ...
    @__T.overload
    def readFromJson(self, json: str, is_text: bool = ..., **kwargs: __T.Any) -> None: ...
    def write(self, oprot: TProtocolBase) -> None: ...
    def __eq__(self, other: __T.Any) -> bool: ...
    def __ne__(self, other: __T.Any) -> bool: ...
    def __dir__(self) -> __T.Sequence[str]: ...
    def _to_python(self) -> "facebook.thrift.annotation.thrift.thrift_types.ExceptionMessage": ...   # type: ignore
    def _to_py3(self) -> "facebook.thrift.annotation.thrift.types.ExceptionMessage": ...   # type: ignore
    def _to_py_deprecated(self) -> ExceptionMessage: ...


class GenerateRuntimeSchema:
    thrift_spec: __T.Tuple[__T.Optional[__T.Tuple[int, int, str, __T.Any, __T.Optional[int], int]]]
    thrift_field_annotations: __T.Dict[int, __T.Dict[str, str]]
    thrift_struct_annotations: __T.Dict[str, str]

    def __init__(
        self,
        name: __T.Optional[str] = ...
    ) -> None:
        ...

    @__property__
    def name(self) -> str: ...
    @name.setter
    def name(self, value: __T.Optional[str]) -> None: ...


    def isUnion(self) -> bool: ...
    def checkRequired(self) -> None: ...
    def read(self, iprot: TProtocolBase) -> None: ...
    @__T.overload
    def readFromJson(self, json: __T.Dict[str, __T.Any], is_text: bool = ..., **kwargs: __T.Any) -> None: ...
    @__T.overload
    def readFromJson(self, json: str, is_text: bool = ..., **kwargs: __T.Any) -> None: ...
    def write(self, oprot: TProtocolBase) -> None: ...
    def __eq__(self, other: __T.Any) -> bool: ...
    def __ne__(self, other: __T.Any) -> bool: ...
    def __dir__(self) -> __T.Sequence[str]: ...
    def _to_python(self) -> "facebook.thrift.annotation.thrift.thrift_types.GenerateRuntimeSchema": ...   # type: ignore
    def _to_py3(self) -> "facebook.thrift.annotation.thrift.types.GenerateRuntimeSchema": ...   # type: ignore
    def _to_py_deprecated(self) -> GenerateRuntimeSchema: ...


class InternBox:
    thrift_spec: __T.Tuple[__T.Optional[__T.Tuple[int, int, str, __T.Any, __T.Optional[int], int]]]
    thrift_field_annotations: __T.Dict[int, __T.Dict[str, str]]
    thrift_struct_annotations: __T.Dict[str, str]

    def __init__(
        self
    ) -> None:
        ...



    def isUnion(self) -> bool: ...
    def checkRequired(self) -> None: ...
    def read(self, iprot: TProtocolBase) -> None: ...
    @__T.overload
    def readFromJson(self, json: __T.Dict[str, __T.Any], is_text: bool = ..., **kwargs: __T.Any) -> None: ...
    @__T.overload
    def readFromJson(self, json: str, is_text: bool = ..., **kwargs: __T.Any) -> None: ...
    def write(self, oprot: TProtocolBase) -> None: ...
    def __eq__(self, other: __T.Any) -> bool: ...
    def __ne__(self, other: __T.Any) -> bool: ...
    def __dir__(self) -> __T.Sequence[str]: ...
    def _to_python(self) -> "facebook.thrift.annotation.thrift.thrift_types.InternBox": ...   # type: ignore
    def _to_py3(self) -> "facebook.thrift.annotation.thrift.types.InternBox": ...   # type: ignore
    def _to_py_deprecated(self) -> InternBox: ...


