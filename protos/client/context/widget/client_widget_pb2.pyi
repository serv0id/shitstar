from options import opts_pb2 as _opts_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ClientWidget(_message.Message):
    __slots__ = ("name", "type", "source", "logic", "display_language", "position", "discovery_id")
    NAME_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    LOGIC_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_LANGUAGE_FIELD_NUMBER: _ClassVar[int]
    POSITION_FIELD_NUMBER: _ClassVar[int]
    DISCOVERY_ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    type: str
    source: str
    logic: str
    display_language: str
    position: int
    discovery_id: str
    def __init__(self, name: _Optional[str] = ..., type: _Optional[str] = ..., source: _Optional[str] = ..., logic: _Optional[str] = ..., display_language: _Optional[str] = ..., position: _Optional[int] = ..., discovery_id: _Optional[str] = ...) -> None: ...
