from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class Creative(_message.Message):
    __slots__ = ("id", "duration_ms")
    ID_FIELD_NUMBER: _ClassVar[int]
    DURATION_MS_FIELD_NUMBER: _ClassVar[int]
    id: str
    duration_ms: int
    def __init__(self, id: _Optional[str] = ..., duration_ms: _Optional[int] = ...) -> None: ...
