from base import actions_pb2 as _actions_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ActionHandlerIntervention(_message.Message):
    __slots__ = ("actions",)
    ACTIONS_FIELD_NUMBER: _ClassVar[int]
    actions: _containers.RepeatedCompositeFieldContainer[_actions_pb2.Actions.Action]
    def __init__(self, actions: _Optional[_Iterable[_Union[_actions_pb2.Actions.Action, _Mapping]]] = ...) -> None: ...
