from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FrequencyCappedStatusAction(_message.Message):
    __slots__ = ("id", "version", "capping_rules")
    ID_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    CAPPING_RULES_FIELD_NUMBER: _ClassVar[int]
    id: str
    version: int
    capping_rules: _containers.RepeatedCompositeFieldContainer[CappingRules]
    def __init__(self, id: _Optional[str] = ..., version: _Optional[int] = ..., capping_rules: _Optional[_Iterable[_Union[CappingRules, _Mapping]]] = ...) -> None: ...

class CappingRules(_message.Message):
    __slots__ = ("every_n_app_launch", "per_n_hour", "per_n_day", "per_n_month", "per_n_year", "per_lifetime", "per_n_minute", "per_n_second", "after_n_app_launch")
    EVERY_N_APP_LAUNCH_FIELD_NUMBER: _ClassVar[int]
    PER_N_HOUR_FIELD_NUMBER: _ClassVar[int]
    PER_N_DAY_FIELD_NUMBER: _ClassVar[int]
    PER_N_MONTH_FIELD_NUMBER: _ClassVar[int]
    PER_N_YEAR_FIELD_NUMBER: _ClassVar[int]
    PER_LIFETIME_FIELD_NUMBER: _ClassVar[int]
    PER_N_MINUTE_FIELD_NUMBER: _ClassVar[int]
    PER_N_SECOND_FIELD_NUMBER: _ClassVar[int]
    AFTER_N_APP_LAUNCH_FIELD_NUMBER: _ClassVar[int]
    every_n_app_launch: Rule
    per_n_hour: Rule
    per_n_day: Rule
    per_n_month: Rule
    per_n_year: Rule
    per_lifetime: Rule
    per_n_minute: Rule
    per_n_second: Rule
    after_n_app_launch: Rule
    def __init__(self, every_n_app_launch: _Optional[_Union[Rule, _Mapping]] = ..., per_n_hour: _Optional[_Union[Rule, _Mapping]] = ..., per_n_day: _Optional[_Union[Rule, _Mapping]] = ..., per_n_month: _Optional[_Union[Rule, _Mapping]] = ..., per_n_year: _Optional[_Union[Rule, _Mapping]] = ..., per_lifetime: _Optional[_Union[Rule, _Mapping]] = ..., per_n_minute: _Optional[_Union[Rule, _Mapping]] = ..., per_n_second: _Optional[_Union[Rule, _Mapping]] = ..., after_n_app_launch: _Optional[_Union[Rule, _Mapping]] = ...) -> None: ...

class Rule(_message.Message):
    __slots__ = ("n", "maxCap", "frequency", "maxCapCount")
    N_FIELD_NUMBER: _ClassVar[int]
    MAXCAP_FIELD_NUMBER: _ClassVar[int]
    FREQUENCY_FIELD_NUMBER: _ClassVar[int]
    MAXCAPCOUNT_FIELD_NUMBER: _ClassVar[int]
    n: int
    maxCap: int
    frequency: int
    maxCapCount: int
    def __init__(self, n: _Optional[int] = ..., maxCap: _Optional[int] = ..., frequency: _Optional[int] = ..., maxCapCount: _Optional[int] = ...) -> None: ...
