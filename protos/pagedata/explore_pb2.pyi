from base import page_data_commons_pb2 as _page_data_commons_pb2
from google.protobuf import any_pb2 as _any_pb2
from base import actions_pb2 as _actions_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ExplorePageData(_message.Message):
    __slots__ = ("page_data_commons", "placeholder", "search_suggestions_url", "search_results_url", "voice_search_enabled", "search_tabs", "instrumentation_context", "keypad_activated", "history_show_limit", "tap_to_history", "searchbar_actions", "experiment", "dynamic_hints")
    class SearchTab(_message.Message):
        __slots__ = ("display_name", "filter_name", "filter_value")
        DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
        FILTER_NAME_FIELD_NUMBER: _ClassVar[int]
        FILTER_VALUE_FIELD_NUMBER: _ClassVar[int]
        display_name: str
        filter_name: str
        filter_value: str
        def __init__(self, display_name: _Optional[str] = ..., filter_name: _Optional[str] = ..., filter_value: _Optional[str] = ...) -> None: ...
    class Experiment(_message.Message):
        __slots__ = ("show_legacy_history_in_zero", "is_dynamic_hint_clickable")
        SHOW_LEGACY_HISTORY_IN_ZERO_FIELD_NUMBER: _ClassVar[int]
        IS_DYNAMIC_HINT_CLICKABLE_FIELD_NUMBER: _ClassVar[int]
        show_legacy_history_in_zero: bool
        is_dynamic_hint_clickable: bool
        def __init__(self, show_legacy_history_in_zero: bool = ..., is_dynamic_hint_clickable: bool = ...) -> None: ...
    class DynamicHint(_message.Message):
        __slots__ = ("display_text", "query")
        DISPLAY_TEXT_FIELD_NUMBER: _ClassVar[int]
        QUERY_FIELD_NUMBER: _ClassVar[int]
        display_text: str
        query: str
        def __init__(self, display_text: _Optional[str] = ..., query: _Optional[str] = ...) -> None: ...
    PAGE_DATA_COMMONS_FIELD_NUMBER: _ClassVar[int]
    PLACEHOLDER_FIELD_NUMBER: _ClassVar[int]
    SEARCH_SUGGESTIONS_URL_FIELD_NUMBER: _ClassVar[int]
    SEARCH_RESULTS_URL_FIELD_NUMBER: _ClassVar[int]
    VOICE_SEARCH_ENABLED_FIELD_NUMBER: _ClassVar[int]
    SEARCH_TABS_FIELD_NUMBER: _ClassVar[int]
    INSTRUMENTATION_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    KEYPAD_ACTIVATED_FIELD_NUMBER: _ClassVar[int]
    HISTORY_SHOW_LIMIT_FIELD_NUMBER: _ClassVar[int]
    TAP_TO_HISTORY_FIELD_NUMBER: _ClassVar[int]
    SEARCHBAR_ACTIONS_FIELD_NUMBER: _ClassVar[int]
    EXPERIMENT_FIELD_NUMBER: _ClassVar[int]
    DYNAMIC_HINTS_FIELD_NUMBER: _ClassVar[int]
    page_data_commons: _page_data_commons_pb2.PageDataCommons
    placeholder: str
    search_suggestions_url: str
    search_results_url: str
    voice_search_enabled: bool
    search_tabs: _containers.RepeatedCompositeFieldContainer[ExplorePageData.SearchTab]
    instrumentation_context: _any_pb2.Any
    keypad_activated: bool
    history_show_limit: int
    tap_to_history: bool
    searchbar_actions: _actions_pb2.Actions
    experiment: ExplorePageData.Experiment
    dynamic_hints: _containers.RepeatedCompositeFieldContainer[ExplorePageData.DynamicHint]
    def __init__(self, page_data_commons: _Optional[_Union[_page_data_commons_pb2.PageDataCommons, _Mapping]] = ..., placeholder: _Optional[str] = ..., search_suggestions_url: _Optional[str] = ..., search_results_url: _Optional[str] = ..., voice_search_enabled: bool = ..., search_tabs: _Optional[_Iterable[_Union[ExplorePageData.SearchTab, _Mapping]]] = ..., instrumentation_context: _Optional[_Union[_any_pb2.Any, _Mapping]] = ..., keypad_activated: bool = ..., history_show_limit: _Optional[int] = ..., tap_to_history: bool = ..., searchbar_actions: _Optional[_Union[_actions_pb2.Actions, _Mapping]] = ..., experiment: _Optional[_Union[ExplorePageData.Experiment, _Mapping]] = ..., dynamic_hints: _Optional[_Iterable[_Union[ExplorePageData.DynamicHint, _Mapping]]] = ...) -> None: ...
