from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class KidsProfileToggle(_message.Message):
    __slots__ = ("is_enabled",)
    IS_ENABLED_FIELD_NUMBER: _ClassVar[int]
    is_enabled: bool
    def __init__(self, is_enabled: bool = ...) -> None: ...
