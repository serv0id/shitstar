from base import widget_commons_pb2 as _widget_commons_pb2
from feature.image import image_pb2 as _image_pb2
from feature.animation import video_animation_pb2 as _video_animation_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class HeroBackdropWidget(_message.Message):
    __slots__ = ("widget_commons", "data")
    class Data(_message.Message):
        __slots__ = ("backdrop_img", "title_cutout", "hero_video", "fallback_backdrop_img")
        BACKDROP_IMG_FIELD_NUMBER: _ClassVar[int]
        TITLE_CUTOUT_FIELD_NUMBER: _ClassVar[int]
        HERO_VIDEO_FIELD_NUMBER: _ClassVar[int]
        FALLBACK_BACKDROP_IMG_FIELD_NUMBER: _ClassVar[int]
        backdrop_img: _image_pb2.Image
        title_cutout: _image_pb2.Image
        hero_video: _video_animation_pb2.VideoAnimation
        fallback_backdrop_img: _image_pb2.Image
        def __init__(self, backdrop_img: _Optional[_Union[_image_pb2.Image, _Mapping]] = ..., title_cutout: _Optional[_Union[_image_pb2.Image, _Mapping]] = ..., hero_video: _Optional[_Union[_video_animation_pb2.VideoAnimation, _Mapping]] = ..., fallback_backdrop_img: _Optional[_Union[_image_pb2.Image, _Mapping]] = ...) -> None: ...
    WIDGET_COMMONS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    widget_commons: _widget_commons_pb2.WidgetCommons
    data: HeroBackdropWidget.Data
    def __init__(self, widget_commons: _Optional[_Union[_widget_commons_pb2.WidgetCommons, _Mapping]] = ..., data: _Optional[_Union[HeroBackdropWidget.Data, _Mapping]] = ...) -> None: ...
