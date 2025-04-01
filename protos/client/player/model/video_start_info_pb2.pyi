from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class VideoStartInfo(_message.Message):
    __slots__ = ("playback_start_resolution_px", "playback_start_bitrate_bps", "startup_bandwidth_bps", "manifest_load_time_ms", "start_up_time_ms", "total_player_load_time_ms", "video_start_position_ms", "started_with_ad", "drm_key_load_time_ms", "first_init_segment_load_time_ms", "first_audio_segment_load_time_ms", "first_video_segment_load_time_ms", "first_subtitle_file_load_time_ms", "drm_certificate_load_time_ms", "bff_load_time_ms", "preroll_resolution_failure_wait_time_ms")
    PLAYBACK_START_RESOLUTION_PX_FIELD_NUMBER: _ClassVar[int]
    PLAYBACK_START_BITRATE_BPS_FIELD_NUMBER: _ClassVar[int]
    STARTUP_BANDWIDTH_BPS_FIELD_NUMBER: _ClassVar[int]
    MANIFEST_LOAD_TIME_MS_FIELD_NUMBER: _ClassVar[int]
    START_UP_TIME_MS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_PLAYER_LOAD_TIME_MS_FIELD_NUMBER: _ClassVar[int]
    VIDEO_START_POSITION_MS_FIELD_NUMBER: _ClassVar[int]
    STARTED_WITH_AD_FIELD_NUMBER: _ClassVar[int]
    DRM_KEY_LOAD_TIME_MS_FIELD_NUMBER: _ClassVar[int]
    FIRST_INIT_SEGMENT_LOAD_TIME_MS_FIELD_NUMBER: _ClassVar[int]
    FIRST_AUDIO_SEGMENT_LOAD_TIME_MS_FIELD_NUMBER: _ClassVar[int]
    FIRST_VIDEO_SEGMENT_LOAD_TIME_MS_FIELD_NUMBER: _ClassVar[int]
    FIRST_SUBTITLE_FILE_LOAD_TIME_MS_FIELD_NUMBER: _ClassVar[int]
    DRM_CERTIFICATE_LOAD_TIME_MS_FIELD_NUMBER: _ClassVar[int]
    BFF_LOAD_TIME_MS_FIELD_NUMBER: _ClassVar[int]
    PREROLL_RESOLUTION_FAILURE_WAIT_TIME_MS_FIELD_NUMBER: _ClassVar[int]
    playback_start_resolution_px: int
    playback_start_bitrate_bps: int
    startup_bandwidth_bps: int
    manifest_load_time_ms: int
    start_up_time_ms: int
    total_player_load_time_ms: int
    video_start_position_ms: int
    started_with_ad: bool
    drm_key_load_time_ms: int
    first_init_segment_load_time_ms: int
    first_audio_segment_load_time_ms: int
    first_video_segment_load_time_ms: int
    first_subtitle_file_load_time_ms: int
    drm_certificate_load_time_ms: int
    bff_load_time_ms: int
    preroll_resolution_failure_wait_time_ms: int
    def __init__(self, playback_start_resolution_px: _Optional[int] = ..., playback_start_bitrate_bps: _Optional[int] = ..., startup_bandwidth_bps: _Optional[int] = ..., manifest_load_time_ms: _Optional[int] = ..., start_up_time_ms: _Optional[int] = ..., total_player_load_time_ms: _Optional[int] = ..., video_start_position_ms: _Optional[int] = ..., started_with_ad: bool = ..., drm_key_load_time_ms: _Optional[int] = ..., first_init_segment_load_time_ms: _Optional[int] = ..., first_audio_segment_load_time_ms: _Optional[int] = ..., first_video_segment_load_time_ms: _Optional[int] = ..., first_subtitle_file_load_time_ms: _Optional[int] = ..., drm_certificate_load_time_ms: _Optional[int] = ..., bff_load_time_ms: _Optional[int] = ..., preroll_resolution_failure_wait_time_ms: _Optional[int] = ...) -> None: ...
