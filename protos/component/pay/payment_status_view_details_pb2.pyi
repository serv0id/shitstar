from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class PaymentStatusViewDetails(_message.Message):
    __slots__ = ("order_id", "payment_status")
    ORDER_ID_FIELD_NUMBER: _ClassVar[int]
    PAYMENT_STATUS_FIELD_NUMBER: _ClassVar[int]
    order_id: str
    payment_status: str
    def __init__(self, order_id: _Optional[str] = ..., payment_status: _Optional[str] = ...) -> None: ...
