from base import widget_commons_pb2 as _widget_commons_pb2
from feature.refresh import refresh_info_pb2 as _refresh_info_pb2
from widget import uat_vertical_content_poster_pb2 as _uat_vertical_content_poster_pb2
from widget import header_pb2 as _header_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class UnifiedAttentionTrayWidget(_message.Message):
    __slots__ = ("widget_commons", "data")
    class Data(_message.Message):
        __slots__ = ("item_template_name", "tray_header", "next_tray_url", "items", "should_fallback")
        ITEM_TEMPLATE_NAME_FIELD_NUMBER: _ClassVar[int]
        TRAY_HEADER_FIELD_NUMBER: _ClassVar[int]
        NEXT_TRAY_URL_FIELD_NUMBER: _ClassVar[int]
        ITEMS_FIELD_NUMBER: _ClassVar[int]
        SHOULD_FALLBACK_FIELD_NUMBER: _ClassVar[int]
        item_template_name: str
        tray_header: _header_pb2.HeaderWidget
        next_tray_url: str
        items: _containers.RepeatedCompositeFieldContainer[UnifiedAttentionTrayWidget.Item]
        should_fallback: bool
        def __init__(self, item_template_name: _Optional[str] = ..., tray_header: _Optional[_Union[_header_pb2.HeaderWidget, _Mapping]] = ..., next_tray_url: _Optional[str] = ..., items: _Optional[_Iterable[_Union[UnifiedAttentionTrayWidget.Item, _Mapping]]] = ..., should_fallback: bool = ...) -> None: ...
    class Item(_message.Message):
        __slots__ = ("uat_vertical_content_poster",)
        UAT_VERTICAL_CONTENT_POSTER_FIELD_NUMBER: _ClassVar[int]
        uat_vertical_content_poster: _uat_vertical_content_poster_pb2.UatVerticalContentPosterWidget
        def __init__(self, uat_vertical_content_poster: _Optional[_Union[_uat_vertical_content_poster_pb2.UatVerticalContentPosterWidget, _Mapping]] = ...) -> None: ...
    WIDGET_COMMONS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    widget_commons: _widget_commons_pb2.WidgetCommons
    data: UnifiedAttentionTrayWidget.Data
    def __init__(self, widget_commons: _Optional[_Union[_widget_commons_pb2.WidgetCommons, _Mapping]] = ..., data: _Optional[_Union[UnifiedAttentionTrayWidget.Data, _Mapping]] = ...) -> None: ...
