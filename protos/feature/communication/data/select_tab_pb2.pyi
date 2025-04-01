from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class SelectTab(_message.Message):
    __slots__ = ("tab_id",)
    TAB_ID_FIELD_NUMBER: _ClassVar[int]
    tab_id: str
    def __init__(self, tab_id: _Optional[str] = ...) -> None: ...
