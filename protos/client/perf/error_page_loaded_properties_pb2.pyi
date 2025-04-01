from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ErrorPageLoadedProperties(_message.Message):
    __slots__ = ("page_type", "error_code")
    PAGE_TYPE_FIELD_NUMBER: _ClassVar[int]
    ERROR_CODE_FIELD_NUMBER: _ClassVar[int]
    page_type: str
    error_code: str
    def __init__(self, page_type: _Optional[str] = ..., error_code: _Optional[str] = ...) -> None: ...
