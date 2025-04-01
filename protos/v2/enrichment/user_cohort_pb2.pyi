from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class UserCohort(_message.Message):
    __slots__ = ("cohort_data", "cohort_data_v2")
    class DataStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNKNOWN_DATA_STATUS: _ClassVar[UserCohort.DataStatus]
        UPDATED: _ClassVar[UserCohort.DataStatus]
        STALE: _ClassVar[UserCohort.DataStatus]
        FAILED: _ClassVar[UserCohort.DataStatus]
        OVERSIZE: _ClassVar[UserCohort.DataStatus]
    UNKNOWN_DATA_STATUS: UserCohort.DataStatus
    UPDATED: UserCohort.DataStatus
    STALE: UserCohort.DataStatus
    FAILED: UserCohort.DataStatus
    OVERSIZE: UserCohort.DataStatus
    class CohortGroup(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNKNOWN_GROUP: _ClassVar[UserCohort.CohortGroup]
        COMMON: _ClassVar[UserCohort.CohortGroup]
        COMMS: _ClassVar[UserCohort.CohortGroup]
        SUBS: _ClassVar[UserCohort.CohortGroup]
        SEGMENTS: _ClassVar[UserCohort.CohortGroup]
    UNKNOWN_GROUP: UserCohort.CohortGroup
    COMMON: UserCohort.CohortGroup
    COMMS: UserCohort.CohortGroup
    SUBS: UserCohort.CohortGroup
    SEGMENTS: UserCohort.CohortGroup
    class CohortIDType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNKNOWN_IDTYPE: _ClassVar[UserCohort.CohortIDType]
        IDTYPE_PID: _ClassVar[UserCohort.CohortIDType]
        IDTYPE_ADID: _ClassVar[UserCohort.CohortIDType]
        IDTYPE_HID: _ClassVar[UserCohort.CohortIDType]
        IDTYPE_DWDID: _ClassVar[UserCohort.CohortIDType]
    UNKNOWN_IDTYPE: UserCohort.CohortIDType
    IDTYPE_PID: UserCohort.CohortIDType
    IDTYPE_ADID: UserCohort.CohortIDType
    IDTYPE_HID: UserCohort.CohortIDType
    IDTYPE_DWDID: UserCohort.CohortIDType
    class CohortDataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: UserCohort.CohortData
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[UserCohort.CohortData, _Mapping]] = ...) -> None: ...
    class CohortDataV2Entry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: UserCohort.CohortDataMap
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[UserCohort.CohortDataMap, _Mapping]] = ...) -> None: ...
    class CohortData(_message.Message):
        __slots__ = ("status", "id_type", "cohort_ids", "cohort_names", "unique_names")
        STATUS_FIELD_NUMBER: _ClassVar[int]
        ID_TYPE_FIELD_NUMBER: _ClassVar[int]
        COHORT_IDS_FIELD_NUMBER: _ClassVar[int]
        COHORT_NAMES_FIELD_NUMBER: _ClassVar[int]
        UNIQUE_NAMES_FIELD_NUMBER: _ClassVar[int]
        status: UserCohort.DataStatus
        id_type: UserCohort.CohortIDType
        cohort_ids: _containers.RepeatedScalarFieldContainer[str]
        cohort_names: _containers.RepeatedScalarFieldContainer[str]
        unique_names: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, status: _Optional[_Union[UserCohort.DataStatus, str]] = ..., id_type: _Optional[_Union[UserCohort.CohortIDType, str]] = ..., cohort_ids: _Optional[_Iterable[str]] = ..., cohort_names: _Optional[_Iterable[str]] = ..., unique_names: _Optional[_Iterable[str]] = ...) -> None: ...
    class CohortDataMap(_message.Message):
        __slots__ = ("cohort_data_map",)
        class CohortDataMapEntry(_message.Message):
            __slots__ = ("key", "value")
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: int
            value: UserCohort.CohortData
            def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[UserCohort.CohortData, _Mapping]] = ...) -> None: ...
        COHORT_DATA_MAP_FIELD_NUMBER: _ClassVar[int]
        cohort_data_map: _containers.MessageMap[int, UserCohort.CohortData]
        def __init__(self, cohort_data_map: _Optional[_Mapping[int, UserCohort.CohortData]] = ...) -> None: ...
    COHORT_DATA_FIELD_NUMBER: _ClassVar[int]
    COHORT_DATA_V2_FIELD_NUMBER: _ClassVar[int]
    cohort_data: _containers.MessageMap[int, UserCohort.CohortData]
    cohort_data_v2: _containers.MessageMap[int, UserCohort.CohortDataMap]
    def __init__(self, cohort_data: _Optional[_Mapping[int, UserCohort.CohortData]] = ..., cohort_data_v2: _Optional[_Mapping[int, UserCohort.CohortDataMap]] = ...) -> None: ...
