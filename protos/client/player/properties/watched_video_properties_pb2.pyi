from client.player.model import buffer_stats_pb2 as _buffer_stats_pb2
from client.player.model import playback_feed_info_pb2 as _playback_feed_info_pb2
from client.player.model import playback_mode_info_pb2 as _playback_mode_info_pb2
from client.player.model import playback_pip_mode_pb2 as _playback_pip_mode_pb2
from client.player.model import playback_session_info_pb2 as _playback_session_info_pb2
from client.player.model import playback_state_info_pb2 as _playback_state_info_pb2
from client.player.model import player_and_device_info_pb2 as _player_and_device_info_pb2
from client.player.model import watch_session_properties_pb2 as _watch_session_properties_pb2
from client.watch import preload_playback_properties_pb2 as _preload_playback_properties_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TriggerType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TRIGGER_TYPE_UNSPECIFIED: _ClassVar[TriggerType]
    TRIGGER_TYPE_VIDEO_QUALITY_CHANGE: _ClassVar[TriggerType]
    TRIGGER_TYPE_AUDIO_CHANGE: _ClassVar[TriggerType]
    TRIGGER_TYPE_CAPTION_CHANGE: _ClassVar[TriggerType]
    TRIGGER_TYPE_ORIENTATION_CHANGE: _ClassVar[TriggerType]
    TRIGGER_TYPE_PIP_ENTERED: _ClassVar[TriggerType]
    TRIGGER_TYPE_PIP_EXIT: _ClassVar[TriggerType]
    TRIGGER_TYPE_ERROR: _ClassVar[TriggerType]
    TRIGGER_TYPE_CASTING_STARTED: _ClassVar[TriggerType]
    TRIGGER_TYPE_VIDEO_PAUSED: _ClassVar[TriggerType]
    TRIGGER_TYPE_PLAYER_EXIT: _ClassVar[TriggerType]
    TRIGGER_TYPE_VIDEO_END_REACHED: _ClassVar[TriggerType]
    TRIGGER_TYPE_TAB_CHANGED: _ClassVar[TriggerType]
    TRIGGER_TYPE_IN_PIP_ENTERED: _ClassVar[TriggerType]
    TRIGGER_TYPE_IN_PIP_EXIT: _ClassVar[TriggerType]
    TRIGGER_TYPE_PLAYBACK_SPEED_CHANGE: _ClassVar[TriggerType]
    TRIGGER_TYPE_VIDEO_PAUSED_AUTO: _ClassVar[TriggerType]
    TRIGGER_TYPE_VIDEO_PAUSED_MANUAL: _ClassVar[TriggerType]
    TRIGGER_TYPE_VR_ENTERED: _ClassVar[TriggerType]
    TRIGGER_TYPE_VR_EXIT: _ClassVar[TriggerType]

class ActionType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ACTION_TYPE_UNSPECIFIED: _ClassVar[ActionType]
    ACTION_TYPE_SCREEN_INTERACTION: _ClassVar[ActionType]
    ACTION_TYPE_OTHERS: _ClassVar[ActionType]
TRIGGER_TYPE_UNSPECIFIED: TriggerType
TRIGGER_TYPE_VIDEO_QUALITY_CHANGE: TriggerType
TRIGGER_TYPE_AUDIO_CHANGE: TriggerType
TRIGGER_TYPE_CAPTION_CHANGE: TriggerType
TRIGGER_TYPE_ORIENTATION_CHANGE: TriggerType
TRIGGER_TYPE_PIP_ENTERED: TriggerType
TRIGGER_TYPE_PIP_EXIT: TriggerType
TRIGGER_TYPE_ERROR: TriggerType
TRIGGER_TYPE_CASTING_STARTED: TriggerType
TRIGGER_TYPE_VIDEO_PAUSED: TriggerType
TRIGGER_TYPE_PLAYER_EXIT: TriggerType
TRIGGER_TYPE_VIDEO_END_REACHED: TriggerType
TRIGGER_TYPE_TAB_CHANGED: TriggerType
TRIGGER_TYPE_IN_PIP_ENTERED: TriggerType
TRIGGER_TYPE_IN_PIP_EXIT: TriggerType
TRIGGER_TYPE_PLAYBACK_SPEED_CHANGE: TriggerType
TRIGGER_TYPE_VIDEO_PAUSED_AUTO: TriggerType
TRIGGER_TYPE_VIDEO_PAUSED_MANUAL: TriggerType
TRIGGER_TYPE_VR_ENTERED: TriggerType
TRIGGER_TYPE_VR_EXIT: TriggerType
ACTION_TYPE_UNSPECIFIED: ActionType
ACTION_TYPE_SCREEN_INTERACTION: ActionType
ACTION_TYPE_OTHERS: ActionType

class WatchedVideoProperties(_message.Message):
    __slots__ = ("player_and_device_info", "playback_session_info", "playback_state_info", "watch_session_properties", "buffer_stats", "playback_mode_info", "is_casting", "trigger_type", "active_tab", "playback_pip_mode", "action_type", "playback_pip_mode_v2", "is_preload", "preload_status", "playback_feed_info", "preload_journey_session_id", "free_timer_consumed_time_ms", "free_timer_accumulated_consumed_time_ms")
    PLAYER_AND_DEVICE_INFO_FIELD_NUMBER: _ClassVar[int]
    PLAYBACK_SESSION_INFO_FIELD_NUMBER: _ClassVar[int]
    PLAYBACK_STATE_INFO_FIELD_NUMBER: _ClassVar[int]
    WATCH_SESSION_PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    BUFFER_STATS_FIELD_NUMBER: _ClassVar[int]
    PLAYBACK_MODE_INFO_FIELD_NUMBER: _ClassVar[int]
    IS_CASTING_FIELD_NUMBER: _ClassVar[int]
    TRIGGER_TYPE_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_TAB_FIELD_NUMBER: _ClassVar[int]
    PLAYBACK_PIP_MODE_FIELD_NUMBER: _ClassVar[int]
    ACTION_TYPE_FIELD_NUMBER: _ClassVar[int]
    PLAYBACK_PIP_MODE_V2_FIELD_NUMBER: _ClassVar[int]
    IS_PRELOAD_FIELD_NUMBER: _ClassVar[int]
    PRELOAD_STATUS_FIELD_NUMBER: _ClassVar[int]
    PLAYBACK_FEED_INFO_FIELD_NUMBER: _ClassVar[int]
    PRELOAD_JOURNEY_SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    FREE_TIMER_CONSUMED_TIME_MS_FIELD_NUMBER: _ClassVar[int]
    FREE_TIMER_ACCUMULATED_CONSUMED_TIME_MS_FIELD_NUMBER: _ClassVar[int]
    player_and_device_info: _player_and_device_info_pb2.PlayerAndDeviceInfo
    playback_session_info: _playback_session_info_pb2.PlaybackSessionInfo
    playback_state_info: _playback_state_info_pb2.PlaybackStateInfo
    watch_session_properties: _watch_session_properties_pb2.WatchSessionProperties
    buffer_stats: _buffer_stats_pb2.BufferStats
    playback_mode_info: _playback_mode_info_pb2.PlaybackModeInfo
    is_casting: bool
    trigger_type: TriggerType
    active_tab: str
    playback_pip_mode: _playback_pip_mode_pb2.PlaybackPIPMode
    action_type: ActionType
    playback_pip_mode_v2: _playback_pip_mode_pb2.PlaybackPipMode
    is_preload: bool
    preload_status: _preload_playback_properties_pb2.PreloadPlaybackProperties.PreloadStatus
    playback_feed_info: _playback_feed_info_pb2.PlaybackFeedInfo
    preload_journey_session_id: str
    free_timer_consumed_time_ms: int
    free_timer_accumulated_consumed_time_ms: int
    def __init__(self, player_and_device_info: _Optional[_Union[_player_and_device_info_pb2.PlayerAndDeviceInfo, _Mapping]] = ..., playback_session_info: _Optional[_Union[_playback_session_info_pb2.PlaybackSessionInfo, _Mapping]] = ..., playback_state_info: _Optional[_Union[_playback_state_info_pb2.PlaybackStateInfo, _Mapping]] = ..., watch_session_properties: _Optional[_Union[_watch_session_properties_pb2.WatchSessionProperties, _Mapping]] = ..., buffer_stats: _Optional[_Union[_buffer_stats_pb2.BufferStats, _Mapping]] = ..., playback_mode_info: _Optional[_Union[_playback_mode_info_pb2.PlaybackModeInfo, _Mapping]] = ..., is_casting: bool = ..., trigger_type: _Optional[_Union[TriggerType, str]] = ..., active_tab: _Optional[str] = ..., playback_pip_mode: _Optional[_Union[_playback_pip_mode_pb2.PlaybackPIPMode, str]] = ..., action_type: _Optional[_Union[ActionType, str]] = ..., playback_pip_mode_v2: _Optional[_Union[_playback_pip_mode_pb2.PlaybackPipMode, str]] = ..., is_preload: bool = ..., preload_status: _Optional[_Union[_preload_playback_properties_pb2.PreloadPlaybackProperties.PreloadStatus, _Mapping]] = ..., playback_feed_info: _Optional[_Union[_playback_feed_info_pb2.PlaybackFeedInfo, _Mapping]] = ..., preload_journey_session_id: _Optional[str] = ..., free_timer_consumed_time_ms: _Optional[int] = ..., free_timer_accumulated_consumed_time_ms: _Optional[int] = ...) -> None: ...
