from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class DeleteListItemAction(_message.Message):
    __slots__ = ("url", "id")
    URL_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    url: str
    id: str
    def __init__(self, url: _Optional[str] = ..., id: _Optional[str] = ...) -> None: ...
