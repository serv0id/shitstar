from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class EventMetadata(_message.Message):
    __slots__ = ("message_id", "ts_occurred_ms")
    MESSAGE_ID_FIELD_NUMBER: _ClassVar[int]
    TS_OCCURRED_MS_FIELD_NUMBER: _ClassVar[int]
    message_id: str
    ts_occurred_ms: int
    def __init__(self, message_id: _Optional[str] = ..., ts_occurred_ms: _Optional[int] = ...) -> None: ...
