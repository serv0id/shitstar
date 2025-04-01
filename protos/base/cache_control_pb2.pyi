from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class CacheControl(_message.Message):
    __slots__ = ("is_cacheable", "ttl_sec")
    IS_CACHEABLE_FIELD_NUMBER: _ClassVar[int]
    TTL_SEC_FIELD_NUMBER: _ClassVar[int]
    is_cacheable: bool
    ttl_sec: int
    def __init__(self, is_cacheable: bool = ..., ttl_sec: _Optional[int] = ...) -> None: ...
