from client.player.model import playback_url_set_type_pb2 as _playback_url_set_type_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PlaybackSessionInfo(_message.Message):
    __slots__ = ("playback_session_id", "playback_tag", "playback_url", "playback_url_host", "playback_url_set_type", "is_downloaded", "is_drm_protected", "drm_provider", "stream_type", "stream_format", "video_length_ms", "downloaded_on_db_version", "fallback_playback_tag", "fallback_playback_url", "is_migrated_from_rocky", "rewrite_segment_domain_enabled", "child_manifest_url_host", "ssai_cohort", "playback_url_cdn_name", "bookmark_position_ms", "watch_session_id", "client_playback_session_id", "download_session_id", "channel_id")
    class DrmProvider(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        DRM_PROVIDER_UNSPECIFIED: _ClassVar[PlaybackSessionInfo.DrmProvider]
        DRM_PROVIDER_WIDEVINE: _ClassVar[PlaybackSessionInfo.DrmProvider]
        DRM_PROVIDER_FAIRPLAY: _ClassVar[PlaybackSessionInfo.DrmProvider]
        DRM_PROVIDER_PLAYREADY: _ClassVar[PlaybackSessionInfo.DrmProvider]
    DRM_PROVIDER_UNSPECIFIED: PlaybackSessionInfo.DrmProvider
    DRM_PROVIDER_WIDEVINE: PlaybackSessionInfo.DrmProvider
    DRM_PROVIDER_FAIRPLAY: PlaybackSessionInfo.DrmProvider
    DRM_PROVIDER_PLAYREADY: PlaybackSessionInfo.DrmProvider
    class StreamType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STREAM_TYPE_UNSPECIFIED: _ClassVar[PlaybackSessionInfo.StreamType]
        STREAM_TYPE_VOD: _ClassVar[PlaybackSessionInfo.StreamType]
        STREAM_TYPE_LIVE: _ClassVar[PlaybackSessionInfo.StreamType]
        STREAM_TYPE_SIMULCAST: _ClassVar[PlaybackSessionInfo.StreamType]
        STREAM_TYPE_VR360: _ClassVar[PlaybackSessionInfo.StreamType]
    STREAM_TYPE_UNSPECIFIED: PlaybackSessionInfo.StreamType
    STREAM_TYPE_VOD: PlaybackSessionInfo.StreamType
    STREAM_TYPE_LIVE: PlaybackSessionInfo.StreamType
    STREAM_TYPE_SIMULCAST: PlaybackSessionInfo.StreamType
    STREAM_TYPE_VR360: PlaybackSessionInfo.StreamType
    class StreamFormat(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STREAM_FORMAT_UNSPECIFIED: _ClassVar[PlaybackSessionInfo.StreamFormat]
        STREAM_FORMAT_DASH: _ClassVar[PlaybackSessionInfo.StreamFormat]
        STREAM_FORMAT_HLS: _ClassVar[PlaybackSessionInfo.StreamFormat]
    STREAM_FORMAT_UNSPECIFIED: PlaybackSessionInfo.StreamFormat
    STREAM_FORMAT_DASH: PlaybackSessionInfo.StreamFormat
    STREAM_FORMAT_HLS: PlaybackSessionInfo.StreamFormat
    PLAYBACK_SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    PLAYBACK_TAG_FIELD_NUMBER: _ClassVar[int]
    PLAYBACK_URL_FIELD_NUMBER: _ClassVar[int]
    PLAYBACK_URL_HOST_FIELD_NUMBER: _ClassVar[int]
    PLAYBACK_URL_SET_TYPE_FIELD_NUMBER: _ClassVar[int]
    IS_DOWNLOADED_FIELD_NUMBER: _ClassVar[int]
    IS_DRM_PROTECTED_FIELD_NUMBER: _ClassVar[int]
    DRM_PROVIDER_FIELD_NUMBER: _ClassVar[int]
    STREAM_TYPE_FIELD_NUMBER: _ClassVar[int]
    STREAM_FORMAT_FIELD_NUMBER: _ClassVar[int]
    VIDEO_LENGTH_MS_FIELD_NUMBER: _ClassVar[int]
    DOWNLOADED_ON_DB_VERSION_FIELD_NUMBER: _ClassVar[int]
    FALLBACK_PLAYBACK_TAG_FIELD_NUMBER: _ClassVar[int]
    FALLBACK_PLAYBACK_URL_FIELD_NUMBER: _ClassVar[int]
    IS_MIGRATED_FROM_ROCKY_FIELD_NUMBER: _ClassVar[int]
    REWRITE_SEGMENT_DOMAIN_ENABLED_FIELD_NUMBER: _ClassVar[int]
    CHILD_MANIFEST_URL_HOST_FIELD_NUMBER: _ClassVar[int]
    SSAI_COHORT_FIELD_NUMBER: _ClassVar[int]
    PLAYBACK_URL_CDN_NAME_FIELD_NUMBER: _ClassVar[int]
    BOOKMARK_POSITION_MS_FIELD_NUMBER: _ClassVar[int]
    WATCH_SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    CLIENT_PLAYBACK_SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    DOWNLOAD_SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    playback_session_id: str
    playback_tag: str
    playback_url: str
    playback_url_host: str
    playback_url_set_type: _playback_url_set_type_pb2.PlaybackUrlSetType
    is_downloaded: bool
    is_drm_protected: bool
    drm_provider: PlaybackSessionInfo.DrmProvider
    stream_type: PlaybackSessionInfo.StreamType
    stream_format: PlaybackSessionInfo.StreamFormat
    video_length_ms: int
    downloaded_on_db_version: int
    fallback_playback_tag: str
    fallback_playback_url: str
    is_migrated_from_rocky: bool
    rewrite_segment_domain_enabled: bool
    child_manifest_url_host: str
    ssai_cohort: str
    playback_url_cdn_name: str
    bookmark_position_ms: int
    watch_session_id: str
    client_playback_session_id: str
    download_session_id: str
    channel_id: str
    def __init__(self, playback_session_id: _Optional[str] = ..., playback_tag: _Optional[str] = ..., playback_url: _Optional[str] = ..., playback_url_host: _Optional[str] = ..., playback_url_set_type: _Optional[_Union[_playback_url_set_type_pb2.PlaybackUrlSetType, str]] = ..., is_downloaded: bool = ..., is_drm_protected: bool = ..., drm_provider: _Optional[_Union[PlaybackSessionInfo.DrmProvider, str]] = ..., stream_type: _Optional[_Union[PlaybackSessionInfo.StreamType, str]] = ..., stream_format: _Optional[_Union[PlaybackSessionInfo.StreamFormat, str]] = ..., video_length_ms: _Optional[int] = ..., downloaded_on_db_version: _Optional[int] = ..., fallback_playback_tag: _Optional[str] = ..., fallback_playback_url: _Optional[str] = ..., is_migrated_from_rocky: bool = ..., rewrite_segment_domain_enabled: bool = ..., child_manifest_url_host: _Optional[str] = ..., ssai_cohort: _Optional[str] = ..., playback_url_cdn_name: _Optional[str] = ..., bookmark_position_ms: _Optional[int] = ..., watch_session_id: _Optional[str] = ..., client_playback_session_id: _Optional[str] = ..., download_session_id: _Optional[str] = ..., channel_id: _Optional[str] = ...) -> None: ...
