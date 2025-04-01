from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ContentItemClientContext(_message.Message):
    __slots__ = ("item_name",)
    ITEM_NAME_FIELD_NUMBER: _ClassVar[int]
    item_name: str
    def __init__(self, item_name: _Optional[str] = ...) -> None: ...
