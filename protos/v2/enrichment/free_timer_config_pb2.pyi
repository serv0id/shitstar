from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class FreeTimerConfig(_message.Message):
    __slots__ = ("consumed_time_ms", "total_time_ms")
    CONSUMED_TIME_MS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_TIME_MS_FIELD_NUMBER: _ClassVar[int]
    consumed_time_ms: int
    total_time_ms: int
    def __init__(self, consumed_time_ms: _Optional[int] = ..., total_time_ms: _Optional[int] = ...) -> None: ...
