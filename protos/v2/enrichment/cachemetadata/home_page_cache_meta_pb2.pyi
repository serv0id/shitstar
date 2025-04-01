from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class HomePageCacheMeta(_message.Message):
    __slots__ = ("user_primary_language", "ab_group_ids", "is_free", "cohort_ids", "maturity_level", "is_profile_kids", "is_upgradable")
    USER_PRIMARY_LANGUAGE_FIELD_NUMBER: _ClassVar[int]
    AB_GROUP_IDS_FIELD_NUMBER: _ClassVar[int]
    IS_FREE_FIELD_NUMBER: _ClassVar[int]
    COHORT_IDS_FIELD_NUMBER: _ClassVar[int]
    MATURITY_LEVEL_FIELD_NUMBER: _ClassVar[int]
    IS_PROFILE_KIDS_FIELD_NUMBER: _ClassVar[int]
    IS_UPGRADABLE_FIELD_NUMBER: _ClassVar[int]
    user_primary_language: str
    ab_group_ids: _containers.RepeatedScalarFieldContainer[str]
    is_free: bool
    cohort_ids: _containers.RepeatedScalarFieldContainer[str]
    maturity_level: str
    is_profile_kids: bool
    is_upgradable: bool
    def __init__(self, user_primary_language: _Optional[str] = ..., ab_group_ids: _Optional[_Iterable[str]] = ..., is_free: bool = ..., cohort_ids: _Optional[_Iterable[str]] = ..., maturity_level: _Optional[str] = ..., is_profile_kids: bool = ..., is_upgradable: bool = ...) -> None: ...
