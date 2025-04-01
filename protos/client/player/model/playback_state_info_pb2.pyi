from component.playback import hardware_accelerated_pb2 as _hardware_accelerated_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class VideoQuality(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    VIDEO_QUALITY_UNSPECIFIED: _ClassVar[VideoQuality]
    VIDEO_QUALITY_AUTO: _ClassVar[VideoQuality]
    VIDEO_QUALITY_LOW: _ClassVar[VideoQuality]
    VIDEO_QUALITY_MEDIUM: _ClassVar[VideoQuality]
    VIDEO_QUALITY_HIGH: _ClassVar[VideoQuality]
    VIDEO_QUALITY_ULTRA: _ClassVar[VideoQuality]
    VIDEO_QUALITY_SD: _ClassVar[VideoQuality]
    VIDEO_QUALITY_HD: _ClassVar[VideoQuality]
    VIDEO_QUALITY_FHD: _ClassVar[VideoQuality]
    VIDEO_QUALITY_4K: _ClassVar[VideoQuality]
VIDEO_QUALITY_UNSPECIFIED: VideoQuality
VIDEO_QUALITY_AUTO: VideoQuality
VIDEO_QUALITY_LOW: VideoQuality
VIDEO_QUALITY_MEDIUM: VideoQuality
VIDEO_QUALITY_HIGH: VideoQuality
VIDEO_QUALITY_ULTRA: VideoQuality
VIDEO_QUALITY_SD: VideoQuality
VIDEO_QUALITY_HD: VideoQuality
VIDEO_QUALITY_FHD: VideoQuality
VIDEO_QUALITY_4K: VideoQuality

class PlaybackStateInfo(_message.Message):
    __slots__ = ("audio_lang_code", "captions_lang_code", "captions_enabled", "audio_language", "captions_language", "current_video_position_ms", "volume_percent", "current_resolution_px", "current_video_bitrate_bps", "is_buffering", "audio_decoder", "video_decoder", "selected_video_quality", "video_decoder_hardware_accelerated")
    AUDIO_LANG_CODE_FIELD_NUMBER: _ClassVar[int]
    CAPTIONS_LANG_CODE_FIELD_NUMBER: _ClassVar[int]
    CAPTIONS_ENABLED_FIELD_NUMBER: _ClassVar[int]
    AUDIO_LANGUAGE_FIELD_NUMBER: _ClassVar[int]
    CAPTIONS_LANGUAGE_FIELD_NUMBER: _ClassVar[int]
    CURRENT_VIDEO_POSITION_MS_FIELD_NUMBER: _ClassVar[int]
    VOLUME_PERCENT_FIELD_NUMBER: _ClassVar[int]
    CURRENT_RESOLUTION_PX_FIELD_NUMBER: _ClassVar[int]
    CURRENT_VIDEO_BITRATE_BPS_FIELD_NUMBER: _ClassVar[int]
    IS_BUFFERING_FIELD_NUMBER: _ClassVar[int]
    AUDIO_DECODER_FIELD_NUMBER: _ClassVar[int]
    VIDEO_DECODER_FIELD_NUMBER: _ClassVar[int]
    SELECTED_VIDEO_QUALITY_FIELD_NUMBER: _ClassVar[int]
    VIDEO_DECODER_HARDWARE_ACCELERATED_FIELD_NUMBER: _ClassVar[int]
    audio_lang_code: str
    captions_lang_code: str
    captions_enabled: bool
    audio_language: str
    captions_language: str
    current_video_position_ms: int
    volume_percent: int
    current_resolution_px: int
    current_video_bitrate_bps: int
    is_buffering: bool
    audio_decoder: str
    video_decoder: str
    selected_video_quality: VideoQuality
    video_decoder_hardware_accelerated: _hardware_accelerated_pb2.HardwareAccelerated
    def __init__(self, audio_lang_code: _Optional[str] = ..., captions_lang_code: _Optional[str] = ..., captions_enabled: bool = ..., audio_language: _Optional[str] = ..., captions_language: _Optional[str] = ..., current_video_position_ms: _Optional[int] = ..., volume_percent: _Optional[int] = ..., current_resolution_px: _Optional[int] = ..., current_video_bitrate_bps: _Optional[int] = ..., is_buffering: bool = ..., audio_decoder: _Optional[str] = ..., video_decoder: _Optional[str] = ..., selected_video_quality: _Optional[_Union[VideoQuality, str]] = ..., video_decoder_hardware_accelerated: _Optional[_Union[_hardware_accelerated_pb2.HardwareAccelerated, str]] = ...) -> None: ...
