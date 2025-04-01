from base import page_data_commons_pb2 as _page_data_commons_pb2
from google.protobuf import any_pb2 as _any_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SearchPageData(_message.Message):
    __slots__ = ("page_data_commons", "query", "instrumentation_context", "tab_name", "filters", "suggested_queries", "result_one_liner", "search_survey_info")
    class Filter(_message.Message):
        __slots__ = ("name", "values")
        NAME_FIELD_NUMBER: _ClassVar[int]
        VALUES_FIELD_NUMBER: _ClassVar[int]
        name: str
        values: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, name: _Optional[str] = ..., values: _Optional[_Iterable[str]] = ...) -> None: ...
    class SuggestedQueries(_message.Message):
        __slots__ = ("display_name", "suggested_query")
        DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
        SUGGESTED_QUERY_FIELD_NUMBER: _ClassVar[int]
        display_name: str
        suggested_query: str
        def __init__(self, display_name: _Optional[str] = ..., suggested_query: _Optional[str] = ...) -> None: ...
    class SearchSurveyInfo(_message.Message):
        __slots__ = ("widget_url", "survey_index")
        WIDGET_URL_FIELD_NUMBER: _ClassVar[int]
        SURVEY_INDEX_FIELD_NUMBER: _ClassVar[int]
        widget_url: str
        survey_index: str
        def __init__(self, widget_url: _Optional[str] = ..., survey_index: _Optional[str] = ...) -> None: ...
    PAGE_DATA_COMMONS_FIELD_NUMBER: _ClassVar[int]
    QUERY_FIELD_NUMBER: _ClassVar[int]
    INSTRUMENTATION_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    TAB_NAME_FIELD_NUMBER: _ClassVar[int]
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    SUGGESTED_QUERIES_FIELD_NUMBER: _ClassVar[int]
    RESULT_ONE_LINER_FIELD_NUMBER: _ClassVar[int]
    SEARCH_SURVEY_INFO_FIELD_NUMBER: _ClassVar[int]
    page_data_commons: _page_data_commons_pb2.PageDataCommons
    query: str
    instrumentation_context: _any_pb2.Any
    tab_name: str
    filters: _containers.RepeatedCompositeFieldContainer[SearchPageData.Filter]
    suggested_queries: _containers.RepeatedCompositeFieldContainer[SearchPageData.SuggestedQueries]
    result_one_liner: str
    search_survey_info: SearchPageData.SearchSurveyInfo
    def __init__(self, page_data_commons: _Optional[_Union[_page_data_commons_pb2.PageDataCommons, _Mapping]] = ..., query: _Optional[str] = ..., instrumentation_context: _Optional[_Union[_any_pb2.Any, _Mapping]] = ..., tab_name: _Optional[str] = ..., filters: _Optional[_Iterable[_Union[SearchPageData.Filter, _Mapping]]] = ..., suggested_queries: _Optional[_Iterable[_Union[SearchPageData.SuggestedQueries, _Mapping]]] = ..., result_one_liner: _Optional[str] = ..., search_survey_info: _Optional[_Union[SearchPageData.SearchSurveyInfo, _Mapping]] = ...) -> None: ...
