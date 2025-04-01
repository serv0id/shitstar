from api.base import context_pb2 as _context_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class BifrostResponse(_message.Message):
    __slots__ = ("status", "error", "data")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    status: bool
    error: Error
    data: Data
    def __init__(self, status: bool = ..., error: _Optional[_Union[Error, _Mapping]] = ..., data: _Optional[_Union[Data, _Mapping]] = ...) -> None: ...

class Error(_message.Message):
    __slots__ = ("err_code", "err_str", "err_debug")
    ERR_CODE_FIELD_NUMBER: _ClassVar[int]
    ERR_STR_FIELD_NUMBER: _ClassVar[int]
    ERR_DEBUG_FIELD_NUMBER: _ClassVar[int]
    err_code: int
    err_str: str
    err_debug: str
    def __init__(self, err_code: _Optional[int] = ..., err_str: _Optional[str] = ..., err_debug: _Optional[str] = ...) -> None: ...

class Data(_message.Message):
    __slots__ = ("common_properties",)
    COMMON_PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    common_properties: _context_pb2.InstrumentationContext
    def __init__(self, common_properties: _Optional[_Union[_context_pb2.InstrumentationContext, _Mapping]] = ...) -> None: ...
