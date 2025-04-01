from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ToggleWatchlist(_message.Message):
    __slots__ = ("content_id",)
    CONTENT_ID_FIELD_NUMBER: _ClassVar[int]
    content_id: str
    def __init__(self, content_id: _Optional[str] = ...) -> None: ...
