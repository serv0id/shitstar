from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class DownloadSizeInfo(_message.Message):
    __slots__ = ("total_display_size", "total_content_size_bytes")
    TOTAL_DISPLAY_SIZE_FIELD_NUMBER: _ClassVar[int]
    TOTAL_CONTENT_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    total_display_size: str
    total_content_size_bytes: int
    def __init__(self, total_display_size: _Optional[str] = ..., total_content_size_bytes: _Optional[int] = ...) -> None: ...
