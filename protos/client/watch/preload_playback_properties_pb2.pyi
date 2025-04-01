from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PreloadPlaybackProperties(_message.Message):
    __slots__ = ()
    class PreloadEligibility(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        PRELOAD_ELIGIBILITY_UNSPECIFIED: _ClassVar[PreloadPlaybackProperties.PreloadEligibility]
        PRELOAD_ELIGIBILITY_NOT_ELIGIBLE: _ClassVar[PreloadPlaybackProperties.PreloadEligibility]
        PRELOAD_ELIGIBILITY_ONLY_BFF: _ClassVar[PreloadPlaybackProperties.PreloadEligibility]
        PRELOAD_ELIGIBILITY_BFF_AND_PLAYBACK: _ClassVar[PreloadPlaybackProperties.PreloadEligibility]
    PRELOAD_ELIGIBILITY_UNSPECIFIED: PreloadPlaybackProperties.PreloadEligibility
    PRELOAD_ELIGIBILITY_NOT_ELIGIBLE: PreloadPlaybackProperties.PreloadEligibility
    PRELOAD_ELIGIBILITY_ONLY_BFF: PreloadPlaybackProperties.PreloadEligibility
    PRELOAD_ELIGIBILITY_BFF_AND_PLAYBACK: PreloadPlaybackProperties.PreloadEligibility
    class PreloadSuccessType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        PRELOAD_SUCCESS_TYPE_UNSPECIFIED: _ClassVar[PreloadPlaybackProperties.PreloadSuccessType]
        PRELOAD_SUCCESS_TYPE_BFF: _ClassVar[PreloadPlaybackProperties.PreloadSuccessType]
        PRELOAD_SUCCESS_TYPE_PLAYBACK: _ClassVar[PreloadPlaybackProperties.PreloadSuccessType]
    PRELOAD_SUCCESS_TYPE_UNSPECIFIED: PreloadPlaybackProperties.PreloadSuccessType
    PRELOAD_SUCCESS_TYPE_BFF: PreloadPlaybackProperties.PreloadSuccessType
    PRELOAD_SUCCESS_TYPE_PLAYBACK: PreloadPlaybackProperties.PreloadSuccessType
    class PreloadFailureType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        PRELOAD_FAILURE_TYPE_UNSPECIFIED: _ClassVar[PreloadPlaybackProperties.PreloadFailureType]
        PRELOAD_FAILURE_TYPE_BFF: _ClassVar[PreloadPlaybackProperties.PreloadFailureType]
        PRELOAD_FAILURE_TYPE_PLAYBACK_DATA: _ClassVar[PreloadPlaybackProperties.PreloadFailureType]
        PRELOAD_FAILURE_TYPE_PREEMPTIVE: _ClassVar[PreloadPlaybackProperties.PreloadFailureType]
        PRELOAD_FAILURE_TYPE_EXITED: _ClassVar[PreloadPlaybackProperties.PreloadFailureType]
    PRELOAD_FAILURE_TYPE_UNSPECIFIED: PreloadPlaybackProperties.PreloadFailureType
    PRELOAD_FAILURE_TYPE_BFF: PreloadPlaybackProperties.PreloadFailureType
    PRELOAD_FAILURE_TYPE_PLAYBACK_DATA: PreloadPlaybackProperties.PreloadFailureType
    PRELOAD_FAILURE_TYPE_PREEMPTIVE: PreloadPlaybackProperties.PreloadFailureType
    PRELOAD_FAILURE_TYPE_EXITED: PreloadPlaybackProperties.PreloadFailureType
    class PreloadPhase(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        PRELOAD_PHASE_UNSPECIFIED: _ClassVar[PreloadPlaybackProperties.PreloadPhase]
        PRELOAD_PHASE_INITIAL: _ClassVar[PreloadPlaybackProperties.PreloadPhase]
        PRELOAD_PHASE_ELLIGIBLE: _ClassVar[PreloadPlaybackProperties.PreloadPhase]
        PRELOAD_PHASE_BFF_TRIGGERED: _ClassVar[PreloadPlaybackProperties.PreloadPhase]
        PRELOAD_PHASE_BFF_FETCHED: _ClassVar[PreloadPlaybackProperties.PreloadPhase]
        PRELOAD_PHASE_PLAYBACK_PRELOADED: _ClassVar[PreloadPlaybackProperties.PreloadPhase]
        PRELOAD_PHASE_PLAYBACK_CONSUMED: _ClassVar[PreloadPlaybackProperties.PreloadPhase]
        PRELOAD_PHASE_ELIGIBLE: _ClassVar[PreloadPlaybackProperties.PreloadPhase]
        PRELOAD_PHASE_CONSUMED: _ClassVar[PreloadPlaybackProperties.PreloadPhase]
    PRELOAD_PHASE_UNSPECIFIED: PreloadPlaybackProperties.PreloadPhase
    PRELOAD_PHASE_INITIAL: PreloadPlaybackProperties.PreloadPhase
    PRELOAD_PHASE_ELLIGIBLE: PreloadPlaybackProperties.PreloadPhase
    PRELOAD_PHASE_BFF_TRIGGERED: PreloadPlaybackProperties.PreloadPhase
    PRELOAD_PHASE_BFF_FETCHED: PreloadPlaybackProperties.PreloadPhase
    PRELOAD_PHASE_PLAYBACK_PRELOADED: PreloadPlaybackProperties.PreloadPhase
    PRELOAD_PHASE_PLAYBACK_CONSUMED: PreloadPlaybackProperties.PreloadPhase
    PRELOAD_PHASE_ELIGIBLE: PreloadPlaybackProperties.PreloadPhase
    PRELOAD_PHASE_CONSUMED: PreloadPlaybackProperties.PreloadPhase
    class PreloadFailureReason(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        PRELOAD_FAILURE_REASON_UNSPECIFIED: _ClassVar[PreloadPlaybackProperties.PreloadFailureReason]
        PRELOAD_FAILURE_REASON_COMMON: _ClassVar[PreloadPlaybackProperties.PreloadFailureReason]
        PRELOAD_FAILURE_REASON_PREEMPTIVE: _ClassVar[PreloadPlaybackProperties.PreloadFailureReason]
        PRELOAD_FAILURE_REASON_EXITED: _ClassVar[PreloadPlaybackProperties.PreloadFailureReason]
        PRELOAD_FAILURE_REASON_BFF_REQUEST_ERROR: _ClassVar[PreloadPlaybackProperties.PreloadFailureReason]
        PRELOAD_FAILURE_REASON_PLAYBACK_REQUEST: _ClassVar[PreloadPlaybackProperties.PreloadFailureReason]
        PRELOAD_FAILURE_REASON_PLAYBACK_EXPIRED: _ClassVar[PreloadPlaybackProperties.PreloadFailureReason]
        PRELOAD_FAILURE_REASON_PLAYBACK_ERROR: _ClassVar[PreloadPlaybackProperties.PreloadFailureReason]
        PRELOAD_FAILURE_REASON_PLAYBACK_NETWORK_ERROR: _ClassVar[PreloadPlaybackProperties.PreloadFailureReason]
        PRELOAD_FAILURE_REASON_OFFLINE_PLAYBACK_ERROR: _ClassVar[PreloadPlaybackProperties.PreloadFailureReason]
        PRELOAD_FAILURE_REASON_WRONG_VIDEO_TYPE: _ClassVar[PreloadPlaybackProperties.PreloadFailureReason]
        PRELOAD_FAILURE_REASON_MISMATCHED_VIDEO_QUALITY: _ClassVar[PreloadPlaybackProperties.PreloadFailureReason]
        PRELOAD_FAILURE_REASON_MISMATCHED_AUIDO: _ClassVar[PreloadPlaybackProperties.PreloadFailureReason]
        PRELOAD_FAILURE_REASON_MISMATCHED_SUBTITLE: _ClassVar[PreloadPlaybackProperties.PreloadFailureReason]
        PRELOAD_FAILURE_REASON_APP_KILLED: _ClassVar[PreloadPlaybackProperties.PreloadFailureReason]
        PRELOAD_FAILURE_REASON_PAGE_REFRESHED: _ClassVar[PreloadPlaybackProperties.PreloadFailureReason]
        PRELOAD_FAILURE_REASON_MISMATCHED_AUDIO: _ClassVar[PreloadPlaybackProperties.PreloadFailureReason]
    PRELOAD_FAILURE_REASON_UNSPECIFIED: PreloadPlaybackProperties.PreloadFailureReason
    PRELOAD_FAILURE_REASON_COMMON: PreloadPlaybackProperties.PreloadFailureReason
    PRELOAD_FAILURE_REASON_PREEMPTIVE: PreloadPlaybackProperties.PreloadFailureReason
    PRELOAD_FAILURE_REASON_EXITED: PreloadPlaybackProperties.PreloadFailureReason
    PRELOAD_FAILURE_REASON_BFF_REQUEST_ERROR: PreloadPlaybackProperties.PreloadFailureReason
    PRELOAD_FAILURE_REASON_PLAYBACK_REQUEST: PreloadPlaybackProperties.PreloadFailureReason
    PRELOAD_FAILURE_REASON_PLAYBACK_EXPIRED: PreloadPlaybackProperties.PreloadFailureReason
    PRELOAD_FAILURE_REASON_PLAYBACK_ERROR: PreloadPlaybackProperties.PreloadFailureReason
    PRELOAD_FAILURE_REASON_PLAYBACK_NETWORK_ERROR: PreloadPlaybackProperties.PreloadFailureReason
    PRELOAD_FAILURE_REASON_OFFLINE_PLAYBACK_ERROR: PreloadPlaybackProperties.PreloadFailureReason
    PRELOAD_FAILURE_REASON_WRONG_VIDEO_TYPE: PreloadPlaybackProperties.PreloadFailureReason
    PRELOAD_FAILURE_REASON_MISMATCHED_VIDEO_QUALITY: PreloadPlaybackProperties.PreloadFailureReason
    PRELOAD_FAILURE_REASON_MISMATCHED_AUIDO: PreloadPlaybackProperties.PreloadFailureReason
    PRELOAD_FAILURE_REASON_MISMATCHED_SUBTITLE: PreloadPlaybackProperties.PreloadFailureReason
    PRELOAD_FAILURE_REASON_APP_KILLED: PreloadPlaybackProperties.PreloadFailureReason
    PRELOAD_FAILURE_REASON_PAGE_REFRESHED: PreloadPlaybackProperties.PreloadFailureReason
    PRELOAD_FAILURE_REASON_MISMATCHED_AUDIO: PreloadPlaybackProperties.PreloadFailureReason
    class PreloadDataType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        PRELOAD_DATA_TYPE_UNSPECIFIED: _ClassVar[PreloadPlaybackProperties.PreloadDataType]
        PRELOAD_DATA_TYPE_BFF: _ClassVar[PreloadPlaybackProperties.PreloadDataType]
        PRELOAD_DATA_TYPE_PLAYBACK: _ClassVar[PreloadPlaybackProperties.PreloadDataType]
    PRELOAD_DATA_TYPE_UNSPECIFIED: PreloadPlaybackProperties.PreloadDataType
    PRELOAD_DATA_TYPE_BFF: PreloadPlaybackProperties.PreloadDataType
    PRELOAD_DATA_TYPE_PLAYBACK: PreloadPlaybackProperties.PreloadDataType
    class PreloadFailureData(_message.Message):
        __slots__ = ("type", "reason")
        TYPE_FIELD_NUMBER: _ClassVar[int]
        REASON_FIELD_NUMBER: _ClassVar[int]
        type: PreloadPlaybackProperties.PreloadFailureType
        reason: PreloadPlaybackProperties.PreloadFailureReason
        def __init__(self, type: _Optional[_Union[PreloadPlaybackProperties.PreloadFailureType, str]] = ..., reason: _Optional[_Union[PreloadPlaybackProperties.PreloadFailureReason, str]] = ...) -> None: ...
    class PreloadStatus(_message.Message):
        __slots__ = ("preload_eligibility", "preload_success_type", "preload_failure_data")
        PRELOAD_ELIGIBILITY_FIELD_NUMBER: _ClassVar[int]
        PRELOAD_SUCCESS_TYPE_FIELD_NUMBER: _ClassVar[int]
        PRELOAD_FAILURE_DATA_FIELD_NUMBER: _ClassVar[int]
        preload_eligibility: PreloadPlaybackProperties.PreloadEligibility
        preload_success_type: PreloadPlaybackProperties.PreloadSuccessType
        preload_failure_data: PreloadPlaybackProperties.PreloadFailureData
        def __init__(self, preload_eligibility: _Optional[_Union[PreloadPlaybackProperties.PreloadEligibility, str]] = ..., preload_success_type: _Optional[_Union[PreloadPlaybackProperties.PreloadSuccessType, str]] = ..., preload_failure_data: _Optional[_Union[PreloadPlaybackProperties.PreloadFailureData, _Mapping]] = ...) -> None: ...
    class PreloadConfig(_message.Message):
        __slots__ = ("multiplayer_preload_enabled", "manifest_preload_enabled", "proxy_server_enabled")
        MULTIPLAYER_PRELOAD_ENABLED_FIELD_NUMBER: _ClassVar[int]
        MANIFEST_PRELOAD_ENABLED_FIELD_NUMBER: _ClassVar[int]
        PROXY_SERVER_ENABLED_FIELD_NUMBER: _ClassVar[int]
        multiplayer_preload_enabled: bool
        manifest_preload_enabled: bool
        proxy_server_enabled: bool
        def __init__(self, multiplayer_preload_enabled: bool = ..., manifest_preload_enabled: bool = ..., proxy_server_enabled: bool = ...) -> None: ...
    class PreloadPhaseChange(_message.Message):
        __slots__ = ("from_phase", "to_phase", "is_successful", "failure_reason", "content_id", "config", "consumed_data_type", "transformed_bytes", "data_size_bytes")
        FROM_PHASE_FIELD_NUMBER: _ClassVar[int]
        TO_PHASE_FIELD_NUMBER: _ClassVar[int]
        IS_SUCCESSFUL_FIELD_NUMBER: _ClassVar[int]
        FAILURE_REASON_FIELD_NUMBER: _ClassVar[int]
        CONTENT_ID_FIELD_NUMBER: _ClassVar[int]
        CONFIG_FIELD_NUMBER: _ClassVar[int]
        CONSUMED_DATA_TYPE_FIELD_NUMBER: _ClassVar[int]
        TRANSFORMED_BYTES_FIELD_NUMBER: _ClassVar[int]
        DATA_SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
        from_phase: PreloadPlaybackProperties.PreloadPhase
        to_phase: PreloadPlaybackProperties.PreloadPhase
        is_successful: bool
        failure_reason: PreloadPlaybackProperties.PreloadFailureReason
        content_id: str
        config: PreloadPlaybackProperties.PreloadConfig
        consumed_data_type: PreloadPlaybackProperties.PreloadDataType
        transformed_bytes: int
        data_size_bytes: int
        def __init__(self, from_phase: _Optional[_Union[PreloadPlaybackProperties.PreloadPhase, str]] = ..., to_phase: _Optional[_Union[PreloadPlaybackProperties.PreloadPhase, str]] = ..., is_successful: bool = ..., failure_reason: _Optional[_Union[PreloadPlaybackProperties.PreloadFailureReason, str]] = ..., content_id: _Optional[str] = ..., config: _Optional[_Union[PreloadPlaybackProperties.PreloadConfig, _Mapping]] = ..., consumed_data_type: _Optional[_Union[PreloadPlaybackProperties.PreloadDataType, str]] = ..., transformed_bytes: _Optional[int] = ..., data_size_bytes: _Optional[int] = ...) -> None: ...
    def __init__(self) -> None: ...

class WatchPreloadProperties(_message.Message):
    __slots__ = ("preload_phase_change", "cid")
    PRELOAD_PHASE_CHANGE_FIELD_NUMBER: _ClassVar[int]
    CID_FIELD_NUMBER: _ClassVar[int]
    preload_phase_change: PreloadPlaybackProperties.PreloadPhaseChange
    cid: str
    def __init__(self, preload_phase_change: _Optional[_Union[PreloadPlaybackProperties.PreloadPhaseChange, _Mapping]] = ..., cid: _Optional[str] = ...) -> None: ...
