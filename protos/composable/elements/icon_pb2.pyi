from feature.color import color_pb2 as _color_pb2
from composable.tokens import dls_tokens_pb2 as _dls_tokens_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Icon(_message.Message):
    __slots__ = ("name", "color", "fixed", "dls_size")
    NAME_FIELD_NUMBER: _ClassVar[int]
    COLOR_FIELD_NUMBER: _ClassVar[int]
    FIXED_FIELD_NUMBER: _ClassVar[int]
    DLS_SIZE_FIELD_NUMBER: _ClassVar[int]
    name: str
    color: _color_pb2.Color
    fixed: int
    dls_size: _dls_tokens_pb2.DLSSize
    def __init__(self, name: _Optional[str] = ..., color: _Optional[_Union[_color_pb2.Color, _Mapping]] = ..., fixed: _Optional[int] = ..., dls_size: _Optional[_Union[_dls_tokens_pb2.DLSSize, str]] = ...) -> None: ...
