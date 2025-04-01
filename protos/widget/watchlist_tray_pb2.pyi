from base import template_pb2 as _template_pb2
from base import widget_commons_pb2 as _widget_commons_pb2
from base import actions_pb2 as _actions_pb2
from widget import header_pb2 as _header_pb2
from widget import vertical_content_poster_pb2 as _vertical_content_poster_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class WatchlistWidget(_message.Message):
    __slots__ = ("template", "widget_commons", "data")
    class Data(_message.Message):
        __slots__ = ("header", "items", "next_watchlist_url", "refresh_info", "tray_header")
        HEADER_FIELD_NUMBER: _ClassVar[int]
        ITEMS_FIELD_NUMBER: _ClassVar[int]
        NEXT_WATCHLIST_URL_FIELD_NUMBER: _ClassVar[int]
        REFRESH_INFO_FIELD_NUMBER: _ClassVar[int]
        TRAY_HEADER_FIELD_NUMBER: _ClassVar[int]
        header: WatchlistWidget.Header
        items: _containers.RepeatedCompositeFieldContainer[WatchlistWidget.Item]
        next_watchlist_url: str
        refresh_info: WatchlistWidget.RefreshInfo
        tray_header: _header_pb2.HeaderWidget
        def __init__(self, header: _Optional[_Union[WatchlistWidget.Header, _Mapping]] = ..., items: _Optional[_Iterable[_Union[WatchlistWidget.Item, _Mapping]]] = ..., next_watchlist_url: _Optional[str] = ..., refresh_info: _Optional[_Union[WatchlistWidget.RefreshInfo, _Mapping]] = ..., tray_header: _Optional[_Union[_header_pb2.HeaderWidget, _Mapping]] = ...) -> None: ...
    class RefreshInfo(_message.Message):
        __slots__ = ("max_age_ms", "refresh_url")
        MAX_AGE_MS_FIELD_NUMBER: _ClassVar[int]
        REFRESH_URL_FIELD_NUMBER: _ClassVar[int]
        max_age_ms: int
        refresh_url: str
        def __init__(self, max_age_ms: _Optional[int] = ..., refresh_url: _Optional[str] = ...) -> None: ...
    class Header(_message.Message):
        __slots__ = ("title", "actions", "cta")
        TITLE_FIELD_NUMBER: _ClassVar[int]
        ACTIONS_FIELD_NUMBER: _ClassVar[int]
        CTA_FIELD_NUMBER: _ClassVar[int]
        title: str
        actions: _actions_pb2.Actions
        cta: WatchlistWidget.IconLabelCTA
        def __init__(self, title: _Optional[str] = ..., actions: _Optional[_Union[_actions_pb2.Actions, _Mapping]] = ..., cta: _Optional[_Union[WatchlistWidget.IconLabelCTA, _Mapping]] = ...) -> None: ...
    class Item(_message.Message):
        __slots__ = ("vertical_content_poster",)
        VERTICAL_CONTENT_POSTER_FIELD_NUMBER: _ClassVar[int]
        vertical_content_poster: _vertical_content_poster_pb2.VerticalContentPosterWidget
        def __init__(self, vertical_content_poster: _Optional[_Union[_vertical_content_poster_pb2.VerticalContentPosterWidget, _Mapping]] = ...) -> None: ...
    class IconLabelCTA(_message.Message):
        __slots__ = ("label", "icon_name", "actions")
        LABEL_FIELD_NUMBER: _ClassVar[int]
        ICON_NAME_FIELD_NUMBER: _ClassVar[int]
        ACTIONS_FIELD_NUMBER: _ClassVar[int]
        label: str
        icon_name: str
        actions: _actions_pb2.Actions
        def __init__(self, label: _Optional[str] = ..., icon_name: _Optional[str] = ..., actions: _Optional[_Union[_actions_pb2.Actions, _Mapping]] = ...) -> None: ...
    TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    WIDGET_COMMONS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    template: _template_pb2.Template
    widget_commons: _widget_commons_pb2.WidgetCommons
    data: WatchlistWidget.Data
    def __init__(self, template: _Optional[_Union[_template_pb2.Template, _Mapping]] = ..., widget_commons: _Optional[_Union[_widget_commons_pb2.WidgetCommons, _Mapping]] = ..., data: _Optional[_Union[WatchlistWidget.Data, _Mapping]] = ...) -> None: ...
