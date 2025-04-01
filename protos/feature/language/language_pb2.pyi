from base import actions_pb2 as _actions_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class Language(_message.Message):
    __slots__ = ("id", "name", "display_name", "iso2code", "iso3code")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    ISO2CODE_FIELD_NUMBER: _ClassVar[int]
    ISO3CODE_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    display_name: str
    iso2code: str
    iso3code: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., display_name: _Optional[str] = ..., iso2code: _Optional[str] = ..., iso3code: _Optional[str] = ...) -> None: ...
