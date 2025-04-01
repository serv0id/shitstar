from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class EntryMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ENTRY_MODE_UNSPECIFIED: _ClassVar[EntryMode]
    ENTRY_MODE_TRAY: _ClassVar[EntryMode]
    ENTRY_MODE_ICON: _ClassVar[EntryMode]
    ENTRY_MODE_MIC: _ClassVar[EntryMode]
    ENTRY_MODE_CONTINUED: _ClassVar[EntryMode]
ENTRY_MODE_UNSPECIFIED: EntryMode
ENTRY_MODE_TRAY: EntryMode
ENTRY_MODE_ICON: EntryMode
ENTRY_MODE_MIC: EntryMode
ENTRY_MODE_CONTINUED: EntryMode

class SearchEntryProperties(_message.Message):
    __slots__ = ("search_session_id", "entry_mode")
    SEARCH_SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    ENTRY_MODE_FIELD_NUMBER: _ClassVar[int]
    search_session_id: str
    entry_mode: EntryMode
    def __init__(self, search_session_id: _Optional[str] = ..., entry_mode: _Optional[_Union[EntryMode, str]] = ...) -> None: ...
