from base import widget_commons_pb2 as _widget_commons_pb2
from widget import media_content_info_small_pb2 as _media_content_info_small_pb2
from widget import media_content_info_large_pb2 as _media_content_info_large_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MediaContentInfoWidget(_message.Message):
    __slots__ = ("widget_commons", "data")
    class Data(_message.Message):
        __slots__ = ("small_info", "large_info")
        SMALL_INFO_FIELD_NUMBER: _ClassVar[int]
        LARGE_INFO_FIELD_NUMBER: _ClassVar[int]
        small_info: _media_content_info_small_pb2.MediaContentInfoSmallWidget
        large_info: _media_content_info_large_pb2.MediaContentInfoLargeWidget
        def __init__(self, small_info: _Optional[_Union[_media_content_info_small_pb2.MediaContentInfoSmallWidget, _Mapping]] = ..., large_info: _Optional[_Union[_media_content_info_large_pb2.MediaContentInfoLargeWidget, _Mapping]] = ...) -> None: ...
    WIDGET_COMMONS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    widget_commons: _widget_commons_pb2.WidgetCommons
    data: MediaContentInfoWidget.Data
    def __init__(self, widget_commons: _Optional[_Union[_widget_commons_pb2.WidgetCommons, _Mapping]] = ..., data: _Optional[_Union[MediaContentInfoWidget.Data, _Mapping]] = ...) -> None: ...
