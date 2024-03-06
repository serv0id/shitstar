from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class RateAppAction(_message.Message):
    __slots__ = ["event_name", "trigger_time"]
    EVENT_NAME_FIELD_NUMBER: _ClassVar[int]
    TRIGGER_TIME_FIELD_NUMBER: _ClassVar[int]
    event_name: str
    trigger_time: int
    def __init__(self, event_name: _Optional[str] = ..., trigger_time: _Optional[int] = ...) -> None: ...
