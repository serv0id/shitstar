from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class Error(_message.Message):
    __slots__ = ("sgai_error_code", "sgai_error_message")
    SGAI_ERROR_CODE_FIELD_NUMBER: _ClassVar[int]
    SGAI_ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    sgai_error_code: int
    sgai_error_message: str
    def __init__(self, sgai_error_code: _Optional[int] = ..., sgai_error_message: _Optional[str] = ...) -> None: ...
