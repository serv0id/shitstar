from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PageType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PAGE_TYPE_UNSPECIFIED: _ClassVar[PageType]
    PAGE_TYPE_SEARCH: _ClassVar[PageType]
    PAGE_TYPE_SEARCH_ZERO: _ClassVar[PageType]
    PAGE_TYPE_EXPLORE: _ClassVar[PageType]
PAGE_TYPE_UNSPECIFIED: PageType
PAGE_TYPE_SEARCH: PageType
PAGE_TYPE_SEARCH_ZERO: PageType
PAGE_TYPE_EXPLORE: PageType

class SearchAppliedFilterProperties(_message.Message):
    __slots__ = ("search_session_id", "search_id", "query_text", "page_type", "search_filter", "is_explicit")
    class SearchFilterEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: StringList
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[StringList, _Mapping]] = ...) -> None: ...
    SEARCH_SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    SEARCH_ID_FIELD_NUMBER: _ClassVar[int]
    QUERY_TEXT_FIELD_NUMBER: _ClassVar[int]
    PAGE_TYPE_FIELD_NUMBER: _ClassVar[int]
    SEARCH_FILTER_FIELD_NUMBER: _ClassVar[int]
    IS_EXPLICIT_FIELD_NUMBER: _ClassVar[int]
    search_session_id: str
    search_id: str
    query_text: str
    page_type: PageType
    search_filter: _containers.MessageMap[str, StringList]
    is_explicit: bool
    def __init__(self, search_session_id: _Optional[str] = ..., search_id: _Optional[str] = ..., query_text: _Optional[str] = ..., page_type: _Optional[_Union[PageType, str]] = ..., search_filter: _Optional[_Mapping[str, StringList]] = ..., is_explicit: bool = ...) -> None: ...

class StringList(_message.Message):
    __slots__ = ("values",)
    VALUES_FIELD_NUMBER: _ClassVar[int]
    values: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, values: _Optional[_Iterable[str]] = ...) -> None: ...
