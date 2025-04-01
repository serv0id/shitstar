from composable.tokens import dls_tokens_pb2 as _dls_tokens_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Edges(_message.Message):
    __slots__ = ("start", "end", "top", "bottom")
    START_FIELD_NUMBER: _ClassVar[int]
    END_FIELD_NUMBER: _ClassVar[int]
    TOP_FIELD_NUMBER: _ClassVar[int]
    BOTTOM_FIELD_NUMBER: _ClassVar[int]
    start: _dls_tokens_pb2.DLSSpacings
    end: _dls_tokens_pb2.DLSSpacings
    top: _dls_tokens_pb2.DLSSpacings
    bottom: _dls_tokens_pb2.DLSSpacings
    def __init__(self, start: _Optional[_Union[_dls_tokens_pb2.DLSSpacings, str]] = ..., end: _Optional[_Union[_dls_tokens_pb2.DLSSpacings, str]] = ..., top: _Optional[_Union[_dls_tokens_pb2.DLSSpacings, str]] = ..., bottom: _Optional[_Union[_dls_tokens_pb2.DLSSpacings, str]] = ...) -> None: ...
