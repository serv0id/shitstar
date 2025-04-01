from client.player.model import playback_feed_info_pb2 as _playback_feed_info_pb2
from client.player.model import playback_mode_info_pb2 as _playback_mode_info_pb2
from client.player.model import playback_pip_mode_pb2 as _playback_pip_mode_pb2
from client.player.model import playback_session_info_pb2 as _playback_session_info_pb2
from client.player.model import playback_state_info_pb2 as _playback_state_info_pb2
from client.player.model import player_and_device_info_pb2 as _player_and_device_info_pb2
from client.player.model import video_start_info_pb2 as _video_start_info_pb2
from client.preload import preload_journey_pb2 as _preload_journey_pb2
from client.preload import preload_models_pb2 as _preload_models_pb2
from client.watch import preload_playback_properties_pb2 as _preload_playback_properties_pb2
from component.freetimer import free_timer_pb2 as _free_timer_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class StartedVideoProperties(_message.Message):
    __slots__ = ("player_and_device_info", "playback_session_info", "playback_state_info", "video_start_info", "playback_mode_info", "is_casting", "playback_pip_mode", "is_preload", "preload_status", "playback_pip_mode_v2", "watch_page_load_time_ms", "playback_feed_info", "is_first_frame_after_watch_attempt", "preload_addition", "preload_info", "preload_video_content_info", "player_load_time_ms", "player_setup_time_ms", "player_load_content_time_ms", "player_after_load_content_time_ms", "free_timer_consumed_time_ms", "free_timer_accumulated_consumed_time_ms", "free_timer_real_source")
    PLAYER_AND_DEVICE_INFO_FIELD_NUMBER: _ClassVar[int]
    PLAYBACK_SESSION_INFO_FIELD_NUMBER: _ClassVar[int]
    PLAYBACK_STATE_INFO_FIELD_NUMBER: _ClassVar[int]
    VIDEO_START_INFO_FIELD_NUMBER: _ClassVar[int]
    PLAYBACK_MODE_INFO_FIELD_NUMBER: _ClassVar[int]
    IS_CASTING_FIELD_NUMBER: _ClassVar[int]
    PLAYBACK_PIP_MODE_FIELD_NUMBER: _ClassVar[int]
    IS_PRELOAD_FIELD_NUMBER: _ClassVar[int]
    PRELOAD_STATUS_FIELD_NUMBER: _ClassVar[int]
    PLAYBACK_PIP_MODE_V2_FIELD_NUMBER: _ClassVar[int]
    WATCH_PAGE_LOAD_TIME_MS_FIELD_NUMBER: _ClassVar[int]
    PLAYBACK_FEED_INFO_FIELD_NUMBER: _ClassVar[int]
    IS_FIRST_FRAME_AFTER_WATCH_ATTEMPT_FIELD_NUMBER: _ClassVar[int]
    PRELOAD_ADDITION_FIELD_NUMBER: _ClassVar[int]
    PRELOAD_INFO_FIELD_NUMBER: _ClassVar[int]
    PRELOAD_VIDEO_CONTENT_INFO_FIELD_NUMBER: _ClassVar[int]
    PLAYER_LOAD_TIME_MS_FIELD_NUMBER: _ClassVar[int]
    PLAYER_SETUP_TIME_MS_FIELD_NUMBER: _ClassVar[int]
    PLAYER_LOAD_CONTENT_TIME_MS_FIELD_NUMBER: _ClassVar[int]
    PLAYER_AFTER_LOAD_CONTENT_TIME_MS_FIELD_NUMBER: _ClassVar[int]
    FREE_TIMER_CONSUMED_TIME_MS_FIELD_NUMBER: _ClassVar[int]
    FREE_TIMER_ACCUMULATED_CONSUMED_TIME_MS_FIELD_NUMBER: _ClassVar[int]
    FREE_TIMER_REAL_SOURCE_FIELD_NUMBER: _ClassVar[int]
    player_and_device_info: _player_and_device_info_pb2.PlayerAndDeviceInfo
    playback_session_info: _playback_session_info_pb2.PlaybackSessionInfo
    playback_state_info: _playback_state_info_pb2.PlaybackStateInfo
    video_start_info: _video_start_info_pb2.VideoStartInfo
    playback_mode_info: _playback_mode_info_pb2.PlaybackModeInfo
    is_casting: bool
    playback_pip_mode: _playback_pip_mode_pb2.PlaybackPIPMode
    is_preload: bool
    preload_status: _preload_playback_properties_pb2.PreloadPlaybackProperties.PreloadStatus
    playback_pip_mode_v2: _playback_pip_mode_pb2.PlaybackPipMode
    watch_page_load_time_ms: int
    playback_feed_info: _playback_feed_info_pb2.PlaybackFeedInfo
    is_first_frame_after_watch_attempt: bool
    preload_addition: _preload_journey_pb2.PreloadAddition
    preload_info: _preload_journey_pb2.PreloadAddition
    preload_video_content_info: _preload_models_pb2.PlaybackMetricsPreloadInfo
    player_load_time_ms: int
    player_setup_time_ms: int
    player_load_content_time_ms: int
    player_after_load_content_time_ms: int
    free_timer_consumed_time_ms: int
    free_timer_accumulated_consumed_time_ms: int
    free_timer_real_source: _free_timer_pb2.FreeTimerRealSource
    def __init__(self, player_and_device_info: _Optional[_Union[_player_and_device_info_pb2.PlayerAndDeviceInfo, _Mapping]] = ..., playback_session_info: _Optional[_Union[_playback_session_info_pb2.PlaybackSessionInfo, _Mapping]] = ..., playback_state_info: _Optional[_Union[_playback_state_info_pb2.PlaybackStateInfo, _Mapping]] = ..., video_start_info: _Optional[_Union[_video_start_info_pb2.VideoStartInfo, _Mapping]] = ..., playback_mode_info: _Optional[_Union[_playback_mode_info_pb2.PlaybackModeInfo, _Mapping]] = ..., is_casting: bool = ..., playback_pip_mode: _Optional[_Union[_playback_pip_mode_pb2.PlaybackPIPMode, str]] = ..., is_preload: bool = ..., preload_status: _Optional[_Union[_preload_playback_properties_pb2.PreloadPlaybackProperties.PreloadStatus, _Mapping]] = ..., playback_pip_mode_v2: _Optional[_Union[_playback_pip_mode_pb2.PlaybackPipMode, str]] = ..., watch_page_load_time_ms: _Optional[int] = ..., playback_feed_info: _Optional[_Union[_playback_feed_info_pb2.PlaybackFeedInfo, _Mapping]] = ..., is_first_frame_after_watch_attempt: bool = ..., preload_addition: _Optional[_Union[_preload_journey_pb2.PreloadAddition, _Mapping]] = ..., preload_info: _Optional[_Union[_preload_journey_pb2.PreloadAddition, _Mapping]] = ..., preload_video_content_info: _Optional[_Union[_preload_models_pb2.PlaybackMetricsPreloadInfo, _Mapping]] = ..., player_load_time_ms: _Optional[int] = ..., player_setup_time_ms: _Optional[int] = ..., player_load_content_time_ms: _Optional[int] = ..., player_after_load_content_time_ms: _Optional[int] = ..., free_timer_consumed_time_ms: _Optional[int] = ..., free_timer_accumulated_consumed_time_ms: _Optional[int] = ..., free_timer_real_source: _Optional[_Union[_free_timer_pb2.FreeTimerRealSource, str]] = ...) -> None: ...
