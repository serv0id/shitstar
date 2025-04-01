from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class CachedResponse(_message.Message):
    __slots__ = ("is_cached_response",)
    IS_CACHED_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    is_cached_response: bool
    def __init__(self, is_cached_response: bool = ...) -> None: ...
