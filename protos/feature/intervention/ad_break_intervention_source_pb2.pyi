from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class AdBreakInterventionSource(_message.Message):
    __slots__ = ("cue_points", "url")
    CUE_POINTS_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    cue_points: _containers.RepeatedScalarFieldContainer[int]
    url: str
    def __init__(self, cue_points: _Optional[_Iterable[int]] = ..., url: _Optional[str] = ...) -> None: ...
