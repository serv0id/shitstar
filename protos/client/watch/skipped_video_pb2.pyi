from client.player.model import playback_pip_mode_pb2 as _playback_pip_mode_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SkippedVideoProperties(_message.Message):
    __slots__ = ("action_duration_secs", "direction", "skip_type", "start_pos_secs", "end_pos_secs", "action_duration_millisecs", "skip_type_v2", "action_type", "is_casting", "action_pos_sec", "is_downloaded", "playback_pip_mode", "player_version", "playback_pip_mode_v2")
    class SkipDirection(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SKIP_DIRECTION_UNSPECIFIED: _ClassVar[SkippedVideoProperties.SkipDirection]
        SKIP_DIRECTION_FORWARD: _ClassVar[SkippedVideoProperties.SkipDirection]
        SKIP_DIRECTION_BACKWARD: _ClassVar[SkippedVideoProperties.SkipDirection]
    SKIP_DIRECTION_UNSPECIFIED: SkippedVideoProperties.SkipDirection
    SKIP_DIRECTION_FORWARD: SkippedVideoProperties.SkipDirection
    SKIP_DIRECTION_BACKWARD: SkippedVideoProperties.SkipDirection
    class SkipType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SKIP_TYPE_UNSPECIFIED: _ClassVar[SkippedVideoProperties.SkipType]
        SKIP_TYPE_SKIP_INTRO: _ClassVar[SkippedVideoProperties.SkipType]
        SKIP_TYPE_SKIP_RECAP: _ClassVar[SkippedVideoProperties.SkipType]
        SKIP_TYPE_SKIP_CREDITS: _ClassVar[SkippedVideoProperties.SkipType]
        SKIP_TYPE_FAST_SEEK: _ClassVar[SkippedVideoProperties.SkipType]
        SKIP_TYPE_SLOW_SEEK: _ClassVar[SkippedVideoProperties.SkipType]
        SKIP_TYPE_SEEK_CANCELLED: _ClassVar[SkippedVideoProperties.SkipType]
        SKIP_TYPE_WATCH_CREDITS: _ClassVar[SkippedVideoProperties.SkipType]
        SKIP_TYPE_UP_NEXT: _ClassVar[SkippedVideoProperties.SkipType]
        SKIP_TYPE_NEXT_EPISODE: _ClassVar[SkippedVideoProperties.SkipType]
        SKIP_TYPE_NORMAL: _ClassVar[SkippedVideoProperties.SkipType]
        SKIP_TYPE_GO_LIVE: _ClassVar[SkippedVideoProperties.SkipType]
        SKIP_TYPE_GO_BACK: _ClassVar[SkippedVideoProperties.SkipType]
        SKIP_TYPE_NEXT_KEY_MOMENT: _ClassVar[SkippedVideoProperties.SkipType]
        SKIP_TYPE_WATCH_INTRO: _ClassVar[SkippedVideoProperties.SkipType]
        SKIP_TYPE_WATCH_RECAP: _ClassVar[SkippedVideoProperties.SkipType]
    SKIP_TYPE_UNSPECIFIED: SkippedVideoProperties.SkipType
    SKIP_TYPE_SKIP_INTRO: SkippedVideoProperties.SkipType
    SKIP_TYPE_SKIP_RECAP: SkippedVideoProperties.SkipType
    SKIP_TYPE_SKIP_CREDITS: SkippedVideoProperties.SkipType
    SKIP_TYPE_FAST_SEEK: SkippedVideoProperties.SkipType
    SKIP_TYPE_SLOW_SEEK: SkippedVideoProperties.SkipType
    SKIP_TYPE_SEEK_CANCELLED: SkippedVideoProperties.SkipType
    SKIP_TYPE_WATCH_CREDITS: SkippedVideoProperties.SkipType
    SKIP_TYPE_UP_NEXT: SkippedVideoProperties.SkipType
    SKIP_TYPE_NEXT_EPISODE: SkippedVideoProperties.SkipType
    SKIP_TYPE_NORMAL: SkippedVideoProperties.SkipType
    SKIP_TYPE_GO_LIVE: SkippedVideoProperties.SkipType
    SKIP_TYPE_GO_BACK: SkippedVideoProperties.SkipType
    SKIP_TYPE_NEXT_KEY_MOMENT: SkippedVideoProperties.SkipType
    SKIP_TYPE_WATCH_INTRO: SkippedVideoProperties.SkipType
    SKIP_TYPE_WATCH_RECAP: SkippedVideoProperties.SkipType
    class ActionType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ACTION_TYPE_UNSPECIFIED: _ClassVar[SkippedVideoProperties.ActionType]
        ACTION_TYPE_SEEK: _ClassVar[SkippedVideoProperties.ActionType]
        ACTION_TYPE_CLICK: _ClassVar[SkippedVideoProperties.ActionType]
        ACTION_TYPE_DOUBLE_CLICK: _ClassVar[SkippedVideoProperties.ActionType]
        ACTION_TYPE_MILESTONE_CLICK: _ClassVar[SkippedVideoProperties.ActionType]
        ACTION_TYPE_ARROW_KEYS: _ClassVar[SkippedVideoProperties.ActionType]
        ACTION_TYPE_SEEKTRAY_SCROLLING: _ClassVar[SkippedVideoProperties.ActionType]
        ACTION_TYPE_AUTO: _ClassVar[SkippedVideoProperties.ActionType]
        ACTION_TYPE_SEEK_VOICE: _ClassVar[SkippedVideoProperties.ActionType]
        ACTION_TYPE_VOICE: _ClassVar[SkippedVideoProperties.ActionType]
        ACTION_TYPE_SEEK_MEDIA_ACTION: _ClassVar[SkippedVideoProperties.ActionType]
    ACTION_TYPE_UNSPECIFIED: SkippedVideoProperties.ActionType
    ACTION_TYPE_SEEK: SkippedVideoProperties.ActionType
    ACTION_TYPE_CLICK: SkippedVideoProperties.ActionType
    ACTION_TYPE_DOUBLE_CLICK: SkippedVideoProperties.ActionType
    ACTION_TYPE_MILESTONE_CLICK: SkippedVideoProperties.ActionType
    ACTION_TYPE_ARROW_KEYS: SkippedVideoProperties.ActionType
    ACTION_TYPE_SEEKTRAY_SCROLLING: SkippedVideoProperties.ActionType
    ACTION_TYPE_AUTO: SkippedVideoProperties.ActionType
    ACTION_TYPE_SEEK_VOICE: SkippedVideoProperties.ActionType
    ACTION_TYPE_VOICE: SkippedVideoProperties.ActionType
    ACTION_TYPE_SEEK_MEDIA_ACTION: SkippedVideoProperties.ActionType
    ACTION_DURATION_SECS_FIELD_NUMBER: _ClassVar[int]
    DIRECTION_FIELD_NUMBER: _ClassVar[int]
    SKIP_TYPE_FIELD_NUMBER: _ClassVar[int]
    START_POS_SECS_FIELD_NUMBER: _ClassVar[int]
    END_POS_SECS_FIELD_NUMBER: _ClassVar[int]
    ACTION_DURATION_MILLISECS_FIELD_NUMBER: _ClassVar[int]
    SKIP_TYPE_V2_FIELD_NUMBER: _ClassVar[int]
    ACTION_TYPE_FIELD_NUMBER: _ClassVar[int]
    IS_CASTING_FIELD_NUMBER: _ClassVar[int]
    ACTION_POS_SEC_FIELD_NUMBER: _ClassVar[int]
    IS_DOWNLOADED_FIELD_NUMBER: _ClassVar[int]
    PLAYBACK_PIP_MODE_FIELD_NUMBER: _ClassVar[int]
    PLAYER_VERSION_FIELD_NUMBER: _ClassVar[int]
    PLAYBACK_PIP_MODE_V2_FIELD_NUMBER: _ClassVar[int]
    action_duration_secs: int
    direction: SkippedVideoProperties.SkipDirection
    skip_type: str
    start_pos_secs: int
    end_pos_secs: int
    action_duration_millisecs: int
    skip_type_v2: SkippedVideoProperties.SkipType
    action_type: SkippedVideoProperties.ActionType
    is_casting: bool
    action_pos_sec: int
    is_downloaded: bool
    playback_pip_mode: _playback_pip_mode_pb2.PlaybackPIPMode
    player_version: str
    playback_pip_mode_v2: _playback_pip_mode_pb2.PlaybackPipMode
    def __init__(self, action_duration_secs: _Optional[int] = ..., direction: _Optional[_Union[SkippedVideoProperties.SkipDirection, str]] = ..., skip_type: _Optional[str] = ..., start_pos_secs: _Optional[int] = ..., end_pos_secs: _Optional[int] = ..., action_duration_millisecs: _Optional[int] = ..., skip_type_v2: _Optional[_Union[SkippedVideoProperties.SkipType, str]] = ..., action_type: _Optional[_Union[SkippedVideoProperties.ActionType, str]] = ..., is_casting: bool = ..., action_pos_sec: _Optional[int] = ..., is_downloaded: bool = ..., playback_pip_mode: _Optional[_Union[_playback_pip_mode_pb2.PlaybackPIPMode, str]] = ..., player_version: _Optional[str] = ..., playback_pip_mode_v2: _Optional[_Union[_playback_pip_mode_pb2.PlaybackPipMode, str]] = ...) -> None: ...
