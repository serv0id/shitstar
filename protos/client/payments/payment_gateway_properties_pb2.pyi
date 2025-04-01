from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class PaymentGatewayProperties(_message.Message):
    __slots__ = ("payment_type", "payment_gateway", "payment_processor")
    PAYMENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    PAYMENT_GATEWAY_FIELD_NUMBER: _ClassVar[int]
    PAYMENT_PROCESSOR_FIELD_NUMBER: _ClassVar[int]
    payment_type: str
    payment_gateway: str
    payment_processor: str
    def __init__(self, payment_type: _Optional[str] = ..., payment_gateway: _Optional[str] = ..., payment_processor: _Optional[str] = ...) -> None: ...
