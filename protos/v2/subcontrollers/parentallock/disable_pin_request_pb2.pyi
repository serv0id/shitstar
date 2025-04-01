from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class DisablePinRequest(_message.Message):
    __slots__ = ("otp", "purpose")
    OTP_FIELD_NUMBER: _ClassVar[int]
    PURPOSE_FIELD_NUMBER: _ClassVar[int]
    otp: str
    purpose: str
    def __init__(self, otp: _Optional[str] = ..., purpose: _Optional[str] = ...) -> None: ...
