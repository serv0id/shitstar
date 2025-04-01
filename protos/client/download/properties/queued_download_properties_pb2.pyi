from client.download.model import download_queue_info_pb2 as _download_queue_info_pb2
from client.download.model import download_request_info_pb2 as _download_request_info_pb2
from client.download.model import download_session_info_pb2 as _download_session_info_pb2
from client.download.model import download_size_info_pb2 as _download_size_info_pb2
from client.download.model import download_stat_info_pb2 as _download_stat_info_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class QueuedDownloadProperties(_message.Message):
    __slots__ = ("download_session_info", "download_stat_info", "download_size_info", "download_request_info", "download_queue_info")
    DOWNLOAD_SESSION_INFO_FIELD_NUMBER: _ClassVar[int]
    DOWNLOAD_STAT_INFO_FIELD_NUMBER: _ClassVar[int]
    DOWNLOAD_SIZE_INFO_FIELD_NUMBER: _ClassVar[int]
    DOWNLOAD_REQUEST_INFO_FIELD_NUMBER: _ClassVar[int]
    DOWNLOAD_QUEUE_INFO_FIELD_NUMBER: _ClassVar[int]
    download_session_info: _download_session_info_pb2.DownloadSessionInfo
    download_stat_info: _download_stat_info_pb2.DownloadStatInfo
    download_size_info: _download_size_info_pb2.DownloadSizeInfo
    download_request_info: _download_request_info_pb2.DownloadRequestInfo
    download_queue_info: _download_queue_info_pb2.DownloadQueueInfo
    def __init__(self, download_session_info: _Optional[_Union[_download_session_info_pb2.DownloadSessionInfo, _Mapping]] = ..., download_stat_info: _Optional[_Union[_download_stat_info_pb2.DownloadStatInfo, _Mapping]] = ..., download_size_info: _Optional[_Union[_download_size_info_pb2.DownloadSizeInfo, _Mapping]] = ..., download_request_info: _Optional[_Union[_download_request_info_pb2.DownloadRequestInfo, _Mapping]] = ..., download_queue_info: _Optional[_Union[_download_queue_info_pb2.DownloadQueueInfo, _Mapping]] = ...) -> None: ...
