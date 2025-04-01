from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class DownloadQueueInfo(_message.Message):
    __slots__ = ("download_queue_position",)
    DOWNLOAD_QUEUE_POSITION_FIELD_NUMBER: _ClassVar[int]
    download_queue_position: int
    def __init__(self, download_queue_position: _Optional[int] = ...) -> None: ...
