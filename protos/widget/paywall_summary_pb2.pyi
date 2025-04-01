from base import template_pb2 as _template_pb2
from base import widget_commons_pb2 as _widget_commons_pb2
from feature.image import image_pb2 as _image_pb2
from widget import auto_scroll_gallery_pb2 as _auto_scroll_gallery_pb2
from widget import text_list_pb2 as _text_list_pb2
from widget import offer_pb2 as _offer_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PaywallSummaryWidget(_message.Message):
    __slots__ = ("template", "widget_commons", "data")
    class SubtitleType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        CALLOUT: _ClassVar[PaywallSummaryWidget.SubtitleType]
        ERROR: _ClassVar[PaywallSummaryWidget.SubtitleType]
        HIGHLIGHT: _ClassVar[PaywallSummaryWidget.SubtitleType]
    CALLOUT: PaywallSummaryWidget.SubtitleType
    ERROR: PaywallSummaryWidget.SubtitleType
    HIGHLIGHT: PaywallSummaryWidget.SubtitleType
    class Data(_message.Message):
        __slots__ = ("bg_image_list", "title", "content_image", "sub_title", "usp_list", "usp_list_data", "plan_callouts", "offer")
        BG_IMAGE_LIST_FIELD_NUMBER: _ClassVar[int]
        TITLE_FIELD_NUMBER: _ClassVar[int]
        CONTENT_IMAGE_FIELD_NUMBER: _ClassVar[int]
        SUB_TITLE_FIELD_NUMBER: _ClassVar[int]
        USP_LIST_FIELD_NUMBER: _ClassVar[int]
        USP_LIST_DATA_FIELD_NUMBER: _ClassVar[int]
        PLAN_CALLOUTS_FIELD_NUMBER: _ClassVar[int]
        OFFER_FIELD_NUMBER: _ClassVar[int]
        bg_image_list: _containers.RepeatedCompositeFieldContainer[_image_pb2.Image]
        title: str
        content_image: _image_pb2.Image
        sub_title: _auto_scroll_gallery_pb2.AutoScrollGalleryWidget.Subtitle
        usp_list: _containers.RepeatedCompositeFieldContainer[_text_list_pb2.TextListWidget.Text]
        usp_list_data: _containers.RepeatedCompositeFieldContainer[PaywallSummaryWidget.IconText]
        plan_callouts: _containers.RepeatedCompositeFieldContainer[PaywallSummaryWidget.PlanCallouts]
        offer: _offer_pb2.OfferWidget
        def __init__(self, bg_image_list: _Optional[_Iterable[_Union[_image_pb2.Image, _Mapping]]] = ..., title: _Optional[str] = ..., content_image: _Optional[_Union[_image_pb2.Image, _Mapping]] = ..., sub_title: _Optional[_Union[_auto_scroll_gallery_pb2.AutoScrollGalleryWidget.Subtitle, _Mapping]] = ..., usp_list: _Optional[_Iterable[_Union[_text_list_pb2.TextListWidget.Text, _Mapping]]] = ..., usp_list_data: _Optional[_Iterable[_Union[PaywallSummaryWidget.IconText, _Mapping]]] = ..., plan_callouts: _Optional[_Iterable[_Union[PaywallSummaryWidget.PlanCallouts, _Mapping]]] = ..., offer: _Optional[_Union[_offer_pb2.OfferWidget, _Mapping]] = ...) -> None: ...
    class IconText(_message.Message):
        __slots__ = ("icon_name", "value")
        ICON_NAME_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        icon_name: str
        value: str
        def __init__(self, icon_name: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    class PlanCallouts(_message.Message):
        __slots__ = ("identifier", "callout")
        IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
        CALLOUT_FIELD_NUMBER: _ClassVar[int]
        identifier: _containers.RepeatedScalarFieldContainer[str]
        callout: PaywallSummaryWidget.Subtitle
        def __init__(self, identifier: _Optional[_Iterable[str]] = ..., callout: _Optional[_Union[PaywallSummaryWidget.Subtitle, _Mapping]] = ...) -> None: ...
    class Subtitle(_message.Message):
        __slots__ = ("type", "info_text", "rich_text", "icon_text", "bullet_text")
        class InfoText(_message.Message):
            __slots__ = ("value",)
            VALUE_FIELD_NUMBER: _ClassVar[int]
            value: str
            def __init__(self, value: _Optional[str] = ...) -> None: ...
        class RichText(_message.Message):
            __slots__ = ("value",)
            VALUE_FIELD_NUMBER: _ClassVar[int]
            value: str
            def __init__(self, value: _Optional[str] = ...) -> None: ...
        class IconText(_message.Message):
            __slots__ = ("icon_name", "value")
            ICON_NAME_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            icon_name: str
            value: str
            def __init__(self, icon_name: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
        class BulletText(_message.Message):
            __slots__ = ("value",)
            VALUE_FIELD_NUMBER: _ClassVar[int]
            value: str
            def __init__(self, value: _Optional[str] = ...) -> None: ...
        TYPE_FIELD_NUMBER: _ClassVar[int]
        INFO_TEXT_FIELD_NUMBER: _ClassVar[int]
        RICH_TEXT_FIELD_NUMBER: _ClassVar[int]
        ICON_TEXT_FIELD_NUMBER: _ClassVar[int]
        BULLET_TEXT_FIELD_NUMBER: _ClassVar[int]
        type: PaywallSummaryWidget.SubtitleType
        info_text: PaywallSummaryWidget.Subtitle.InfoText
        rich_text: PaywallSummaryWidget.Subtitle.RichText
        icon_text: PaywallSummaryWidget.Subtitle.IconText
        bullet_text: PaywallSummaryWidget.Subtitle.BulletText
        def __init__(self, type: _Optional[_Union[PaywallSummaryWidget.SubtitleType, str]] = ..., info_text: _Optional[_Union[PaywallSummaryWidget.Subtitle.InfoText, _Mapping]] = ..., rich_text: _Optional[_Union[PaywallSummaryWidget.Subtitle.RichText, _Mapping]] = ..., icon_text: _Optional[_Union[PaywallSummaryWidget.Subtitle.IconText, _Mapping]] = ..., bullet_text: _Optional[_Union[PaywallSummaryWidget.Subtitle.BulletText, _Mapping]] = ...) -> None: ...
    TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    WIDGET_COMMONS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    template: _template_pb2.Template
    widget_commons: _widget_commons_pb2.WidgetCommons
    data: PaywallSummaryWidget.Data
    def __init__(self, template: _Optional[_Union[_template_pb2.Template, _Mapping]] = ..., widget_commons: _Optional[_Union[_widget_commons_pb2.WidgetCommons, _Mapping]] = ..., data: _Optional[_Union[PaywallSummaryWidget.Data, _Mapping]] = ...) -> None: ...
