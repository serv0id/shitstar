from feature.image import image_pb2 as _image_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ErrorInfo(_message.Message):
    __slots__ = ("title", "message", "error_code")
    TITLE_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    ERROR_CODE_FIELD_NUMBER: _ClassVar[int]
    title: str
    message: str
    error_code: str
    def __init__(self, title: _Optional[str] = ..., message: _Optional[str] = ..., error_code: _Optional[str] = ...) -> None: ...
