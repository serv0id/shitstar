from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class TabList(_message.Message):
    __slots__ = ("selected_tab_name", "selected_tab_index", "count", "tab_count")
    SELECTED_TAB_NAME_FIELD_NUMBER: _ClassVar[int]
    SELECTED_TAB_INDEX_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    TAB_COUNT_FIELD_NUMBER: _ClassVar[int]
    selected_tab_name: str
    selected_tab_index: int
    count: int
    tab_count: int
    def __init__(self, selected_tab_name: _Optional[str] = ..., selected_tab_index: _Optional[int] = ..., count: _Optional[int] = ..., tab_count: _Optional[int] = ...) -> None: ...
