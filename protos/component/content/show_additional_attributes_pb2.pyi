from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ShowType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SHOW_TYPE_UNSPECIFIED: _ClassVar[ShowType]
    SHOW_TYPE_SEASONAL: _ClassVar[ShowType]
    SHOW_TYPE_SEQUENTIAL: _ClassVar[ShowType]
SHOW_TYPE_UNSPECIFIED: ShowType
SHOW_TYPE_SEASONAL: ShowType
SHOW_TYPE_SEQUENTIAL: ShowType

class ShowAdditionalAttributes(_message.Message):
    __slots__ = ("is_btv", "show_type", "is_archived")
    IS_BTV_FIELD_NUMBER: _ClassVar[int]
    SHOW_TYPE_FIELD_NUMBER: _ClassVar[int]
    IS_ARCHIVED_FIELD_NUMBER: _ClassVar[int]
    is_btv: bool
    show_type: ShowType
    is_archived: bool
    def __init__(self, is_btv: bool = ..., show_type: _Optional[_Union[ShowType, str]] = ..., is_archived: bool = ...) -> None: ...
