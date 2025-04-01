from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class BestResultMatch(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    BEST_RESULT_MATCH_UNSPECIFIED: _ClassVar[BestResultMatch]
    BEST_RESULT_MATCH_HERO: _ClassVar[BestResultMatch]
    BEST_RESULT_MATCH_TOP: _ClassVar[BestResultMatch]
    BEST_RESULT_MATCH_MORE: _ClassVar[BestResultMatch]
    BEST_RESULT_MATCH_SIMILAR: _ClassVar[BestResultMatch]
    BEST_RESULT_MATCH_NO_RESULT: _ClassVar[BestResultMatch]

class ResponseType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    RESPONSE_TYPE_UNSPECIFIED: _ClassVar[ResponseType]
    RESPONSE_TYPE_SEARCH: _ClassVar[ResponseType]
    RESPONSE_TYPE_SEARCH_ZERO: _ClassVar[ResponseType]
    RESPONSE_TYPE_EXPLORE: _ClassVar[ResponseType]
    RESPONSE_TYPE_SEARCH_GLOBAL: _ClassVar[ResponseType]

class QueryIntent(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    QUERY_INTENT_UNSPECIFIED: _ClassVar[QueryIntent]
    QUERY_INTENT_NAV: _ClassVar[QueryIntent]
    QUERY_INTENT_BROAD: _ClassVar[QueryIntent]

class ContentTypeIntent(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CONTENT_TYPE_INTENT_UNSPECIFIED: _ClassVar[ContentTypeIntent]
    CONTENT_TYPE_INTENT_MOVIE: _ClassVar[ContentTypeIntent]
    CONTENT_TYPE_INTENT_TV_SHOW: _ClassVar[ContentTypeIntent]
    CONTENT_TYPE_INTENT_CHANNEL: _ClassVar[ContentTypeIntent]
    CONTENT_TYPE_INTENT_SPORTS: _ClassVar[ContentTypeIntent]
    CONTENT_TYPE_INTENT_NEWS: _ClassVar[ContentTypeIntent]
    CONTENT_TYPE_INTENT_CELEBRITY: _ClassVar[ContentTypeIntent]
    CONTENT_TYPE_INTENT_CLIP: _ClassVar[ContentTypeIntent]
    CONTENT_TYPE_INTENT_GENERAL: _ClassVar[ContentTypeIntent]
    CONTENT_TYPE_INTENT_ENTERTAINMENT: _ClassVar[ContentTypeIntent]

class PageName(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PAGE_NAME_UNSPECIFIED: _ClassVar[PageName]
    PAGE_NAME_SEARCH: _ClassVar[PageName]
    PAGE_NAME_SEARCH_ZERO: _ClassVar[PageName]
BEST_RESULT_MATCH_UNSPECIFIED: BestResultMatch
BEST_RESULT_MATCH_HERO: BestResultMatch
BEST_RESULT_MATCH_TOP: BestResultMatch
BEST_RESULT_MATCH_MORE: BestResultMatch
BEST_RESULT_MATCH_SIMILAR: BestResultMatch
BEST_RESULT_MATCH_NO_RESULT: BestResultMatch
RESPONSE_TYPE_UNSPECIFIED: ResponseType
RESPONSE_TYPE_SEARCH: ResponseType
RESPONSE_TYPE_SEARCH_ZERO: ResponseType
RESPONSE_TYPE_EXPLORE: ResponseType
RESPONSE_TYPE_SEARCH_GLOBAL: ResponseType
QUERY_INTENT_UNSPECIFIED: QueryIntent
QUERY_INTENT_NAV: QueryIntent
QUERY_INTENT_BROAD: QueryIntent
CONTENT_TYPE_INTENT_UNSPECIFIED: ContentTypeIntent
CONTENT_TYPE_INTENT_MOVIE: ContentTypeIntent
CONTENT_TYPE_INTENT_TV_SHOW: ContentTypeIntent
CONTENT_TYPE_INTENT_CHANNEL: ContentTypeIntent
CONTENT_TYPE_INTENT_SPORTS: ContentTypeIntent
CONTENT_TYPE_INTENT_NEWS: ContentTypeIntent
CONTENT_TYPE_INTENT_CELEBRITY: ContentTypeIntent
CONTENT_TYPE_INTENT_CLIP: ContentTypeIntent
CONTENT_TYPE_INTENT_GENERAL: ContentTypeIntent
CONTENT_TYPE_INTENT_ENTERTAINMENT: ContentTypeIntent
PAGE_NAME_UNSPECIFIED: PageName
PAGE_NAME_SEARCH: PageName
PAGE_NAME_SEARCH_ZERO: PageName

class SearchResponseProperties(_message.Message):
    __slots__ = ("response_type", "query_text", "content_type_intent", "total_results_count", "channel", "page_name", "query_language", "search_algo_flags", "query_intent", "best_result_match", "rules_enabled")
    RESPONSE_TYPE_FIELD_NUMBER: _ClassVar[int]
    QUERY_TEXT_FIELD_NUMBER: _ClassVar[int]
    CONTENT_TYPE_INTENT_FIELD_NUMBER: _ClassVar[int]
    TOTAL_RESULTS_COUNT_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_FIELD_NUMBER: _ClassVar[int]
    PAGE_NAME_FIELD_NUMBER: _ClassVar[int]
    QUERY_LANGUAGE_FIELD_NUMBER: _ClassVar[int]
    SEARCH_ALGO_FLAGS_FIELD_NUMBER: _ClassVar[int]
    QUERY_INTENT_FIELD_NUMBER: _ClassVar[int]
    BEST_RESULT_MATCH_FIELD_NUMBER: _ClassVar[int]
    RULES_ENABLED_FIELD_NUMBER: _ClassVar[int]
    response_type: ResponseType
    query_text: str
    content_type_intent: ContentTypeIntent
    total_results_count: int
    channel: str
    page_name: PageName
    query_language: str
    search_algo_flags: str
    query_intent: QueryIntent
    best_result_match: BestResultMatch
    rules_enabled: bool
    def __init__(self, response_type: _Optional[_Union[ResponseType, str]] = ..., query_text: _Optional[str] = ..., content_type_intent: _Optional[_Union[ContentTypeIntent, str]] = ..., total_results_count: _Optional[int] = ..., channel: _Optional[str] = ..., page_name: _Optional[_Union[PageName, str]] = ..., query_language: _Optional[str] = ..., search_algo_flags: _Optional[str] = ..., query_intent: _Optional[_Union[QueryIntent, str]] = ..., best_result_match: _Optional[_Union[BestResultMatch, str]] = ..., rules_enabled: bool = ...) -> None: ...
