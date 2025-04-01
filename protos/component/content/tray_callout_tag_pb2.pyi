from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class TrayCalloutTag(_message.Message):
    __slots__ = ("name", "category", "format", "position")
    NAME_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_FIELD_NUMBER: _ClassVar[int]
    FORMAT_FIELD_NUMBER: _ClassVar[int]
    POSITION_FIELD_NUMBER: _ClassVar[int]
    name: str
    category: str
    format: str
    position: str
    def __init__(self, name: _Optional[str] = ..., category: _Optional[str] = ..., format: _Optional[str] = ..., position: _Optional[str] = ...) -> None: ...
