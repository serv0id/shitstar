from base import actions_pb2 as _actions_pb2
from base import widget_commons_pb2 as _widget_commons_pb2
from feature.ad import display_video_pb2 as _display_video_pb2
from feature.ad import display_image_pb2 as _display_image_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class VideoDisplayAdWidget(_message.Message):
    __slots__ = ("widget_commons", "data")
    class Data(_message.Message):
        __slots__ = ("video_ad", "image_ad", "action")
        VIDEO_AD_FIELD_NUMBER: _ClassVar[int]
        IMAGE_AD_FIELD_NUMBER: _ClassVar[int]
        ACTION_FIELD_NUMBER: _ClassVar[int]
        video_ad: _display_video_pb2.DisplayVideo
        image_ad: _display_image_pb2.DisplayImage
        action: _actions_pb2.Actions
        def __init__(self, video_ad: _Optional[_Union[_display_video_pb2.DisplayVideo, _Mapping]] = ..., image_ad: _Optional[_Union[_display_image_pb2.DisplayImage, _Mapping]] = ..., action: _Optional[_Union[_actions_pb2.Actions, _Mapping]] = ...) -> None: ...
    WIDGET_COMMONS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    widget_commons: _widget_commons_pb2.WidgetCommons
    data: VideoDisplayAdWidget.Data
    def __init__(self, widget_commons: _Optional[_Union[_widget_commons_pb2.WidgetCommons, _Mapping]] = ..., data: _Optional[_Union[VideoDisplayAdWidget.Data, _Mapping]] = ...) -> None: ...
