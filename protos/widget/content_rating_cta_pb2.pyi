from base import widget_commons_pb2 as _widget_commons_pb2
from widget import tooltip_action_menu_pb2 as _tooltip_action_menu_pb2
from feature.image import lottie_pb2 as _lottie_pb2
from feature.image import image_pb2 as _image_pb2
from base import actions_pb2 as _actions_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ContentRatingCtaWidget(_message.Message):
    __slots__ = ("widget_commons", "data")
    class CTAType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        DEFAULT: _ClassVar[ContentRatingCtaWidget.CTAType]
        CENTER_VERTICAL: _ClassVar[ContentRatingCtaWidget.CTAType]
        CENTER_HORIZONTAL: _ClassVar[ContentRatingCtaWidget.CTAType]
    DEFAULT: ContentRatingCtaWidget.CTAType
    CENTER_VERTICAL: ContentRatingCtaWidget.CTAType
    CENTER_HORIZONTAL: ContentRatingCtaWidget.CTAType
    class Data(_message.Message):
        __slots__ = ("content_id", "rate_label", "rated_label", "is_rated", "actions", "lottie", "image", "tooltip_action_menu_widget", "cta_type")
        CONTENT_ID_FIELD_NUMBER: _ClassVar[int]
        RATE_LABEL_FIELD_NUMBER: _ClassVar[int]
        RATED_LABEL_FIELD_NUMBER: _ClassVar[int]
        IS_RATED_FIELD_NUMBER: _ClassVar[int]
        ACTIONS_FIELD_NUMBER: _ClassVar[int]
        LOTTIE_FIELD_NUMBER: _ClassVar[int]
        IMAGE_FIELD_NUMBER: _ClassVar[int]
        TOOLTIP_ACTION_MENU_WIDGET_FIELD_NUMBER: _ClassVar[int]
        CTA_TYPE_FIELD_NUMBER: _ClassVar[int]
        content_id: str
        rate_label: str
        rated_label: str
        is_rated: bool
        actions: _actions_pb2.Actions
        lottie: _lottie_pb2.Lottie
        image: _image_pb2.Image
        tooltip_action_menu_widget: _tooltip_action_menu_pb2.TooltipActionMenuWidget
        cta_type: ContentRatingCtaWidget.CTAType
        def __init__(self, content_id: _Optional[str] = ..., rate_label: _Optional[str] = ..., rated_label: _Optional[str] = ..., is_rated: bool = ..., actions: _Optional[_Union[_actions_pb2.Actions, _Mapping]] = ..., lottie: _Optional[_Union[_lottie_pb2.Lottie, _Mapping]] = ..., image: _Optional[_Union[_image_pb2.Image, _Mapping]] = ..., tooltip_action_menu_widget: _Optional[_Union[_tooltip_action_menu_pb2.TooltipActionMenuWidget, _Mapping]] = ..., cta_type: _Optional[_Union[ContentRatingCtaWidget.CTAType, str]] = ...) -> None: ...
    WIDGET_COMMONS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    widget_commons: _widget_commons_pb2.WidgetCommons
    data: ContentRatingCtaWidget.Data
    def __init__(self, widget_commons: _Optional[_Union[_widget_commons_pb2.WidgetCommons, _Mapping]] = ..., data: _Optional[_Union[ContentRatingCtaWidget.Data, _Mapping]] = ...) -> None: ...
