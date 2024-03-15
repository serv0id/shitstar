from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class PaymentStatusTrackMeta(_message.Message):
    __slots__ = ["transaction_id", "pack_id", "order_id"]
    TRANSACTION_ID_FIELD_NUMBER: _ClassVar[int]
    PACK_ID_FIELD_NUMBER: _ClassVar[int]
    ORDER_ID_FIELD_NUMBER: _ClassVar[int]
    transaction_id: str
    pack_id: str
    order_id: str
    def __init__(self, transaction_id: _Optional[str] = ..., pack_id: _Optional[str] = ..., order_id: _Optional[str] = ...) -> None: ...
