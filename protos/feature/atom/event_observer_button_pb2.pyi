from feature.atom import button_pb2 as _button_pb2
from feature.atom import toggle_button_pb2 as _toggle_button_pb2
from feature.atom import toggle_lottie_button_pb2 as _toggle_lottie_button_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class EventObserverButton(_message.Message):
    __slots__ = ("event", "button")
    EVENT_FIELD_NUMBER: _ClassVar[int]
    BUTTON_FIELD_NUMBER: _ClassVar[int]
    event: FeatureEvent
    button: CTA
    def __init__(self, event: _Optional[_Union[FeatureEvent, _Mapping]] = ..., button: _Optional[_Union[CTA, _Mapping]] = ...) -> None: ...

class FeatureEvent(_message.Message):
    __slots__ = ("event_name", "identifier", "data")
    EVENT_NAME_FIELD_NUMBER: _ClassVar[int]
    IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    event_name: str
    identifier: str
    data: EventData
    def __init__(self, event_name: _Optional[str] = ..., identifier: _Optional[str] = ..., data: _Optional[_Union[EventData, _Mapping]] = ...) -> None: ...

class CTA(_message.Message):
    __slots__ = ("toggle_button", "toggle_lottie_button", "button")
    TOGGLE_BUTTON_FIELD_NUMBER: _ClassVar[int]
    TOGGLE_LOTTIE_BUTTON_FIELD_NUMBER: _ClassVar[int]
    BUTTON_FIELD_NUMBER: _ClassVar[int]
    toggle_button: _toggle_button_pb2.ToggleButton
    toggle_lottie_button: _toggle_lottie_button_pb2.ToggleLottieButton
    button: _button_pb2.Button
    def __init__(self, toggle_button: _Optional[_Union[_toggle_button_pb2.ToggleButton, _Mapping]] = ..., toggle_lottie_button: _Optional[_Union[_toggle_lottie_button_pb2.ToggleLottieButton, _Mapping]] = ..., button: _Optional[_Union[_button_pb2.Button, _Mapping]] = ...) -> None: ...

class EventData(_message.Message):
    __slots__ = ("toggle_event_data", "player_subs_nudge_data")
    TOGGLE_EVENT_DATA_FIELD_NUMBER: _ClassVar[int]
    PLAYER_SUBS_NUDGE_DATA_FIELD_NUMBER: _ClassVar[int]
    toggle_event_data: ToggleEventData
    player_subs_nudge_data: PlayerFreePreviewNudgeData
    def __init__(self, toggle_event_data: _Optional[_Union[ToggleEventData, _Mapping]] = ..., player_subs_nudge_data: _Optional[_Union[PlayerFreePreviewNudgeData, _Mapping]] = ...) -> None: ...

class ToggleEventData(_message.Message):
    __slots__ = ("is_selected",)
    IS_SELECTED_FIELD_NUMBER: _ClassVar[int]
    is_selected: bool
    def __init__(self, is_selected: bool = ...) -> None: ...

class PlayerFreePreviewNudgeData(_message.Message):
    __slots__ = ("total_duration_s", "start_shown_duration_s", "end_shown_duration_s", "timer_placeholder", "current_time_stamp_s", "seek_thumbnail_subs_info")
    TOTAL_DURATION_S_FIELD_NUMBER: _ClassVar[int]
    START_SHOWN_DURATION_S_FIELD_NUMBER: _ClassVar[int]
    END_SHOWN_DURATION_S_FIELD_NUMBER: _ClassVar[int]
    TIMER_PLACEHOLDER_FIELD_NUMBER: _ClassVar[int]
    CURRENT_TIME_STAMP_S_FIELD_NUMBER: _ClassVar[int]
    SEEK_THUMBNAIL_SUBS_INFO_FIELD_NUMBER: _ClassVar[int]
    total_duration_s: int
    start_shown_duration_s: int
    end_shown_duration_s: int
    timer_placeholder: str
    current_time_stamp_s: int
    seek_thumbnail_subs_info: str
    def __init__(self, total_duration_s: _Optional[int] = ..., start_shown_duration_s: _Optional[int] = ..., end_shown_duration_s: _Optional[int] = ..., timer_placeholder: _Optional[str] = ..., current_time_stamp_s: _Optional[int] = ..., seek_thumbnail_subs_info: _Optional[str] = ...) -> None: ...
