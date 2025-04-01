from composable.tokens import dls_tokens_pb2 as _dls_tokens_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CornerRadius(_message.Message):
    __slots__ = ("topStart", "topEnd", "bottomStart", "bottomEnd")
    TOPSTART_FIELD_NUMBER: _ClassVar[int]
    TOPEND_FIELD_NUMBER: _ClassVar[int]
    BOTTOMSTART_FIELD_NUMBER: _ClassVar[int]
    BOTTOMEND_FIELD_NUMBER: _ClassVar[int]
    topStart: _dls_tokens_pb2.DLSRadius
    topEnd: _dls_tokens_pb2.DLSRadius
    bottomStart: _dls_tokens_pb2.DLSRadius
    bottomEnd: _dls_tokens_pb2.DLSRadius
    def __init__(self, topStart: _Optional[_Union[_dls_tokens_pb2.DLSRadius, str]] = ..., topEnd: _Optional[_Union[_dls_tokens_pb2.DLSRadius, str]] = ..., bottomStart: _Optional[_Union[_dls_tokens_pb2.DLSRadius, str]] = ..., bottomEnd: _Optional[_Union[_dls_tokens_pb2.DLSRadius, str]] = ...) -> None: ...
