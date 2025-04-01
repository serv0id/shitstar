from base import actions_pb2 as _actions_pb2
from base import widget_commons_pb2 as _widget_commons_pb2
from feature.image import image_pb2 as _image_pb2
from feature.image import lottie_pb2 as _lottie_pb2
from feature.trackers import url_trackers_pb2 as _url_trackers_pb2
from feature.accessibility import accessibility_pb2 as _accessibility_pb2
from feature.ad import badge_pb2 as _badge_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class LottieBannerWidget(_message.Message):
    __slots__ = ("widget_commons", "data")
    class Data(_message.Message):
        __slots__ = ("placeholder_image", "action", "lottie", "tracker", "desc", "alt", "badge")
        PLACEHOLDER_IMAGE_FIELD_NUMBER: _ClassVar[int]
        ACTION_FIELD_NUMBER: _ClassVar[int]
        LOTTIE_FIELD_NUMBER: _ClassVar[int]
        TRACKER_FIELD_NUMBER: _ClassVar[int]
        DESC_FIELD_NUMBER: _ClassVar[int]
        ALT_FIELD_NUMBER: _ClassVar[int]
        BADGE_FIELD_NUMBER: _ClassVar[int]
        placeholder_image: _image_pb2.Image
        action: _actions_pb2.Actions
        lottie: _lottie_pb2.Lottie
        tracker: _url_trackers_pb2.UrlTrackers
        desc: str
        alt: _accessibility_pb2.Accessibility
        badge: _badge_pb2.AdBadge
        def __init__(self, placeholder_image: _Optional[_Union[_image_pb2.Image, _Mapping]] = ..., action: _Optional[_Union[_actions_pb2.Actions, _Mapping]] = ..., lottie: _Optional[_Union[_lottie_pb2.Lottie, _Mapping]] = ..., tracker: _Optional[_Union[_url_trackers_pb2.UrlTrackers, _Mapping]] = ..., desc: _Optional[str] = ..., alt: _Optional[_Union[_accessibility_pb2.Accessibility, _Mapping]] = ..., badge: _Optional[_Union[_badge_pb2.AdBadge, _Mapping]] = ...) -> None: ...
    WIDGET_COMMONS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    widget_commons: _widget_commons_pb2.WidgetCommons
    data: LottieBannerWidget.Data
    def __init__(self, widget_commons: _Optional[_Union[_widget_commons_pb2.WidgetCommons, _Mapping]] = ..., data: _Optional[_Union[LottieBannerWidget.Data, _Mapping]] = ...) -> None: ...
