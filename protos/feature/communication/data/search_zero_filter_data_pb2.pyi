from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class SearchZeroFilterData(_message.Message):
    __slots__ = ["filter_id", "widget_url"]
    FILTER_ID_FIELD_NUMBER: _ClassVar[int]
    WIDGET_URL_FIELD_NUMBER: _ClassVar[int]
    filter_id: str
    widget_url: str
    def __init__(self, filter_id: _Optional[str] = ..., widget_url: _Optional[str] = ...) -> None: ...
