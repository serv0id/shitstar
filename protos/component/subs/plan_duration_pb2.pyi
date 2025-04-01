from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PlanDuration(_message.Message):
    __slots__ = ("plan_frequency", "plan_duration_type")
    class DurationType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        DURATION_TYPE_UNSPECIFIED: _ClassVar[PlanDuration.DurationType]
        DURATION_TYPE_DAY: _ClassVar[PlanDuration.DurationType]
        DURATION_TYPE_WEEK: _ClassVar[PlanDuration.DurationType]
        DURATION_TYPE_MONTH: _ClassVar[PlanDuration.DurationType]
        DURATION_TYPE_YEAR: _ClassVar[PlanDuration.DurationType]
    DURATION_TYPE_UNSPECIFIED: PlanDuration.DurationType
    DURATION_TYPE_DAY: PlanDuration.DurationType
    DURATION_TYPE_WEEK: PlanDuration.DurationType
    DURATION_TYPE_MONTH: PlanDuration.DurationType
    DURATION_TYPE_YEAR: PlanDuration.DurationType
    PLAN_FREQUENCY_FIELD_NUMBER: _ClassVar[int]
    PLAN_DURATION_TYPE_FIELD_NUMBER: _ClassVar[int]
    plan_frequency: int
    plan_duration_type: PlanDuration.DurationType
    def __init__(self, plan_frequency: _Optional[int] = ..., plan_duration_type: _Optional[_Union[PlanDuration.DurationType, str]] = ...) -> None: ...
