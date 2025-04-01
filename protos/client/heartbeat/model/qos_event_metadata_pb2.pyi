from options import opts_pb2 as _opts_pb2
from client.heartbeat.model import http_connection_stats_pb2 as _http_connection_stats_pb2
from client.player.model import playback_state_info_pb2 as _playback_state_info_pb2
from component.playback import resolution_pb2 as _resolution_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SpeedTestType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SPEED_TEST_TYPE_UNSPECIFIED: _ClassVar[SpeedTestType]
    SPEED_TEST_TYPE_LONG_REQUEST: _ClassVar[SpeedTestType]
    SPEED_TEST_TYPE_MULTI_BUFFERS: _ClassVar[SpeedTestType]
    SPEED_TEST_TYPE_MANUALLY: _ClassVar[SpeedTestType]
SPEED_TEST_TYPE_UNSPECIFIED: SpeedTestType
SPEED_TEST_TYPE_LONG_REQUEST: SpeedTestType
SPEED_TEST_TYPE_MULTI_BUFFERS: SpeedTestType
SPEED_TEST_TYPE_MANUALLY: SpeedTestType

class QosEventMetadata(_message.Message):
    __slots__ = ("video_position_ms", "buffer_length_ms", "offset_play_attempt_ms", "error_code", "error_message", "shift_reason", "seek_to_ms", "download_manifest_bitrate_kbps", "download_resolution", "estimated_bandwidth_kbps", "rtt_ms", "render_manifest_bitrate_kbps", "stream_resolution", "stream_width_pixel", "duration_in_current_state_ms", "decoded_frames", "available_duration_ms", "download_duration_ms", "download_bytes", "url", "reason", "is_first_rebuffer", "init_bandwidth_kbps", "resolution", "action_type", "detail_sent_offset_ms", "url_sent_offset_ms", "drm_sent_offset_ms", "master_manifest_sent_offset_ms", "child_manifest_sent_offset_ms", "init_segment_sent_offset_ms", "first_video_sent_offset_ms", "detail_received_offset_ms", "drm_received_offset_ms", "master_manifest_received_offset_ms", "child_manifest_received_offset_ms", "init_segment_received_offset_ms", "first_video_received_offset_ms", "url_received_offset_ms", "decoder_init_count", "decoder_release_count", "dropped_buffer_count", "dropped_to_keyframe_count", "input_buffer_count", "max_consecutive_dropped_buffer_count", "rendered_output_buffer_count", "skipped_input_buffer_count", "skipped_output_buffer_count", "total_video_frame_processing_offset_us", "video_frame_processing_offset_count", "min_positive_vfpo", "max_positive_vfpo", "min_negative_vfpo", "max_negative_vfpo", "last_segment", "live_edge_position_ms", "disc_old_position_ms", "disc_new_position_ms", "disc_reason", "max_memory_bytes", "total_memory_bytes", "used_memory_bytes", "free_memory_bytes", "exit_type", "current_state", "previous_selected_quality_level", "data_type", "playing_ad", "memory_level", "master_manifest_info", "drm_license_info", "video_metadata_info", "first_init_segment_info", "first_video_segment_info", "first_audio_segment_info", "first_subtitle_file_info", "http_connection_stats", "byte_range", "bytes_downloaded", "tracks", "bitrate_lowerbound_bps", "bitrate_upperbound_bps", "width_lowerbound_px", "width_upperbound_px", "buffer_goal_ms", "bitrate_bps", "abr_algorithm", "abr_parameters", "abr_context", "certificate_sent_offset_ms", "certificate_received_offset_ms", "drm_license_url", "resume_at", "last_updated_msq", "ts_last_manifest_refresh_ms", "manifest_msq", "msq_mismatch_count", "current_presentation_timestamp_us", "expected_presentation_timestamp_us", "did_auto_seek", "speed_test_type", "speed_test_infos", "buffereds", "is_resume_from_seek", "cdn_name", "url_host", "timestamp_difference_ms", "is_buffering", "video_stuck_duration_ms", "connection_speed", "stream_bandwidth_kbps", "manifest_period_count", "audio_buffer_length", "gaps_jumped", "buffered_start_time_ms", "buffered_end_time_ms", "is_retrying_with_last_playback_asset")
    class ExitType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        EXIT_TYPE_UNSPECIFIED: _ClassVar[QosEventMetadata.ExitType]
        EXIT_TYPE_USER_LEAVE: _ClassVar[QosEventMetadata.ExitType]
        EXIT_TYPE_NEW_VIDEO: _ClassVar[QosEventMetadata.ExitType]
        EXIT_TYPE_ENTITLEMENT_FAIL: _ClassVar[QosEventMetadata.ExitType]
        EXIT_TYPE_OUT_OF_FREE_WATCH: _ClassVar[QosEventMetadata.ExitType]
        EXIT_TYPE_OTHER: _ClassVar[QosEventMetadata.ExitType]
    EXIT_TYPE_UNSPECIFIED: QosEventMetadata.ExitType
    EXIT_TYPE_USER_LEAVE: QosEventMetadata.ExitType
    EXIT_TYPE_NEW_VIDEO: QosEventMetadata.ExitType
    EXIT_TYPE_ENTITLEMENT_FAIL: QosEventMetadata.ExitType
    EXIT_TYPE_OUT_OF_FREE_WATCH: QosEventMetadata.ExitType
    EXIT_TYPE_OTHER: QosEventMetadata.ExitType
    class CurrentState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        CURRENT_STATE_UNSPECIFIED: _ClassVar[QosEventMetadata.CurrentState]
        CURRENT_STATE_STARTUP: _ClassVar[QosEventMetadata.CurrentState]
        CURRENT_STATE_PLAYING: _ClassVar[QosEventMetadata.CurrentState]
        CURRENT_STATE_PAUSED: _ClassVar[QosEventMetadata.CurrentState]
        CURRENT_STATE_SEEKING: _ClassVar[QosEventMetadata.CurrentState]
        CURRENT_STATE_REBUFFERING: _ClassVar[QosEventMetadata.CurrentState]
        CURRENT_STATE_OTHER: _ClassVar[QosEventMetadata.CurrentState]
    CURRENT_STATE_UNSPECIFIED: QosEventMetadata.CurrentState
    CURRENT_STATE_STARTUP: QosEventMetadata.CurrentState
    CURRENT_STATE_PLAYING: QosEventMetadata.CurrentState
    CURRENT_STATE_PAUSED: QosEventMetadata.CurrentState
    CURRENT_STATE_SEEKING: QosEventMetadata.CurrentState
    CURRENT_STATE_REBUFFERING: QosEventMetadata.CurrentState
    CURRENT_STATE_OTHER: QosEventMetadata.CurrentState
    class DataType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        DATA_TYPE_UNSPECIFIED: _ClassVar[QosEventMetadata.DataType]
        DATA_TYPE_VIDEO: _ClassVar[QosEventMetadata.DataType]
        DATA_TYPE_AUDIO: _ClassVar[QosEventMetadata.DataType]
        DATA_TYPE_MANIFEST: _ClassVar[QosEventMetadata.DataType]
        DATA_TYPE_SUBTITLE: _ClassVar[QosEventMetadata.DataType]
        DATA_TYPE_DRM: _ClassVar[QosEventMetadata.DataType]
        DATA_TYPE_OTHER: _ClassVar[QosEventMetadata.DataType]
        DATA_TYPE_INIT: _ClassVar[QosEventMetadata.DataType]
        DATA_TYPE_CERTIFICATE: _ClassVar[QosEventMetadata.DataType]
        DATA_TYPE_BFF: _ClassVar[QosEventMetadata.DataType]
        DATA_TYPE_PC: _ClassVar[QosEventMetadata.DataType]
        DATA_TYPE_CHECK_DOWNLOAD: _ClassVar[QosEventMetadata.DataType]
        DATA_TYPE_START_DOWNLOAD: _ClassVar[QosEventMetadata.DataType]
        DATA_TYPE_CLIENT_CAPABILITIES: _ClassVar[QosEventMetadata.DataType]
        DATA_TYPE_PROTO_PARSING: _ClassVar[QosEventMetadata.DataType]
        DATA_TYPE_PLAYER_INITIALIZATION: _ClassVar[QosEventMetadata.DataType]
    DATA_TYPE_UNSPECIFIED: QosEventMetadata.DataType
    DATA_TYPE_VIDEO: QosEventMetadata.DataType
    DATA_TYPE_AUDIO: QosEventMetadata.DataType
    DATA_TYPE_MANIFEST: QosEventMetadata.DataType
    DATA_TYPE_SUBTITLE: QosEventMetadata.DataType
    DATA_TYPE_DRM: QosEventMetadata.DataType
    DATA_TYPE_OTHER: QosEventMetadata.DataType
    DATA_TYPE_INIT: QosEventMetadata.DataType
    DATA_TYPE_CERTIFICATE: QosEventMetadata.DataType
    DATA_TYPE_BFF: QosEventMetadata.DataType
    DATA_TYPE_PC: QosEventMetadata.DataType
    DATA_TYPE_CHECK_DOWNLOAD: QosEventMetadata.DataType
    DATA_TYPE_START_DOWNLOAD: QosEventMetadata.DataType
    DATA_TYPE_CLIENT_CAPABILITIES: QosEventMetadata.DataType
    DATA_TYPE_PROTO_PARSING: QosEventMetadata.DataType
    DATA_TYPE_PLAYER_INITIALIZATION: QosEventMetadata.DataType
    class PlayingAd(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        PLAYING_AD_UNSPECIFIED: _ClassVar[QosEventMetadata.PlayingAd]
        PLAYING_AD_YES: _ClassVar[QosEventMetadata.PlayingAd]
        PLAYING_AD_NO: _ClassVar[QosEventMetadata.PlayingAd]
        PLAYING_AD_UNKNOWN: _ClassVar[QosEventMetadata.PlayingAd]
    PLAYING_AD_UNSPECIFIED: QosEventMetadata.PlayingAd
    PLAYING_AD_YES: QosEventMetadata.PlayingAd
    PLAYING_AD_NO: QosEventMetadata.PlayingAd
    PLAYING_AD_UNKNOWN: QosEventMetadata.PlayingAd
    class MemoryLevel(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        MEMORY_LEVEL_UNSPECIFIED: _ClassVar[QosEventMetadata.MemoryLevel]
        MEMORY_LEVEL_TRIM_MEMORY_DEFAULT: _ClassVar[QosEventMetadata.MemoryLevel]
        MEMORY_LEVEL_TRIM_MEMORY_COMPLETE: _ClassVar[QosEventMetadata.MemoryLevel]
        MEMORY_LEVEL_TRIM_MEMORY_MODERATE: _ClassVar[QosEventMetadata.MemoryLevel]
        MEMORY_LEVEL_TRIM_MEMORY_BACKGROUND: _ClassVar[QosEventMetadata.MemoryLevel]
        MEMORY_LEVEL_TRIM_MEMORY_UI_HIDDEN: _ClassVar[QosEventMetadata.MemoryLevel]
        MEMORY_LEVEL_TRIM_MEMORY_RUNNING_CRITICAL: _ClassVar[QosEventMetadata.MemoryLevel]
        MEMORY_LEVEL_TRIM_MEMORY_RUNNING_LOW: _ClassVar[QosEventMetadata.MemoryLevel]
        MEMORY_LEVEL_TRIM_MEMORY_RUNNING_MODERATE: _ClassVar[QosEventMetadata.MemoryLevel]
    MEMORY_LEVEL_UNSPECIFIED: QosEventMetadata.MemoryLevel
    MEMORY_LEVEL_TRIM_MEMORY_DEFAULT: QosEventMetadata.MemoryLevel
    MEMORY_LEVEL_TRIM_MEMORY_COMPLETE: QosEventMetadata.MemoryLevel
    MEMORY_LEVEL_TRIM_MEMORY_MODERATE: QosEventMetadata.MemoryLevel
    MEMORY_LEVEL_TRIM_MEMORY_BACKGROUND: QosEventMetadata.MemoryLevel
    MEMORY_LEVEL_TRIM_MEMORY_UI_HIDDEN: QosEventMetadata.MemoryLevel
    MEMORY_LEVEL_TRIM_MEMORY_RUNNING_CRITICAL: QosEventMetadata.MemoryLevel
    MEMORY_LEVEL_TRIM_MEMORY_RUNNING_LOW: QosEventMetadata.MemoryLevel
    MEMORY_LEVEL_TRIM_MEMORY_RUNNING_MODERATE: QosEventMetadata.MemoryLevel
    VIDEO_POSITION_MS_FIELD_NUMBER: _ClassVar[int]
    BUFFER_LENGTH_MS_FIELD_NUMBER: _ClassVar[int]
    OFFSET_PLAY_ATTEMPT_MS_FIELD_NUMBER: _ClassVar[int]
    ERROR_CODE_FIELD_NUMBER: _ClassVar[int]
    ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    SHIFT_REASON_FIELD_NUMBER: _ClassVar[int]
    SEEK_TO_MS_FIELD_NUMBER: _ClassVar[int]
    DOWNLOAD_MANIFEST_BITRATE_KBPS_FIELD_NUMBER: _ClassVar[int]
    DOWNLOAD_RESOLUTION_FIELD_NUMBER: _ClassVar[int]
    ESTIMATED_BANDWIDTH_KBPS_FIELD_NUMBER: _ClassVar[int]
    RTT_MS_FIELD_NUMBER: _ClassVar[int]
    RENDER_MANIFEST_BITRATE_KBPS_FIELD_NUMBER: _ClassVar[int]
    STREAM_RESOLUTION_FIELD_NUMBER: _ClassVar[int]
    STREAM_WIDTH_PIXEL_FIELD_NUMBER: _ClassVar[int]
    DURATION_IN_CURRENT_STATE_MS_FIELD_NUMBER: _ClassVar[int]
    DECODED_FRAMES_FIELD_NUMBER: _ClassVar[int]
    AVAILABLE_DURATION_MS_FIELD_NUMBER: _ClassVar[int]
    DOWNLOAD_DURATION_MS_FIELD_NUMBER: _ClassVar[int]
    DOWNLOAD_BYTES_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    IS_FIRST_REBUFFER_FIELD_NUMBER: _ClassVar[int]
    INIT_BANDWIDTH_KBPS_FIELD_NUMBER: _ClassVar[int]
    RESOLUTION_FIELD_NUMBER: _ClassVar[int]
    ACTION_TYPE_FIELD_NUMBER: _ClassVar[int]
    DETAIL_SENT_OFFSET_MS_FIELD_NUMBER: _ClassVar[int]
    URL_SENT_OFFSET_MS_FIELD_NUMBER: _ClassVar[int]
    DRM_SENT_OFFSET_MS_FIELD_NUMBER: _ClassVar[int]
    MASTER_MANIFEST_SENT_OFFSET_MS_FIELD_NUMBER: _ClassVar[int]
    CHILD_MANIFEST_SENT_OFFSET_MS_FIELD_NUMBER: _ClassVar[int]
    INIT_SEGMENT_SENT_OFFSET_MS_FIELD_NUMBER: _ClassVar[int]
    FIRST_VIDEO_SENT_OFFSET_MS_FIELD_NUMBER: _ClassVar[int]
    DETAIL_RECEIVED_OFFSET_MS_FIELD_NUMBER: _ClassVar[int]
    DRM_RECEIVED_OFFSET_MS_FIELD_NUMBER: _ClassVar[int]
    MASTER_MANIFEST_RECEIVED_OFFSET_MS_FIELD_NUMBER: _ClassVar[int]
    CHILD_MANIFEST_RECEIVED_OFFSET_MS_FIELD_NUMBER: _ClassVar[int]
    INIT_SEGMENT_RECEIVED_OFFSET_MS_FIELD_NUMBER: _ClassVar[int]
    FIRST_VIDEO_RECEIVED_OFFSET_MS_FIELD_NUMBER: _ClassVar[int]
    URL_RECEIVED_OFFSET_MS_FIELD_NUMBER: _ClassVar[int]
    DECODER_INIT_COUNT_FIELD_NUMBER: _ClassVar[int]
    DECODER_RELEASE_COUNT_FIELD_NUMBER: _ClassVar[int]
    DROPPED_BUFFER_COUNT_FIELD_NUMBER: _ClassVar[int]
    DROPPED_TO_KEYFRAME_COUNT_FIELD_NUMBER: _ClassVar[int]
    INPUT_BUFFER_COUNT_FIELD_NUMBER: _ClassVar[int]
    MAX_CONSECUTIVE_DROPPED_BUFFER_COUNT_FIELD_NUMBER: _ClassVar[int]
    RENDERED_OUTPUT_BUFFER_COUNT_FIELD_NUMBER: _ClassVar[int]
    SKIPPED_INPUT_BUFFER_COUNT_FIELD_NUMBER: _ClassVar[int]
    SKIPPED_OUTPUT_BUFFER_COUNT_FIELD_NUMBER: _ClassVar[int]
    TOTAL_VIDEO_FRAME_PROCESSING_OFFSET_US_FIELD_NUMBER: _ClassVar[int]
    VIDEO_FRAME_PROCESSING_OFFSET_COUNT_FIELD_NUMBER: _ClassVar[int]
    MIN_POSITIVE_VFPO_FIELD_NUMBER: _ClassVar[int]
    MAX_POSITIVE_VFPO_FIELD_NUMBER: _ClassVar[int]
    MIN_NEGATIVE_VFPO_FIELD_NUMBER: _ClassVar[int]
    MAX_NEGATIVE_VFPO_FIELD_NUMBER: _ClassVar[int]
    LAST_SEGMENT_FIELD_NUMBER: _ClassVar[int]
    LIVE_EDGE_POSITION_MS_FIELD_NUMBER: _ClassVar[int]
    DISC_OLD_POSITION_MS_FIELD_NUMBER: _ClassVar[int]
    DISC_NEW_POSITION_MS_FIELD_NUMBER: _ClassVar[int]
    DISC_REASON_FIELD_NUMBER: _ClassVar[int]
    MAX_MEMORY_BYTES_FIELD_NUMBER: _ClassVar[int]
    TOTAL_MEMORY_BYTES_FIELD_NUMBER: _ClassVar[int]
    USED_MEMORY_BYTES_FIELD_NUMBER: _ClassVar[int]
    FREE_MEMORY_BYTES_FIELD_NUMBER: _ClassVar[int]
    EXIT_TYPE_FIELD_NUMBER: _ClassVar[int]
    CURRENT_STATE_FIELD_NUMBER: _ClassVar[int]
    PREVIOUS_SELECTED_QUALITY_LEVEL_FIELD_NUMBER: _ClassVar[int]
    DATA_TYPE_FIELD_NUMBER: _ClassVar[int]
    PLAYING_AD_FIELD_NUMBER: _ClassVar[int]
    MEMORY_LEVEL_FIELD_NUMBER: _ClassVar[int]
    MASTER_MANIFEST_INFO_FIELD_NUMBER: _ClassVar[int]
    DRM_LICENSE_INFO_FIELD_NUMBER: _ClassVar[int]
    VIDEO_METADATA_INFO_FIELD_NUMBER: _ClassVar[int]
    FIRST_INIT_SEGMENT_INFO_FIELD_NUMBER: _ClassVar[int]
    FIRST_VIDEO_SEGMENT_INFO_FIELD_NUMBER: _ClassVar[int]
    FIRST_AUDIO_SEGMENT_INFO_FIELD_NUMBER: _ClassVar[int]
    FIRST_SUBTITLE_FILE_INFO_FIELD_NUMBER: _ClassVar[int]
    HTTP_CONNECTION_STATS_FIELD_NUMBER: _ClassVar[int]
    BYTE_RANGE_FIELD_NUMBER: _ClassVar[int]
    BYTES_DOWNLOADED_FIELD_NUMBER: _ClassVar[int]
    TRACKS_FIELD_NUMBER: _ClassVar[int]
    BITRATE_LOWERBOUND_BPS_FIELD_NUMBER: _ClassVar[int]
    BITRATE_UPPERBOUND_BPS_FIELD_NUMBER: _ClassVar[int]
    WIDTH_LOWERBOUND_PX_FIELD_NUMBER: _ClassVar[int]
    WIDTH_UPPERBOUND_PX_FIELD_NUMBER: _ClassVar[int]
    BUFFER_GOAL_MS_FIELD_NUMBER: _ClassVar[int]
    BITRATE_BPS_FIELD_NUMBER: _ClassVar[int]
    ABR_ALGORITHM_FIELD_NUMBER: _ClassVar[int]
    ABR_PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    ABR_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    CERTIFICATE_SENT_OFFSET_MS_FIELD_NUMBER: _ClassVar[int]
    CERTIFICATE_RECEIVED_OFFSET_MS_FIELD_NUMBER: _ClassVar[int]
    DRM_LICENSE_URL_FIELD_NUMBER: _ClassVar[int]
    RESUME_AT_FIELD_NUMBER: _ClassVar[int]
    LAST_UPDATED_MSQ_FIELD_NUMBER: _ClassVar[int]
    TS_LAST_MANIFEST_REFRESH_MS_FIELD_NUMBER: _ClassVar[int]
    MANIFEST_MSQ_FIELD_NUMBER: _ClassVar[int]
    MSQ_MISMATCH_COUNT_FIELD_NUMBER: _ClassVar[int]
    CURRENT_PRESENTATION_TIMESTAMP_US_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_PRESENTATION_TIMESTAMP_US_FIELD_NUMBER: _ClassVar[int]
    DID_AUTO_SEEK_FIELD_NUMBER: _ClassVar[int]
    SPEED_TEST_TYPE_FIELD_NUMBER: _ClassVar[int]
    SPEED_TEST_INFOS_FIELD_NUMBER: _ClassVar[int]
    BUFFEREDS_FIELD_NUMBER: _ClassVar[int]
    IS_RESUME_FROM_SEEK_FIELD_NUMBER: _ClassVar[int]
    CDN_NAME_FIELD_NUMBER: _ClassVar[int]
    URL_HOST_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_DIFFERENCE_MS_FIELD_NUMBER: _ClassVar[int]
    IS_BUFFERING_FIELD_NUMBER: _ClassVar[int]
    VIDEO_STUCK_DURATION_MS_FIELD_NUMBER: _ClassVar[int]
    CONNECTION_SPEED_FIELD_NUMBER: _ClassVar[int]
    STREAM_BANDWIDTH_KBPS_FIELD_NUMBER: _ClassVar[int]
    MANIFEST_PERIOD_COUNT_FIELD_NUMBER: _ClassVar[int]
    AUDIO_BUFFER_LENGTH_FIELD_NUMBER: _ClassVar[int]
    GAPS_JUMPED_FIELD_NUMBER: _ClassVar[int]
    BUFFERED_START_TIME_MS_FIELD_NUMBER: _ClassVar[int]
    BUFFERED_END_TIME_MS_FIELD_NUMBER: _ClassVar[int]
    IS_RETRYING_WITH_LAST_PLAYBACK_ASSET_FIELD_NUMBER: _ClassVar[int]
    video_position_ms: int
    buffer_length_ms: int
    offset_play_attempt_ms: int
    error_code: str
    error_message: str
    shift_reason: int
    seek_to_ms: int
    download_manifest_bitrate_kbps: int
    download_resolution: _resolution_pb2.Resolution
    estimated_bandwidth_kbps: int
    rtt_ms: int
    render_manifest_bitrate_kbps: int
    stream_resolution: _resolution_pb2.Resolution
    stream_width_pixel: int
    duration_in_current_state_ms: int
    decoded_frames: int
    available_duration_ms: int
    download_duration_ms: int
    download_bytes: int
    url: str
    reason: str
    is_first_rebuffer: bool
    init_bandwidth_kbps: int
    resolution: _resolution_pb2.Resolution
    action_type: str
    detail_sent_offset_ms: int
    url_sent_offset_ms: int
    drm_sent_offset_ms: int
    master_manifest_sent_offset_ms: int
    child_manifest_sent_offset_ms: int
    init_segment_sent_offset_ms: int
    first_video_sent_offset_ms: int
    detail_received_offset_ms: int
    drm_received_offset_ms: int
    master_manifest_received_offset_ms: int
    child_manifest_received_offset_ms: int
    init_segment_received_offset_ms: int
    first_video_received_offset_ms: int
    url_received_offset_ms: int
    decoder_init_count: int
    decoder_release_count: int
    dropped_buffer_count: int
    dropped_to_keyframe_count: int
    input_buffer_count: int
    max_consecutive_dropped_buffer_count: int
    rendered_output_buffer_count: int
    skipped_input_buffer_count: int
    skipped_output_buffer_count: int
    total_video_frame_processing_offset_us: int
    video_frame_processing_offset_count: int
    min_positive_vfpo: int
    max_positive_vfpo: int
    min_negative_vfpo: int
    max_negative_vfpo: int
    last_segment: str
    live_edge_position_ms: int
    disc_old_position_ms: int
    disc_new_position_ms: int
    disc_reason: str
    max_memory_bytes: int
    total_memory_bytes: int
    used_memory_bytes: int
    free_memory_bytes: int
    exit_type: QosEventMetadata.ExitType
    current_state: QosEventMetadata.CurrentState
    previous_selected_quality_level: _playback_state_info_pb2.VideoQuality
    data_type: QosEventMetadata.DataType
    playing_ad: QosEventMetadata.PlayingAd
    memory_level: QosEventMetadata.MemoryLevel
    master_manifest_info: _http_connection_stats_pb2.HttpConnectionStats
    drm_license_info: _http_connection_stats_pb2.HttpConnectionStats
    video_metadata_info: _http_connection_stats_pb2.HttpConnectionStats
    first_init_segment_info: _http_connection_stats_pb2.HttpConnectionStats
    first_video_segment_info: _http_connection_stats_pb2.HttpConnectionStats
    first_audio_segment_info: _http_connection_stats_pb2.HttpConnectionStats
    first_subtitle_file_info: _http_connection_stats_pb2.HttpConnectionStats
    http_connection_stats: _http_connection_stats_pb2.HttpConnectionStats
    byte_range: str
    bytes_downloaded: int
    tracks: Tracks
    bitrate_lowerbound_bps: int
    bitrate_upperbound_bps: int
    width_lowerbound_px: int
    width_upperbound_px: int
    buffer_goal_ms: int
    bitrate_bps: int
    abr_algorithm: str
    abr_parameters: str
    abr_context: str
    certificate_sent_offset_ms: int
    certificate_received_offset_ms: int
    drm_license_url: str
    resume_at: int
    last_updated_msq: int
    ts_last_manifest_refresh_ms: int
    manifest_msq: int
    msq_mismatch_count: int
    current_presentation_timestamp_us: int
    expected_presentation_timestamp_us: int
    did_auto_seek: bool
    speed_test_type: SpeedTestType
    speed_test_infos: _containers.RepeatedCompositeFieldContainer[SpeedTestInfo]
    buffereds: _containers.RepeatedCompositeFieldContainer[Buffered]
    is_resume_from_seek: bool
    cdn_name: str
    url_host: str
    timestamp_difference_ms: int
    is_buffering: bool
    video_stuck_duration_ms: int
    connection_speed: str
    stream_bandwidth_kbps: int
    manifest_period_count: int
    audio_buffer_length: int
    gaps_jumped: int
    buffered_start_time_ms: int
    buffered_end_time_ms: int
    is_retrying_with_last_playback_asset: bool
    def __init__(self, video_position_ms: _Optional[int] = ..., buffer_length_ms: _Optional[int] = ..., offset_play_attempt_ms: _Optional[int] = ..., error_code: _Optional[str] = ..., error_message: _Optional[str] = ..., shift_reason: _Optional[int] = ..., seek_to_ms: _Optional[int] = ..., download_manifest_bitrate_kbps: _Optional[int] = ..., download_resolution: _Optional[_Union[_resolution_pb2.Resolution, _Mapping]] = ..., estimated_bandwidth_kbps: _Optional[int] = ..., rtt_ms: _Optional[int] = ..., render_manifest_bitrate_kbps: _Optional[int] = ..., stream_resolution: _Optional[_Union[_resolution_pb2.Resolution, _Mapping]] = ..., stream_width_pixel: _Optional[int] = ..., duration_in_current_state_ms: _Optional[int] = ..., decoded_frames: _Optional[int] = ..., available_duration_ms: _Optional[int] = ..., download_duration_ms: _Optional[int] = ..., download_bytes: _Optional[int] = ..., url: _Optional[str] = ..., reason: _Optional[str] = ..., is_first_rebuffer: bool = ..., init_bandwidth_kbps: _Optional[int] = ..., resolution: _Optional[_Union[_resolution_pb2.Resolution, _Mapping]] = ..., action_type: _Optional[str] = ..., detail_sent_offset_ms: _Optional[int] = ..., url_sent_offset_ms: _Optional[int] = ..., drm_sent_offset_ms: _Optional[int] = ..., master_manifest_sent_offset_ms: _Optional[int] = ..., child_manifest_sent_offset_ms: _Optional[int] = ..., init_segment_sent_offset_ms: _Optional[int] = ..., first_video_sent_offset_ms: _Optional[int] = ..., detail_received_offset_ms: _Optional[int] = ..., drm_received_offset_ms: _Optional[int] = ..., master_manifest_received_offset_ms: _Optional[int] = ..., child_manifest_received_offset_ms: _Optional[int] = ..., init_segment_received_offset_ms: _Optional[int] = ..., first_video_received_offset_ms: _Optional[int] = ..., url_received_offset_ms: _Optional[int] = ..., decoder_init_count: _Optional[int] = ..., decoder_release_count: _Optional[int] = ..., dropped_buffer_count: _Optional[int] = ..., dropped_to_keyframe_count: _Optional[int] = ..., input_buffer_count: _Optional[int] = ..., max_consecutive_dropped_buffer_count: _Optional[int] = ..., rendered_output_buffer_count: _Optional[int] = ..., skipped_input_buffer_count: _Optional[int] = ..., skipped_output_buffer_count: _Optional[int] = ..., total_video_frame_processing_offset_us: _Optional[int] = ..., video_frame_processing_offset_count: _Optional[int] = ..., min_positive_vfpo: _Optional[int] = ..., max_positive_vfpo: _Optional[int] = ..., min_negative_vfpo: _Optional[int] = ..., max_negative_vfpo: _Optional[int] = ..., last_segment: _Optional[str] = ..., live_edge_position_ms: _Optional[int] = ..., disc_old_position_ms: _Optional[int] = ..., disc_new_position_ms: _Optional[int] = ..., disc_reason: _Optional[str] = ..., max_memory_bytes: _Optional[int] = ..., total_memory_bytes: _Optional[int] = ..., used_memory_bytes: _Optional[int] = ..., free_memory_bytes: _Optional[int] = ..., exit_type: _Optional[_Union[QosEventMetadata.ExitType, str]] = ..., current_state: _Optional[_Union[QosEventMetadata.CurrentState, str]] = ..., previous_selected_quality_level: _Optional[_Union[_playback_state_info_pb2.VideoQuality, str]] = ..., data_type: _Optional[_Union[QosEventMetadata.DataType, str]] = ..., playing_ad: _Optional[_Union[QosEventMetadata.PlayingAd, str]] = ..., memory_level: _Optional[_Union[QosEventMetadata.MemoryLevel, str]] = ..., master_manifest_info: _Optional[_Union[_http_connection_stats_pb2.HttpConnectionStats, _Mapping]] = ..., drm_license_info: _Optional[_Union[_http_connection_stats_pb2.HttpConnectionStats, _Mapping]] = ..., video_metadata_info: _Optional[_Union[_http_connection_stats_pb2.HttpConnectionStats, _Mapping]] = ..., first_init_segment_info: _Optional[_Union[_http_connection_stats_pb2.HttpConnectionStats, _Mapping]] = ..., first_video_segment_info: _Optional[_Union[_http_connection_stats_pb2.HttpConnectionStats, _Mapping]] = ..., first_audio_segment_info: _Optional[_Union[_http_connection_stats_pb2.HttpConnectionStats, _Mapping]] = ..., first_subtitle_file_info: _Optional[_Union[_http_connection_stats_pb2.HttpConnectionStats, _Mapping]] = ..., http_connection_stats: _Optional[_Union[_http_connection_stats_pb2.HttpConnectionStats, _Mapping]] = ..., byte_range: _Optional[str] = ..., bytes_downloaded: _Optional[int] = ..., tracks: _Optional[_Union[Tracks, _Mapping]] = ..., bitrate_lowerbound_bps: _Optional[int] = ..., bitrate_upperbound_bps: _Optional[int] = ..., width_lowerbound_px: _Optional[int] = ..., width_upperbound_px: _Optional[int] = ..., buffer_goal_ms: _Optional[int] = ..., bitrate_bps: _Optional[int] = ..., abr_algorithm: _Optional[str] = ..., abr_parameters: _Optional[str] = ..., abr_context: _Optional[str] = ..., certificate_sent_offset_ms: _Optional[int] = ..., certificate_received_offset_ms: _Optional[int] = ..., drm_license_url: _Optional[str] = ..., resume_at: _Optional[int] = ..., last_updated_msq: _Optional[int] = ..., ts_last_manifest_refresh_ms: _Optional[int] = ..., manifest_msq: _Optional[int] = ..., msq_mismatch_count: _Optional[int] = ..., current_presentation_timestamp_us: _Optional[int] = ..., expected_presentation_timestamp_us: _Optional[int] = ..., did_auto_seek: bool = ..., speed_test_type: _Optional[_Union[SpeedTestType, str]] = ..., speed_test_infos: _Optional[_Iterable[_Union[SpeedTestInfo, _Mapping]]] = ..., buffereds: _Optional[_Iterable[_Union[Buffered, _Mapping]]] = ..., is_resume_from_seek: bool = ..., cdn_name: _Optional[str] = ..., url_host: _Optional[str] = ..., timestamp_difference_ms: _Optional[int] = ..., is_buffering: bool = ..., video_stuck_duration_ms: _Optional[int] = ..., connection_speed: _Optional[str] = ..., stream_bandwidth_kbps: _Optional[int] = ..., manifest_period_count: _Optional[int] = ..., audio_buffer_length: _Optional[int] = ..., gaps_jumped: _Optional[int] = ..., buffered_start_time_ms: _Optional[int] = ..., buffered_end_time_ms: _Optional[int] = ..., is_retrying_with_last_playback_asset: bool = ...) -> None: ...

class Tracks(_message.Message):
    __slots__ = ("audio_tracks", "video_tracks")
    AUDIO_TRACKS_FIELD_NUMBER: _ClassVar[int]
    VIDEO_TRACKS_FIELD_NUMBER: _ClassVar[int]
    audio_tracks: _containers.RepeatedCompositeFieldContainer[TrackInfo]
    video_tracks: _containers.RepeatedCompositeFieldContainer[TrackInfo]
    def __init__(self, audio_tracks: _Optional[_Iterable[_Union[TrackInfo, _Mapping]]] = ..., video_tracks: _Optional[_Iterable[_Union[TrackInfo, _Mapping]]] = ...) -> None: ...

class TrackInfo(_message.Message):
    __slots__ = ("bitrate_bps", "resolution_px")
    BITRATE_BPS_FIELD_NUMBER: _ClassVar[int]
    RESOLUTION_PX_FIELD_NUMBER: _ClassVar[int]
    bitrate_bps: int
    resolution_px: str
    def __init__(self, bitrate_bps: _Optional[int] = ..., resolution_px: _Optional[str] = ...) -> None: ...

class SpeedTestInfo(_message.Message):
    __slots__ = ("request_url", "download_bytes", "download_start_time_ms", "download_end_time_ms", "cdn_connection_stats", "http_error_code", "error_message")
    REQUEST_URL_FIELD_NUMBER: _ClassVar[int]
    DOWNLOAD_BYTES_FIELD_NUMBER: _ClassVar[int]
    DOWNLOAD_START_TIME_MS_FIELD_NUMBER: _ClassVar[int]
    DOWNLOAD_END_TIME_MS_FIELD_NUMBER: _ClassVar[int]
    CDN_CONNECTION_STATS_FIELD_NUMBER: _ClassVar[int]
    HTTP_ERROR_CODE_FIELD_NUMBER: _ClassVar[int]
    ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    request_url: str
    download_bytes: int
    download_start_time_ms: int
    download_end_time_ms: int
    cdn_connection_stats: _http_connection_stats_pb2.HttpConnectionStats
    http_error_code: str
    error_message: str
    def __init__(self, request_url: _Optional[str] = ..., download_bytes: _Optional[int] = ..., download_start_time_ms: _Optional[int] = ..., download_end_time_ms: _Optional[int] = ..., cdn_connection_stats: _Optional[_Union[_http_connection_stats_pb2.HttpConnectionStats, _Mapping]] = ..., http_error_code: _Optional[str] = ..., error_message: _Optional[str] = ...) -> None: ...

class Buffered(_message.Message):
    __slots__ = ("start", "end")
    START_FIELD_NUMBER: _ClassVar[int]
    END_FIELD_NUMBER: _ClassVar[int]
    start: int
    end: int
    def __init__(self, start: _Optional[int] = ..., end: _Optional[int] = ...) -> None: ...
