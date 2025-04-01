from google.protobuf import any_pb2 as _any_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class WidgetWrapper(_message.Message):
    __slots__ = ("template", "widget")
    TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    WIDGET_FIELD_NUMBER: _ClassVar[int]
    template: str
    widget: _any_pb2.Any
    def __init__(self, template: _Optional[str] = ..., widget: _Optional[_Union[_any_pb2.Any, _Mapping]] = ...) -> None: ...
