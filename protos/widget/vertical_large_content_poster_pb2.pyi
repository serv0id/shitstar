from base import template_pb2 as _template_pb2
from base import widget_commons_pb2 as _widget_commons_pb2
from base import actions_pb2 as _actions_pb2
from feature.image import image_pb2 as _image_pb2
from feature.accessibility import accessibility_pb2 as _accessibility_pb2
from feature.autoplay import autoplay_info_pb2 as _autoplay_info_pb2
from feature.content_language_preference import content_language_preference_pb2 as _content_language_preference_pb2
from feature.language import language_pb2 as _language_pb2
from feature.remind_me import remind_me_info_pb2 as _remind_me_info_pb2
from feature.watchlist import watchlist_info_pb2 as _watchlist_info_pb2
from widget import expanded_content_poster_pb2 as _expanded_content_poster_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class VerticalLargeContentPosterWidget(_message.Message):
    __slots__ = ("template", "widget_commons", "data")
    class Data(_message.Message):
        __slots__ = ("image", "actions", "expanded_content_poster", "live_badge", "alt", "content_id")
        IMAGE_FIELD_NUMBER: _ClassVar[int]
        ACTIONS_FIELD_NUMBER: _ClassVar[int]
        EXPANDED_CONTENT_POSTER_FIELD_NUMBER: _ClassVar[int]
        LIVE_BADGE_FIELD_NUMBER: _ClassVar[int]
        ALT_FIELD_NUMBER: _ClassVar[int]
        CONTENT_ID_FIELD_NUMBER: _ClassVar[int]
        image: _image_pb2.Image
        actions: _actions_pb2.Actions
        expanded_content_poster: _expanded_content_poster_pb2.ExpandedContentPosterWidget
        live_badge: VerticalLargeContentPosterWidget.LiveBadge
        alt: _accessibility_pb2.Accessibility
        content_id: str
        def __init__(self, image: _Optional[_Union[_image_pb2.Image, _Mapping]] = ..., actions: _Optional[_Union[_actions_pb2.Actions, _Mapping]] = ..., expanded_content_poster: _Optional[_Union[_expanded_content_poster_pb2.ExpandedContentPosterWidget, _Mapping]] = ..., live_badge: _Optional[_Union[VerticalLargeContentPosterWidget.LiveBadge, _Mapping]] = ..., alt: _Optional[_Union[_accessibility_pb2.Accessibility, _Mapping]] = ..., content_id: _Optional[str] = ...) -> None: ...
    class LiveBadge(_message.Message):
        __slots__ = ("text_image",)
        TEXT_IMAGE_FIELD_NUMBER: _ClassVar[int]
        text_image: _image_pb2.Image
        def __init__(self, text_image: _Optional[_Union[_image_pb2.Image, _Mapping]] = ...) -> None: ...
    TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    WIDGET_COMMONS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    template: _template_pb2.Template
    widget_commons: _widget_commons_pb2.WidgetCommons
    data: VerticalLargeContentPosterWidget.Data
    def __init__(self, template: _Optional[_Union[_template_pb2.Template, _Mapping]] = ..., widget_commons: _Optional[_Union[_widget_commons_pb2.WidgetCommons, _Mapping]] = ..., data: _Optional[_Union[VerticalLargeContentPosterWidget.Data, _Mapping]] = ...) -> None: ...
