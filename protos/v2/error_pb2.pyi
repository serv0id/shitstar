from google.protobuf import any_pb2 as _any_pb2
from protos.v2 import widget_pb2 as _widget_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Error(_message.Message):
    __slots__ = ["error_code", "error_message", "data", "widget_wrapper"]
    ERROR_CODE_FIELD_NUMBER: _ClassVar[int]
    ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    WIDGET_WRAPPER_FIELD_NUMBER: _ClassVar[int]
    error_code: str
    error_message: str
    data: _any_pb2.Any
    widget_wrapper: _widget_pb2.WidgetWrapper
    def __init__(self, error_code: _Optional[str] = ..., error_message: _Optional[str] = ..., data: _Optional[_Union[_any_pb2.Any, _Mapping]] = ..., widget_wrapper: _Optional[_Union[_widget_pb2.WidgetWrapper, _Mapping]] = ...) -> None: ...
