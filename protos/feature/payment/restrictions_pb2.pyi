from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class Restriction(_message.Message):
    __slots__ = ["regex"]
    REGEX_FIELD_NUMBER: _ClassVar[int]
    regex: str
    def __init__(self, regex: _Optional[str] = ...) -> None: ...
