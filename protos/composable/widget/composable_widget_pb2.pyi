from base import widget_commons_pb2 as _widget_commons_pb2
from google.protobuf import any_pb2 as _any_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ComposableWidget(_message.Message):
    __slots__ = ("widget_commons", "data")
    WIDGET_COMMONS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    widget_commons: _widget_commons_pb2.WidgetCommons
    data: _any_pb2.Any
    def __init__(self, widget_commons: _Optional[_Union[_widget_commons_pb2.WidgetCommons, _Mapping]] = ..., data: _Optional[_Union[_any_pb2.Any, _Mapping]] = ...) -> None: ...
