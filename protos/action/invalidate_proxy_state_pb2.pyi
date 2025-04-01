from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class UpdateProxyStateTTLAction(_message.Message):
    __slots__ = ("key", "ttl")
    KEY_FIELD_NUMBER: _ClassVar[int]
    TTL_FIELD_NUMBER: _ClassVar[int]
    key: str
    ttl: int
    def __init__(self, key: _Optional[str] = ..., ttl: _Optional[int] = ...) -> None: ...
