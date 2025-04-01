from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class PaymentMethodsViewDetails(_message.Message):
    __slots__ = ("selected_plan", "offer_applied", "payment_methods", "payment_methods_offers")
    SELECTED_PLAN_FIELD_NUMBER: _ClassVar[int]
    OFFER_APPLIED_FIELD_NUMBER: _ClassVar[int]
    PAYMENT_METHODS_FIELD_NUMBER: _ClassVar[int]
    PAYMENT_METHODS_OFFERS_FIELD_NUMBER: _ClassVar[int]
    selected_plan: str
    offer_applied: str
    payment_methods: _containers.RepeatedScalarFieldContainer[str]
    payment_methods_offers: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, selected_plan: _Optional[str] = ..., offer_applied: _Optional[str] = ..., payment_methods: _Optional[_Iterable[str]] = ..., payment_methods_offers: _Optional[_Iterable[str]] = ...) -> None: ...
