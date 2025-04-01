from client.payments import payment_common_properties_pb2 as _payment_common_properties_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PaymentResponse(_message.Message):
    __slots__ = ("payment_common_properties", "response_time", "order_id")
    PAYMENT_COMMON_PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_TIME_FIELD_NUMBER: _ClassVar[int]
    ORDER_ID_FIELD_NUMBER: _ClassVar[int]
    payment_common_properties: _payment_common_properties_pb2.PaymentCommonProperties
    response_time: int
    order_id: str
    def __init__(self, payment_common_properties: _Optional[_Union[_payment_common_properties_pb2.PaymentCommonProperties, _Mapping]] = ..., response_time: _Optional[int] = ..., order_id: _Optional[str] = ...) -> None: ...
