from client.search import search_session_info_pb2 as _search_session_info_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class InterfaceType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    INTERFACE_TYPE_UNSPECIFIED: _ClassVar[InterfaceType]
    INTERFACE_TYPE_HISTORY: _ClassVar[InterfaceType]
    INTERFACE_TYPE_TRENDING: _ClassVar[InterfaceType]
    INTERFACE_TYPE_TOP_RESULT: _ClassVar[InterfaceType]
    INTERFACE_TYPE_HERO_RESULT: _ClassVar[InterfaceType]
    INTERFACE_TYPE_MORE_RESULT: _ClassVar[InterfaceType]
    INTERFACE_TYPE_RELATED_SEARCH: _ClassVar[InterfaceType]
    INTERFACE_TYPE_TYPEAHEAD: _ClassVar[InterfaceType]
    INTERFACE_TYPE_EXPLORE: _ClassVar[InterfaceType]
    INTERFACE_TYPE_SCOREBOARD: _ClassVar[InterfaceType]
    INTERFACE_TYPE_FILTER: _ClassVar[InterfaceType]
    INTERFACE_TYPE_SIMILAR_RESULT: _ClassVar[InterfaceType]
    INTERFACE_TYPE_MORE_LIKE_THIS: _ClassVar[InterfaceType]
    INTERFACE_TYPE_YOU_MAY_ALSO_LIKE: _ClassVar[InterfaceType]
    INTERFACE_TYPE_POPULAR_CLIPS: _ClassVar[InterfaceType]

class PageType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PAGE_TYPE_UNSPECIFIED: _ClassVar[PageType]
    PAGE_TYPE_EXPLORE: _ClassVar[PageType]
    PAGE_TYPE_SEARCH: _ClassVar[PageType]
    PAGE_TYPE_SEARCH_ZERO: _ClassVar[PageType]
INTERFACE_TYPE_UNSPECIFIED: InterfaceType
INTERFACE_TYPE_HISTORY: InterfaceType
INTERFACE_TYPE_TRENDING: InterfaceType
INTERFACE_TYPE_TOP_RESULT: InterfaceType
INTERFACE_TYPE_HERO_RESULT: InterfaceType
INTERFACE_TYPE_MORE_RESULT: InterfaceType
INTERFACE_TYPE_RELATED_SEARCH: InterfaceType
INTERFACE_TYPE_TYPEAHEAD: InterfaceType
INTERFACE_TYPE_EXPLORE: InterfaceType
INTERFACE_TYPE_SCOREBOARD: InterfaceType
INTERFACE_TYPE_FILTER: InterfaceType
INTERFACE_TYPE_SIMILAR_RESULT: InterfaceType
INTERFACE_TYPE_MORE_LIKE_THIS: InterfaceType
INTERFACE_TYPE_YOU_MAY_ALSO_LIKE: InterfaceType
INTERFACE_TYPE_POPULAR_CLIPS: InterfaceType
PAGE_TYPE_UNSPECIFIED: PageType
PAGE_TYPE_EXPLORE: PageType
PAGE_TYPE_SEARCH: PageType
PAGE_TYPE_SEARCH_ZERO: PageType

class SearchInfoProperties(_message.Message):
    __slots__ = ("interface_type", "query_text", "page_type", "primary_language", "widget_filter")
    INTERFACE_TYPE_FIELD_NUMBER: _ClassVar[int]
    QUERY_TEXT_FIELD_NUMBER: _ClassVar[int]
    PAGE_TYPE_FIELD_NUMBER: _ClassVar[int]
    PRIMARY_LANGUAGE_FIELD_NUMBER: _ClassVar[int]
    WIDGET_FILTER_FIELD_NUMBER: _ClassVar[int]
    interface_type: InterfaceType
    query_text: str
    page_type: PageType
    primary_language: str
    widget_filter: str
    def __init__(self, interface_type: _Optional[_Union[InterfaceType, str]] = ..., query_text: _Optional[str] = ..., page_type: _Optional[_Union[PageType, str]] = ..., primary_language: _Optional[str] = ..., widget_filter: _Optional[str] = ...) -> None: ...
