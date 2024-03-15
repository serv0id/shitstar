from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class FormQuestion(_message.Message):
    __slots__ = ["id", "title", "subtitle", "error_message"]
    ID_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    SUBTITLE_FIELD_NUMBER: _ClassVar[int]
    ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    id: str
    title: str
    subtitle: str
    error_message: str
    def __init__(self, id: _Optional[str] = ..., title: _Optional[str] = ..., subtitle: _Optional[str] = ..., error_message: _Optional[str] = ...) -> None: ...
