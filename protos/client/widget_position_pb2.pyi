from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class WidgetPosition(_message.Message):
    __slots__ = ("widget_position", "tile_position")
    WIDGET_POSITION_FIELD_NUMBER: _ClassVar[int]
    TILE_POSITION_FIELD_NUMBER: _ClassVar[int]
    widget_position: int
    tile_position: int
    def __init__(self, widget_position: _Optional[int] = ..., tile_position: _Optional[int] = ...) -> None: ...
