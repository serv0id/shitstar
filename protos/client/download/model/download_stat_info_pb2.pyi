from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class DownloadStatInfo(_message.Message):
    __slots__ = ("active_download_time_ms", "total_download_time_ms", "percentage_downloaded", "percentage_downloaded_round")
    ACTIVE_DOWNLOAD_TIME_MS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_DOWNLOAD_TIME_MS_FIELD_NUMBER: _ClassVar[int]
    PERCENTAGE_DOWNLOADED_FIELD_NUMBER: _ClassVar[int]
    PERCENTAGE_DOWNLOADED_ROUND_FIELD_NUMBER: _ClassVar[int]
    active_download_time_ms: int
    total_download_time_ms: int
    percentage_downloaded: float
    percentage_downloaded_round: int
    def __init__(self, active_download_time_ms: _Optional[int] = ..., total_download_time_ms: _Optional[int] = ..., percentage_downloaded: _Optional[float] = ..., percentage_downloaded_round: _Optional[int] = ...) -> None: ...
