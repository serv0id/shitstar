from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class AppRestartAction(_message.Message):
    __slots__ = ["flush_identity_storage"]
    FLUSH_IDENTITY_STORAGE_FIELD_NUMBER: _ClassVar[int]
    flush_identity_storage: bool
    def __init__(self, flush_identity_storage: bool = ...) -> None: ...
