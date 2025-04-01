from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ViewedWatchPage(_message.Message):
    __slots__ = ("screen_mode",)
    class ScreenMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SCREEN_MODE_UNSPECIFIED: _ClassVar[ViewedWatchPage.ScreenMode]
        SCREEN_MODE_PORTRAIT: _ClassVar[ViewedWatchPage.ScreenMode]
        SCREEN_MODE_LANDSCAPE: _ClassVar[ViewedWatchPage.ScreenMode]
    SCREEN_MODE_UNSPECIFIED: ViewedWatchPage.ScreenMode
    SCREEN_MODE_PORTRAIT: ViewedWatchPage.ScreenMode
    SCREEN_MODE_LANDSCAPE: ViewedWatchPage.ScreenMode
    SCREEN_MODE_FIELD_NUMBER: _ClassVar[int]
    screen_mode: ViewedWatchPage.ScreenMode
    def __init__(self, screen_mode: _Optional[_Union[ViewedWatchPage.ScreenMode, str]] = ...) -> None: ...
