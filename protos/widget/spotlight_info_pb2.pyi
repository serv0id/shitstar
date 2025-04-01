from base import widget_commons_pb2 as _widget_commons_pb2
from widget import spotlight_info_gec_pb2 as _spotlight_info_gec_pb2
from widget import spotlight_info_cw_pb2 as _spotlight_info_cw_pb2
from feature.image import image_pb2 as _image_pb2
from feature.animation import video_animation_pb2 as _video_animation_pb2
from feature.autoplay import autoplay_info_pb2 as _autoplay_info_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SpotlightInfoWidget(_message.Message):
    __slots__ = ("widget_commons", "data")
    class Data(_message.Message):
        __slots__ = ("hero_img", "hero_video", "autoplay_info", "tray_bg_img", "spotlight_info_gec", "spotlight_info_cw")
        HERO_IMG_FIELD_NUMBER: _ClassVar[int]
        HERO_VIDEO_FIELD_NUMBER: _ClassVar[int]
        AUTOPLAY_INFO_FIELD_NUMBER: _ClassVar[int]
        TRAY_BG_IMG_FIELD_NUMBER: _ClassVar[int]
        SPOTLIGHT_INFO_GEC_FIELD_NUMBER: _ClassVar[int]
        SPOTLIGHT_INFO_CW_FIELD_NUMBER: _ClassVar[int]
        hero_img: _image_pb2.Image
        hero_video: _video_animation_pb2.VideoAnimation
        autoplay_info: _autoplay_info_pb2.AutoplayInfo
        tray_bg_img: _image_pb2.Image
        spotlight_info_gec: _spotlight_info_gec_pb2.SpotlightInfoGecWidget
        spotlight_info_cw: _spotlight_info_cw_pb2.SpotlightInfoCwWidget
        def __init__(self, hero_img: _Optional[_Union[_image_pb2.Image, _Mapping]] = ..., hero_video: _Optional[_Union[_video_animation_pb2.VideoAnimation, _Mapping]] = ..., autoplay_info: _Optional[_Union[_autoplay_info_pb2.AutoplayInfo, _Mapping]] = ..., tray_bg_img: _Optional[_Union[_image_pb2.Image, _Mapping]] = ..., spotlight_info_gec: _Optional[_Union[_spotlight_info_gec_pb2.SpotlightInfoGecWidget, _Mapping]] = ..., spotlight_info_cw: _Optional[_Union[_spotlight_info_cw_pb2.SpotlightInfoCwWidget, _Mapping]] = ...) -> None: ...
    WIDGET_COMMONS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    widget_commons: _widget_commons_pb2.WidgetCommons
    data: SpotlightInfoWidget.Data
    def __init__(self, widget_commons: _Optional[_Union[_widget_commons_pb2.WidgetCommons, _Mapping]] = ..., data: _Optional[_Union[SpotlightInfoWidget.Data, _Mapping]] = ...) -> None: ...
