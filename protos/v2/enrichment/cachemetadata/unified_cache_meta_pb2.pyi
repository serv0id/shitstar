from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CohortGroup(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    UNKNOWN_GROUP: _ClassVar[CohortGroup]
    COMMON: _ClassVar[CohortGroup]
    COMMS: _ClassVar[CohortGroup]
    SUBS: _ClassVar[CohortGroup]
    SEGMENTS: _ClassVar[CohortGroup]
UNKNOWN_GROUP: CohortGroup
COMMON: CohortGroup
COMMS: CohortGroup
SUBS: CohortGroup
SEGMENTS: CohortGroup

class UnifiedCacheMetadata(_message.Message):
    __slots__ = ("user_primary_language", "user_default_sports_language", "is_logged_in", "ab_group_ids", "cdn_distribution_key", "is_free", "cohort_ids", "client_capabilities", "maturity_level", "is_profile_kids", "is_upgradable", "cohort_unique_names", "ssai_tag", "max_resolution")
    class CohortIdsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: ListOfCohortIDs
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[ListOfCohortIDs, _Mapping]] = ...) -> None: ...
    class CohortUniqueNamesEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: ListOfCohortUniqueNames
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[ListOfCohortUniqueNames, _Mapping]] = ...) -> None: ...
    USER_PRIMARY_LANGUAGE_FIELD_NUMBER: _ClassVar[int]
    USER_DEFAULT_SPORTS_LANGUAGE_FIELD_NUMBER: _ClassVar[int]
    IS_LOGGED_IN_FIELD_NUMBER: _ClassVar[int]
    AB_GROUP_IDS_FIELD_NUMBER: _ClassVar[int]
    CDN_DISTRIBUTION_KEY_FIELD_NUMBER: _ClassVar[int]
    IS_FREE_FIELD_NUMBER: _ClassVar[int]
    COHORT_IDS_FIELD_NUMBER: _ClassVar[int]
    CLIENT_CAPABILITIES_FIELD_NUMBER: _ClassVar[int]
    MATURITY_LEVEL_FIELD_NUMBER: _ClassVar[int]
    IS_PROFILE_KIDS_FIELD_NUMBER: _ClassVar[int]
    IS_UPGRADABLE_FIELD_NUMBER: _ClassVar[int]
    COHORT_UNIQUE_NAMES_FIELD_NUMBER: _ClassVar[int]
    SSAI_TAG_FIELD_NUMBER: _ClassVar[int]
    MAX_RESOLUTION_FIELD_NUMBER: _ClassVar[int]
    user_primary_language: str
    user_default_sports_language: str
    is_logged_in: bool
    ab_group_ids: _containers.RepeatedScalarFieldContainer[str]
    cdn_distribution_key: int
    is_free: bool
    cohort_ids: _containers.MessageMap[int, ListOfCohortIDs]
    client_capabilities: ClientCapabilities
    maturity_level: str
    is_profile_kids: bool
    is_upgradable: bool
    cohort_unique_names: _containers.MessageMap[int, ListOfCohortUniqueNames]
    ssai_tag: str
    max_resolution: str
    def __init__(self, user_primary_language: _Optional[str] = ..., user_default_sports_language: _Optional[str] = ..., is_logged_in: bool = ..., ab_group_ids: _Optional[_Iterable[str]] = ..., cdn_distribution_key: _Optional[int] = ..., is_free: bool = ..., cohort_ids: _Optional[_Mapping[int, ListOfCohortIDs]] = ..., client_capabilities: _Optional[_Union[ClientCapabilities, _Mapping]] = ..., maturity_level: _Optional[str] = ..., is_profile_kids: bool = ..., is_upgradable: bool = ..., cohort_unique_names: _Optional[_Mapping[int, ListOfCohortUniqueNames]] = ..., ssai_tag: _Optional[str] = ..., max_resolution: _Optional[str] = ...) -> None: ...

class ClientCapabilities(_message.Message):
    __slots__ = ("video_codec", "resolution", "ads", "container", "orientation")
    VIDEO_CODEC_FIELD_NUMBER: _ClassVar[int]
    RESOLUTION_FIELD_NUMBER: _ClassVar[int]
    ADS_FIELD_NUMBER: _ClassVar[int]
    CONTAINER_FIELD_NUMBER: _ClassVar[int]
    ORIENTATION_FIELD_NUMBER: _ClassVar[int]
    video_codec: _containers.RepeatedScalarFieldContainer[str]
    resolution: _containers.RepeatedScalarFieldContainer[str]
    ads: _containers.RepeatedScalarFieldContainer[str]
    container: _containers.RepeatedScalarFieldContainer[str]
    orientation: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, video_codec: _Optional[_Iterable[str]] = ..., resolution: _Optional[_Iterable[str]] = ..., ads: _Optional[_Iterable[str]] = ..., container: _Optional[_Iterable[str]] = ..., orientation: _Optional[_Iterable[str]] = ...) -> None: ...

class ListOfCohortIDs(_message.Message):
    __slots__ = ("cohortIDs",)
    COHORTIDS_FIELD_NUMBER: _ClassVar[int]
    cohortIDs: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, cohortIDs: _Optional[_Iterable[str]] = ...) -> None: ...

class ListOfCohortUniqueNames(_message.Message):
    __slots__ = ("cohortUniqueNames",)
    COHORTUNIQUENAMES_FIELD_NUMBER: _ClassVar[int]
    cohortUniqueNames: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, cohortUniqueNames: _Optional[_Iterable[str]] = ...) -> None: ...
