from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class WatchlistInfo(_message.Message):
    __slots__ = ["content_id", "is_watchlisted", "timestamp"]
    CONTENT_ID_FIELD_NUMBER: _ClassVar[int]
    IS_WATCHLISTED_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    content_id: str
    is_watchlisted: bool
    timestamp: int
    def __init__(self, content_id: _Optional[str] = ..., is_watchlisted: bool = ..., timestamp: _Optional[int] = ...) -> None: ...
