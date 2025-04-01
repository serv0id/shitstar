from client.player.model import buffer_stats_pb2 as _buffer_stats_pb2
from client.player.model import playback_error_info_pb2 as _playback_error_info_pb2
from client.player.model import playback_mode_info_pb2 as _playback_mode_info_pb2
from client.player.model import playback_pip_mode_pb2 as _playback_pip_mode_pb2
from client.player.model import playback_session_info_pb2 as _playback_session_info_pb2
from client.player.model import playback_state_info_pb2 as _playback_state_info_pb2
from client.player.model import player_and_device_info_pb2 as _player_and_device_info_pb2
from client.preload import preload_journey_pb2 as _preload_journey_pb2
from client.preload import preload_models_pb2 as _preload_models_pb2
from client.watch import preload_playback_properties_pb2 as _preload_playback_properties_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FailedVideoProperties(_message.Message):
    __slots__ = ("player_and_device_info", "playback_session_info", "playback_state_info", "playback_error_info", "buffer_stats", "playback_mode_info", "is_casting", "playback_pip_mode", "is_preload", "preload_status", "playback_pip_mode_v2", "preload_info", "preload_video_content_info", "free_timer_consumed_time_ms", "free_timer_accumulated_consumed_time_ms")
    PLAYER_AND_DEVICE_INFO_FIELD_NUMBER: _ClassVar[int]
    PLAYBACK_SESSION_INFO_FIELD_NUMBER: _ClassVar[int]
    PLAYBACK_STATE_INFO_FIELD_NUMBER: _ClassVar[int]
    PLAYBACK_ERROR_INFO_FIELD_NUMBER: _ClassVar[int]
    BUFFER_STATS_FIELD_NUMBER: _ClassVar[int]
    PLAYBACK_MODE_INFO_FIELD_NUMBER: _ClassVar[int]
    IS_CASTING_FIELD_NUMBER: _ClassVar[int]
    PLAYBACK_PIP_MODE_FIELD_NUMBER: _ClassVar[int]
    IS_PRELOAD_FIELD_NUMBER: _ClassVar[int]
    PRELOAD_STATUS_FIELD_NUMBER: _ClassVar[int]
    PLAYBACK_PIP_MODE_V2_FIELD_NUMBER: _ClassVar[int]
    PRELOAD_INFO_FIELD_NUMBER: _ClassVar[int]
    PRELOAD_VIDEO_CONTENT_INFO_FIELD_NUMBER: _ClassVar[int]
    FREE_TIMER_CONSUMED_TIME_MS_FIELD_NUMBER: _ClassVar[int]
    FREE_TIMER_ACCUMULATED_CONSUMED_TIME_MS_FIELD_NUMBER: _ClassVar[int]
    player_and_device_info: _player_and_device_info_pb2.PlayerAndDeviceInfo
    playback_session_info: _playback_session_info_pb2.PlaybackSessionInfo
    playback_state_info: _playback_state_info_pb2.PlaybackStateInfo
    playback_error_info: _playback_error_info_pb2.PlaybackErrorInfo
    buffer_stats: _buffer_stats_pb2.BufferStats
    playback_mode_info: _playback_mode_info_pb2.PlaybackModeInfo
    is_casting: bool
    playback_pip_mode: _playback_pip_mode_pb2.PlaybackPIPMode
    is_preload: bool
    preload_status: _preload_playback_properties_pb2.PreloadPlaybackProperties.PreloadStatus
    playback_pip_mode_v2: _playback_pip_mode_pb2.PlaybackPipMode
    preload_info: _preload_journey_pb2.PreloadAddition
    preload_video_content_info: _preload_models_pb2.PlaybackMetricsPreloadInfo
    free_timer_consumed_time_ms: int
    free_timer_accumulated_consumed_time_ms: int
    def __init__(self, player_and_device_info: _Optional[_Union[_player_and_device_info_pb2.PlayerAndDeviceInfo, _Mapping]] = ..., playback_session_info: _Optional[_Union[_playback_session_info_pb2.PlaybackSessionInfo, _Mapping]] = ..., playback_state_info: _Optional[_Union[_playback_state_info_pb2.PlaybackStateInfo, _Mapping]] = ..., playback_error_info: _Optional[_Union[_playback_error_info_pb2.PlaybackErrorInfo, _Mapping]] = ..., buffer_stats: _Optional[_Union[_buffer_stats_pb2.BufferStats, _Mapping]] = ..., playback_mode_info: _Optional[_Union[_playback_mode_info_pb2.PlaybackModeInfo, _Mapping]] = ..., is_casting: bool = ..., playback_pip_mode: _Optional[_Union[_playback_pip_mode_pb2.PlaybackPIPMode, str]] = ..., is_preload: bool = ..., preload_status: _Optional[_Union[_preload_playback_properties_pb2.PreloadPlaybackProperties.PreloadStatus, _Mapping]] = ..., playback_pip_mode_v2: _Optional[_Union[_playback_pip_mode_pb2.PlaybackPipMode, str]] = ..., preload_info: _Optional[_Union[_preload_journey_pb2.PreloadAddition, _Mapping]] = ..., preload_video_content_info: _Optional[_Union[_preload_models_pb2.PlaybackMetricsPreloadInfo, _Mapping]] = ..., free_timer_consumed_time_ms: _Optional[int] = ..., free_timer_accumulated_consumed_time_ms: _Optional[int] = ...) -> None: ...
