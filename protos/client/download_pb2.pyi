from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class DownloadManager(_message.Message):
    __slots__ = ("download_manager_id", "download_size", "requested_bytes", "download_manager_version")
    DOWNLOAD_MANAGER_ID_FIELD_NUMBER: _ClassVar[int]
    DOWNLOAD_SIZE_FIELD_NUMBER: _ClassVar[int]
    REQUESTED_BYTES_FIELD_NUMBER: _ClassVar[int]
    DOWNLOAD_MANAGER_VERSION_FIELD_NUMBER: _ClassVar[int]
    download_manager_id: str
    download_size: int
    requested_bytes: int
    download_manager_version: str
    def __init__(self, download_manager_id: _Optional[str] = ..., download_size: _Optional[int] = ..., requested_bytes: _Optional[int] = ..., download_manager_version: _Optional[str] = ...) -> None: ...
