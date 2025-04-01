from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class Preroll(_message.Message):
    __slots__ = ("server_url", "payload")
    SERVER_URL_FIELD_NUMBER: _ClassVar[int]
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    server_url: str
    payload: str
    def __init__(self, server_url: _Optional[str] = ..., payload: _Optional[str] = ...) -> None: ...
