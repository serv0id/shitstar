from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class RefreshWidgetRequest(_message.Message):
    __slots__ = ["widget_wrapper_id", "widget_url"]
    WIDGET_WRAPPER_ID_FIELD_NUMBER: _ClassVar[int]
    WIDGET_URL_FIELD_NUMBER: _ClassVar[int]
    widget_wrapper_id: str
    widget_url: str
    def __init__(self, widget_wrapper_id: _Optional[str] = ..., widget_url: _Optional[str] = ...) -> None: ...

class DeferredWidgetRequest(_message.Message):
    __slots__ = ["widget_wrapper_id", "widget_url"]
    WIDGET_WRAPPER_ID_FIELD_NUMBER: _ClassVar[int]
    WIDGET_URL_FIELD_NUMBER: _ClassVar[int]
    widget_wrapper_id: str
    widget_url: str
    def __init__(self, widget_wrapper_id: _Optional[str] = ..., widget_url: _Optional[str] = ...) -> None: ...
