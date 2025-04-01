from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ProfileDetails(_message.Message):
    __slots__ = ("highest_maturity_rating", "display_image", "display_image_position", "is_default", "is_kid_toggle_enabled", "is_parental_lock_enabled")
    HIGHEST_MATURITY_RATING_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_IMAGE_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_IMAGE_POSITION_FIELD_NUMBER: _ClassVar[int]
    IS_DEFAULT_FIELD_NUMBER: _ClassVar[int]
    IS_KID_TOGGLE_ENABLED_FIELD_NUMBER: _ClassVar[int]
    IS_PARENTAL_LOCK_ENABLED_FIELD_NUMBER: _ClassVar[int]
    highest_maturity_rating: str
    display_image: str
    display_image_position: int
    is_default: bool
    is_kid_toggle_enabled: bool
    is_parental_lock_enabled: bool
    def __init__(self, highest_maturity_rating: _Optional[str] = ..., display_image: _Optional[str] = ..., display_image_position: _Optional[int] = ..., is_default: bool = ..., is_kid_toggle_enabled: bool = ..., is_parental_lock_enabled: bool = ...) -> None: ...
