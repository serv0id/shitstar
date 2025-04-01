from component.subs import plan_duration_pb2 as _plan_duration_pb2
from component.subs import plan_price_pb2 as _plan_price_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Plan(_message.Message):
    __slots__ = ("plan_id", "plan_family", "plan_duration", "plan_price")
    PLAN_ID_FIELD_NUMBER: _ClassVar[int]
    PLAN_FAMILY_FIELD_NUMBER: _ClassVar[int]
    PLAN_DURATION_FIELD_NUMBER: _ClassVar[int]
    PLAN_PRICE_FIELD_NUMBER: _ClassVar[int]
    plan_id: str
    plan_family: str
    plan_duration: _plan_duration_pb2.PlanDuration
    plan_price: _plan_price_pb2.PlanPrice
    def __init__(self, plan_id: _Optional[str] = ..., plan_family: _Optional[str] = ..., plan_duration: _Optional[_Union[_plan_duration_pb2.PlanDuration, _Mapping]] = ..., plan_price: _Optional[_Union[_plan_price_pb2.PlanPrice, _Mapping]] = ...) -> None: ...
