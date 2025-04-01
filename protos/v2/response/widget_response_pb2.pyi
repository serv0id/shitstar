from v2 import widget_pb2 as _widget_pb2
from v2 import error_pb2 as _error_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class WidgetResponse(_message.Message):
    __slots__ = ("success", "error")
    class Success(_message.Message):
        __slots__ = ("widget_wrapper",)
        WIDGET_WRAPPER_FIELD_NUMBER: _ClassVar[int]
        widget_wrapper: _widget_pb2.WidgetWrapper
        def __init__(self, widget_wrapper: _Optional[_Union[_widget_pb2.WidgetWrapper, _Mapping]] = ...) -> None: ...
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    success: WidgetResponse.Success
    error: _error_pb2.Error
    def __init__(self, success: _Optional[_Union[WidgetResponse.Success, _Mapping]] = ..., error: _Optional[_Union[_error_pb2.Error, _Mapping]] = ...) -> None: ...
