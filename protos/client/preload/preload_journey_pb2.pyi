from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PreloadStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PRELOAD_STATUS_UNSPECIFIED: _ClassVar[PreloadStatus]
    PRELOAD_STATUS_NO_PRELOAD: _ClassVar[PreloadStatus]
    PRELOAD_STATUS_BFF: _ClassVar[PreloadStatus]
    PRELOAD_STATUS_MANIFEST: _ClassVar[PreloadStatus]
    PRELOAD_STATUS_VIDEO_SEGMENT: _ClassVar[PreloadStatus]
    PRELOAD_STATUS_NOT_APPLICABLE: _ClassVar[PreloadStatus]
PRELOAD_STATUS_UNSPECIFIED: PreloadStatus
PRELOAD_STATUS_NO_PRELOAD: PreloadStatus
PRELOAD_STATUS_BFF: PreloadStatus
PRELOAD_STATUS_MANIFEST: PreloadStatus
PRELOAD_STATUS_VIDEO_SEGMENT: PreloadStatus
PRELOAD_STATUS_NOT_APPLICABLE: PreloadStatus

class PreloadAddition(_message.Message):
    __slots__ = ("preload_source", "status")
    PRELOAD_SOURCE_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    preload_source: PreloadSource
    status: PreloadStatus
    def __init__(self, preload_source: _Optional[_Union[PreloadSource, _Mapping]] = ..., status: _Optional[_Union[PreloadStatus, str]] = ...) -> None: ...

class PreloadSource(_message.Message):
    __slots__ = ("preload_source_type", "bff_source_type", "network", "cache")
    class PreloadSourceType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        PRELOAD_SOURCE_TYPE_UNSPECIFIED: _ClassVar[PreloadSource.PreloadSourceType]
        PRELOAD_SOURCE_TYPE_NETWORK: _ClassVar[PreloadSource.PreloadSourceType]
        PRELOAD_SOURCE_TYPE_CACHE: _ClassVar[PreloadSource.PreloadSourceType]
    PRELOAD_SOURCE_TYPE_UNSPECIFIED: PreloadSource.PreloadSourceType
    PRELOAD_SOURCE_TYPE_NETWORK: PreloadSource.PreloadSourceType
    PRELOAD_SOURCE_TYPE_CACHE: PreloadSource.PreloadSourceType
    class Network(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class Cache(_message.Message):
        __slots__ = ("identifier", "target", "cache_identifier")
        IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
        TARGET_FIELD_NUMBER: _ClassVar[int]
        CACHE_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
        identifier: str
        target: str
        cache_identifier: str
        def __init__(self, identifier: _Optional[str] = ..., target: _Optional[str] = ..., cache_identifier: _Optional[str] = ...) -> None: ...
    PRELOAD_SOURCE_TYPE_FIELD_NUMBER: _ClassVar[int]
    BFF_SOURCE_TYPE_FIELD_NUMBER: _ClassVar[int]
    NETWORK_FIELD_NUMBER: _ClassVar[int]
    CACHE_FIELD_NUMBER: _ClassVar[int]
    preload_source_type: PreloadSource.PreloadSourceType
    bff_source_type: PreloadSource.PreloadSourceType
    network: PreloadSource.Network
    cache: PreloadSource.Cache
    def __init__(self, preload_source_type: _Optional[_Union[PreloadSource.PreloadSourceType, str]] = ..., bff_source_type: _Optional[_Union[PreloadSource.PreloadSourceType, str]] = ..., network: _Optional[_Union[PreloadSource.Network, _Mapping]] = ..., cache: _Optional[_Union[PreloadSource.Cache, _Mapping]] = ...) -> None: ...

class PreloadJourneyProperties(_message.Message):
    __slots__ = ("stage", "api_type", "status", "failure_reason", "preload_session_id", "url")
    class Stage(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STAGE_UNSPECIFIED: _ClassVar[PreloadJourneyProperties.Stage]
        STAGE_RECEIVED: _ClassVar[PreloadJourneyProperties.Stage]
        STAGE_START: _ClassVar[PreloadJourneyProperties.Stage]
        STAGE_FINISH: _ClassVar[PreloadJourneyProperties.Stage]
        STAGE_CONSUME: _ClassVar[PreloadJourneyProperties.Stage]
        STAGE_FAILED: _ClassVar[PreloadJourneyProperties.Stage]
    STAGE_UNSPECIFIED: PreloadJourneyProperties.Stage
    STAGE_RECEIVED: PreloadJourneyProperties.Stage
    STAGE_START: PreloadJourneyProperties.Stage
    STAGE_FINISH: PreloadJourneyProperties.Stage
    STAGE_CONSUME: PreloadJourneyProperties.Stage
    STAGE_FAILED: PreloadJourneyProperties.Stage
    class ApiType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        API_TYPE_UNSPECIFIED: _ClassVar[PreloadJourneyProperties.ApiType]
        API_TYPE_PAGE_BFF: _ClassVar[PreloadJourneyProperties.ApiType]
        API_TYPE_WIDGET_BFF: _ClassVar[PreloadJourneyProperties.ApiType]
    API_TYPE_UNSPECIFIED: PreloadJourneyProperties.ApiType
    API_TYPE_PAGE_BFF: PreloadJourneyProperties.ApiType
    API_TYPE_WIDGET_BFF: PreloadJourneyProperties.ApiType
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATUS_UNSPECIFIED: _ClassVar[PreloadJourneyProperties.Status]
        STATUS_TRIGGERED: _ClassVar[PreloadJourneyProperties.Status]
        STATUS_SUCCESS: _ClassVar[PreloadJourneyProperties.Status]
        STATUS_FAILURE: _ClassVar[PreloadJourneyProperties.Status]
    STATUS_UNSPECIFIED: PreloadJourneyProperties.Status
    STATUS_TRIGGERED: PreloadJourneyProperties.Status
    STATUS_SUCCESS: PreloadJourneyProperties.Status
    STATUS_FAILURE: PreloadJourneyProperties.Status
    class FailureReason(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        FAILURE_REASON_UNSPECIFIED: _ClassVar[PreloadJourneyProperties.FailureReason]
        FAILURE_REASON_API_FAILED: _ClassVar[PreloadJourneyProperties.FailureReason]
        FAILURE_REASON_NONE: _ClassVar[PreloadJourneyProperties.FailureReason]
    FAILURE_REASON_UNSPECIFIED: PreloadJourneyProperties.FailureReason
    FAILURE_REASON_API_FAILED: PreloadJourneyProperties.FailureReason
    FAILURE_REASON_NONE: PreloadJourneyProperties.FailureReason
    STAGE_FIELD_NUMBER: _ClassVar[int]
    API_TYPE_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_REASON_FIELD_NUMBER: _ClassVar[int]
    PRELOAD_SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    stage: PreloadJourneyProperties.Stage
    api_type: PreloadJourneyProperties.ApiType
    status: PreloadJourneyProperties.Status
    failure_reason: PreloadJourneyProperties.FailureReason
    preload_session_id: str
    url: str
    def __init__(self, stage: _Optional[_Union[PreloadJourneyProperties.Stage, str]] = ..., api_type: _Optional[_Union[PreloadJourneyProperties.ApiType, str]] = ..., status: _Optional[_Union[PreloadJourneyProperties.Status, str]] = ..., failure_reason: _Optional[_Union[PreloadJourneyProperties.FailureReason, str]] = ..., preload_session_id: _Optional[str] = ..., url: _Optional[str] = ...) -> None: ...
