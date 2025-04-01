from client.player.model import client_capabilities_pb2 as _client_capabilities_pb2
from client.player.model import playback_mode_info_pb2 as _playback_mode_info_pb2
from client.player.model import playback_pip_mode_pb2 as _playback_pip_mode_pb2
from client.player.model import playback_session_info_pb2 as _playback_session_info_pb2
from client.player.model import stream_mode_pb2 as _stream_mode_pb2
from client.player.model import video_initiation_type_pb2 as _video_initiation_type_pb2
from client.preload import preload_journey_pb2 as _preload_journey_pb2
from client.preload import preload_models_pb2 as _preload_models_pb2
from client.watch import preload_playback_properties_pb2 as _preload_playback_properties_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FailedPlaybackApi(_message.Message):
    __slots__ = ("error_code", "error_http_status_code", "failed_url", "is_casting", "is_downloaded", "client_page_id", "play_type", "player_orientation", "playback_pip_mode", "is_preload", "preload_status", "player_version", "exception_message", "mode", "playback_pip_mode_v2", "client_capabilities", "is_retry_attempt", "total_time_to_failure_ms", "watch_session_id", "bff_source_type", "preload_bff_status", "previous_page_orientation", "initiation_source", "initiation_type", "client_playback_session_id", "stream_type")
    ERROR_CODE_FIELD_NUMBER: _ClassVar[int]
    ERROR_HTTP_STATUS_CODE_FIELD_NUMBER: _ClassVar[int]
    FAILED_URL_FIELD_NUMBER: _ClassVar[int]
    IS_CASTING_FIELD_NUMBER: _ClassVar[int]
    IS_DOWNLOADED_FIELD_NUMBER: _ClassVar[int]
    CLIENT_PAGE_ID_FIELD_NUMBER: _ClassVar[int]
    PLAY_TYPE_FIELD_NUMBER: _ClassVar[int]
    PLAYER_ORIENTATION_FIELD_NUMBER: _ClassVar[int]
    PLAYBACK_PIP_MODE_FIELD_NUMBER: _ClassVar[int]
    IS_PRELOAD_FIELD_NUMBER: _ClassVar[int]
    PRELOAD_STATUS_FIELD_NUMBER: _ClassVar[int]
    PLAYER_VERSION_FIELD_NUMBER: _ClassVar[int]
    EXCEPTION_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    MODE_FIELD_NUMBER: _ClassVar[int]
    PLAYBACK_PIP_MODE_V2_FIELD_NUMBER: _ClassVar[int]
    CLIENT_CAPABILITIES_FIELD_NUMBER: _ClassVar[int]
    IS_RETRY_ATTEMPT_FIELD_NUMBER: _ClassVar[int]
    TOTAL_TIME_TO_FAILURE_MS_FIELD_NUMBER: _ClassVar[int]
    WATCH_SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    BFF_SOURCE_TYPE_FIELD_NUMBER: _ClassVar[int]
    PRELOAD_BFF_STATUS_FIELD_NUMBER: _ClassVar[int]
    PREVIOUS_PAGE_ORIENTATION_FIELD_NUMBER: _ClassVar[int]
    INITIATION_SOURCE_FIELD_NUMBER: _ClassVar[int]
    INITIATION_TYPE_FIELD_NUMBER: _ClassVar[int]
    CLIENT_PLAYBACK_SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    STREAM_TYPE_FIELD_NUMBER: _ClassVar[int]
    error_code: str
    error_http_status_code: int
    failed_url: str
    is_casting: bool
    is_downloaded: bool
    client_page_id: str
    play_type: str
    player_orientation: _playback_mode_info_pb2.PlayerOrientation
    playback_pip_mode: _playback_pip_mode_pb2.PlaybackPIPMode
    is_preload: bool
    preload_status: _preload_playback_properties_pb2.PreloadPlaybackProperties.PreloadStatus
    player_version: str
    exception_message: str
    mode: _stream_mode_pb2.StreamMode
    playback_pip_mode_v2: _playback_pip_mode_pb2.PlaybackPipMode
    client_capabilities: _client_capabilities_pb2.ClientCapabilities
    is_retry_attempt: bool
    total_time_to_failure_ms: int
    watch_session_id: str
    bff_source_type: _preload_models_pb2.PreloadModels.DataSourceTypeDetail
    preload_bff_status: _preload_journey_pb2.PreloadStatus
    previous_page_orientation: _playback_mode_info_pb2.PlayerOrientation
    initiation_source: _video_initiation_type_pb2.VideoInitiationSource
    initiation_type: _video_initiation_type_pb2.VideoInitiationType
    client_playback_session_id: str
    stream_type: _playback_session_info_pb2.PlaybackSessionInfo.StreamType
    def __init__(self, error_code: _Optional[str] = ..., error_http_status_code: _Optional[int] = ..., failed_url: _Optional[str] = ..., is_casting: bool = ..., is_downloaded: bool = ..., client_page_id: _Optional[str] = ..., play_type: _Optional[str] = ..., player_orientation: _Optional[_Union[_playback_mode_info_pb2.PlayerOrientation, str]] = ..., playback_pip_mode: _Optional[_Union[_playback_pip_mode_pb2.PlaybackPIPMode, str]] = ..., is_preload: bool = ..., preload_status: _Optional[_Union[_preload_playback_properties_pb2.PreloadPlaybackProperties.PreloadStatus, _Mapping]] = ..., player_version: _Optional[str] = ..., exception_message: _Optional[str] = ..., mode: _Optional[_Union[_stream_mode_pb2.StreamMode, str]] = ..., playback_pip_mode_v2: _Optional[_Union[_playback_pip_mode_pb2.PlaybackPipMode, str]] = ..., client_capabilities: _Optional[_Union[_client_capabilities_pb2.ClientCapabilities, _Mapping]] = ..., is_retry_attempt: bool = ..., total_time_to_failure_ms: _Optional[int] = ..., watch_session_id: _Optional[str] = ..., bff_source_type: _Optional[_Union[_preload_models_pb2.PreloadModels.DataSourceTypeDetail, _Mapping]] = ..., preload_bff_status: _Optional[_Union[_preload_journey_pb2.PreloadStatus, str]] = ..., previous_page_orientation: _Optional[_Union[_playback_mode_info_pb2.PlayerOrientation, str]] = ..., initiation_source: _Optional[_Union[_video_initiation_type_pb2.VideoInitiationSource, str]] = ..., initiation_type: _Optional[_Union[_video_initiation_type_pb2.VideoInitiationType, str]] = ..., client_playback_session_id: _Optional[str] = ..., stream_type: _Optional[_Union[_playback_session_info_pb2.PlaybackSessionInfo.StreamType, str]] = ...) -> None: ...
