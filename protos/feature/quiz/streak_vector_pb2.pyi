from feature.image import illustration_pb2 as _illustration_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class StreakVector(_message.Message):
    __slots__ = ("title", "streaks")
    TITLE_FIELD_NUMBER: _ClassVar[int]
    STREAKS_FIELD_NUMBER: _ClassVar[int]
    title: str
    streaks: _containers.RepeatedCompositeFieldContainer[_illustration_pb2.Illustration]
    def __init__(self, title: _Optional[str] = ..., streaks: _Optional[_Iterable[_Union[_illustration_pb2.Illustration, _Mapping]]] = ...) -> None: ...
