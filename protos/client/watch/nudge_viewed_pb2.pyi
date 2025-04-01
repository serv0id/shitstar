from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class NudgeType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    NUDGE_TYPE_UNSPECIFIED: _ClassVar[NudgeType]
    NUDGE_TYPE_NETWORK_PROBLEM: _ClassVar[NudgeType]
NUDGE_TYPE_UNSPECIFIED: NudgeType
NUDGE_TYPE_NETWORK_PROBLEM: NudgeType

class NudgeViewed(_message.Message):
    __slots__ = ("nudge_type", "meta")
    class Meta(_message.Message):
        __slots__ = ("network_problem",)
        NETWORK_PROBLEM_FIELD_NUMBER: _ClassVar[int]
        network_problem: NetworkProblem
        def __init__(self, network_problem: _Optional[_Union[NetworkProblem, _Mapping]] = ...) -> None: ...
    NUDGE_TYPE_FIELD_NUMBER: _ClassVar[int]
    META_FIELD_NUMBER: _ClassVar[int]
    nudge_type: NudgeType
    meta: NudgeViewed.Meta
    def __init__(self, nudge_type: _Optional[_Union[NudgeType, str]] = ..., meta: _Optional[_Union[NudgeViewed.Meta, _Mapping]] = ...) -> None: ...

class NetworkProblem(_message.Message):
    __slots__ = ("bitrate_kbps", "indicated_bitrate_kbps")
    BITRATE_KBPS_FIELD_NUMBER: _ClassVar[int]
    INDICATED_BITRATE_KBPS_FIELD_NUMBER: _ClassVar[int]
    bitrate_kbps: float
    indicated_bitrate_kbps: float
    def __init__(self, bitrate_kbps: _Optional[float] = ..., indicated_bitrate_kbps: _Optional[float] = ...) -> None: ...
