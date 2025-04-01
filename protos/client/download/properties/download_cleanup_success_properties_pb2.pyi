from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class DownloadCleanupSuccessProperties(_message.Message):
    __slots__ = ("total_download_deleted_count", "total_space_cleared_bytes")
    TOTAL_DOWNLOAD_DELETED_COUNT_FIELD_NUMBER: _ClassVar[int]
    TOTAL_SPACE_CLEARED_BYTES_FIELD_NUMBER: _ClassVar[int]
    total_download_deleted_count: int
    total_space_cleared_bytes: int
    def __init__(self, total_download_deleted_count: _Optional[int] = ..., total_space_cleared_bytes: _Optional[int] = ...) -> None: ...
