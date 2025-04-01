from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class SpaceCacheMeta(_message.Message):
    __slots__ = ("user_primary_language", "is_logged_in", "is_free", "cohort_ids", "maturity_level", "ab_group_ids")
    USER_PRIMARY_LANGUAGE_FIELD_NUMBER: _ClassVar[int]
    IS_LOGGED_IN_FIELD_NUMBER: _ClassVar[int]
    IS_FREE_FIELD_NUMBER: _ClassVar[int]
    COHORT_IDS_FIELD_NUMBER: _ClassVar[int]
    MATURITY_LEVEL_FIELD_NUMBER: _ClassVar[int]
    AB_GROUP_IDS_FIELD_NUMBER: _ClassVar[int]
    user_primary_language: str
    is_logged_in: bool
    is_free: bool
    cohort_ids: _containers.RepeatedScalarFieldContainer[str]
    maturity_level: str
    ab_group_ids: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, user_primary_language: _Optional[str] = ..., is_logged_in: bool = ..., is_free: bool = ..., cohort_ids: _Optional[_Iterable[str]] = ..., maturity_level: _Optional[str] = ..., ab_group_ids: _Optional[_Iterable[str]] = ...) -> None: ...
