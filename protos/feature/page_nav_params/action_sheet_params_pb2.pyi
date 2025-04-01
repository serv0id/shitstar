from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ActionSheetParams(_message.Message):
    __slots__ = ("bg_overlay_type", "auto_dismissal_timer")
    class BGOverlayType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        DEFAULT: _ClassVar[ActionSheetParams.BGOverlayType]
        CLEAR: _ClassVar[ActionSheetParams.BGOverlayType]
        WATCH_PAGE_CURTAIN: _ClassVar[ActionSheetParams.BGOverlayType]
    DEFAULT: ActionSheetParams.BGOverlayType
    CLEAR: ActionSheetParams.BGOverlayType
    WATCH_PAGE_CURTAIN: ActionSheetParams.BGOverlayType
    class AutoDismissalTimer(_message.Message):
        __slots__ = ("timer_duration_in_seconds",)
        TIMER_DURATION_IN_SECONDS_FIELD_NUMBER: _ClassVar[int]
        timer_duration_in_seconds: int
        def __init__(self, timer_duration_in_seconds: _Optional[int] = ...) -> None: ...
    BG_OVERLAY_TYPE_FIELD_NUMBER: _ClassVar[int]
    AUTO_DISMISSAL_TIMER_FIELD_NUMBER: _ClassVar[int]
    bg_overlay_type: ActionSheetParams.BGOverlayType
    auto_dismissal_timer: ActionSheetParams.AutoDismissalTimer
    def __init__(self, bg_overlay_type: _Optional[_Union[ActionSheetParams.BGOverlayType, str]] = ..., auto_dismissal_timer: _Optional[_Union[ActionSheetParams.AutoDismissalTimer, _Mapping]] = ...) -> None: ...
