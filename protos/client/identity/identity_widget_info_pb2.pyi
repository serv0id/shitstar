from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class IdentityWidgetInfo(_message.Message):
    __slots__ = ("page", "widget_name", "display_text")
    PAGE_FIELD_NUMBER: _ClassVar[int]
    WIDGET_NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_TEXT_FIELD_NUMBER: _ClassVar[int]
    page: str
    widget_name: str
    display_text: str
    def __init__(self, page: _Optional[str] = ..., widget_name: _Optional[str] = ..., display_text: _Optional[str] = ...) -> None: ...
