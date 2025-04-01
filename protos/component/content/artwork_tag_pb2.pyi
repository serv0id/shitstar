from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ArtworkTag(_message.Message):
    __slots__ = ("script_language", "variant", "artwork_lang_logic", "theme")
    SCRIPT_LANGUAGE_FIELD_NUMBER: _ClassVar[int]
    VARIANT_FIELD_NUMBER: _ClassVar[int]
    ARTWORK_LANG_LOGIC_FIELD_NUMBER: _ClassVar[int]
    THEME_FIELD_NUMBER: _ClassVar[int]
    script_language: str
    variant: str
    artwork_lang_logic: str
    theme: str
    def __init__(self, script_language: _Optional[str] = ..., variant: _Optional[str] = ..., artwork_lang_logic: _Optional[str] = ..., theme: _Optional[str] = ...) -> None: ...
