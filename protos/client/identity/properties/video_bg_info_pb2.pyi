from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class NetworkType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    NETWORK_TYPE_UNSPECIFIED: _ClassVar[NetworkType]
    NETWORK_TYPE_WIFI: _ClassVar[NetworkType]
    NETWORK_TYPE_MOBILE_DATA: _ClassVar[NetworkType]
NETWORK_TYPE_UNSPECIFIED: NetworkType
NETWORK_TYPE_WIFI: NetworkType
NETWORK_TYPE_MOBILE_DATA: NetworkType

class ScreenSize(_message.Message):
    __slots__ = ("screen_width", "screen_height")
    SCREEN_WIDTH_FIELD_NUMBER: _ClassVar[int]
    SCREEN_HEIGHT_FIELD_NUMBER: _ClassVar[int]
    screen_width: str
    screen_height: str
    def __init__(self, screen_width: _Optional[str] = ..., screen_height: _Optional[str] = ...) -> None: ...
