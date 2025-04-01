from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ViewedMySpacePage(_message.Message):
    __slots__ = ("display_text",)
    DISPLAY_TEXT_FIELD_NUMBER: _ClassVar[int]
    display_text: str
    def __init__(self, display_text: _Optional[str] = ...) -> None: ...
