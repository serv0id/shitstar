from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class EditProfileRequest(_message.Message):
    __slots__ = ("profile_id", "new_name", "new_avatar_id")
    PROFILE_ID_FIELD_NUMBER: _ClassVar[int]
    NEW_NAME_FIELD_NUMBER: _ClassVar[int]
    NEW_AVATAR_ID_FIELD_NUMBER: _ClassVar[int]
    profile_id: str
    new_name: str
    new_avatar_id: str
    def __init__(self, profile_id: _Optional[str] = ..., new_name: _Optional[str] = ..., new_avatar_id: _Optional[str] = ...) -> None: ...
