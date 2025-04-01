from client.payments import payment_common_properties_pb2 as _payment_common_properties_pb2
from client.payments import payment_gateway_properties_pb2 as _payment_gateway_properties_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PaymentError(_message.Message):
    __slots__ = ("payment_common_properties", "payment_gateway_properties", "error_code", "error_message", "error_type", "order_id")
    PAYMENT_COMMON_PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    PAYMENT_GATEWAY_PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    ERROR_CODE_FIELD_NUMBER: _ClassVar[int]
    ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    ERROR_TYPE_FIELD_NUMBER: _ClassVar[int]
    ORDER_ID_FIELD_NUMBER: _ClassVar[int]
    payment_common_properties: _payment_common_properties_pb2.PaymentCommonProperties
    payment_gateway_properties: _payment_gateway_properties_pb2.PaymentGatewayProperties
    error_code: str
    error_message: str
    error_type: str
    order_id: str
    def __init__(self, payment_common_properties: _Optional[_Union[_payment_common_properties_pb2.PaymentCommonProperties, _Mapping]] = ..., payment_gateway_properties: _Optional[_Union[_payment_gateway_properties_pb2.PaymentGatewayProperties, _Mapping]] = ..., error_code: _Optional[str] = ..., error_message: _Optional[str] = ..., error_type: _Optional[str] = ..., order_id: _Optional[str] = ...) -> None: ...
