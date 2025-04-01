from composable.tokens import dls_tokens_pb2 as _dls_tokens_pb2
from feature.color import color_pb2 as _color_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Border(_message.Message):
    __slots__ = ("width", "color")
    WIDTH_FIELD_NUMBER: _ClassVar[int]
    COLOR_FIELD_NUMBER: _ClassVar[int]
    width: _dls_tokens_pb2.DLSBorderWidth
    color: _color_pb2.Color
    def __init__(self, width: _Optional[_Union[_dls_tokens_pb2.DLSBorderWidth, str]] = ..., color: _Optional[_Union[_color_pb2.Color, _Mapping]] = ...) -> None: ...
