from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class QuestionSectionProperties(_message.Message):
    __slots__ = ("section_type", "section_id", "section_position")
    SECTION_TYPE_FIELD_NUMBER: _ClassVar[int]
    SECTION_ID_FIELD_NUMBER: _ClassVar[int]
    SECTION_POSITION_FIELD_NUMBER: _ClassVar[int]
    section_type: str
    section_id: str
    section_position: int
    def __init__(self, section_type: _Optional[str] = ..., section_id: _Optional[str] = ..., section_position: _Optional[int] = ...) -> None: ...
