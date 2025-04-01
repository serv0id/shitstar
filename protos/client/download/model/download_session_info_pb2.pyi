from client.download.model import available_quality_pb2 as _available_quality_pb2
from client.player.model import player_and_device_info_pb2 as _player_and_device_info_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DownloadSessionInfo(_message.Message):
    __slots__ = ("id", "playback_tag", "is_drm_protected", "downloaded_quality", "player_and_device_info", "playback_url", "playback_url_host", "download_manager_version", "download_uuid")
    ID_FIELD_NUMBER: _ClassVar[int]
    PLAYBACK_TAG_FIELD_NUMBER: _ClassVar[int]
    IS_DRM_PROTECTED_FIELD_NUMBER: _ClassVar[int]
    DOWNLOADED_QUALITY_FIELD_NUMBER: _ClassVar[int]
    PLAYER_AND_DEVICE_INFO_FIELD_NUMBER: _ClassVar[int]
    PLAYBACK_URL_FIELD_NUMBER: _ClassVar[int]
    PLAYBACK_URL_HOST_FIELD_NUMBER: _ClassVar[int]
    DOWNLOAD_MANAGER_VERSION_FIELD_NUMBER: _ClassVar[int]
    DOWNLOAD_UUID_FIELD_NUMBER: _ClassVar[int]
    id: str
    playback_tag: str
    is_drm_protected: bool
    downloaded_quality: _available_quality_pb2.AvailableQuality
    player_and_device_info: _player_and_device_info_pb2.PlayerAndDeviceInfo
    playback_url: str
    playback_url_host: str
    download_manager_version: str
    download_uuid: str
    def __init__(self, id: _Optional[str] = ..., playback_tag: _Optional[str] = ..., is_drm_protected: bool = ..., downloaded_quality: _Optional[_Union[_available_quality_pb2.AvailableQuality, str]] = ..., player_and_device_info: _Optional[_Union[_player_and_device_info_pb2.PlayerAndDeviceInfo, _Mapping]] = ..., playback_url: _Optional[str] = ..., playback_url_host: _Optional[str] = ..., download_manager_version: _Optional[str] = ..., download_uuid: _Optional[str] = ...) -> None: ...
