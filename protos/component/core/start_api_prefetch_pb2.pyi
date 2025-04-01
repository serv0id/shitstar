from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class StartApiPrefetchState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    START_API_PREFETCH_STATE_UNSPECIFIED: _ClassVar[StartApiPrefetchState]
    START_API_PREFETCH_STATE_SCHEDULED: _ClassVar[StartApiPrefetchState]
    START_API_PREFETCH_STATE_TRIGGERED: _ClassVar[StartApiPrefetchState]
START_API_PREFETCH_STATE_UNSPECIFIED: StartApiPrefetchState
START_API_PREFETCH_STATE_SCHEDULED: StartApiPrefetchState
START_API_PREFETCH_STATE_TRIGGERED: StartApiPrefetchState

class StartApiPrefetchProperties(_message.Message):
    __slots__ = ("start_api_prefetch_state", "start_api_prefetch_time_ms", "start_api_prefetch_id")
    START_API_PREFETCH_STATE_FIELD_NUMBER: _ClassVar[int]
    START_API_PREFETCH_TIME_MS_FIELD_NUMBER: _ClassVar[int]
    START_API_PREFETCH_ID_FIELD_NUMBER: _ClassVar[int]
    start_api_prefetch_state: StartApiPrefetchState
    start_api_prefetch_time_ms: int
    start_api_prefetch_id: str
    def __init__(self, start_api_prefetch_state: _Optional[_Union[StartApiPrefetchState, str]] = ..., start_api_prefetch_time_ms: _Optional[int] = ..., start_api_prefetch_id: _Optional[str] = ...) -> None: ...
