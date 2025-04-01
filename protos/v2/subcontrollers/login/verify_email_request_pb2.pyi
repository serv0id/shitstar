from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class VerifyEmailRequest(_message.Message):
    __slots__ = ("email_address", "verification_code")
    EMAIL_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    VERIFICATION_CODE_FIELD_NUMBER: _ClassVar[int]
    email_address: str
    verification_code: str
    def __init__(self, email_address: _Optional[str] = ..., verification_code: _Optional[str] = ...) -> None: ...
