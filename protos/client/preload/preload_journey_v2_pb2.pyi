from client.preload import preload_journey_pb2 as _preload_journey_pb2
from client.preload import preload_models_pb2 as _preload_models_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PreloadAdditionV2(_message.Message):
    __slots__ = ("preload_source_v2", "preload_status_v2")
    PRELOAD_SOURCE_V2_FIELD_NUMBER: _ClassVar[int]
    PRELOAD_STATUS_V2_FIELD_NUMBER: _ClassVar[int]
    preload_source_v2: PreloadSourceV2
    preload_status_v2: _preload_journey_pb2.PreloadStatus
    def __init__(self, preload_source_v2: _Optional[_Union[PreloadSourceV2, _Mapping]] = ..., preload_status_v2: _Optional[_Union[_preload_journey_pb2.PreloadStatus, str]] = ...) -> None: ...

class PreloadSourceV2(_message.Message):
    __slots__ = ("preload_source_type_v2", "bff_source_type_v2", "bff_source_type_v3", "network", "cache")
    class PreloadSourceType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        PRELOAD_SOURCE_TYPE_UNSPECIFIED: _ClassVar[PreloadSourceV2.PreloadSourceType]
        PRELOAD_SOURCE_TYPE_NETWORK: _ClassVar[PreloadSourceV2.PreloadSourceType]
        PRELOAD_SOURCE_TYPE_CACHE: _ClassVar[PreloadSourceV2.PreloadSourceType]
    PRELOAD_SOURCE_TYPE_UNSPECIFIED: PreloadSourceV2.PreloadSourceType
    PRELOAD_SOURCE_TYPE_NETWORK: PreloadSourceV2.PreloadSourceType
    PRELOAD_SOURCE_TYPE_CACHE: PreloadSourceV2.PreloadSourceType
    class Network(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class Cache(_message.Message):
        __slots__ = ("cache_identifier_v2",)
        CACHE_IDENTIFIER_V2_FIELD_NUMBER: _ClassVar[int]
        cache_identifier_v2: str
        def __init__(self, cache_identifier_v2: _Optional[str] = ...) -> None: ...
    PRELOAD_SOURCE_TYPE_V2_FIELD_NUMBER: _ClassVar[int]
    BFF_SOURCE_TYPE_V2_FIELD_NUMBER: _ClassVar[int]
    BFF_SOURCE_TYPE_V3_FIELD_NUMBER: _ClassVar[int]
    NETWORK_FIELD_NUMBER: _ClassVar[int]
    CACHE_FIELD_NUMBER: _ClassVar[int]
    preload_source_type_v2: PreloadSourceV2.PreloadSourceType
    bff_source_type_v2: PreloadSourceV2.PreloadSourceType
    bff_source_type_v3: _preload_models_pb2.PreloadModels.DataSourceTypeDetail
    network: PreloadSourceV2.Network
    cache: PreloadSourceV2.Cache
    def __init__(self, preload_source_type_v2: _Optional[_Union[PreloadSourceV2.PreloadSourceType, str]] = ..., bff_source_type_v2: _Optional[_Union[PreloadSourceV2.PreloadSourceType, str]] = ..., bff_source_type_v3: _Optional[_Union[_preload_models_pb2.PreloadModels.DataSourceTypeDetail, _Mapping]] = ..., network: _Optional[_Union[PreloadSourceV2.Network, _Mapping]] = ..., cache: _Optional[_Union[PreloadSourceV2.Cache, _Mapping]] = ...) -> None: ...

class PreloadJourneyPropertiesV2(_message.Message):
    __slots__ = ("preload_journey_stage", "preload_journey_api_type", "preload_journey_status", "preload_journey_failure_reason", "preload_journey_url", "preload_journey_session_id", "bff_preload", "bff_preload_apis", "player_data_preload", "player_data_preload_apis", "bff_preload_consumed", "player_data_preload_consumed", "preload_player_data_type")
    class Stage(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STAGE_UNSPECIFIED: _ClassVar[PreloadJourneyPropertiesV2.Stage]
        STAGE_RECEIVED: _ClassVar[PreloadJourneyPropertiesV2.Stage]
        STAGE_START: _ClassVar[PreloadJourneyPropertiesV2.Stage]
        STAGE_FINISH: _ClassVar[PreloadJourneyPropertiesV2.Stage]
        STAGE_CONSUME: _ClassVar[PreloadJourneyPropertiesV2.Stage]
        STAGE_FAILED: _ClassVar[PreloadJourneyPropertiesV2.Stage]
    STAGE_UNSPECIFIED: PreloadJourneyPropertiesV2.Stage
    STAGE_RECEIVED: PreloadJourneyPropertiesV2.Stage
    STAGE_START: PreloadJourneyPropertiesV2.Stage
    STAGE_FINISH: PreloadJourneyPropertiesV2.Stage
    STAGE_CONSUME: PreloadJourneyPropertiesV2.Stage
    STAGE_FAILED: PreloadJourneyPropertiesV2.Stage
    class ApiType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        API_TYPE_UNSPECIFIED: _ClassVar[PreloadJourneyPropertiesV2.ApiType]
        API_TYPE_PAGE_BFF: _ClassVar[PreloadJourneyPropertiesV2.ApiType]
        API_TYPE_WIDGET_BFF: _ClassVar[PreloadJourneyPropertiesV2.ApiType]
    API_TYPE_UNSPECIFIED: PreloadJourneyPropertiesV2.ApiType
    API_TYPE_PAGE_BFF: PreloadJourneyPropertiesV2.ApiType
    API_TYPE_WIDGET_BFF: PreloadJourneyPropertiesV2.ApiType
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATUS_UNSPECIFIED: _ClassVar[PreloadJourneyPropertiesV2.Status]
        STATUS_TRIGGERED: _ClassVar[PreloadJourneyPropertiesV2.Status]
        STATUS_SUCCESS: _ClassVar[PreloadJourneyPropertiesV2.Status]
        STATUS_FAILURE: _ClassVar[PreloadJourneyPropertiesV2.Status]
        STATUS_SUCCESSFUL: _ClassVar[PreloadJourneyPropertiesV2.Status]
        STATUS_FAILED: _ClassVar[PreloadJourneyPropertiesV2.Status]
        STATUS_NOT_APPLICABLE_DUE_TO_NETWORK: _ClassVar[PreloadJourneyPropertiesV2.Status]
        STATUS_NOT_APPLICABLE_DUE_TO_BUFFERED_DURATION: _ClassVar[PreloadJourneyPropertiesV2.Status]
        STATUS_NOT_APPLICABLE_DUE_TO_LPD: _ClassVar[PreloadJourneyPropertiesV2.Status]
        STATUS_NOT_APPLICABLE_DUE_TO_UNSUPPORTED_MASTER_MANIFEST: _ClassVar[PreloadJourneyPropertiesV2.Status]
        STATUS_RECEIVED: _ClassVar[PreloadJourneyPropertiesV2.Status]
        STATUS_CONSUMED: _ClassVar[PreloadJourneyPropertiesV2.Status]
        STATUS_PARTIALLY_CONSUMED: _ClassVar[PreloadJourneyPropertiesV2.Status]
        STATUS_NOT_APPLICABLE_DUE_TO_UNSUPPORTED_CDN: _ClassVar[PreloadJourneyPropertiesV2.Status]
        STATUS_NOT_APPLICABLE_DUE_TO_UNSUPPORTED_DOMAIN: _ClassVar[PreloadJourneyPropertiesV2.Status]
        STATUS_NOT_APPLICABLE_DUE_TO_THIRD_PARTY_AD: _ClassVar[PreloadJourneyPropertiesV2.Status]
        STATUS_NOT_APPLICABLE_DUE_TO_FALLBACK_AD: _ClassVar[PreloadJourneyPropertiesV2.Status]
        STATUS_NOT_APPLICABLE_DUE_TO_WRAPPER_RESULUTION_FAILURE: _ClassVar[PreloadJourneyPropertiesV2.Status]
        STATUS_NOT_APPLICABLE_DUE_TO_VAST_PARSING_FAILURE: _ClassVar[PreloadJourneyPropertiesV2.Status]
        STATUS_NOT_APPLICABLE_DUE_TO_UNSUPPORTED_VIDEO_FORMATE: _ClassVar[PreloadJourneyPropertiesV2.Status]
    STATUS_UNSPECIFIED: PreloadJourneyPropertiesV2.Status
    STATUS_TRIGGERED: PreloadJourneyPropertiesV2.Status
    STATUS_SUCCESS: PreloadJourneyPropertiesV2.Status
    STATUS_FAILURE: PreloadJourneyPropertiesV2.Status
    STATUS_SUCCESSFUL: PreloadJourneyPropertiesV2.Status
    STATUS_FAILED: PreloadJourneyPropertiesV2.Status
    STATUS_NOT_APPLICABLE_DUE_TO_NETWORK: PreloadJourneyPropertiesV2.Status
    STATUS_NOT_APPLICABLE_DUE_TO_BUFFERED_DURATION: PreloadJourneyPropertiesV2.Status
    STATUS_NOT_APPLICABLE_DUE_TO_LPD: PreloadJourneyPropertiesV2.Status
    STATUS_NOT_APPLICABLE_DUE_TO_UNSUPPORTED_MASTER_MANIFEST: PreloadJourneyPropertiesV2.Status
    STATUS_RECEIVED: PreloadJourneyPropertiesV2.Status
    STATUS_CONSUMED: PreloadJourneyPropertiesV2.Status
    STATUS_PARTIALLY_CONSUMED: PreloadJourneyPropertiesV2.Status
    STATUS_NOT_APPLICABLE_DUE_TO_UNSUPPORTED_CDN: PreloadJourneyPropertiesV2.Status
    STATUS_NOT_APPLICABLE_DUE_TO_UNSUPPORTED_DOMAIN: PreloadJourneyPropertiesV2.Status
    STATUS_NOT_APPLICABLE_DUE_TO_THIRD_PARTY_AD: PreloadJourneyPropertiesV2.Status
    STATUS_NOT_APPLICABLE_DUE_TO_FALLBACK_AD: PreloadJourneyPropertiesV2.Status
    STATUS_NOT_APPLICABLE_DUE_TO_WRAPPER_RESULUTION_FAILURE: PreloadJourneyPropertiesV2.Status
    STATUS_NOT_APPLICABLE_DUE_TO_VAST_PARSING_FAILURE: PreloadJourneyPropertiesV2.Status
    STATUS_NOT_APPLICABLE_DUE_TO_UNSUPPORTED_VIDEO_FORMATE: PreloadJourneyPropertiesV2.Status
    class FailureReason(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        FAILURE_REASON_UNSPECIFIED: _ClassVar[PreloadJourneyPropertiesV2.FailureReason]
        FAILURE_REASON_API_FAILED: _ClassVar[PreloadJourneyPropertiesV2.FailureReason]
        FAILURE_REASON_NONE: _ClassVar[PreloadJourneyPropertiesV2.FailureReason]
    FAILURE_REASON_UNSPECIFIED: PreloadJourneyPropertiesV2.FailureReason
    FAILURE_REASON_API_FAILED: PreloadJourneyPropertiesV2.FailureReason
    FAILURE_REASON_NONE: PreloadJourneyPropertiesV2.FailureReason
    PRELOAD_JOURNEY_STAGE_FIELD_NUMBER: _ClassVar[int]
    PRELOAD_JOURNEY_API_TYPE_FIELD_NUMBER: _ClassVar[int]
    PRELOAD_JOURNEY_STATUS_FIELD_NUMBER: _ClassVar[int]
    PRELOAD_JOURNEY_FAILURE_REASON_FIELD_NUMBER: _ClassVar[int]
    PRELOAD_JOURNEY_URL_FIELD_NUMBER: _ClassVar[int]
    PRELOAD_JOURNEY_SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    BFF_PRELOAD_FIELD_NUMBER: _ClassVar[int]
    BFF_PRELOAD_APIS_FIELD_NUMBER: _ClassVar[int]
    PLAYER_DATA_PRELOAD_FIELD_NUMBER: _ClassVar[int]
    PLAYER_DATA_PRELOAD_APIS_FIELD_NUMBER: _ClassVar[int]
    BFF_PRELOAD_CONSUMED_FIELD_NUMBER: _ClassVar[int]
    PLAYER_DATA_PRELOAD_CONSUMED_FIELD_NUMBER: _ClassVar[int]
    PRELOAD_PLAYER_DATA_TYPE_FIELD_NUMBER: _ClassVar[int]
    preload_journey_stage: PreloadJourneyPropertiesV2.Stage
    preload_journey_api_type: PreloadJourneyPropertiesV2.ApiType
    preload_journey_status: PreloadJourneyPropertiesV2.Status
    preload_journey_failure_reason: PreloadJourneyPropertiesV2.FailureReason
    preload_journey_url: str
    preload_journey_session_id: str
    bff_preload: PreloadJourneyPropertiesV2.Status
    bff_preload_apis: _containers.RepeatedScalarFieldContainer[_preload_models_pb2.PreloadModels.BffApi]
    player_data_preload: PreloadJourneyPropertiesV2.Status
    player_data_preload_apis: _containers.RepeatedScalarFieldContainer[str]
    bff_preload_consumed: bool
    player_data_preload_consumed: bool
    preload_player_data_type: _preload_models_pb2.PreloadModels.DataType
    def __init__(self, preload_journey_stage: _Optional[_Union[PreloadJourneyPropertiesV2.Stage, str]] = ..., preload_journey_api_type: _Optional[_Union[PreloadJourneyPropertiesV2.ApiType, str]] = ..., preload_journey_status: _Optional[_Union[PreloadJourneyPropertiesV2.Status, str]] = ..., preload_journey_failure_reason: _Optional[_Union[PreloadJourneyPropertiesV2.FailureReason, str]] = ..., preload_journey_url: _Optional[str] = ..., preload_journey_session_id: _Optional[str] = ..., bff_preload: _Optional[_Union[PreloadJourneyPropertiesV2.Status, str]] = ..., bff_preload_apis: _Optional[_Iterable[_Union[_preload_models_pb2.PreloadModels.BffApi, str]]] = ..., player_data_preload: _Optional[_Union[PreloadJourneyPropertiesV2.Status, str]] = ..., player_data_preload_apis: _Optional[_Iterable[str]] = ..., bff_preload_consumed: bool = ..., player_data_preload_consumed: bool = ..., preload_player_data_type: _Optional[_Union[_preload_models_pb2.PreloadModels.DataType, str]] = ...) -> None: ...
