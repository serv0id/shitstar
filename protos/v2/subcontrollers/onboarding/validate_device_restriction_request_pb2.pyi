from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ValidateDeviceRestrictionRequest(_message.Message):
    __slots__ = ("session_ids",)
    SESSION_IDS_FIELD_NUMBER: _ClassVar[int]
    session_ids: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, session_ids: _Optional[_Iterable[str]] = ...) -> None: ...
