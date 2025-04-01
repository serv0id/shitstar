from component.content import tab_list_pb2 as _tab_list_pb2
from component.content import tray_callout_tag_pb2 as _tray_callout_tag_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class WidgetSource(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    WIDGET_SOURCE_UNSPECIFIED: _ClassVar[WidgetSource]
    WIDGET_SOURCE_PERSONA: _ClassVar[WidgetSource]
    WIDGET_SOURCE_CMS: _ClassVar[WidgetSource]
    WIDGET_SOURCE_SEARCH: _ClassVar[WidgetSource]
    WIDGET_SOURCE_WATCH: _ClassVar[WidgetSource]
WIDGET_SOURCE_UNSPECIFIED: WidgetSource
WIDGET_SOURCE_PERSONA: WidgetSource
WIDGET_SOURCE_CMS: WidgetSource
WIDGET_SOURCE_SEARCH: WidgetSource
WIDGET_SOURCE_WATCH: WidgetSource

class Widget(_message.Message):
    __slots__ = ("id", "name", "type", "source", "logic", "display_language", "position", "tray_callout_tags", "time_remaining_in_hrs", "is_timer_visible", "rows_count", "ranking_logic", "tab_list", "load_time_ms", "initiation_source", "theme_details", "view_type")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    LOGIC_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_LANGUAGE_FIELD_NUMBER: _ClassVar[int]
    POSITION_FIELD_NUMBER: _ClassVar[int]
    TRAY_CALLOUT_TAGS_FIELD_NUMBER: _ClassVar[int]
    TIME_REMAINING_IN_HRS_FIELD_NUMBER: _ClassVar[int]
    IS_TIMER_VISIBLE_FIELD_NUMBER: _ClassVar[int]
    ROWS_COUNT_FIELD_NUMBER: _ClassVar[int]
    RANKING_LOGIC_FIELD_NUMBER: _ClassVar[int]
    TAB_LIST_FIELD_NUMBER: _ClassVar[int]
    LOAD_TIME_MS_FIELD_NUMBER: _ClassVar[int]
    INITIATION_SOURCE_FIELD_NUMBER: _ClassVar[int]
    THEME_DETAILS_FIELD_NUMBER: _ClassVar[int]
    VIEW_TYPE_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    type: str
    source: WidgetSource
    logic: str
    display_language: str
    position: int
    tray_callout_tags: _containers.RepeatedCompositeFieldContainer[_tray_callout_tag_pb2.TrayCalloutTag]
    time_remaining_in_hrs: int
    is_timer_visible: bool
    rows_count: int
    ranking_logic: str
    tab_list: _tab_list_pb2.TabList
    load_time_ms: int
    initiation_source: str
    theme_details: str
    view_type: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., type: _Optional[str] = ..., source: _Optional[_Union[WidgetSource, str]] = ..., logic: _Optional[str] = ..., display_language: _Optional[str] = ..., position: _Optional[int] = ..., tray_callout_tags: _Optional[_Iterable[_Union[_tray_callout_tag_pb2.TrayCalloutTag, _Mapping]]] = ..., time_remaining_in_hrs: _Optional[int] = ..., is_timer_visible: bool = ..., rows_count: _Optional[int] = ..., ranking_logic: _Optional[str] = ..., tab_list: _Optional[_Union[_tab_list_pb2.TabList, _Mapping]] = ..., load_time_ms: _Optional[int] = ..., initiation_source: _Optional[str] = ..., theme_details: _Optional[str] = ..., view_type: _Optional[str] = ...) -> None: ...
