from client.download.model import download_session_info_pb2 as _download_session_info_pb2
from client.download.model import download_stat_info_pb2 as _download_stat_info_pb2
from client.download.model import download_state_pb2 as _download_state_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ActiveDownloadProperties(_message.Message):
    __slots__ = ("download_session_info", "download_stat_info", "deleted_content_info", "previous_download_state")
    DOWNLOAD_SESSION_INFO_FIELD_NUMBER: _ClassVar[int]
    DOWNLOAD_STAT_INFO_FIELD_NUMBER: _ClassVar[int]
    DELETED_CONTENT_INFO_FIELD_NUMBER: _ClassVar[int]
    PREVIOUS_DOWNLOAD_STATE_FIELD_NUMBER: _ClassVar[int]
    download_session_info: _download_session_info_pb2.DownloadSessionInfo
    download_stat_info: _download_stat_info_pb2.DownloadStatInfo
    deleted_content_info: DeletedContentInfo
    previous_download_state: _download_state_pb2.DownloadState
    def __init__(self, download_session_info: _Optional[_Union[_download_session_info_pb2.DownloadSessionInfo, _Mapping]] = ..., download_stat_info: _Optional[_Union[_download_stat_info_pb2.DownloadStatInfo, _Mapping]] = ..., deleted_content_info: _Optional[_Union[DeletedContentInfo, _Mapping]] = ..., previous_download_state: _Optional[_Union[_download_state_pb2.DownloadState, str]] = ...) -> None: ...

class DeletedContentInfo(_message.Message):
    __slots__ = ("is_bulk_delete", "content_ids")
    IS_BULK_DELETE_FIELD_NUMBER: _ClassVar[int]
    CONTENT_IDS_FIELD_NUMBER: _ClassVar[int]
    is_bulk_delete: bool
    content_ids: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, is_bulk_delete: bool = ..., content_ids: _Optional[_Iterable[str]] = ...) -> None: ...
