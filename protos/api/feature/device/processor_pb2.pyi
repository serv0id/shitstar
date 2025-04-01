from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ProcessorInfo(_message.Message):
    __slots__ = ("active_processor_count",)
    ACTIVE_PROCESSOR_COUNT_FIELD_NUMBER: _ClassVar[int]
    active_processor_count: int
    def __init__(self, active_processor_count: _Optional[int] = ...) -> None: ...
