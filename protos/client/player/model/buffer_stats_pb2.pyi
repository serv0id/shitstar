from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class BufferStats(_message.Message):
    __slots__ = ("total_buffered_duration_ms", "total_buffered_length_bytes")
    TOTAL_BUFFERED_DURATION_MS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_BUFFERED_LENGTH_BYTES_FIELD_NUMBER: _ClassVar[int]
    total_buffered_duration_ms: int
    total_buffered_length_bytes: int
    def __init__(self, total_buffered_duration_ms: _Optional[int] = ..., total_buffered_length_bytes: _Optional[int] = ...) -> None: ...
