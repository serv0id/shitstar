from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class SurveyViewedProperties(_message.Message):
    __slots__ = ("query_text", "page_type")
    QUERY_TEXT_FIELD_NUMBER: _ClassVar[int]
    PAGE_TYPE_FIELD_NUMBER: _ClassVar[int]
    query_text: str
    page_type: str
    def __init__(self, query_text: _Optional[str] = ..., page_type: _Optional[str] = ...) -> None: ...
