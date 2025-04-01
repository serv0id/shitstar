from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class WatchState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    NOT_STARTED: _ClassVar[WatchState]
    WATCHING: _ClassVar[WatchState]
    WATCHED: _ClassVar[WatchState]
NOT_STARTED: WatchState
WATCHING: WatchState
WATCHED: WatchState

class CwInfo(_message.Message):
    __slots__ = ("content_id", "resume_at", "duration", "timestamp", "watch_state", "overwrite_client_info", "watch_ratio", "parent_content_id")
    CONTENT_ID_FIELD_NUMBER: _ClassVar[int]
    RESUME_AT_FIELD_NUMBER: _ClassVar[int]
    DURATION_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    WATCH_STATE_FIELD_NUMBER: _ClassVar[int]
    OVERWRITE_CLIENT_INFO_FIELD_NUMBER: _ClassVar[int]
    WATCH_RATIO_FIELD_NUMBER: _ClassVar[int]
    PARENT_CONTENT_ID_FIELD_NUMBER: _ClassVar[int]
    content_id: str
    resume_at: int
    duration: int
    timestamp: int
    watch_state: WatchState
    overwrite_client_info: bool
    watch_ratio: float
    parent_content_id: str
    def __init__(self, content_id: _Optional[str] = ..., resume_at: _Optional[int] = ..., duration: _Optional[int] = ..., timestamp: _Optional[int] = ..., watch_state: _Optional[_Union[WatchState, str]] = ..., overwrite_client_info: bool = ..., watch_ratio: _Optional[float] = ..., parent_content_id: _Optional[str] = ...) -> None: ...
