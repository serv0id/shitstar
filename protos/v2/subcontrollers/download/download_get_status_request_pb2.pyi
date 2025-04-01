from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class DownloadStatusRequest(_message.Message):
    __slots__ = ("download_id", "profile_id")
    DOWNLOAD_ID_FIELD_NUMBER: _ClassVar[int]
    PROFILE_ID_FIELD_NUMBER: _ClassVar[int]
    download_id: str
    profile_id: str
    def __init__(self, download_id: _Optional[str] = ..., profile_id: _Optional[str] = ...) -> None: ...
