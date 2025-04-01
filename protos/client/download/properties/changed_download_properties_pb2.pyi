from client.download.model import available_quality_pb2 as _available_quality_pb2
from client.download.model import download_session_info_pb2 as _download_session_info_pb2
from client.download.model import download_size_info_pb2 as _download_size_info_pb2
from client.download.model import download_stat_info_pb2 as _download_stat_info_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ChangedDownloadProperties(_message.Message):
    __slots__ = ("download_session_info", "download_stat_info", "download_size_info", "previous_download_id", "new_download_quality", "previous_download_quality", "is_remember_for_next_time")
    DOWNLOAD_SESSION_INFO_FIELD_NUMBER: _ClassVar[int]
    DOWNLOAD_STAT_INFO_FIELD_NUMBER: _ClassVar[int]
    DOWNLOAD_SIZE_INFO_FIELD_NUMBER: _ClassVar[int]
    PREVIOUS_DOWNLOAD_ID_FIELD_NUMBER: _ClassVar[int]
    NEW_DOWNLOAD_QUALITY_FIELD_NUMBER: _ClassVar[int]
    PREVIOUS_DOWNLOAD_QUALITY_FIELD_NUMBER: _ClassVar[int]
    IS_REMEMBER_FOR_NEXT_TIME_FIELD_NUMBER: _ClassVar[int]
    download_session_info: _download_session_info_pb2.DownloadSessionInfo
    download_stat_info: _download_stat_info_pb2.DownloadStatInfo
    download_size_info: _download_size_info_pb2.DownloadSizeInfo
    previous_download_id: str
    new_download_quality: _available_quality_pb2.AvailableQuality
    previous_download_quality: _available_quality_pb2.AvailableQuality
    is_remember_for_next_time: bool
    def __init__(self, download_session_info: _Optional[_Union[_download_session_info_pb2.DownloadSessionInfo, _Mapping]] = ..., download_stat_info: _Optional[_Union[_download_stat_info_pb2.DownloadStatInfo, _Mapping]] = ..., download_size_info: _Optional[_Union[_download_size_info_pb2.DownloadSizeInfo, _Mapping]] = ..., previous_download_id: _Optional[str] = ..., new_download_quality: _Optional[_Union[_available_quality_pb2.AvailableQuality, str]] = ..., previous_download_quality: _Optional[_Union[_available_quality_pb2.AvailableQuality, str]] = ..., is_remember_for_next_time: bool = ...) -> None: ...
