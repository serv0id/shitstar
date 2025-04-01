from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ResetParentalLockRequest(_message.Message):
    __slots__ = ("pin", "otp", "purpose")
    PIN_FIELD_NUMBER: _ClassVar[int]
    OTP_FIELD_NUMBER: _ClassVar[int]
    PURPOSE_FIELD_NUMBER: _ClassVar[int]
    pin: str
    otp: str
    purpose: str
    def __init__(self, pin: _Optional[str] = ..., otp: _Optional[str] = ..., purpose: _Optional[str] = ...) -> None: ...
