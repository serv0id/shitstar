from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class StartPrefetchState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    START_PREFETCH_STATE_UNSPECIFIED: _ClassVar[StartPrefetchState]
    START_PREFETCH_STATE_SCHEDULED: _ClassVar[StartPrefetchState]
    START_PREFETCH_STATE_TRIGGERED: _ClassVar[StartPrefetchState]

class EventCategory(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EVENT_CATEGORY_UNSPECIFIED: _ClassVar[EventCategory]
    EVENT_CATEGORY_NON_STAGGERED: _ClassVar[EventCategory]
    EVENT_CATEGORY_STAGGERED_TOKEN_CHANGED: _ClassVar[EventCategory]
    EVENT_CATEGORY_STAGGERED_WORK_EXECUTED: _ClassVar[EventCategory]
START_PREFETCH_STATE_UNSPECIFIED: StartPrefetchState
START_PREFETCH_STATE_SCHEDULED: StartPrefetchState
START_PREFETCH_STATE_TRIGGERED: StartPrefetchState
EVENT_CATEGORY_UNSPECIFIED: EventCategory
EVENT_CATEGORY_NON_STAGGERED: EventCategory
EVENT_CATEGORY_STAGGERED_TOKEN_CHANGED: EventCategory
EVENT_CATEGORY_STAGGERED_WORK_EXECUTED: EventCategory

class StartApiPrefetchProps(_message.Message):
    __slots__ = ("start_prefetch_state", "start_prefetch_time_ms", "start_prefetch_id", "event_category", "staggered_campaign_id", "staggered_delay_mins", "staggered_enqueued_time_ms", "staggered_executed_time_ms")
    START_PREFETCH_STATE_FIELD_NUMBER: _ClassVar[int]
    START_PREFETCH_TIME_MS_FIELD_NUMBER: _ClassVar[int]
    START_PREFETCH_ID_FIELD_NUMBER: _ClassVar[int]
    EVENT_CATEGORY_FIELD_NUMBER: _ClassVar[int]
    STAGGERED_CAMPAIGN_ID_FIELD_NUMBER: _ClassVar[int]
    STAGGERED_DELAY_MINS_FIELD_NUMBER: _ClassVar[int]
    STAGGERED_ENQUEUED_TIME_MS_FIELD_NUMBER: _ClassVar[int]
    STAGGERED_EXECUTED_TIME_MS_FIELD_NUMBER: _ClassVar[int]
    start_prefetch_state: StartPrefetchState
    start_prefetch_time_ms: int
    start_prefetch_id: str
    event_category: EventCategory
    staggered_campaign_id: str
    staggered_delay_mins: int
    staggered_enqueued_time_ms: int
    staggered_executed_time_ms: int
    def __init__(self, start_prefetch_state: _Optional[_Union[StartPrefetchState, str]] = ..., start_prefetch_time_ms: _Optional[int] = ..., start_prefetch_id: _Optional[str] = ..., event_category: _Optional[_Union[EventCategory, str]] = ..., staggered_campaign_id: _Optional[str] = ..., staggered_delay_mins: _Optional[int] = ..., staggered_enqueued_time_ms: _Optional[int] = ..., staggered_executed_time_ms: _Optional[int] = ...) -> None: ...
