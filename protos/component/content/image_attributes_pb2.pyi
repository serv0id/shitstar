from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ImageAttributes(_message.Message):
    __slots__ = ("script_language", "callout_languages", "image_variant", "artwork_logic", "theme")
    SCRIPT_LANGUAGE_FIELD_NUMBER: _ClassVar[int]
    CALLOUT_LANGUAGES_FIELD_NUMBER: _ClassVar[int]
    IMAGE_VARIANT_FIELD_NUMBER: _ClassVar[int]
    ARTWORK_LOGIC_FIELD_NUMBER: _ClassVar[int]
    THEME_FIELD_NUMBER: _ClassVar[int]
    script_language: str
    callout_languages: str
    image_variant: str
    artwork_logic: str
    theme: str
    def __init__(self, script_language: _Optional[str] = ..., callout_languages: _Optional[str] = ..., image_variant: _Optional[str] = ..., artwork_logic: _Optional[str] = ..., theme: _Optional[str] = ...) -> None: ...
