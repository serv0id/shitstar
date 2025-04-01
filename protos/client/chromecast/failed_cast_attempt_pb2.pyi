from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class FailedCastAttemptProperties(_message.Message):
    __slots__ = ("error_code",)
    ERROR_CODE_FIELD_NUMBER: _ClassVar[int]
    error_code: str
    def __init__(self, error_code: _Optional[str] = ...) -> None: ...
