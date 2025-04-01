from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class Context(_message.Message):
    __slots__ = ("url", "value")
    URL_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    url: str
    value: bytes
    def __init__(self, url: _Optional[str] = ..., value: _Optional[bytes] = ...) -> None: ...
