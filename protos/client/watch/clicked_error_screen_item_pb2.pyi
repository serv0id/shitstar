from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ClickedErrorScreenItem(_message.Message):
    __slots__ = ("clicked_cta", "error_code", "widget_type", "widget_name", "widget_source", "widget_logic", "widget_template")
    CLICKED_CTA_FIELD_NUMBER: _ClassVar[int]
    ERROR_CODE_FIELD_NUMBER: _ClassVar[int]
    WIDGET_TYPE_FIELD_NUMBER: _ClassVar[int]
    WIDGET_NAME_FIELD_NUMBER: _ClassVar[int]
    WIDGET_SOURCE_FIELD_NUMBER: _ClassVar[int]
    WIDGET_LOGIC_FIELD_NUMBER: _ClassVar[int]
    WIDGET_TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    clicked_cta: str
    error_code: str
    widget_type: str
    widget_name: str
    widget_source: str
    widget_logic: str
    widget_template: str
    def __init__(self, clicked_cta: _Optional[str] = ..., error_code: _Optional[str] = ..., widget_type: _Optional[str] = ..., widget_name: _Optional[str] = ..., widget_source: _Optional[str] = ..., widget_logic: _Optional[str] = ..., widget_template: _Optional[str] = ...) -> None: ...
