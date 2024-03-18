from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class RefreshInfo(_message.Message):
    __slots__ = ["max_age_ms", "refresh_url"]
    MAX_AGE_MS_FIELD_NUMBER: _ClassVar[int]
    REFRESH_URL_FIELD_NUMBER: _ClassVar[int]
    max_age_ms: int
    refresh_url: str
    def __init__(self, max_age_ms: _Optional[int] = ..., refresh_url: _Optional[str] = ...) -> None: ...
