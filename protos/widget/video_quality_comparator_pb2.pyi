from base import widget_commons_pb2 as _widget_commons_pb2
from widget import video_display_ad_pb2 as _video_display_ad_pb2
from widget import header_pb2 as _header_pb2
from feature.atom import button_pb2 as _button_pb2
from feature.ad import media_clarity_comparator_overlay_pb2 as _media_clarity_comparator_overlay_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class VideoQualityComparatorWidget(_message.Message):
    __slots__ = ("widget_commons", "data")
    class Data(_message.Message):
        __slots__ = ("header_widget", "video_widget", "media_clarity_comparator_overlay", "button")
        HEADER_WIDGET_FIELD_NUMBER: _ClassVar[int]
        VIDEO_WIDGET_FIELD_NUMBER: _ClassVar[int]
        MEDIA_CLARITY_COMPARATOR_OVERLAY_FIELD_NUMBER: _ClassVar[int]
        BUTTON_FIELD_NUMBER: _ClassVar[int]
        header_widget: _header_pb2.HeaderWidget
        video_widget: _video_display_ad_pb2.VideoDisplayAdWidget
        media_clarity_comparator_overlay: _media_clarity_comparator_overlay_pb2.MediaClarityComparatorOverlay
        button: _button_pb2.Button
        def __init__(self, header_widget: _Optional[_Union[_header_pb2.HeaderWidget, _Mapping]] = ..., video_widget: _Optional[_Union[_video_display_ad_pb2.VideoDisplayAdWidget, _Mapping]] = ..., media_clarity_comparator_overlay: _Optional[_Union[_media_clarity_comparator_overlay_pb2.MediaClarityComparatorOverlay, _Mapping]] = ..., button: _Optional[_Union[_button_pb2.Button, _Mapping]] = ...) -> None: ...
    WIDGET_COMMONS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    widget_commons: _widget_commons_pb2.WidgetCommons
    data: VideoQualityComparatorWidget.Data
    def __init__(self, widget_commons: _Optional[_Union[_widget_commons_pb2.WidgetCommons, _Mapping]] = ..., data: _Optional[_Union[VideoQualityComparatorWidget.Data, _Mapping]] = ...) -> None: ...
