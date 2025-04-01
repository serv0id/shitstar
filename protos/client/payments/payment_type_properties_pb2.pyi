from component.subs import plan_pb2 as _plan_pb2
from options import opts_pb2 as _opts_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PaymentTypeProperties(_message.Message):
    __slots__ = ("plan_properties", "payment_type")
    class PaymentType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        PAYMENT_TYPE_UNSPECIFIED: _ClassVar[PaymentTypeProperties.PaymentType]
        PAYMENT_TYPE_GOOGLE: _ClassVar[PaymentTypeProperties.PaymentType]
        PAYMENT_TYPE_ITUNES: _ClassVar[PaymentTypeProperties.PaymentType]
        PAYMENT_TYPE_WEB: _ClassVar[PaymentTypeProperties.PaymentType]
        PAYMENT_TYPE_D2C: _ClassVar[PaymentTypeProperties.PaymentType]
        PAYMENT_TYPE_NO_MANDATE: _ClassVar[PaymentTypeProperties.PaymentType]
    PAYMENT_TYPE_UNSPECIFIED: PaymentTypeProperties.PaymentType
    PAYMENT_TYPE_GOOGLE: PaymentTypeProperties.PaymentType
    PAYMENT_TYPE_ITUNES: PaymentTypeProperties.PaymentType
    PAYMENT_TYPE_WEB: PaymentTypeProperties.PaymentType
    PAYMENT_TYPE_D2C: PaymentTypeProperties.PaymentType
    PAYMENT_TYPE_NO_MANDATE: PaymentTypeProperties.PaymentType
    PLAN_PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    PAYMENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    plan_properties: _plan_pb2.Plan
    payment_type: PaymentTypeProperties.PaymentType
    def __init__(self, plan_properties: _Optional[_Union[_plan_pb2.Plan, _Mapping]] = ..., payment_type: _Optional[_Union[PaymentTypeProperties.PaymentType, str]] = ...) -> None: ...
