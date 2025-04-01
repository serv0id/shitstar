from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class GestureOnboardingProperties(_message.Message):
    __slots__ = ("available_gestures_count", "available_gestures")
    AVAILABLE_GESTURES_COUNT_FIELD_NUMBER: _ClassVar[int]
    AVAILABLE_GESTURES_FIELD_NUMBER: _ClassVar[int]
    available_gestures_count: int
    available_gestures: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, available_gestures_count: _Optional[int] = ..., available_gestures: _Optional[_Iterable[str]] = ...) -> None: ...
