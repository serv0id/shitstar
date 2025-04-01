from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ShowStickyMenuToastAction(_message.Message):
    __slots__ = ("infinite_config", "timer_config")
    class InfiniteConfig(_message.Message):
        __slots__ = ("ui_config",)
        UI_CONFIG_FIELD_NUMBER: _ClassVar[int]
        ui_config: ShowStickyMenuToastAction.UIConfig
        def __init__(self, ui_config: _Optional[_Union[ShowStickyMenuToastAction.UIConfig, _Mapping]] = ...) -> None: ...
    class TimerConfig(_message.Message):
        __slots__ = ("time_interval_ms", "start_timer_ui_config", "infinite_config", "timer_config")
        TIME_INTERVAL_MS_FIELD_NUMBER: _ClassVar[int]
        START_TIMER_UI_CONFIG_FIELD_NUMBER: _ClassVar[int]
        INFINITE_CONFIG_FIELD_NUMBER: _ClassVar[int]
        TIMER_CONFIG_FIELD_NUMBER: _ClassVar[int]
        time_interval_ms: int
        start_timer_ui_config: ShowStickyMenuToastAction.UIConfig
        infinite_config: ShowStickyMenuToastAction.InfiniteConfig
        timer_config: ShowStickyMenuToastAction.TimerConfig
        def __init__(self, time_interval_ms: _Optional[int] = ..., start_timer_ui_config: _Optional[_Union[ShowStickyMenuToastAction.UIConfig, _Mapping]] = ..., infinite_config: _Optional[_Union[ShowStickyMenuToastAction.InfiniteConfig, _Mapping]] = ..., timer_config: _Optional[_Union[ShowStickyMenuToastAction.TimerConfig, _Mapping]] = ...) -> None: ...
    class UIConfig(_message.Message):
        __slots__ = ("message", "bg_color", "text_color", "icon")
        MESSAGE_FIELD_NUMBER: _ClassVar[int]
        BG_COLOR_FIELD_NUMBER: _ClassVar[int]
        TEXT_COLOR_FIELD_NUMBER: _ClassVar[int]
        ICON_FIELD_NUMBER: _ClassVar[int]
        message: str
        bg_color: str
        text_color: str
        icon: str
        def __init__(self, message: _Optional[str] = ..., bg_color: _Optional[str] = ..., text_color: _Optional[str] = ..., icon: _Optional[str] = ...) -> None: ...
    INFINITE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    TIMER_CONFIG_FIELD_NUMBER: _ClassVar[int]
    infinite_config: ShowStickyMenuToastAction.InfiniteConfig
    timer_config: ShowStickyMenuToastAction.TimerConfig
    def __init__(self, infinite_config: _Optional[_Union[ShowStickyMenuToastAction.InfiniteConfig, _Mapping]] = ..., timer_config: _Optional[_Union[ShowStickyMenuToastAction.TimerConfig, _Mapping]] = ...) -> None: ...
