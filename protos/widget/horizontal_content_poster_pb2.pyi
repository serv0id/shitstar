from base import widget_commons_pb2 as _widget_commons_pb2
from base import actions_pb2 as _actions_pb2
from feature.image import image_pb2 as _image_pb2
from widget import spotlight_info_pb2 as _spotlight_info_pb2
from feature.accessibility import accessibility_pb2 as _accessibility_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class HorizontalContentPosterWidget(_message.Message):
    __slots__ = ("widget_commons", "data")
    class Data(_message.Message):
        __slots__ = ("image", "actions", "spotlight_info", "live_badge", "alt", "content_id")
        IMAGE_FIELD_NUMBER: _ClassVar[int]
        ACTIONS_FIELD_NUMBER: _ClassVar[int]
        SPOTLIGHT_INFO_FIELD_NUMBER: _ClassVar[int]
        LIVE_BADGE_FIELD_NUMBER: _ClassVar[int]
        ALT_FIELD_NUMBER: _ClassVar[int]
        CONTENT_ID_FIELD_NUMBER: _ClassVar[int]
        image: _image_pb2.Image
        actions: _actions_pb2.Actions
        spotlight_info: _spotlight_info_pb2.SpotlightInfoWidget
        live_badge: HorizontalContentPosterWidget.LiveBadge
        alt: _accessibility_pb2.Accessibility
        content_id: str
        def __init__(self, image: _Optional[_Union[_image_pb2.Image, _Mapping]] = ..., actions: _Optional[_Union[_actions_pb2.Actions, _Mapping]] = ..., spotlight_info: _Optional[_Union[_spotlight_info_pb2.SpotlightInfoWidget, _Mapping]] = ..., live_badge: _Optional[_Union[HorizontalContentPosterWidget.LiveBadge, _Mapping]] = ..., alt: _Optional[_Union[_accessibility_pb2.Accessibility, _Mapping]] = ..., content_id: _Optional[str] = ...) -> None: ...
    class LiveBadge(_message.Message):
        __slots__ = ("text_image",)
        TEXT_IMAGE_FIELD_NUMBER: _ClassVar[int]
        text_image: _image_pb2.Image
        def __init__(self, text_image: _Optional[_Union[_image_pb2.Image, _Mapping]] = ...) -> None: ...
    WIDGET_COMMONS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    widget_commons: _widget_commons_pb2.WidgetCommons
    data: HorizontalContentPosterWidget.Data
    def __init__(self, widget_commons: _Optional[_Union[_widget_commons_pb2.WidgetCommons, _Mapping]] = ..., data: _Optional[_Union[HorizontalContentPosterWidget.Data, _Mapping]] = ...) -> None: ...
