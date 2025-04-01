from base import widget_commons_pb2 as _widget_commons_pb2
from base import actions_pb2 as _actions_pb2
from feature.image import image_pb2 as _image_pb2
from feature.image import screen_size_image_pb2 as _screen_size_image_pb2
from feature.trackers import url_trackers_pb2 as _url_trackers_pb2
from feature.ad import badge_pb2 as _badge_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ImageBannerWidget(_message.Message):
    __slots__ = ("widget_commons", "data")
    class Data(_message.Message):
        __slots__ = ("bg_image", "actions", "image", "tracker", "badge")
        BG_IMAGE_FIELD_NUMBER: _ClassVar[int]
        ACTIONS_FIELD_NUMBER: _ClassVar[int]
        IMAGE_FIELD_NUMBER: _ClassVar[int]
        TRACKER_FIELD_NUMBER: _ClassVar[int]
        BADGE_FIELD_NUMBER: _ClassVar[int]
        bg_image: _image_pb2.Image
        actions: _actions_pb2.Actions
        image: _screen_size_image_pb2.ScreenSizeImage
        tracker: _url_trackers_pb2.UrlTrackers
        badge: _badge_pb2.AdBadge
        def __init__(self, bg_image: _Optional[_Union[_image_pb2.Image, _Mapping]] = ..., actions: _Optional[_Union[_actions_pb2.Actions, _Mapping]] = ..., image: _Optional[_Union[_screen_size_image_pb2.ScreenSizeImage, _Mapping]] = ..., tracker: _Optional[_Union[_url_trackers_pb2.UrlTrackers, _Mapping]] = ..., badge: _Optional[_Union[_badge_pb2.AdBadge, _Mapping]] = ...) -> None: ...
    WIDGET_COMMONS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    widget_commons: _widget_commons_pb2.WidgetCommons
    data: ImageBannerWidget.Data
    def __init__(self, widget_commons: _Optional[_Union[_widget_commons_pb2.WidgetCommons, _Mapping]] = ..., data: _Optional[_Union[ImageBannerWidget.Data, _Mapping]] = ...) -> None: ...
