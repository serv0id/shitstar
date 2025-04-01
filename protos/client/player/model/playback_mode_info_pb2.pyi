from client.player.model import stream_mode_pb2 as _stream_mode_pb2
from client.player.model import video_initiation_type_pb2 as _video_initiation_type_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PlayerOrientation(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PLAYER_ORIENTATION_UNSPECIFIED: _ClassVar[PlayerOrientation]
    PLAYER_ORIENTATION_PORTRAIT: _ClassVar[PlayerOrientation]
    PLAYER_ORIENTATION_LANDSCAPE: _ClassVar[PlayerOrientation]
    PLAYER_ORIENTATION_MINIMISED_LANDSCAPE: _ClassVar[PlayerOrientation]

class PlayType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PLAY_TYPE_UNSPECIFIED: _ClassVar[PlayType]
    PLAY_TYPE_MASTHEAD: _ClassVar[PlayType]
    PLAY_TYPE_WATCH_PAGE: _ClassVar[PlayType]
PLAYER_ORIENTATION_UNSPECIFIED: PlayerOrientation
PLAYER_ORIENTATION_PORTRAIT: PlayerOrientation
PLAYER_ORIENTATION_LANDSCAPE: PlayerOrientation
PLAYER_ORIENTATION_MINIMISED_LANDSCAPE: PlayerOrientation
PLAY_TYPE_UNSPECIFIED: PlayType
PLAY_TYPE_MASTHEAD: PlayType
PLAY_TYPE_WATCH_PAGE: PlayType

class PlaybackModeInfo(_message.Message):
    __slots__ = ("screen_mode", "is_fullscreen", "is_picture_in_picture", "airplay_enabled", "has_exited", "play_type", "auto_played", "player_orientation", "referrer_autoplay_language", "dh_logo_shown", "dh_logo_text", "appsuite_base", "retry_count", "mode", "previous_page_orientation", "initiation_source", "initiation_type")
    SCREEN_MODE_FIELD_NUMBER: _ClassVar[int]
    IS_FULLSCREEN_FIELD_NUMBER: _ClassVar[int]
    IS_PICTURE_IN_PICTURE_FIELD_NUMBER: _ClassVar[int]
    AIRPLAY_ENABLED_FIELD_NUMBER: _ClassVar[int]
    HAS_EXITED_FIELD_NUMBER: _ClassVar[int]
    PLAY_TYPE_FIELD_NUMBER: _ClassVar[int]
    AUTO_PLAYED_FIELD_NUMBER: _ClassVar[int]
    PLAYER_ORIENTATION_FIELD_NUMBER: _ClassVar[int]
    REFERRER_AUTOPLAY_LANGUAGE_FIELD_NUMBER: _ClassVar[int]
    DH_LOGO_SHOWN_FIELD_NUMBER: _ClassVar[int]
    DH_LOGO_TEXT_FIELD_NUMBER: _ClassVar[int]
    APPSUITE_BASE_FIELD_NUMBER: _ClassVar[int]
    RETRY_COUNT_FIELD_NUMBER: _ClassVar[int]
    MODE_FIELD_NUMBER: _ClassVar[int]
    PREVIOUS_PAGE_ORIENTATION_FIELD_NUMBER: _ClassVar[int]
    INITIATION_SOURCE_FIELD_NUMBER: _ClassVar[int]
    INITIATION_TYPE_FIELD_NUMBER: _ClassVar[int]
    screen_mode: PlayerOrientation
    is_fullscreen: bool
    is_picture_in_picture: bool
    airplay_enabled: bool
    has_exited: bool
    play_type: PlayType
    auto_played: bool
    player_orientation: PlayerOrientation
    referrer_autoplay_language: str
    dh_logo_shown: bool
    dh_logo_text: str
    appsuite_base: str
    retry_count: int
    mode: _stream_mode_pb2.StreamMode
    previous_page_orientation: PlayerOrientation
    initiation_source: _video_initiation_type_pb2.VideoInitiationSource
    initiation_type: _video_initiation_type_pb2.VideoInitiationType
    def __init__(self, screen_mode: _Optional[_Union[PlayerOrientation, str]] = ..., is_fullscreen: bool = ..., is_picture_in_picture: bool = ..., airplay_enabled: bool = ..., has_exited: bool = ..., play_type: _Optional[_Union[PlayType, str]] = ..., auto_played: bool = ..., player_orientation: _Optional[_Union[PlayerOrientation, str]] = ..., referrer_autoplay_language: _Optional[str] = ..., dh_logo_shown: bool = ..., dh_logo_text: _Optional[str] = ..., appsuite_base: _Optional[str] = ..., retry_count: _Optional[int] = ..., mode: _Optional[_Union[_stream_mode_pb2.StreamMode, str]] = ..., previous_page_orientation: _Optional[_Union[PlayerOrientation, str]] = ..., initiation_source: _Optional[_Union[_video_initiation_type_pb2.VideoInitiationSource, str]] = ..., initiation_type: _Optional[_Union[_video_initiation_type_pb2.VideoInitiationType, str]] = ...) -> None: ...
