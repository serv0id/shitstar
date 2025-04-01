from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class VideoAnimation(_message.Message):
    __slots__ = ("type", "src", "duration_in_ms")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    SRC_FIELD_NUMBER: _ClassVar[int]
    DURATION_IN_MS_FIELD_NUMBER: _ClassVar[int]
    type: str
    src: str
    duration_in_ms: int
    def __init__(self, type: _Optional[str] = ..., src: _Optional[str] = ..., duration_in_ms: _Optional[int] = ...) -> None: ...
