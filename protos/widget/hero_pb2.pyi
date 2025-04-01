from base import widget_commons_pb2 as _widget_commons_pb2
from feature.image import illustration_pb2 as _illustration_pb2
from feature.image import image_pb2 as _image_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class HeroWidget(_message.Message):
    __slots__ = ("widget_commons", "data")
    class WidgetAlignment(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        DEFAULT: _ClassVar[HeroWidget.WidgetAlignment]
        CENTER: _ClassVar[HeroWidget.WidgetAlignment]
        LEFT: _ClassVar[HeroWidget.WidgetAlignment]
    DEFAULT: HeroWidget.WidgetAlignment
    CENTER: HeroWidget.WidgetAlignment
    LEFT: HeroWidget.WidgetAlignment
    class Data(_message.Message):
        __slots__ = ("illustration", "title", "sub_title", "should_animate_content", "over_sheet_lottie_name", "widget_config", "subtitle_color", "bg_image")
        ILLUSTRATION_FIELD_NUMBER: _ClassVar[int]
        TITLE_FIELD_NUMBER: _ClassVar[int]
        SUB_TITLE_FIELD_NUMBER: _ClassVar[int]
        SHOULD_ANIMATE_CONTENT_FIELD_NUMBER: _ClassVar[int]
        OVER_SHEET_LOTTIE_NAME_FIELD_NUMBER: _ClassVar[int]
        WIDGET_CONFIG_FIELD_NUMBER: _ClassVar[int]
        SUBTITLE_COLOR_FIELD_NUMBER: _ClassVar[int]
        BG_IMAGE_FIELD_NUMBER: _ClassVar[int]
        illustration: _illustration_pb2.Illustration
        title: str
        sub_title: str
        should_animate_content: bool
        over_sheet_lottie_name: str
        widget_config: HeroWidget.WidgetConfig
        subtitle_color: str
        bg_image: _image_pb2.Image
        def __init__(self, illustration: _Optional[_Union[_illustration_pb2.Illustration, _Mapping]] = ..., title: _Optional[str] = ..., sub_title: _Optional[str] = ..., should_animate_content: bool = ..., over_sheet_lottie_name: _Optional[str] = ..., widget_config: _Optional[_Union[HeroWidget.WidgetConfig, _Mapping]] = ..., subtitle_color: _Optional[str] = ..., bg_image: _Optional[_Union[_image_pb2.Image, _Mapping]] = ...) -> None: ...
    class WidgetConfig(_message.Message):
        __slots__ = ("widget_alignment",)
        WIDGET_ALIGNMENT_FIELD_NUMBER: _ClassVar[int]
        widget_alignment: HeroWidget.WidgetAlignment
        def __init__(self, widget_alignment: _Optional[_Union[HeroWidget.WidgetAlignment, str]] = ...) -> None: ...
    WIDGET_COMMONS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    widget_commons: _widget_commons_pb2.WidgetCommons
    data: HeroWidget.Data
    def __init__(self, widget_commons: _Optional[_Union[_widget_commons_pb2.WidgetCommons, _Mapping]] = ..., data: _Optional[_Union[HeroWidget.Data, _Mapping]] = ...) -> None: ...
