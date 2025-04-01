from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class SubtitleAsset(_message.Message):
    __slots__ = ("language_name", "iso3code", "url")
    LANGUAGE_NAME_FIELD_NUMBER: _ClassVar[int]
    ISO3CODE_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    language_name: str
    iso3code: str
    url: str
    def __init__(self, language_name: _Optional[str] = ..., iso3code: _Optional[str] = ..., url: _Optional[str] = ...) -> None: ...
