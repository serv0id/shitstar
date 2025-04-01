from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ScreenOrientation(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SCREEN_ORIENTATION_UNSPECIFIED: _ClassVar[ScreenOrientation]
    SCREEN_ORIENTATION_PORTRAIT: _ClassVar[ScreenOrientation]
    SCREEN_ORIENTATION_LANDSCAPE: _ClassVar[ScreenOrientation]
SCREEN_ORIENTATION_UNSPECIFIED: ScreenOrientation
SCREEN_ORIENTATION_PORTRAIT: ScreenOrientation
SCREEN_ORIENTATION_LANDSCAPE: ScreenOrientation

class Orientation(_message.Message):
    __slots__ = ("orientation",)
    ORIENTATION_FIELD_NUMBER: _ClassVar[int]
    orientation: ScreenOrientation
    def __init__(self, orientation: _Optional[_Union[ScreenOrientation, str]] = ...) -> None: ...
