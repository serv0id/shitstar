from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class SelectableItem(_message.Message):
    __slots__ = ("id", "title", "description", "selected_url")
    ID_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    SELECTED_URL_FIELD_NUMBER: _ClassVar[int]
    id: str
    title: str
    description: str
    selected_url: str
    def __init__(self, id: _Optional[str] = ..., title: _Optional[str] = ..., description: _Optional[str] = ..., selected_url: _Optional[str] = ...) -> None: ...
