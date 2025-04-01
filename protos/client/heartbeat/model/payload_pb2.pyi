from client.heartbeat.model import ad_event_pb2 as _ad_event_pb2
from client.heartbeat.model import payload_trigger_pb2 as _payload_trigger_pb2
from client.heartbeat.model import qos_event_pb2 as _qos_event_pb2
from client.heartbeat.model import viewport_pb2 as _viewport_pb2
from client.player.model import playback_session_info_pb2 as _playback_session_info_pb2
from client.player.model import playback_state_info_pb2 as _playback_state_info_pb2
from component.playback import hardware_accelerated_pb2 as _hardware_accelerated_pb2
from component.playback import play_type_pb2 as _play_type_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Payload(_message.Message):
    __slots__ = ("payload_counter", "ts_created_ms", "sending_trigger", "playback_session_id", "ad_events", "qos_events", "viewport", "video_stream_codec", "audio_stream_codec", "playback_url", "playback_tag", "media_host", "stream_host", "stream_drm_provider", "stream_type", "stream_format", "stream_duration_ms", "has_preroll", "playback_status", "audio_decoder", "video_decoder", "video_quality_level", "video_position_ms", "is_downloaded", "is_fallback", "ab_id", "audio_lang_code", "audio_language", "client_playback_session_id", "session_type", "play_type", "video_decoder_hardware_accelerated", "client_content_id", "client_download_session_id", "battery_strength_percent", "battery_capacity_mah_current", "is_lpd", "battery_used_mah", "is_battery_drain_reliable", "channel_id")
    class PlaybackStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        PLAYBACK_STATUS_UNSPECIFIED: _ClassVar[Payload.PlaybackStatus]
        PLAYBACK_STATUS_PLAYING: _ClassVar[Payload.PlaybackStatus]
        PLAYBACK_STATUS_PAUSED: _ClassVar[Payload.PlaybackStatus]
        PLAYBACK_STATUS_STOPPED: _ClassVar[Payload.PlaybackStatus]
    PLAYBACK_STATUS_UNSPECIFIED: Payload.PlaybackStatus
    PLAYBACK_STATUS_PLAYING: Payload.PlaybackStatus
    PLAYBACK_STATUS_PAUSED: Payload.PlaybackStatus
    PLAYBACK_STATUS_STOPPED: Payload.PlaybackStatus
    class SessionType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SESSION_TYPE_UNSPECIFIED: _ClassVar[Payload.SessionType]
        SESSION_TYPE_PLAYBACK: _ClassVar[Payload.SessionType]
        SESSION_TYPE_OFFLINE_DOWNLOAD: _ClassVar[Payload.SessionType]
    SESSION_TYPE_UNSPECIFIED: Payload.SessionType
    SESSION_TYPE_PLAYBACK: Payload.SessionType
    SESSION_TYPE_OFFLINE_DOWNLOAD: Payload.SessionType
    PAYLOAD_COUNTER_FIELD_NUMBER: _ClassVar[int]
    TS_CREATED_MS_FIELD_NUMBER: _ClassVar[int]
    SENDING_TRIGGER_FIELD_NUMBER: _ClassVar[int]
    PLAYBACK_SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    AD_EVENTS_FIELD_NUMBER: _ClassVar[int]
    QOS_EVENTS_FIELD_NUMBER: _ClassVar[int]
    VIEWPORT_FIELD_NUMBER: _ClassVar[int]
    VIDEO_STREAM_CODEC_FIELD_NUMBER: _ClassVar[int]
    AUDIO_STREAM_CODEC_FIELD_NUMBER: _ClassVar[int]
    PLAYBACK_URL_FIELD_NUMBER: _ClassVar[int]
    PLAYBACK_TAG_FIELD_NUMBER: _ClassVar[int]
    MEDIA_HOST_FIELD_NUMBER: _ClassVar[int]
    STREAM_HOST_FIELD_NUMBER: _ClassVar[int]
    STREAM_DRM_PROVIDER_FIELD_NUMBER: _ClassVar[int]
    STREAM_TYPE_FIELD_NUMBER: _ClassVar[int]
    STREAM_FORMAT_FIELD_NUMBER: _ClassVar[int]
    STREAM_DURATION_MS_FIELD_NUMBER: _ClassVar[int]
    HAS_PREROLL_FIELD_NUMBER: _ClassVar[int]
    PLAYBACK_STATUS_FIELD_NUMBER: _ClassVar[int]
    AUDIO_DECODER_FIELD_NUMBER: _ClassVar[int]
    VIDEO_DECODER_FIELD_NUMBER: _ClassVar[int]
    VIDEO_QUALITY_LEVEL_FIELD_NUMBER: _ClassVar[int]
    VIDEO_POSITION_MS_FIELD_NUMBER: _ClassVar[int]
    IS_DOWNLOADED_FIELD_NUMBER: _ClassVar[int]
    IS_FALLBACK_FIELD_NUMBER: _ClassVar[int]
    AB_ID_FIELD_NUMBER: _ClassVar[int]
    AUDIO_LANG_CODE_FIELD_NUMBER: _ClassVar[int]
    AUDIO_LANGUAGE_FIELD_NUMBER: _ClassVar[int]
    CLIENT_PLAYBACK_SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    SESSION_TYPE_FIELD_NUMBER: _ClassVar[int]
    PLAY_TYPE_FIELD_NUMBER: _ClassVar[int]
    VIDEO_DECODER_HARDWARE_ACCELERATED_FIELD_NUMBER: _ClassVar[int]
    CLIENT_CONTENT_ID_FIELD_NUMBER: _ClassVar[int]
    CLIENT_DOWNLOAD_SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    BATTERY_STRENGTH_PERCENT_FIELD_NUMBER: _ClassVar[int]
    BATTERY_CAPACITY_MAH_CURRENT_FIELD_NUMBER: _ClassVar[int]
    IS_LPD_FIELD_NUMBER: _ClassVar[int]
    BATTERY_USED_MAH_FIELD_NUMBER: _ClassVar[int]
    IS_BATTERY_DRAIN_RELIABLE_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    payload_counter: int
    ts_created_ms: int
    sending_trigger: _payload_trigger_pb2.PayloadTrigger
    playback_session_id: str
    ad_events: _containers.RepeatedCompositeFieldContainer[_ad_event_pb2.AdEvent]
    qos_events: _containers.RepeatedCompositeFieldContainer[_qos_event_pb2.QosEvent]
    viewport: _viewport_pb2.Viewport
    video_stream_codec: str
    audio_stream_codec: str
    playback_url: str
    playback_tag: str
    media_host: str
    stream_host: str
    stream_drm_provider: _playback_session_info_pb2.PlaybackSessionInfo.DrmProvider
    stream_type: _playback_session_info_pb2.PlaybackSessionInfo.StreamType
    stream_format: _playback_session_info_pb2.PlaybackSessionInfo.StreamFormat
    stream_duration_ms: int
    has_preroll: bool
    playback_status: Payload.PlaybackStatus
    audio_decoder: str
    video_decoder: str
    video_quality_level: _playback_state_info_pb2.VideoQuality
    video_position_ms: int
    is_downloaded: bool
    is_fallback: bool
    ab_id: str
    audio_lang_code: str
    audio_language: str
    client_playback_session_id: str
    session_type: Payload.SessionType
    play_type: _play_type_pb2.PlayType
    video_decoder_hardware_accelerated: _hardware_accelerated_pb2.HardwareAccelerated
    client_content_id: str
    client_download_session_id: str
    battery_strength_percent: int
    battery_capacity_mah_current: int
    is_lpd: bool
    battery_used_mah: int
    is_battery_drain_reliable: bool
    channel_id: str
    def __init__(self, payload_counter: _Optional[int] = ..., ts_created_ms: _Optional[int] = ..., sending_trigger: _Optional[_Union[_payload_trigger_pb2.PayloadTrigger, str]] = ..., playback_session_id: _Optional[str] = ..., ad_events: _Optional[_Iterable[_Union[_ad_event_pb2.AdEvent, _Mapping]]] = ..., qos_events: _Optional[_Iterable[_Union[_qos_event_pb2.QosEvent, _Mapping]]] = ..., viewport: _Optional[_Union[_viewport_pb2.Viewport, str]] = ..., video_stream_codec: _Optional[str] = ..., audio_stream_codec: _Optional[str] = ..., playback_url: _Optional[str] = ..., playback_tag: _Optional[str] = ..., media_host: _Optional[str] = ..., stream_host: _Optional[str] = ..., stream_drm_provider: _Optional[_Union[_playback_session_info_pb2.PlaybackSessionInfo.DrmProvider, str]] = ..., stream_type: _Optional[_Union[_playback_session_info_pb2.PlaybackSessionInfo.StreamType, str]] = ..., stream_format: _Optional[_Union[_playback_session_info_pb2.PlaybackSessionInfo.StreamFormat, str]] = ..., stream_duration_ms: _Optional[int] = ..., has_preroll: bool = ..., playback_status: _Optional[_Union[Payload.PlaybackStatus, str]] = ..., audio_decoder: _Optional[str] = ..., video_decoder: _Optional[str] = ..., video_quality_level: _Optional[_Union[_playback_state_info_pb2.VideoQuality, str]] = ..., video_position_ms: _Optional[int] = ..., is_downloaded: bool = ..., is_fallback: bool = ..., ab_id: _Optional[str] = ..., audio_lang_code: _Optional[str] = ..., audio_language: _Optional[str] = ..., client_playback_session_id: _Optional[str] = ..., session_type: _Optional[_Union[Payload.SessionType, str]] = ..., play_type: _Optional[_Union[_play_type_pb2.PlayType, str]] = ..., video_decoder_hardware_accelerated: _Optional[_Union[_hardware_accelerated_pb2.HardwareAccelerated, str]] = ..., client_content_id: _Optional[str] = ..., client_download_session_id: _Optional[str] = ..., battery_strength_percent: _Optional[int] = ..., battery_capacity_mah_current: _Optional[int] = ..., is_lpd: bool = ..., battery_used_mah: _Optional[int] = ..., is_battery_drain_reliable: bool = ..., channel_id: _Optional[str] = ...) -> None: ...
