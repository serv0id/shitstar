from client.preload import preload_journey_pb2 as _preload_journey_pb2
from client.watch import player_manager_properties_pb2 as _player_manager_properties_pb2
from client.watch import preload_playback_properties_pb2 as _preload_playback_properties_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class WatchPageLoadedProperties(_message.Message):
    __slots__ = ("bff_preparation_time_ms", "time_between_bff_and_player_ms", "player_load_time_ms", "is_player_already_loaded", "is_cast", "player_setup_time_ms", "player_load_content_time_ms", "player_after_load_content_time_ms", "player_manager_properties", "preload_status", "triggered_by_up_next_ios_only", "preload_in_watch", "player_version", "player_manifest_parse_manifest_ms", "player_manifest_init_drm_ms", "player_manifest_load_ms", "player_manifest_combine_periods_ms", "player_manifest_media_capabilities_ms", "player_manifest_license_ms", "watch_session_id", "preload_info", "watch_player_client_capability_time_ms")
    BFF_PREPARATION_TIME_MS_FIELD_NUMBER: _ClassVar[int]
    TIME_BETWEEN_BFF_AND_PLAYER_MS_FIELD_NUMBER: _ClassVar[int]
    PLAYER_LOAD_TIME_MS_FIELD_NUMBER: _ClassVar[int]
    IS_PLAYER_ALREADY_LOADED_FIELD_NUMBER: _ClassVar[int]
    IS_CAST_FIELD_NUMBER: _ClassVar[int]
    PLAYER_SETUP_TIME_MS_FIELD_NUMBER: _ClassVar[int]
    PLAYER_LOAD_CONTENT_TIME_MS_FIELD_NUMBER: _ClassVar[int]
    PLAYER_AFTER_LOAD_CONTENT_TIME_MS_FIELD_NUMBER: _ClassVar[int]
    PLAYER_MANAGER_PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    PRELOAD_STATUS_FIELD_NUMBER: _ClassVar[int]
    TRIGGERED_BY_UP_NEXT_IOS_ONLY_FIELD_NUMBER: _ClassVar[int]
    PRELOAD_IN_WATCH_FIELD_NUMBER: _ClassVar[int]
    PLAYER_VERSION_FIELD_NUMBER: _ClassVar[int]
    PLAYER_MANIFEST_PARSE_MANIFEST_MS_FIELD_NUMBER: _ClassVar[int]
    PLAYER_MANIFEST_INIT_DRM_MS_FIELD_NUMBER: _ClassVar[int]
    PLAYER_MANIFEST_LOAD_MS_FIELD_NUMBER: _ClassVar[int]
    PLAYER_MANIFEST_COMBINE_PERIODS_MS_FIELD_NUMBER: _ClassVar[int]
    PLAYER_MANIFEST_MEDIA_CAPABILITIES_MS_FIELD_NUMBER: _ClassVar[int]
    PLAYER_MANIFEST_LICENSE_MS_FIELD_NUMBER: _ClassVar[int]
    WATCH_SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    PRELOAD_INFO_FIELD_NUMBER: _ClassVar[int]
    WATCH_PLAYER_CLIENT_CAPABILITY_TIME_MS_FIELD_NUMBER: _ClassVar[int]
    bff_preparation_time_ms: int
    time_between_bff_and_player_ms: int
    player_load_time_ms: int
    is_player_already_loaded: bool
    is_cast: bool
    player_setup_time_ms: int
    player_load_content_time_ms: int
    player_after_load_content_time_ms: int
    player_manager_properties: _player_manager_properties_pb2.PlayerManagerProperties
    preload_status: _preload_playback_properties_pb2.PreloadPlaybackProperties.PreloadStatus
    triggered_by_up_next_ios_only: bool
    preload_in_watch: bool
    player_version: str
    player_manifest_parse_manifest_ms: int
    player_manifest_init_drm_ms: int
    player_manifest_load_ms: int
    player_manifest_combine_periods_ms: int
    player_manifest_media_capabilities_ms: int
    player_manifest_license_ms: int
    watch_session_id: str
    preload_info: _preload_journey_pb2.PreloadAddition
    watch_player_client_capability_time_ms: int
    def __init__(self, bff_preparation_time_ms: _Optional[int] = ..., time_between_bff_and_player_ms: _Optional[int] = ..., player_load_time_ms: _Optional[int] = ..., is_player_already_loaded: bool = ..., is_cast: bool = ..., player_setup_time_ms: _Optional[int] = ..., player_load_content_time_ms: _Optional[int] = ..., player_after_load_content_time_ms: _Optional[int] = ..., player_manager_properties: _Optional[_Union[_player_manager_properties_pb2.PlayerManagerProperties, _Mapping]] = ..., preload_status: _Optional[_Union[_preload_playback_properties_pb2.PreloadPlaybackProperties.PreloadStatus, _Mapping]] = ..., triggered_by_up_next_ios_only: bool = ..., preload_in_watch: bool = ..., player_version: _Optional[str] = ..., player_manifest_parse_manifest_ms: _Optional[int] = ..., player_manifest_init_drm_ms: _Optional[int] = ..., player_manifest_load_ms: _Optional[int] = ..., player_manifest_combine_periods_ms: _Optional[int] = ..., player_manifest_media_capabilities_ms: _Optional[int] = ..., player_manifest_license_ms: _Optional[int] = ..., watch_session_id: _Optional[str] = ..., preload_info: _Optional[_Union[_preload_journey_pb2.PreloadAddition, _Mapping]] = ..., watch_player_client_capability_time_ms: _Optional[int] = ...) -> None: ...
