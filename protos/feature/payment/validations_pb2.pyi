from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class Validation(_message.Message):
    __slots__ = ("regex", "message")
    REGEX_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    regex: str
    message: str
    def __init__(self, regex: _Optional[str] = ..., message: _Optional[str] = ...) -> None: ...
