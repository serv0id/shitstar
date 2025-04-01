from client.download.model import download_error_info_pb2 as _download_error_info_pb2
from client.download.model import download_session_info_pb2 as _download_session_info_pb2
from client.download.model import download_size_info_pb2 as _download_size_info_pb2
from client.download.model import download_stat_info_pb2 as _download_stat_info_pb2
from client.download.model import journey_type_pb2 as _journey_type_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FailedDownloadProperties(_message.Message):
    __slots__ = ("download_session_info", "download_stat_info", "download_size_info", "download_error_info", "average_speed_in_mbps", "failed_journey_type")
    DOWNLOAD_SESSION_INFO_FIELD_NUMBER: _ClassVar[int]
    DOWNLOAD_STAT_INFO_FIELD_NUMBER: _ClassVar[int]
    DOWNLOAD_SIZE_INFO_FIELD_NUMBER: _ClassVar[int]
    DOWNLOAD_ERROR_INFO_FIELD_NUMBER: _ClassVar[int]
    AVERAGE_SPEED_IN_MBPS_FIELD_NUMBER: _ClassVar[int]
    FAILED_JOURNEY_TYPE_FIELD_NUMBER: _ClassVar[int]
    download_session_info: _download_session_info_pb2.DownloadSessionInfo
    download_stat_info: _download_stat_info_pb2.DownloadStatInfo
    download_size_info: _download_size_info_pb2.DownloadSizeInfo
    download_error_info: _download_error_info_pb2.DownloadErrorInfo
    average_speed_in_mbps: int
    failed_journey_type: _journey_type_pb2.JourneyType
    def __init__(self, download_session_info: _Optional[_Union[_download_session_info_pb2.DownloadSessionInfo, _Mapping]] = ..., download_stat_info: _Optional[_Union[_download_stat_info_pb2.DownloadStatInfo, _Mapping]] = ..., download_size_info: _Optional[_Union[_download_size_info_pb2.DownloadSizeInfo, _Mapping]] = ..., download_error_info: _Optional[_Union[_download_error_info_pb2.DownloadErrorInfo, _Mapping]] = ..., average_speed_in_mbps: _Optional[int] = ..., failed_journey_type: _Optional[_Union[_journey_type_pb2.JourneyType, str]] = ...) -> None: ...
