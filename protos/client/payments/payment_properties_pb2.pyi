from client.payments import failure_properties_pb2 as _failure_properties_pb2
from client.payments import payment_type_properties_pb2 as _payment_type_properties_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PaymentProperties(_message.Message):
    __slots__ = ("plan_id", "payment_type", "payment_type_properties", "failure_properties", "payment_instrument_offers", "partner", "offer", "offer_status", "source", "cohorts")
    class PaymentType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        PAYMENT_TYPE_UNSPECIFIED: _ClassVar[PaymentProperties.PaymentType]
        PAYMENT_TYPE_GOOGLE: _ClassVar[PaymentProperties.PaymentType]
        PAYMENT_TYPE_ITUNES: _ClassVar[PaymentProperties.PaymentType]
    PAYMENT_TYPE_UNSPECIFIED: PaymentProperties.PaymentType
    PAYMENT_TYPE_GOOGLE: PaymentProperties.PaymentType
    PAYMENT_TYPE_ITUNES: PaymentProperties.PaymentType
    class OfferStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        OFFER_STATUS_UNSPECIFIED: _ClassVar[PaymentProperties.OfferStatus]
        OFFER_STATUS_APPLIED: _ClassVar[PaymentProperties.OfferStatus]
        OFFER_STATUS_INVALID: _ClassVar[PaymentProperties.OfferStatus]
    OFFER_STATUS_UNSPECIFIED: PaymentProperties.OfferStatus
    OFFER_STATUS_APPLIED: PaymentProperties.OfferStatus
    OFFER_STATUS_INVALID: PaymentProperties.OfferStatus
    class Source(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SOURCE_UNSPECIFIED: _ClassVar[PaymentProperties.Source]
        SOURCE_SKIP_PSP: _ClassVar[PaymentProperties.Source]
    SOURCE_UNSPECIFIED: PaymentProperties.Source
    SOURCE_SKIP_PSP: PaymentProperties.Source
    PLAN_ID_FIELD_NUMBER: _ClassVar[int]
    PAYMENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    PAYMENT_TYPE_PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    FAILURE_PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    PAYMENT_INSTRUMENT_OFFERS_FIELD_NUMBER: _ClassVar[int]
    PARTNER_FIELD_NUMBER: _ClassVar[int]
    OFFER_FIELD_NUMBER: _ClassVar[int]
    OFFER_STATUS_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    COHORTS_FIELD_NUMBER: _ClassVar[int]
    plan_id: str
    payment_type: PaymentProperties.PaymentType
    payment_type_properties: _payment_type_properties_pb2.PaymentTypeProperties
    failure_properties: _failure_properties_pb2.FailureProperties
    payment_instrument_offers: _containers.RepeatedScalarFieldContainer[str]
    partner: str
    offer: str
    offer_status: PaymentProperties.OfferStatus
    source: PaymentProperties.Source
    cohorts: str
    def __init__(self, plan_id: _Optional[str] = ..., payment_type: _Optional[_Union[PaymentProperties.PaymentType, str]] = ..., payment_type_properties: _Optional[_Union[_payment_type_properties_pb2.PaymentTypeProperties, _Mapping]] = ..., failure_properties: _Optional[_Union[_failure_properties_pb2.FailureProperties, _Mapping]] = ..., payment_instrument_offers: _Optional[_Iterable[str]] = ..., partner: _Optional[str] = ..., offer: _Optional[str] = ..., offer_status: _Optional[_Union[PaymentProperties.OfferStatus, str]] = ..., source: _Optional[_Union[PaymentProperties.Source, str]] = ..., cohorts: _Optional[str] = ...) -> None: ...
