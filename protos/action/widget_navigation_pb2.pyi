from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class WidgetNavigationAction(_message.Message):
    __slots__ = ["widget_id"]
    WIDGET_ID_FIELD_NUMBER: _ClassVar[int]
    widget_id: str
    def __init__(self, widget_id: _Optional[str] = ...) -> None: ...
