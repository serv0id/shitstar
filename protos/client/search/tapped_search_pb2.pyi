from client.search import search_applied_filter_pb2 as _search_applied_filter_pb2
from client.search import search_session_info_pb2 as _search_session_info_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SearchInterface(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SEARCH_INTERFACE_UNSPECIFIED: _ClassVar[SearchInterface]
    SEARCH_INTERFACE_HISTORY: _ClassVar[SearchInterface]
    SEARCH_INTERFACE_TRENDING: _ClassVar[SearchInterface]
    SEARCH_INTERFACE_RELATED_SEARCH: _ClassVar[SearchInterface]
    SEARCH_INTERFACE_TYPEAHEAD: _ClassVar[SearchInterface]
    SEARCH_INTERFACE_AUTO_SUGGEST: _ClassVar[SearchInterface]
SEARCH_INTERFACE_UNSPECIFIED: SearchInterface
SEARCH_INTERFACE_HISTORY: SearchInterface
SEARCH_INTERFACE_TRENDING: SearchInterface
SEARCH_INTERFACE_RELATED_SEARCH: SearchInterface
SEARCH_INTERFACE_TYPEAHEAD: SearchInterface
SEARCH_INTERFACE_AUTO_SUGGEST: SearchInterface

class TappedSearchProperties(_message.Message):
    __slots__ = ("search_session_id", "search_id", "query_text", "page_type", "search_interface", "search_action", "display_text", "position", "extra_info")
    SEARCH_SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    SEARCH_ID_FIELD_NUMBER: _ClassVar[int]
    QUERY_TEXT_FIELD_NUMBER: _ClassVar[int]
    PAGE_TYPE_FIELD_NUMBER: _ClassVar[int]
    SEARCH_INTERFACE_FIELD_NUMBER: _ClassVar[int]
    SEARCH_ACTION_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_TEXT_FIELD_NUMBER: _ClassVar[int]
    POSITION_FIELD_NUMBER: _ClassVar[int]
    EXTRA_INFO_FIELD_NUMBER: _ClassVar[int]
    search_session_id: str
    search_id: str
    query_text: str
    page_type: _search_applied_filter_pb2.PageType
    search_interface: SearchInterface
    search_action: _search_session_info_pb2.SearchAction
    display_text: str
    position: int
    extra_info: str
    def __init__(self, search_session_id: _Optional[str] = ..., search_id: _Optional[str] = ..., query_text: _Optional[str] = ..., page_type: _Optional[_Union[_search_applied_filter_pb2.PageType, str]] = ..., search_interface: _Optional[_Union[SearchInterface, str]] = ..., search_action: _Optional[_Union[_search_session_info_pb2.SearchAction, str]] = ..., display_text: _Optional[str] = ..., position: _Optional[int] = ..., extra_info: _Optional[str] = ...) -> None: ...
