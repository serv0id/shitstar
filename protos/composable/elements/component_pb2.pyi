from composable.base import commons_pb2 as _commons_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Component(_message.Message):
    __slots__ = ("component_commons", "dsl", "style")
    COMPONENT_COMMONS_FIELD_NUMBER: _ClassVar[int]
    DSL_FIELD_NUMBER: _ClassVar[int]
    STYLE_FIELD_NUMBER: _ClassVar[int]
    component_commons: _commons_pb2.ComponentCommons
    dsl: str
    style: bytes
    def __init__(self, component_commons: _Optional[_Union[_commons_pb2.ComponentCommons, _Mapping]] = ..., dsl: _Optional[str] = ..., style: _Optional[bytes] = ...) -> None: ...
