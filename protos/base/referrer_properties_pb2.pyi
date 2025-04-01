from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ReferrerProperties(_message.Message):
    __slots__ = ("referrer_widget_id", "referrer_widget_name", "referrer_page_name")
    REFERRER_WIDGET_ID_FIELD_NUMBER: _ClassVar[int]
    REFERRER_WIDGET_NAME_FIELD_NUMBER: _ClassVar[int]
    REFERRER_PAGE_NAME_FIELD_NUMBER: _ClassVar[int]
    referrer_widget_id: str
    referrer_widget_name: str
    referrer_page_name: str
    def __init__(self, referrer_widget_id: _Optional[str] = ..., referrer_widget_name: _Optional[str] = ..., referrer_page_name: _Optional[str] = ...) -> None: ...
