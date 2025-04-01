from client.search import search_session_info_pb2 as _search_session_info_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SearchHistoryProperties(_message.Message):
    __slots__ = ("session_info", "tile_position")
    SESSION_INFO_FIELD_NUMBER: _ClassVar[int]
    TILE_POSITION_FIELD_NUMBER: _ClassVar[int]
    session_info: _search_session_info_pb2.SearchSessionProperties
    tile_position: int
    def __init__(self, session_info: _Optional[_Union[_search_session_info_pb2.SearchSessionProperties, _Mapping]] = ..., tile_position: _Optional[int] = ...) -> None: ...
