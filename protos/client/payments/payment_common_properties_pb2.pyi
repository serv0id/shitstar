from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class PaymentCommonProperties(_message.Message):
    __slots__ = ("placement", "request_id")
    PLACEMENT_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    placement: str
    request_id: str
    def __init__(self, placement: _Optional[str] = ..., request_id: _Optional[str] = ...) -> None: ...
