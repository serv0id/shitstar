from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class PaywallPageCacheMeta(_message.Message):
    __slots__ = ("is_logged_in", "is_free", "ab_group_ids", "cohort_unique_names")
    IS_LOGGED_IN_FIELD_NUMBER: _ClassVar[int]
    IS_FREE_FIELD_NUMBER: _ClassVar[int]
    AB_GROUP_IDS_FIELD_NUMBER: _ClassVar[int]
    COHORT_UNIQUE_NAMES_FIELD_NUMBER: _ClassVar[int]
    is_logged_in: bool
    is_free: bool
    ab_group_ids: _containers.RepeatedScalarFieldContainer[str]
    cohort_unique_names: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, is_logged_in: bool = ..., is_free: bool = ..., ab_group_ids: _Optional[_Iterable[str]] = ..., cohort_unique_names: _Optional[_Iterable[str]] = ...) -> None: ...
