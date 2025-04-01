from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PaymentMethodDetails(_message.Message):
    __slots__ = ("event_name", "event_type", "pack_id", "payment_method", "payment_provider", "payment_processor", "other_params")
    class EventType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        EVENT_TYPE_UNSPECIFIED: _ClassVar[PaymentMethodDetails.EventType]
        EVENT_TYPE_CLICKED: _ClassVar[PaymentMethodDetails.EventType]
        EVENT_TYPE_VIEWED: _ClassVar[PaymentMethodDetails.EventType]
    EVENT_TYPE_UNSPECIFIED: PaymentMethodDetails.EventType
    EVENT_TYPE_CLICKED: PaymentMethodDetails.EventType
    EVENT_TYPE_VIEWED: PaymentMethodDetails.EventType
    class OtherParams(_message.Message):
        __slots__ = ("upi_params",)
        UPI_PARAMS_FIELD_NUMBER: _ClassVar[int]
        upi_params: PaymentMethodDetails.UPIParams
        def __init__(self, upi_params: _Optional[_Union[PaymentMethodDetails.UPIParams, _Mapping]] = ...) -> None: ...
    class UPIParams(_message.Message):
        __slots__ = ("upi_application_name",)
        UPI_APPLICATION_NAME_FIELD_NUMBER: _ClassVar[int]
        upi_application_name: str
        def __init__(self, upi_application_name: _Optional[str] = ...) -> None: ...
    EVENT_NAME_FIELD_NUMBER: _ClassVar[int]
    EVENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    PACK_ID_FIELD_NUMBER: _ClassVar[int]
    PAYMENT_METHOD_FIELD_NUMBER: _ClassVar[int]
    PAYMENT_PROVIDER_FIELD_NUMBER: _ClassVar[int]
    PAYMENT_PROCESSOR_FIELD_NUMBER: _ClassVar[int]
    OTHER_PARAMS_FIELD_NUMBER: _ClassVar[int]
    event_name: str
    event_type: PaymentMethodDetails.EventType
    pack_id: str
    payment_method: str
    payment_provider: str
    payment_processor: str
    other_params: PaymentMethodDetails.OtherParams
    def __init__(self, event_name: _Optional[str] = ..., event_type: _Optional[_Union[PaymentMethodDetails.EventType, str]] = ..., pack_id: _Optional[str] = ..., payment_method: _Optional[str] = ..., payment_provider: _Optional[str] = ..., payment_processor: _Optional[str] = ..., other_params: _Optional[_Union[PaymentMethodDetails.OtherParams, _Mapping]] = ...) -> None: ...
