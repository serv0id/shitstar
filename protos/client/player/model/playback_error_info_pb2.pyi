from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ErrorStage(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ERROR_STAGE_UNSPECIFIED: _ClassVar[ErrorStage]
    ERROR_STAGE_FETCH_URL: _ClassVar[ErrorStage]
    ERROR_STAGE_INIT_PLAYER: _ClassVar[ErrorStage]
    ERROR_STAGE_LICENSE_URL: _ClassVar[ErrorStage]
    ERROR_STAGE_MASTER_PLAYLIST: _ClassVar[ErrorStage]
    ERROR_STAGE_MEDIA_SEGMENT: _ClassVar[ErrorStage]
    ERROR_STAGE_PLAYING: _ClassVar[ErrorStage]
ERROR_STAGE_UNSPECIFIED: ErrorStage
ERROR_STAGE_FETCH_URL: ErrorStage
ERROR_STAGE_INIT_PLAYER: ErrorStage
ERROR_STAGE_LICENSE_URL: ErrorStage
ERROR_STAGE_MASTER_PLAYLIST: ErrorStage
ERROR_STAGE_MEDIA_SEGMENT: ErrorStage
ERROR_STAGE_PLAYING: ErrorStage

class PlaybackErrorInfo(_message.Message):
    __slots__ = ("error_code", "error_http_status_code", "failed_url", "error_stage", "error_description", "error_logs", "is_ads_playing", "native_error_code", "is_playback_started", "is_switching_to_fallback", "time_to_failure_ms", "request_cookie", "bff_load_time_ms", "total_time_to_failure_ms", "is_retrying_with_last_playback_asset", "failed_channel_id")
    ERROR_CODE_FIELD_NUMBER: _ClassVar[int]
    ERROR_HTTP_STATUS_CODE_FIELD_NUMBER: _ClassVar[int]
    FAILED_URL_FIELD_NUMBER: _ClassVar[int]
    ERROR_STAGE_FIELD_NUMBER: _ClassVar[int]
    ERROR_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    ERROR_LOGS_FIELD_NUMBER: _ClassVar[int]
    IS_ADS_PLAYING_FIELD_NUMBER: _ClassVar[int]
    NATIVE_ERROR_CODE_FIELD_NUMBER: _ClassVar[int]
    IS_PLAYBACK_STARTED_FIELD_NUMBER: _ClassVar[int]
    IS_SWITCHING_TO_FALLBACK_FIELD_NUMBER: _ClassVar[int]
    TIME_TO_FAILURE_MS_FIELD_NUMBER: _ClassVar[int]
    REQUEST_COOKIE_FIELD_NUMBER: _ClassVar[int]
    BFF_LOAD_TIME_MS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_TIME_TO_FAILURE_MS_FIELD_NUMBER: _ClassVar[int]
    IS_RETRYING_WITH_LAST_PLAYBACK_ASSET_FIELD_NUMBER: _ClassVar[int]
    FAILED_CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    error_code: str
    error_http_status_code: int
    failed_url: str
    error_stage: ErrorStage
    error_description: str
    error_logs: str
    is_ads_playing: bool
    native_error_code: str
    is_playback_started: bool
    is_switching_to_fallback: bool
    time_to_failure_ms: int
    request_cookie: str
    bff_load_time_ms: int
    total_time_to_failure_ms: int
    is_retrying_with_last_playback_asset: bool
    failed_channel_id: str
    def __init__(self, error_code: _Optional[str] = ..., error_http_status_code: _Optional[int] = ..., failed_url: _Optional[str] = ..., error_stage: _Optional[_Union[ErrorStage, str]] = ..., error_description: _Optional[str] = ..., error_logs: _Optional[str] = ..., is_ads_playing: bool = ..., native_error_code: _Optional[str] = ..., is_playback_started: bool = ..., is_switching_to_fallback: bool = ..., time_to_failure_ms: _Optional[int] = ..., request_cookie: _Optional[str] = ..., bff_load_time_ms: _Optional[int] = ..., total_time_to_failure_ms: _Optional[int] = ..., is_retrying_with_last_playback_asset: bool = ..., failed_channel_id: _Optional[str] = ...) -> None: ...
