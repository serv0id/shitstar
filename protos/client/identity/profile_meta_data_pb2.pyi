from component.identity import enum_pb2 as _enum_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ProfileMetaData(_message.Message):
    __slots__ = ("display_image_position", "is_kid_toggle_enabled", "is_parental_lock_enabled")
    DISPLAY_IMAGE_POSITION_FIELD_NUMBER: _ClassVar[int]
    IS_KID_TOGGLE_ENABLED_FIELD_NUMBER: _ClassVar[int]
    IS_PARENTAL_LOCK_ENABLED_FIELD_NUMBER: _ClassVar[int]
    display_image_position: int
    is_kid_toggle_enabled: bool
    is_parental_lock_enabled: bool
    def __init__(self, display_image_position: _Optional[int] = ..., is_kid_toggle_enabled: bool = ..., is_parental_lock_enabled: bool = ...) -> None: ...
