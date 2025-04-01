from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ContentCard(_message.Message):
    __slots__ = ("action_text",)
    ACTION_TEXT_FIELD_NUMBER: _ClassVar[int]
    action_text: str
    def __init__(self, action_text: _Optional[str] = ...) -> None: ...
