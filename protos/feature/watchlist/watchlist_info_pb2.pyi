from feature.accessibility import accessibility_pb2 as _accessibility_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class WatchlistInfo(_message.Message):
    __slots__ = ("content_id", "is_watchlisted", "timestamp", "alt_add", "alt_remove", "content_title")
    CONTENT_ID_FIELD_NUMBER: _ClassVar[int]
    IS_WATCHLISTED_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    ALT_ADD_FIELD_NUMBER: _ClassVar[int]
    ALT_REMOVE_FIELD_NUMBER: _ClassVar[int]
    CONTENT_TITLE_FIELD_NUMBER: _ClassVar[int]
    content_id: str
    is_watchlisted: bool
    timestamp: int
    alt_add: _accessibility_pb2.Accessibility
    alt_remove: _accessibility_pb2.Accessibility
    content_title: str
    def __init__(self, content_id: _Optional[str] = ..., is_watchlisted: bool = ..., timestamp: _Optional[int] = ..., alt_add: _Optional[_Union[_accessibility_pb2.Accessibility, _Mapping]] = ..., alt_remove: _Optional[_Union[_accessibility_pb2.Accessibility, _Mapping]] = ..., content_title: _Optional[str] = ...) -> None: ...
