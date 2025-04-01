from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class WatchSessionProperties(_message.Message):
    __slots__ = ("watch_time_seconds", "buffer_time_ms", "seek_time_ms", "buffer_count", "total_seek_count", "rewind_count", "skip_forward_count", "stall_count", "bytes_downloaded", "dropped_video_frames", "msq_error_count", "missing_discontinuity_tag_count", "audio_sink_error_count", "bytes_downloaded_v2", "ssai_failover_count", "ssai_recovery_count", "playback_speed", "content_playback_time_seconds", "video_up_shift_count", "video_down_shift_count", "induced_buffer_time_ms", "induced_buffer_count", "msq_error_count_audio", "missing_discontinuity_tag_count_audio", "stale_manifest_count", "stale_manifest_count_audio", "video_sink_timestamp_jump_seek_count", "video_playback_stuck_count", "video_playback_unstuck_count", "battery_used_mah", "is_battery_drain_reliable")
    WATCH_TIME_SECONDS_FIELD_NUMBER: _ClassVar[int]
    BUFFER_TIME_MS_FIELD_NUMBER: _ClassVar[int]
    SEEK_TIME_MS_FIELD_NUMBER: _ClassVar[int]
    BUFFER_COUNT_FIELD_NUMBER: _ClassVar[int]
    TOTAL_SEEK_COUNT_FIELD_NUMBER: _ClassVar[int]
    REWIND_COUNT_FIELD_NUMBER: _ClassVar[int]
    SKIP_FORWARD_COUNT_FIELD_NUMBER: _ClassVar[int]
    STALL_COUNT_FIELD_NUMBER: _ClassVar[int]
    BYTES_DOWNLOADED_FIELD_NUMBER: _ClassVar[int]
    DROPPED_VIDEO_FRAMES_FIELD_NUMBER: _ClassVar[int]
    MSQ_ERROR_COUNT_FIELD_NUMBER: _ClassVar[int]
    MISSING_DISCONTINUITY_TAG_COUNT_FIELD_NUMBER: _ClassVar[int]
    AUDIO_SINK_ERROR_COUNT_FIELD_NUMBER: _ClassVar[int]
    BYTES_DOWNLOADED_V2_FIELD_NUMBER: _ClassVar[int]
    SSAI_FAILOVER_COUNT_FIELD_NUMBER: _ClassVar[int]
    SSAI_RECOVERY_COUNT_FIELD_NUMBER: _ClassVar[int]
    PLAYBACK_SPEED_FIELD_NUMBER: _ClassVar[int]
    CONTENT_PLAYBACK_TIME_SECONDS_FIELD_NUMBER: _ClassVar[int]
    VIDEO_UP_SHIFT_COUNT_FIELD_NUMBER: _ClassVar[int]
    VIDEO_DOWN_SHIFT_COUNT_FIELD_NUMBER: _ClassVar[int]
    INDUCED_BUFFER_TIME_MS_FIELD_NUMBER: _ClassVar[int]
    INDUCED_BUFFER_COUNT_FIELD_NUMBER: _ClassVar[int]
    MSQ_ERROR_COUNT_AUDIO_FIELD_NUMBER: _ClassVar[int]
    MISSING_DISCONTINUITY_TAG_COUNT_AUDIO_FIELD_NUMBER: _ClassVar[int]
    STALE_MANIFEST_COUNT_FIELD_NUMBER: _ClassVar[int]
    STALE_MANIFEST_COUNT_AUDIO_FIELD_NUMBER: _ClassVar[int]
    VIDEO_SINK_TIMESTAMP_JUMP_SEEK_COUNT_FIELD_NUMBER: _ClassVar[int]
    VIDEO_PLAYBACK_STUCK_COUNT_FIELD_NUMBER: _ClassVar[int]
    VIDEO_PLAYBACK_UNSTUCK_COUNT_FIELD_NUMBER: _ClassVar[int]
    BATTERY_USED_MAH_FIELD_NUMBER: _ClassVar[int]
    IS_BATTERY_DRAIN_RELIABLE_FIELD_NUMBER: _ClassVar[int]
    watch_time_seconds: int
    buffer_time_ms: int
    seek_time_ms: int
    buffer_count: int
    total_seek_count: int
    rewind_count: int
    skip_forward_count: int
    stall_count: int
    bytes_downloaded: int
    dropped_video_frames: int
    msq_error_count: int
    missing_discontinuity_tag_count: int
    audio_sink_error_count: int
    bytes_downloaded_v2: int
    ssai_failover_count: int
    ssai_recovery_count: int
    playback_speed: float
    content_playback_time_seconds: int
    video_up_shift_count: int
    video_down_shift_count: int
    induced_buffer_time_ms: int
    induced_buffer_count: int
    msq_error_count_audio: int
    missing_discontinuity_tag_count_audio: int
    stale_manifest_count: int
    stale_manifest_count_audio: int
    video_sink_timestamp_jump_seek_count: int
    video_playback_stuck_count: int
    video_playback_unstuck_count: int
    battery_used_mah: int
    is_battery_drain_reliable: bool
    def __init__(self, watch_time_seconds: _Optional[int] = ..., buffer_time_ms: _Optional[int] = ..., seek_time_ms: _Optional[int] = ..., buffer_count: _Optional[int] = ..., total_seek_count: _Optional[int] = ..., rewind_count: _Optional[int] = ..., skip_forward_count: _Optional[int] = ..., stall_count: _Optional[int] = ..., bytes_downloaded: _Optional[int] = ..., dropped_video_frames: _Optional[int] = ..., msq_error_count: _Optional[int] = ..., missing_discontinuity_tag_count: _Optional[int] = ..., audio_sink_error_count: _Optional[int] = ..., bytes_downloaded_v2: _Optional[int] = ..., ssai_failover_count: _Optional[int] = ..., ssai_recovery_count: _Optional[int] = ..., playback_speed: _Optional[float] = ..., content_playback_time_seconds: _Optional[int] = ..., video_up_shift_count: _Optional[int] = ..., video_down_shift_count: _Optional[int] = ..., induced_buffer_time_ms: _Optional[int] = ..., induced_buffer_count: _Optional[int] = ..., msq_error_count_audio: _Optional[int] = ..., missing_discontinuity_tag_count_audio: _Optional[int] = ..., stale_manifest_count: _Optional[int] = ..., stale_manifest_count_audio: _Optional[int] = ..., video_sink_timestamp_jump_seek_count: _Optional[int] = ..., video_playback_stuck_count: _Optional[int] = ..., video_playback_unstuck_count: _Optional[int] = ..., battery_used_mah: _Optional[int] = ..., is_battery_drain_reliable: bool = ...) -> None: ...
