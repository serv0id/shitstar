from base import widget_commons_pb2 as _widget_commons_pb2
from base import actions_pb2 as _actions_pb2
from feature.image import image_pb2 as _image_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class HorizontalMediumContentPosterWidget(_message.Message):
    __slots__ = ("widget_commons", "data")
    class Data(_message.Message):
        __slots__ = ("image", "actions", "live_badge", "content_id")
        IMAGE_FIELD_NUMBER: _ClassVar[int]
        ACTIONS_FIELD_NUMBER: _ClassVar[int]
        LIVE_BADGE_FIELD_NUMBER: _ClassVar[int]
        CONTENT_ID_FIELD_NUMBER: _ClassVar[int]
        image: _image_pb2.Image
        actions: _actions_pb2.Actions
        live_badge: HorizontalMediumContentPosterWidget.LiveBadge
        content_id: str
        def __init__(self, image: _Optional[_Union[_image_pb2.Image, _Mapping]] = ..., actions: _Optional[_Union[_actions_pb2.Actions, _Mapping]] = ..., live_badge: _Optional[_Union[HorizontalMediumContentPosterWidget.LiveBadge, _Mapping]] = ..., content_id: _Optional[str] = ...) -> None: ...
    class LiveBadge(_message.Message):
        __slots__ = ("text_image",)
        TEXT_IMAGE_FIELD_NUMBER: _ClassVar[int]
        text_image: _image_pb2.Image
        def __init__(self, text_image: _Optional[_Union[_image_pb2.Image, _Mapping]] = ...) -> None: ...
    WIDGET_COMMONS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    widget_commons: _widget_commons_pb2.WidgetCommons
    data: HorizontalMediumContentPosterWidget.Data
    def __init__(self, widget_commons: _Optional[_Union[_widget_commons_pb2.WidgetCommons, _Mapping]] = ..., data: _Optional[_Union[HorizontalMediumContentPosterWidget.Data, _Mapping]] = ...) -> None: ...
