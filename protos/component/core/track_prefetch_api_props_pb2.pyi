from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PrefetchApiState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PREFETCH_API_STATE_UNSPECIFIED: _ClassVar[PrefetchApiState]
    PREFETCH_API_STATE_SUCCESS: _ClassVar[PrefetchApiState]
    PREFETCH_API_STATE_FAILURE: _ClassVar[PrefetchApiState]
PREFETCH_API_STATE_UNSPECIFIED: PrefetchApiState
PREFETCH_API_STATE_SUCCESS: PrefetchApiState
PREFETCH_API_STATE_FAILURE: PrefetchApiState

class TrackPrefetchApiProps(_message.Message):
    __slots__ = ("prefetch_api_state", "prefetch_page_type", "is_prefetch_api_allowed", "is_prefetch_api_triggered", "cache_expiry_time_ms", "cache_created_time_ms", "cache_validity_left_time_ms")
    PREFETCH_API_STATE_FIELD_NUMBER: _ClassVar[int]
    PREFETCH_PAGE_TYPE_FIELD_NUMBER: _ClassVar[int]
    IS_PREFETCH_API_ALLOWED_FIELD_NUMBER: _ClassVar[int]
    IS_PREFETCH_API_TRIGGERED_FIELD_NUMBER: _ClassVar[int]
    CACHE_EXPIRY_TIME_MS_FIELD_NUMBER: _ClassVar[int]
    CACHE_CREATED_TIME_MS_FIELD_NUMBER: _ClassVar[int]
    CACHE_VALIDITY_LEFT_TIME_MS_FIELD_NUMBER: _ClassVar[int]
    prefetch_api_state: PrefetchApiState
    prefetch_page_type: str
    is_prefetch_api_allowed: bool
    is_prefetch_api_triggered: bool
    cache_expiry_time_ms: int
    cache_created_time_ms: int
    cache_validity_left_time_ms: int
    def __init__(self, prefetch_api_state: _Optional[_Union[PrefetchApiState, str]] = ..., prefetch_page_type: _Optional[str] = ..., is_prefetch_api_allowed: bool = ..., is_prefetch_api_triggered: bool = ..., cache_expiry_time_ms: _Optional[int] = ..., cache_created_time_ms: _Optional[int] = ..., cache_validity_left_time_ms: _Optional[int] = ...) -> None: ...
