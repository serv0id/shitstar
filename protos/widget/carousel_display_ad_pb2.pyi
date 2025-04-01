from base import widget_commons_pb2 as _widget_commons_pb2
from base import actions_pb2 as _actions_pb2
from feature.trackers import url_trackers_pb2 as _url_trackers_pb2
from feature.ad import display_image_pb2 as _display_image_pb2
from feature.image import screen_size_image_pb2 as _screen_size_image_pb2
from feature.image import image_pb2 as _image_pb2
from feature.accessibility import accessibility_pb2 as _accessibility_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CarouselDisplayAdWidget(_message.Message):
    __slots__ = ("widget_commons", "data")
    class Data(_message.Message):
        __slots__ = ("logo", "badge", "title", "subTitle", "cta", "tracker", "item", "carousel_desc", "carousel_ad_type")
        class CarouselAdType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            UNKNOWN: _ClassVar[CarouselDisplayAdWidget.Data.CarouselAdType]
            STANDARD: _ClassVar[CarouselDisplayAdWidget.Data.CarouselAdType]
            ACCORDION: _ClassVar[CarouselDisplayAdWidget.Data.CarouselAdType]
        UNKNOWN: CarouselDisplayAdWidget.Data.CarouselAdType
        STANDARD: CarouselDisplayAdWidget.Data.CarouselAdType
        ACCORDION: CarouselDisplayAdWidget.Data.CarouselAdType
        class Badge(_message.Message):
            __slots__ = ("label", "desc")
            LABEL_FIELD_NUMBER: _ClassVar[int]
            DESC_FIELD_NUMBER: _ClassVar[int]
            label: str
            desc: str
            def __init__(self, label: _Optional[str] = ..., desc: _Optional[str] = ...) -> None: ...
        class Cta(_message.Message):
            __slots__ = ("label", "bg_color", "desc", "action")
            LABEL_FIELD_NUMBER: _ClassVar[int]
            BG_COLOR_FIELD_NUMBER: _ClassVar[int]
            DESC_FIELD_NUMBER: _ClassVar[int]
            ACTION_FIELD_NUMBER: _ClassVar[int]
            label: str
            bg_color: str
            desc: str
            action: _actions_pb2.Actions
            def __init__(self, label: _Optional[str] = ..., bg_color: _Optional[str] = ..., desc: _Optional[str] = ..., action: _Optional[_Union[_actions_pb2.Actions, _Mapping]] = ...) -> None: ...
        LOGO_FIELD_NUMBER: _ClassVar[int]
        BADGE_FIELD_NUMBER: _ClassVar[int]
        TITLE_FIELD_NUMBER: _ClassVar[int]
        SUBTITLE_FIELD_NUMBER: _ClassVar[int]
        CTA_FIELD_NUMBER: _ClassVar[int]
        TRACKER_FIELD_NUMBER: _ClassVar[int]
        ITEM_FIELD_NUMBER: _ClassVar[int]
        CAROUSEL_DESC_FIELD_NUMBER: _ClassVar[int]
        CAROUSEL_AD_TYPE_FIELD_NUMBER: _ClassVar[int]
        logo: _image_pb2.Image
        badge: CarouselDisplayAdWidget.Data.Badge
        title: str
        subTitle: str
        cta: CarouselDisplayAdWidget.Data.Cta
        tracker: _url_trackers_pb2.UrlTrackers
        item: _containers.RepeatedCompositeFieldContainer[CarouselDisplayAdWidget.Item]
        carousel_desc: str
        carousel_ad_type: CarouselDisplayAdWidget.Data.CarouselAdType
        def __init__(self, logo: _Optional[_Union[_image_pb2.Image, _Mapping]] = ..., badge: _Optional[_Union[CarouselDisplayAdWidget.Data.Badge, _Mapping]] = ..., title: _Optional[str] = ..., subTitle: _Optional[str] = ..., cta: _Optional[_Union[CarouselDisplayAdWidget.Data.Cta, _Mapping]] = ..., tracker: _Optional[_Union[_url_trackers_pb2.UrlTrackers, _Mapping]] = ..., item: _Optional[_Iterable[_Union[CarouselDisplayAdWidget.Item, _Mapping]]] = ..., carousel_desc: _Optional[str] = ..., carousel_ad_type: _Optional[_Union[CarouselDisplayAdWidget.Data.CarouselAdType, str]] = ...) -> None: ...
    class Item(_message.Message):
        __slots__ = ("image", "label", "action", "tracker", "alt")
        IMAGE_FIELD_NUMBER: _ClassVar[int]
        LABEL_FIELD_NUMBER: _ClassVar[int]
        ACTION_FIELD_NUMBER: _ClassVar[int]
        TRACKER_FIELD_NUMBER: _ClassVar[int]
        ALT_FIELD_NUMBER: _ClassVar[int]
        image: _screen_size_image_pb2.ScreenSizeImage
        label: str
        action: _actions_pb2.Actions
        tracker: _url_trackers_pb2.UrlTrackers
        alt: _accessibility_pb2.Accessibility
        def __init__(self, image: _Optional[_Union[_screen_size_image_pb2.ScreenSizeImage, _Mapping]] = ..., label: _Optional[str] = ..., action: _Optional[_Union[_actions_pb2.Actions, _Mapping]] = ..., tracker: _Optional[_Union[_url_trackers_pb2.UrlTrackers, _Mapping]] = ..., alt: _Optional[_Union[_accessibility_pb2.Accessibility, _Mapping]] = ...) -> None: ...
    WIDGET_COMMONS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    widget_commons: _widget_commons_pb2.WidgetCommons
    data: CarouselDisplayAdWidget.Data
    def __init__(self, widget_commons: _Optional[_Union[_widget_commons_pb2.WidgetCommons, _Mapping]] = ..., data: _Optional[_Union[CarouselDisplayAdWidget.Data, _Mapping]] = ...) -> None: ...
