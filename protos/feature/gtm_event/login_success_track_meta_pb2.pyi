from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class LoginSuccessTrackMeta(_message.Message):
    __slots__ = ("mobile_number", "email")
    MOBILE_NUMBER_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    mobile_number: str
    email: str
    def __init__(self, mobile_number: _Optional[str] = ..., email: _Optional[str] = ...) -> None: ...
