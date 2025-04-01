from google.protobuf import any_pb2 as _any_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PlayerContentRatingNudgeEventData(_message.Message):
    __slots__ = ("wrapper_action",)
    WRAPPER_ACTION_FIELD_NUMBER: _ClassVar[int]
    wrapper_action: _containers.RepeatedCompositeFieldContainer[_any_pb2.Any]
    def __init__(self, wrapper_action: _Optional[_Iterable[_Union[_any_pb2.Any, _Mapping]]] = ...) -> None: ...
