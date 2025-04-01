from client.player.model import playback_mode_info_pb2 as _playback_mode_info_pb2
from client.player.model import playback_session_info_pb2 as _playback_session_info_pb2
from client.player.model import stream_mode_pb2 as _stream_mode_pb2
from client.player.model import video_initiation_type_pb2 as _video_initiation_type_pb2
from client.watch import preload_playback_properties_pb2 as _preload_playback_properties_pb2
from component.content import content_pb2 as _content_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class WatchAttemptProperties(_message.Message):
    __slots__ = ("content", "page_url", "available_languages", "original_language", "is_casting", "is_downloaded", "client_page_id", "play_type", "is_preload", "preload_status", "player_version", "mode", "is_other_content_in_pip", "watch_session_id", "previous_page_orientation", "initiation_source", "initiation_type", "client_playback_session_id", "stream_type")
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_URL_FIELD_NUMBER: _ClassVar[int]
    AVAILABLE_LANGUAGES_FIELD_NUMBER: _ClassVar[int]
    ORIGINAL_LANGUAGE_FIELD_NUMBER: _ClassVar[int]
    IS_CASTING_FIELD_NUMBER: _ClassVar[int]
    IS_DOWNLOADED_FIELD_NUMBER: _ClassVar[int]
    CLIENT_PAGE_ID_FIELD_NUMBER: _ClassVar[int]
    PLAY_TYPE_FIELD_NUMBER: _ClassVar[int]
    IS_PRELOAD_FIELD_NUMBER: _ClassVar[int]
    PRELOAD_STATUS_FIELD_NUMBER: _ClassVar[int]
    PLAYER_VERSION_FIELD_NUMBER: _ClassVar[int]
    MODE_FIELD_NUMBER: _ClassVar[int]
    IS_OTHER_CONTENT_IN_PIP_FIELD_NUMBER: _ClassVar[int]
    WATCH_SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    PREVIOUS_PAGE_ORIENTATION_FIELD_NUMBER: _ClassVar[int]
    INITIATION_SOURCE_FIELD_NUMBER: _ClassVar[int]
    INITIATION_TYPE_FIELD_NUMBER: _ClassVar[int]
    CLIENT_PLAYBACK_SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    STREAM_TYPE_FIELD_NUMBER: _ClassVar[int]
    content: _content_pb2.Content
    page_url: str
    available_languages: _containers.RepeatedScalarFieldContainer[str]
    original_language: str
    is_casting: bool
    is_downloaded: bool
    client_page_id: str
    play_type: str
    is_preload: bool
    preload_status: _preload_playback_properties_pb2.PreloadPlaybackProperties.PreloadStatus
    player_version: str
    mode: _stream_mode_pb2.StreamMode
    is_other_content_in_pip: bool
    watch_session_id: str
    previous_page_orientation: _playback_mode_info_pb2.PlayerOrientation
    initiation_source: _video_initiation_type_pb2.VideoInitiationSource
    initiation_type: _video_initiation_type_pb2.VideoInitiationType
    client_playback_session_id: str
    stream_type: _playback_session_info_pb2.PlaybackSessionInfo.StreamType
    def __init__(self, content: _Optional[_Union[_content_pb2.Content, _Mapping]] = ..., page_url: _Optional[str] = ..., available_languages: _Optional[_Iterable[str]] = ..., original_language: _Optional[str] = ..., is_casting: bool = ..., is_downloaded: bool = ..., client_page_id: _Optional[str] = ..., play_type: _Optional[str] = ..., is_preload: bool = ..., preload_status: _Optional[_Union[_preload_playback_properties_pb2.PreloadPlaybackProperties.PreloadStatus, _Mapping]] = ..., player_version: _Optional[str] = ..., mode: _Optional[_Union[_stream_mode_pb2.StreamMode, str]] = ..., is_other_content_in_pip: bool = ..., watch_session_id: _Optional[str] = ..., previous_page_orientation: _Optional[_Union[_playback_mode_info_pb2.PlayerOrientation, str]] = ..., initiation_source: _Optional[_Union[_video_initiation_type_pb2.VideoInitiationSource, str]] = ..., initiation_type: _Optional[_Union[_video_initiation_type_pb2.VideoInitiationType, str]] = ..., client_playback_session_id: _Optional[str] = ..., stream_type: _Optional[_Union[_playback_session_info_pb2.PlaybackSessionInfo.StreamType, str]] = ...) -> None: ...
