from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class SearchEraseProperties(_message.Message):
    __slots__ = ("search_session_id", "last_search_id", "last_query_text")
    SEARCH_SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    LAST_SEARCH_ID_FIELD_NUMBER: _ClassVar[int]
    LAST_QUERY_TEXT_FIELD_NUMBER: _ClassVar[int]
    search_session_id: str
    last_search_id: str
    last_query_text: str
    def __init__(self, search_session_id: _Optional[str] = ..., last_search_id: _Optional[str] = ..., last_query_text: _Optional[str] = ...) -> None: ...
