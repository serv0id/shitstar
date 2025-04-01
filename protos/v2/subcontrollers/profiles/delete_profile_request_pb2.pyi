from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class DeleteProfileRequest(_message.Message):
    __slots__ = ("deleting_profile_id",)
    DELETING_PROFILE_ID_FIELD_NUMBER: _ClassVar[int]
    deleting_profile_id: str
    def __init__(self, deleting_profile_id: _Optional[str] = ...) -> None: ...
