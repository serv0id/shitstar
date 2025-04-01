from v2 import widget_pb2 as _widget_pb2
from v2 import error_pb2 as _error_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MoreWidgetsResponse(_message.Message):
    __slots__ = ("success", "error")
    class Success(_message.Message):
        __slots__ = ("widget_wrappers", "more_widgets_url")
        WIDGET_WRAPPERS_FIELD_NUMBER: _ClassVar[int]
        MORE_WIDGETS_URL_FIELD_NUMBER: _ClassVar[int]
        widget_wrappers: _containers.RepeatedCompositeFieldContainer[_widget_pb2.WidgetWrapper]
        more_widgets_url: str
        def __init__(self, widget_wrappers: _Optional[_Iterable[_Union[_widget_pb2.WidgetWrapper, _Mapping]]] = ..., more_widgets_url: _Optional[str] = ...) -> None: ...
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    success: MoreWidgetsResponse.Success
    error: _error_pb2.Error
    def __init__(self, success: _Optional[_Union[MoreWidgetsResponse.Success, _Mapping]] = ..., error: _Optional[_Union[_error_pb2.Error, _Mapping]] = ...) -> None: ...
