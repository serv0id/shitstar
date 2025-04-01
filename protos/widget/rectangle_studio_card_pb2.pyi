from base import template_pb2 as _template_pb2
from base import widget_commons_pb2 as _widget_commons_pb2
from feature.image import image_pb2 as _image_pb2
from base import actions_pb2 as _actions_pb2
from feature.animation import video_animation_pb2 as _video_animation_pb2
from widget import spotlight_info_pb2 as _spotlight_info_pb2
from feature.accessibility import accessibility_pb2 as _accessibility_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class RectangleStudioCardWidget(_message.Message):
    __slots__ = ("template", "widget_commons", "data")
    class Data(_message.Message):
        __slots__ = ("image", "actions", "video_animation", "expanded_content_poster", "spotlight_info", "alt")
        IMAGE_FIELD_NUMBER: _ClassVar[int]
        ACTIONS_FIELD_NUMBER: _ClassVar[int]
        VIDEO_ANIMATION_FIELD_NUMBER: _ClassVar[int]
        EXPANDED_CONTENT_POSTER_FIELD_NUMBER: _ClassVar[int]
        SPOTLIGHT_INFO_FIELD_NUMBER: _ClassVar[int]
        ALT_FIELD_NUMBER: _ClassVar[int]
        image: _image_pb2.Image
        actions: _actions_pb2.Actions
        video_animation: _video_animation_pb2.VideoAnimation
        expanded_content_poster: RectangleStudioCardWidget.ExpandedContentPoster
        spotlight_info: _spotlight_info_pb2.SpotlightInfoWidget
        alt: _accessibility_pb2.Accessibility
        def __init__(self, image: _Optional[_Union[_image_pb2.Image, _Mapping]] = ..., actions: _Optional[_Union[_actions_pb2.Actions, _Mapping]] = ..., video_animation: _Optional[_Union[_video_animation_pb2.VideoAnimation, _Mapping]] = ..., expanded_content_poster: _Optional[_Union[RectangleStudioCardWidget.ExpandedContentPoster, _Mapping]] = ..., spotlight_info: _Optional[_Union[_spotlight_info_pb2.SpotlightInfoWidget, _Mapping]] = ..., alt: _Optional[_Union[_accessibility_pb2.Accessibility, _Mapping]] = ...) -> None: ...
    class ExpandedContentPoster(_message.Message):
        __slots__ = ("image", "video_animation")
        IMAGE_FIELD_NUMBER: _ClassVar[int]
        VIDEO_ANIMATION_FIELD_NUMBER: _ClassVar[int]
        image: _image_pb2.Image
        video_animation: _video_animation_pb2.VideoAnimation
        def __init__(self, image: _Optional[_Union[_image_pb2.Image, _Mapping]] = ..., video_animation: _Optional[_Union[_video_animation_pb2.VideoAnimation, _Mapping]] = ...) -> None: ...
    TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    WIDGET_COMMONS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    template: _template_pb2.Template
    widget_commons: _widget_commons_pb2.WidgetCommons
    data: RectangleStudioCardWidget.Data
    def __init__(self, template: _Optional[_Union[_template_pb2.Template, _Mapping]] = ..., widget_commons: _Optional[_Union[_widget_commons_pb2.WidgetCommons, _Mapping]] = ..., data: _Optional[_Union[RectangleStudioCardWidget.Data, _Mapping]] = ...) -> None: ...
