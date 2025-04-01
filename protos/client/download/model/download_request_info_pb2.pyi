from client.download.model import available_quality_pb2 as _available_quality_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DownloadRequestInfo(_message.Message):
    __slots__ = ("available_sizes", "highest_available_quality", "download_manager_name", "download_manager_version", "requested_quality", "is_bilingual_ui_opted_in", "available_qualities")
    class DownloadManagerName(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        DOWNLOAD_MANAGER_NAME_UNSPECIFIED: _ClassVar[DownloadRequestInfo.DownloadManagerName]
        DOWNLOAD_MANAGER_NAME_HS_ANDROID: _ClassVar[DownloadRequestInfo.DownloadManagerName]
        DOWNLOAD_MANAGER_NAME_HS_IOS: _ClassVar[DownloadRequestInfo.DownloadManagerName]
    DOWNLOAD_MANAGER_NAME_UNSPECIFIED: DownloadRequestInfo.DownloadManagerName
    DOWNLOAD_MANAGER_NAME_HS_ANDROID: DownloadRequestInfo.DownloadManagerName
    DOWNLOAD_MANAGER_NAME_HS_IOS: DownloadRequestInfo.DownloadManagerName
    AVAILABLE_SIZES_FIELD_NUMBER: _ClassVar[int]
    HIGHEST_AVAILABLE_QUALITY_FIELD_NUMBER: _ClassVar[int]
    DOWNLOAD_MANAGER_NAME_FIELD_NUMBER: _ClassVar[int]
    DOWNLOAD_MANAGER_VERSION_FIELD_NUMBER: _ClassVar[int]
    REQUESTED_QUALITY_FIELD_NUMBER: _ClassVar[int]
    IS_BILINGUAL_UI_OPTED_IN_FIELD_NUMBER: _ClassVar[int]
    AVAILABLE_QUALITIES_FIELD_NUMBER: _ClassVar[int]
    available_sizes: int
    highest_available_quality: _available_quality_pb2.AvailableQuality
    download_manager_name: DownloadRequestInfo.DownloadManagerName
    download_manager_version: str
    requested_quality: _available_quality_pb2.AvailableQuality
    is_bilingual_ui_opted_in: bool
    available_qualities: _containers.RepeatedScalarFieldContainer[_available_quality_pb2.AvailableQuality]
    def __init__(self, available_sizes: _Optional[int] = ..., highest_available_quality: _Optional[_Union[_available_quality_pb2.AvailableQuality, str]] = ..., download_manager_name: _Optional[_Union[DownloadRequestInfo.DownloadManagerName, str]] = ..., download_manager_version: _Optional[str] = ..., requested_quality: _Optional[_Union[_available_quality_pb2.AvailableQuality, str]] = ..., is_bilingual_ui_opted_in: bool = ..., available_qualities: _Optional[_Iterable[_Union[_available_quality_pb2.AvailableQuality, str]]] = ...) -> None: ...
