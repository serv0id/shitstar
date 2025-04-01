from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class DownloadErrorInfo(_message.Message):
    __slots__ = ("error_code", "http_error_code", "error_message", "failed_url", "error_logs", "native_error_code")
    ERROR_CODE_FIELD_NUMBER: _ClassVar[int]
    HTTP_ERROR_CODE_FIELD_NUMBER: _ClassVar[int]
    ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    FAILED_URL_FIELD_NUMBER: _ClassVar[int]
    ERROR_LOGS_FIELD_NUMBER: _ClassVar[int]
    NATIVE_ERROR_CODE_FIELD_NUMBER: _ClassVar[int]
    error_code: str
    http_error_code: int
    error_message: str
    failed_url: str
    error_logs: str
    native_error_code: str
    def __init__(self, error_code: _Optional[str] = ..., http_error_code: _Optional[int] = ..., error_message: _Optional[str] = ..., failed_url: _Optional[str] = ..., error_logs: _Optional[str] = ..., native_error_code: _Optional[str] = ...) -> None: ...
