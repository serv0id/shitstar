from base import actions_pb2 as _actions_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Link(_message.Message):
    __slots__ = ("data",)
    class Data(_message.Message):
        __slots__ = ("actions", "text")
        ACTIONS_FIELD_NUMBER: _ClassVar[int]
        TEXT_FIELD_NUMBER: _ClassVar[int]
        actions: _actions_pb2.Actions
        text: str
        def __init__(self, actions: _Optional[_Union[_actions_pb2.Actions, _Mapping]] = ..., text: _Optional[str] = ...) -> None: ...
    DATA_FIELD_NUMBER: _ClassVar[int]
    data: Link.Data
    def __init__(self, data: _Optional[_Union[Link.Data, _Mapping]] = ...) -> None: ...
