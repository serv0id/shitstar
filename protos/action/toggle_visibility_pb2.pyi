from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ToggleVisibilityAction(_message.Message):
    __slots__ = ("isVisible",)
    ISVISIBLE_FIELD_NUMBER: _ClassVar[int]
    isVisible: bool
    def __init__(self, isVisible: bool = ...) -> None: ...
