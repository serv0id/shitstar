from client.ads import type_pb2 as _type_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AdSlot(_message.Message):
    __slots__ = ("type", "slot", "id")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    SLOT_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    type: _type_pb2.AdType
    slot: int
    id: str
    def __init__(self, type: _Optional[_Union[_type_pb2.AdType, str]] = ..., slot: _Optional[int] = ..., id: _Optional[str] = ...) -> None: ...
