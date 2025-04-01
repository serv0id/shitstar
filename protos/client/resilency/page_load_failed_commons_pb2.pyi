from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class PageLoadFailedCommons(_message.Message):
    __slots__ = ("error_code", "error_message", "failed_page_tempalte", "request_id", "url", "retry_count")
    ERROR_CODE_FIELD_NUMBER: _ClassVar[int]
    ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    FAILED_PAGE_TEMPALTE_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    RETRY_COUNT_FIELD_NUMBER: _ClassVar[int]
    error_code: str
    error_message: str
    failed_page_tempalte: str
    request_id: str
    url: str
    retry_count: int
    def __init__(self, error_code: _Optional[str] = ..., error_message: _Optional[str] = ..., failed_page_tempalte: _Optional[str] = ..., request_id: _Optional[str] = ..., url: _Optional[str] = ..., retry_count: _Optional[int] = ...) -> None: ...
