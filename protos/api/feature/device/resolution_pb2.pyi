from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ScreenResolutionType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SCREEN_RESOLUTION_TYPE_UNSPECIFIED: _ClassVar[ScreenResolutionType]
    SCREEN_RESOLUTION_TYPE_LDPI: _ClassVar[ScreenResolutionType]
    SCREEN_RESOLUTION_TYPE_MDPI: _ClassVar[ScreenResolutionType]
    SCREEN_RESOLUTION_TYPE_HDPI: _ClassVar[ScreenResolutionType]
    SCREEN_RESOLUTION_TYPE_XHDPI: _ClassVar[ScreenResolutionType]
    SCREEN_RESOLUTION_TYPE_XXHDPI: _ClassVar[ScreenResolutionType]
    SCREEN_RESOLUTION_TYPE_XXXHDPI: _ClassVar[ScreenResolutionType]
SCREEN_RESOLUTION_TYPE_UNSPECIFIED: ScreenResolutionType
SCREEN_RESOLUTION_TYPE_LDPI: ScreenResolutionType
SCREEN_RESOLUTION_TYPE_MDPI: ScreenResolutionType
SCREEN_RESOLUTION_TYPE_HDPI: ScreenResolutionType
SCREEN_RESOLUTION_TYPE_XHDPI: ScreenResolutionType
SCREEN_RESOLUTION_TYPE_XXHDPI: ScreenResolutionType
SCREEN_RESOLUTION_TYPE_XXXHDPI: ScreenResolutionType

class Resolution(_message.Message):
    __slots__ = ("width_px", "height_px", "screen_resolution_type")
    WIDTH_PX_FIELD_NUMBER: _ClassVar[int]
    HEIGHT_PX_FIELD_NUMBER: _ClassVar[int]
    SCREEN_RESOLUTION_TYPE_FIELD_NUMBER: _ClassVar[int]
    width_px: int
    height_px: int
    screen_resolution_type: ScreenResolutionType
    def __init__(self, width_px: _Optional[int] = ..., height_px: _Optional[int] = ..., screen_resolution_type: _Optional[_Union[ScreenResolutionType, str]] = ...) -> None: ...
