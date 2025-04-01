from base import widget_commons_pb2 as _widget_commons_pb2
from feature.refresh import refresh_info_pb2 as _refresh_info_pb2
from widget import header_pb2 as _header_pb2
from widget import hero_content_display_pb2 as _hero_content_display_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MarqueeTrayWidget(_message.Message):
    __slots__ = ("widget_commons", "data")
    class Data(_message.Message):
        __slots__ = ("header", "hero_content_display_widget", "refresh_info")
        HEADER_FIELD_NUMBER: _ClassVar[int]
        HERO_CONTENT_DISPLAY_WIDGET_FIELD_NUMBER: _ClassVar[int]
        REFRESH_INFO_FIELD_NUMBER: _ClassVar[int]
        header: _header_pb2.HeaderWidget
        hero_content_display_widget: _hero_content_display_pb2.HeroContentDisplayWidget
        refresh_info: _refresh_info_pb2.RefreshInfo
        def __init__(self, header: _Optional[_Union[_header_pb2.HeaderWidget, _Mapping]] = ..., hero_content_display_widget: _Optional[_Union[_hero_content_display_pb2.HeroContentDisplayWidget, _Mapping]] = ..., refresh_info: _Optional[_Union[_refresh_info_pb2.RefreshInfo, _Mapping]] = ...) -> None: ...
    WIDGET_COMMONS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    widget_commons: _widget_commons_pb2.WidgetCommons
    data: MarqueeTrayWidget.Data
    def __init__(self, widget_commons: _Optional[_Union[_widget_commons_pb2.WidgetCommons, _Mapping]] = ..., data: _Optional[_Union[MarqueeTrayWidget.Data, _Mapping]] = ...) -> None: ...
