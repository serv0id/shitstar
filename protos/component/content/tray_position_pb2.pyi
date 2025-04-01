from component.content import tray_pb2 as _tray_pb2
from component.content import widget_pb2 as _widget_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TrayPosition(_message.Message):
    __slots__ = ("tray", "position", "widget")
    TRAY_FIELD_NUMBER: _ClassVar[int]
    POSITION_FIELD_NUMBER: _ClassVar[int]
    WIDGET_FIELD_NUMBER: _ClassVar[int]
    tray: _tray_pb2.Tray
    position: int
    widget: _widget_pb2.Widget
    def __init__(self, tray: _Optional[_Union[_tray_pb2.Tray, _Mapping]] = ..., position: _Optional[int] = ..., widget: _Optional[_Union[_widget_pb2.Widget, _Mapping]] = ...) -> None: ...
