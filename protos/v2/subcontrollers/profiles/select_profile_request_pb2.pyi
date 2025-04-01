from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class SelectProfileRequest(_message.Message):
    __slots__ = ("profile_id", "parental_lock_pin")
    PROFILE_ID_FIELD_NUMBER: _ClassVar[int]
    PARENTAL_LOCK_PIN_FIELD_NUMBER: _ClassVar[int]
    profile_id: str
    parental_lock_pin: str
    def __init__(self, profile_id: _Optional[str] = ..., parental_lock_pin: _Optional[str] = ...) -> None: ...
