from client.search import search_queried_pb2 as _search_queried_pb2
from google.protobuf import any_pb2 as _any_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SearchAction(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SEARCH_ACTION_UNSPECIFIED: _ClassVar[SearchAction]
    SEARCH_ACTION_RESULTS: _ClassVar[SearchAction]
    SEARCH_ACTION_WATCHLIST: _ClassVar[SearchAction]
    SEARCH_ACTION_CW: _ClassVar[SearchAction]
    SEARCH_ACTION_DOWNLOAD: _ClassVar[SearchAction]
    SEARCH_ACTION_PLAY: _ClassVar[SearchAction]
    SEARCH_ACTION_PLAY_TRAILER: _ClassVar[SearchAction]
    SEARCH_ACTION_SEARCH: _ClassVar[SearchAction]
    SEARCH_ACTION_FILTER: _ClassVar[SearchAction]

class QueryIntent(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    QUERY_INTENT_UNSPECIFIED: _ClassVar[QueryIntent]
    QUERY_INTENT_NAV: _ClassVar[QueryIntent]
    QUERY_INTENT_BROAD: _ClassVar[QueryIntent]
SEARCH_ACTION_UNSPECIFIED: SearchAction
SEARCH_ACTION_RESULTS: SearchAction
SEARCH_ACTION_WATCHLIST: SearchAction
SEARCH_ACTION_CW: SearchAction
SEARCH_ACTION_DOWNLOAD: SearchAction
SEARCH_ACTION_PLAY: SearchAction
SEARCH_ACTION_PLAY_TRAILER: SearchAction
SEARCH_ACTION_SEARCH: SearchAction
SEARCH_ACTION_FILTER: SearchAction
QUERY_INTENT_UNSPECIFIED: QueryIntent
QUERY_INTENT_NAV: QueryIntent
QUERY_INTENT_BROAD: QueryIntent

class SearchSessionProperties(_message.Message):
    __slots__ = ("search_session_id", "search_id", "search_action", "query_input", "search_latency", "other_properties", "impression_count", "history_tile_position")
    SEARCH_SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    SEARCH_ID_FIELD_NUMBER: _ClassVar[int]
    SEARCH_ACTION_FIELD_NUMBER: _ClassVar[int]
    QUERY_INPUT_FIELD_NUMBER: _ClassVar[int]
    SEARCH_LATENCY_FIELD_NUMBER: _ClassVar[int]
    OTHER_PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    IMPRESSION_COUNT_FIELD_NUMBER: _ClassVar[int]
    HISTORY_TILE_POSITION_FIELD_NUMBER: _ClassVar[int]
    search_session_id: str
    search_id: str
    search_action: SearchAction
    query_input: _search_queried_pb2.QueryInput
    search_latency: int
    other_properties: _any_pb2.Any
    impression_count: int
    history_tile_position: int
    def __init__(self, search_session_id: _Optional[str] = ..., search_id: _Optional[str] = ..., search_action: _Optional[_Union[SearchAction, str]] = ..., query_input: _Optional[_Union[_search_queried_pb2.QueryInput, str]] = ..., search_latency: _Optional[int] = ..., other_properties: _Optional[_Union[_any_pb2.Any, _Mapping]] = ..., impression_count: _Optional[int] = ..., history_tile_position: _Optional[int] = ...) -> None: ...
