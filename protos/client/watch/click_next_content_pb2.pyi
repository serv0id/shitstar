from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ClickedNextContentProperties(_message.Message):
    __slots__ = ("clicked_pos_sec", "next_content_id")
    CLICKED_POS_SEC_FIELD_NUMBER: _ClassVar[int]
    NEXT_CONTENT_ID_FIELD_NUMBER: _ClassVar[int]
    clicked_pos_sec: int
    next_content_id: str
    def __init__(self, clicked_pos_sec: _Optional[int] = ..., next_content_id: _Optional[str] = ...) -> None: ...
