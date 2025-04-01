from feature.player import playback_params_pb2 as _playback_params_pb2
from feature.player import playback_stream_params_pb2 as _playback_stream_params_pb2
from feature.content_language_preference import content_language_preference_pb2 as _content_language_preference_pb2
from feature.player import subtitle_asset_pb2 as _subtitle_asset_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MediaAsset(_message.Message):
    __slots__ = ("primary", "fallback", "repeat_mode", "default_audio_language", "default_text_language", "session_id", "language_preference_info", "subtitle_assets", "primary_stream")
    PRIMARY_FIELD_NUMBER: _ClassVar[int]
    FALLBACK_FIELD_NUMBER: _ClassVar[int]
    REPEAT_MODE_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_AUDIO_LANGUAGE_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_TEXT_LANGUAGE_FIELD_NUMBER: _ClassVar[int]
    SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_PREFERENCE_INFO_FIELD_NUMBER: _ClassVar[int]
    SUBTITLE_ASSETS_FIELD_NUMBER: _ClassVar[int]
    PRIMARY_STREAM_FIELD_NUMBER: _ClassVar[int]
    primary: _playback_params_pb2.PlaybackParams
    fallback: _playback_params_pb2.PlaybackParams
    repeat_mode: bool
    default_audio_language: str
    default_text_language: str
    session_id: str
    language_preference_info: _content_language_preference_pb2.ContentLanguagePreference
    subtitle_assets: _containers.RepeatedCompositeFieldContainer[_subtitle_asset_pb2.SubtitleAsset]
    primary_stream: _playback_stream_params_pb2.PlaybackStreamParams
    def __init__(self, primary: _Optional[_Union[_playback_params_pb2.PlaybackParams, _Mapping]] = ..., fallback: _Optional[_Union[_playback_params_pb2.PlaybackParams, _Mapping]] = ..., repeat_mode: bool = ..., default_audio_language: _Optional[str] = ..., default_text_language: _Optional[str] = ..., session_id: _Optional[str] = ..., language_preference_info: _Optional[_Union[_content_language_preference_pb2.ContentLanguagePreference, _Mapping]] = ..., subtitle_assets: _Optional[_Iterable[_Union[_subtitle_asset_pb2.SubtitleAsset, _Mapping]]] = ..., primary_stream: _Optional[_Union[_playback_stream_params_pb2.PlaybackStreamParams, _Mapping]] = ...) -> None: ...
