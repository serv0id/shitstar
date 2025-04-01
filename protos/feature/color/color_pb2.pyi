from composable.tokens import dls_tokens_pb2 as _dls_tokens_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Color(_message.Message):
    __slots__ = ("hex_code", "dls_color")
    HEX_CODE_FIELD_NUMBER: _ClassVar[int]
    DLS_COLOR_FIELD_NUMBER: _ClassVar[int]
    hex_code: str
    dls_color: _dls_tokens_pb2.DLSColors
    def __init__(self, hex_code: _Optional[str] = ..., dls_color: _Optional[_Union[_dls_tokens_pb2.DLSColors, str]] = ...) -> None: ...
