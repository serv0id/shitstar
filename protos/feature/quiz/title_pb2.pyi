from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class Title(_message.Message):
    __slots__ = ("title", "subtitle")
    TITLE_FIELD_NUMBER: _ClassVar[int]
    SUBTITLE_FIELD_NUMBER: _ClassVar[int]
    title: str
    subtitle: str
    def __init__(self, title: _Optional[str] = ..., subtitle: _Optional[str] = ...) -> None: ...
