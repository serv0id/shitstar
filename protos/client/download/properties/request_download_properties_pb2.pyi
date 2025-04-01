from client.download.model import download_request_info_pb2 as _download_request_info_pb2
from client.download.model import download_session_info_pb2 as _download_session_info_pb2
from client.download.model import download_size_info_pb2 as _download_size_info_pb2
from client.download.model import download_stat_info_pb2 as _download_stat_info_pb2
from client.download.model import journey_type_pb2 as _journey_type_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class RequestDownloadProperties(_message.Message):
    __slots__ = ("download_session_info", "download_stat_info", "download_size_info", "download_request_info", "journey_type", "requested_journey_type")
    class JourneyType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        JOURNEY_TYPE_UNSPECIFIED: _ClassVar[RequestDownloadProperties.JourneyType]
        JOURNEY_TYPE_NORMAL: _ClassVar[RequestDownloadProperties.JourneyType]
        JOURNEY_TYPE_RETRY_MANUAL: _ClassVar[RequestDownloadProperties.JourneyType]
        JOURNEY_TYPE_RETRY_AUTO: _ClassVar[RequestDownloadProperties.JourneyType]
    JOURNEY_TYPE_UNSPECIFIED: RequestDownloadProperties.JourneyType
    JOURNEY_TYPE_NORMAL: RequestDownloadProperties.JourneyType
    JOURNEY_TYPE_RETRY_MANUAL: RequestDownloadProperties.JourneyType
    JOURNEY_TYPE_RETRY_AUTO: RequestDownloadProperties.JourneyType
    DOWNLOAD_SESSION_INFO_FIELD_NUMBER: _ClassVar[int]
    DOWNLOAD_STAT_INFO_FIELD_NUMBER: _ClassVar[int]
    DOWNLOAD_SIZE_INFO_FIELD_NUMBER: _ClassVar[int]
    DOWNLOAD_REQUEST_INFO_FIELD_NUMBER: _ClassVar[int]
    JOURNEY_TYPE_FIELD_NUMBER: _ClassVar[int]
    REQUESTED_JOURNEY_TYPE_FIELD_NUMBER: _ClassVar[int]
    download_session_info: _download_session_info_pb2.DownloadSessionInfo
    download_stat_info: _download_stat_info_pb2.DownloadStatInfo
    download_size_info: _download_size_info_pb2.DownloadSizeInfo
    download_request_info: _download_request_info_pb2.DownloadRequestInfo
    journey_type: RequestDownloadProperties.JourneyType
    requested_journey_type: _journey_type_pb2.JourneyType
    def __init__(self, download_session_info: _Optional[_Union[_download_session_info_pb2.DownloadSessionInfo, _Mapping]] = ..., download_stat_info: _Optional[_Union[_download_stat_info_pb2.DownloadStatInfo, _Mapping]] = ..., download_size_info: _Optional[_Union[_download_size_info_pb2.DownloadSizeInfo, _Mapping]] = ..., download_request_info: _Optional[_Union[_download_request_info_pb2.DownloadRequestInfo, _Mapping]] = ..., journey_type: _Optional[_Union[RequestDownloadProperties.JourneyType, str]] = ..., requested_journey_type: _Optional[_Union[_journey_type_pb2.JourneyType, str]] = ...) -> None: ...
