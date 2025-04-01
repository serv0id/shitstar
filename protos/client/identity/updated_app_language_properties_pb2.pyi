from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class UpdatedAppLanguageProperties(_message.Message):
    __slots__ = ("old_language", "new_language")
    OLD_LANGUAGE_FIELD_NUMBER: _ClassVar[int]
    NEW_LANGUAGE_FIELD_NUMBER: _ClassVar[int]
    old_language: str
    new_language: str
    def __init__(self, old_language: _Optional[str] = ..., new_language: _Optional[str] = ...) -> None: ...
