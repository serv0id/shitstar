from base import widget_commons_pb2 as _widget_commons_pb2
from widget import scrollable_tray_pb2 as _scrollable_tray_pb2
from feature.refresh import refresh_info_pb2 as _refresh_info_pb2
from feature.community import community_info_pb2 as _community_info_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CommunityContainerWidget(_message.Message):
    __slots__ = ("widget_commons", "refresh_info", "community_info", "scrollable_tray")
    WIDGET_COMMONS_FIELD_NUMBER: _ClassVar[int]
    REFRESH_INFO_FIELD_NUMBER: _ClassVar[int]
    COMMUNITY_INFO_FIELD_NUMBER: _ClassVar[int]
    SCROLLABLE_TRAY_FIELD_NUMBER: _ClassVar[int]
    widget_commons: _widget_commons_pb2.WidgetCommons
    refresh_info: _refresh_info_pb2.RefreshInfo
    community_info: _community_info_pb2.CommunityInfo
    scrollable_tray: _scrollable_tray_pb2.ScrollableTrayWidget
    def __init__(self, widget_commons: _Optional[_Union[_widget_commons_pb2.WidgetCommons, _Mapping]] = ..., refresh_info: _Optional[_Union[_refresh_info_pb2.RefreshInfo, _Mapping]] = ..., community_info: _Optional[_Union[_community_info_pb2.CommunityInfo, _Mapping]] = ..., scrollable_tray: _Optional[_Union[_scrollable_tray_pb2.ScrollableTrayWidget, _Mapping]] = ...) -> None: ...
