from base import template_pb2 as _template_pb2
from base import widget_commons_pb2 as _widget_commons_pb2
from base import actions_pb2 as _actions_pb2
from feature.image import image_pb2 as _image_pb2
from feature.image import screen_size_image_pb2 as _screen_size_image_pb2
from feature.trackers import url_trackers_pb2 as _url_trackers_pb2
from feature.image import illustration_pb2 as _illustration_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FeedHeaderWidget(_message.Message):
    __slots__ = ("base_header", "ads_header")
    BASE_HEADER_FIELD_NUMBER: _ClassVar[int]
    ADS_HEADER_FIELD_NUMBER: _ClassVar[int]
    base_header: BaseFeedHeaderWidget
    ads_header: AdsFeedHeaderWidget
    def __init__(self, base_header: _Optional[_Union[BaseFeedHeaderWidget, _Mapping]] = ..., ads_header: _Optional[_Union[AdsFeedHeaderWidget, _Mapping]] = ...) -> None: ...

class BaseFeedHeaderWidget(_message.Message):
    __slots__ = ("widget_commons", "data")
    class HeaderType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        BASE: _ClassVar[BaseFeedHeaderWidget.HeaderType]
        HIGHLIGHT_BLUE: _ClassVar[BaseFeedHeaderWidget.HeaderType]
        HIGHLIGHT_GOLD: _ClassVar[BaseFeedHeaderWidget.HeaderType]
    BASE: BaseFeedHeaderWidget.HeaderType
    HIGHLIGHT_BLUE: BaseFeedHeaderWidget.HeaderType
    HIGHLIGHT_GOLD: BaseFeedHeaderWidget.HeaderType
    class Data(_message.Message):
        __slots__ = ("title", "description", "type", "icon", "actions")
        TITLE_FIELD_NUMBER: _ClassVar[int]
        DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
        TYPE_FIELD_NUMBER: _ClassVar[int]
        ICON_FIELD_NUMBER: _ClassVar[int]
        ACTIONS_FIELD_NUMBER: _ClassVar[int]
        title: str
        description: str
        type: BaseFeedHeaderWidget.HeaderType
        icon: _illustration_pb2.Illustration
        actions: _actions_pb2.Actions
        def __init__(self, title: _Optional[str] = ..., description: _Optional[str] = ..., type: _Optional[_Union[BaseFeedHeaderWidget.HeaderType, str]] = ..., icon: _Optional[_Union[_illustration_pb2.Illustration, _Mapping]] = ..., actions: _Optional[_Union[_actions_pb2.Actions, _Mapping]] = ...) -> None: ...
    WIDGET_COMMONS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    widget_commons: _widget_commons_pb2.WidgetCommons
    data: BaseFeedHeaderWidget.Data
    def __init__(self, widget_commons: _Optional[_Union[_widget_commons_pb2.WidgetCommons, _Mapping]] = ..., data: _Optional[_Union[BaseFeedHeaderWidget.Data, _Mapping]] = ...) -> None: ...

class AdsFeedHeaderWidget(_message.Message):
    __slots__ = ("widget_commons", "data")
    class Data(_message.Message):
        __slots__ = ("image", "ad_type", "title", "description", "button", "badge", "creative_image", "tracker", "actions")
        class Button(_message.Message):
            __slots__ = ("text", "desc", "actions")
            TEXT_FIELD_NUMBER: _ClassVar[int]
            DESC_FIELD_NUMBER: _ClassVar[int]
            ACTIONS_FIELD_NUMBER: _ClassVar[int]
            text: str
            desc: str
            actions: _actions_pb2.Actions
            def __init__(self, text: _Optional[str] = ..., desc: _Optional[str] = ..., actions: _Optional[_Union[_actions_pb2.Actions, _Mapping]] = ...) -> None: ...
        IMAGE_FIELD_NUMBER: _ClassVar[int]
        AD_TYPE_FIELD_NUMBER: _ClassVar[int]
        TITLE_FIELD_NUMBER: _ClassVar[int]
        DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
        BUTTON_FIELD_NUMBER: _ClassVar[int]
        BADGE_FIELD_NUMBER: _ClassVar[int]
        CREATIVE_IMAGE_FIELD_NUMBER: _ClassVar[int]
        TRACKER_FIELD_NUMBER: _ClassVar[int]
        ACTIONS_FIELD_NUMBER: _ClassVar[int]
        image: _image_pb2.Image
        ad_type: int
        title: str
        description: str
        button: AdsFeedHeaderWidget.Data.Button
        badge: AdsFeedHeaderWidget.Badge
        creative_image: _screen_size_image_pb2.ScreenSizeImage
        tracker: _url_trackers_pb2.UrlTrackers
        actions: _actions_pb2.Actions
        def __init__(self, image: _Optional[_Union[_image_pb2.Image, _Mapping]] = ..., ad_type: _Optional[int] = ..., title: _Optional[str] = ..., description: _Optional[str] = ..., button: _Optional[_Union[AdsFeedHeaderWidget.Data.Button, _Mapping]] = ..., badge: _Optional[_Union[AdsFeedHeaderWidget.Badge, _Mapping]] = ..., creative_image: _Optional[_Union[_screen_size_image_pb2.ScreenSizeImage, _Mapping]] = ..., tracker: _Optional[_Union[_url_trackers_pb2.UrlTrackers, _Mapping]] = ..., actions: _Optional[_Union[_actions_pb2.Actions, _Mapping]] = ...) -> None: ...
    class Badge(_message.Message):
        __slots__ = ("label", "desc")
        LABEL_FIELD_NUMBER: _ClassVar[int]
        DESC_FIELD_NUMBER: _ClassVar[int]
        label: str
        desc: str
        def __init__(self, label: _Optional[str] = ..., desc: _Optional[str] = ...) -> None: ...
    WIDGET_COMMONS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    widget_commons: _widget_commons_pb2.WidgetCommons
    data: AdsFeedHeaderWidget.Data
    def __init__(self, widget_commons: _Optional[_Union[_widget_commons_pb2.WidgetCommons, _Mapping]] = ..., data: _Optional[_Union[AdsFeedHeaderWidget.Data, _Mapping]] = ...) -> None: ...
