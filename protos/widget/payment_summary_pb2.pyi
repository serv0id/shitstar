from base import template_pb2 as _template_pb2
from base import widget_commons_pb2 as _widget_commons_pb2
from feature.image import image_pb2 as _image_pb2
from feature.branding import brand_pb2 as _brand_pb2
from widget import text_list_pb2 as _text_list_pb2
from widget import divider_pb2 as _divider_pb2
from feature.tag import tag_pb2 as _tag_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PaymentSummaryWidget(_message.Message):
    __slots__ = ("widget_commons", "data")
    class OfferStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ACTIVE: _ClassVar[PaymentSummaryWidget.OfferStatus]
        EXPIRED: _ClassVar[PaymentSummaryWidget.OfferStatus]
    ACTIVE: PaymentSummaryWidget.OfferStatus
    EXPIRED: PaymentSummaryWidget.OfferStatus
    class WidgetType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[PaymentSummaryWidget.WidgetType]
        TEXT_LIST: _ClassVar[PaymentSummaryWidget.WidgetType]
        DIVIDER: _ClassVar[PaymentSummaryWidget.WidgetType]
        TAGS: _ClassVar[PaymentSummaryWidget.WidgetType]
    UNSPECIFIED: PaymentSummaryWidget.WidgetType
    TEXT_LIST: PaymentSummaryWidget.WidgetType
    DIVIDER: PaymentSummaryWidget.WidgetType
    TAGS: PaymentSummaryWidget.WidgetType
    class Data(_message.Message):
        __slots__ = ("bg_image_list", "logo", "title_desc", "price_deduction", "offer", "text_list", "widget_wrapper")
        BG_IMAGE_LIST_FIELD_NUMBER: _ClassVar[int]
        LOGO_FIELD_NUMBER: _ClassVar[int]
        TITLE_DESC_FIELD_NUMBER: _ClassVar[int]
        PRICE_DEDUCTION_FIELD_NUMBER: _ClassVar[int]
        OFFER_FIELD_NUMBER: _ClassVar[int]
        TEXT_LIST_FIELD_NUMBER: _ClassVar[int]
        WIDGET_WRAPPER_FIELD_NUMBER: _ClassVar[int]
        bg_image_list: _containers.RepeatedCompositeFieldContainer[_image_pb2.Image]
        logo: _brand_pb2.Brand
        title_desc: PaymentSummaryWidget.PlanTitles
        price_deduction: PaymentSummaryWidget.PriceDeduction
        offer: PaymentSummaryWidget.OfferDetails
        text_list: _containers.RepeatedCompositeFieldContainer[PaymentSummaryWidget.TextList]
        widget_wrapper: _containers.RepeatedCompositeFieldContainer[PaymentSummaryWidget.WidgetWrapper]
        def __init__(self, bg_image_list: _Optional[_Iterable[_Union[_image_pb2.Image, _Mapping]]] = ..., logo: _Optional[_Union[_brand_pb2.Brand, str]] = ..., title_desc: _Optional[_Union[PaymentSummaryWidget.PlanTitles, _Mapping]] = ..., price_deduction: _Optional[_Union[PaymentSummaryWidget.PriceDeduction, _Mapping]] = ..., offer: _Optional[_Union[PaymentSummaryWidget.OfferDetails, _Mapping]] = ..., text_list: _Optional[_Iterable[_Union[PaymentSummaryWidget.TextList, _Mapping]]] = ..., widget_wrapper: _Optional[_Iterable[_Union[PaymentSummaryWidget.WidgetWrapper, _Mapping]]] = ...) -> None: ...
    class WidgetWrapper(_message.Message):
        __slots__ = ("widget_type", "text_list_elements", "divider", "tags")
        WIDGET_TYPE_FIELD_NUMBER: _ClassVar[int]
        TEXT_LIST_ELEMENTS_FIELD_NUMBER: _ClassVar[int]
        DIVIDER_FIELD_NUMBER: _ClassVar[int]
        TAGS_FIELD_NUMBER: _ClassVar[int]
        widget_type: PaymentSummaryWidget.WidgetType
        text_list_elements: _text_list_pb2.TextListWidget
        divider: _divider_pb2.DividerWidget
        tags: PaymentSummaryWidget.Tags
        def __init__(self, widget_type: _Optional[_Union[PaymentSummaryWidget.WidgetType, str]] = ..., text_list_elements: _Optional[_Union[_text_list_pb2.TextListWidget, _Mapping]] = ..., divider: _Optional[_Union[_divider_pb2.DividerWidget, _Mapping]] = ..., tags: _Optional[_Union[PaymentSummaryWidget.Tags, _Mapping]] = ...) -> None: ...
    class PlanTitles(_message.Message):
        __slots__ = ("title", "addon_title", "sub_title", "tags")
        TITLE_FIELD_NUMBER: _ClassVar[int]
        ADDON_TITLE_FIELD_NUMBER: _ClassVar[int]
        SUB_TITLE_FIELD_NUMBER: _ClassVar[int]
        TAGS_FIELD_NUMBER: _ClassVar[int]
        title: str
        addon_title: str
        sub_title: str
        tags: PaymentSummaryWidget.Tags
        def __init__(self, title: _Optional[str] = ..., addon_title: _Optional[str] = ..., sub_title: _Optional[str] = ..., tags: _Optional[_Union[PaymentSummaryWidget.Tags, _Mapping]] = ...) -> None: ...
    class PriceDeduction(_message.Message):
        __slots__ = ("new_price", "old_price", "deduction_details")
        NEW_PRICE_FIELD_NUMBER: _ClassVar[int]
        OLD_PRICE_FIELD_NUMBER: _ClassVar[int]
        DEDUCTION_DETAILS_FIELD_NUMBER: _ClassVar[int]
        new_price: str
        old_price: str
        deduction_details: _containers.RepeatedCompositeFieldContainer[PaymentSummaryWidget.DeductionDetail]
        def __init__(self, new_price: _Optional[str] = ..., old_price: _Optional[str] = ..., deduction_details: _Optional[_Iterable[_Union[PaymentSummaryWidget.DeductionDetail, _Mapping]]] = ...) -> None: ...
    class DeductionDetail(_message.Message):
        __slots__ = ("info", "price")
        INFO_FIELD_NUMBER: _ClassVar[int]
        PRICE_FIELD_NUMBER: _ClassVar[int]
        info: str
        price: str
        def __init__(self, info: _Optional[str] = ..., price: _Optional[str] = ...) -> None: ...
    class OfferDetails(_message.Message):
        __slots__ = ("offer_icon", "offer_status", "offer_text")
        OFFER_ICON_FIELD_NUMBER: _ClassVar[int]
        OFFER_STATUS_FIELD_NUMBER: _ClassVar[int]
        OFFER_TEXT_FIELD_NUMBER: _ClassVar[int]
        offer_icon: str
        offer_status: PaymentSummaryWidget.OfferStatus
        offer_text: str
        def __init__(self, offer_icon: _Optional[str] = ..., offer_status: _Optional[_Union[PaymentSummaryWidget.OfferStatus, str]] = ..., offer_text: _Optional[str] = ...) -> None: ...
    class TextList(_message.Message):
        __slots__ = ("icon", "text")
        ICON_FIELD_NUMBER: _ClassVar[int]
        TEXT_FIELD_NUMBER: _ClassVar[int]
        icon: str
        text: str
        def __init__(self, icon: _Optional[str] = ..., text: _Optional[str] = ...) -> None: ...
    class Tags(_message.Message):
        __slots__ = ("tags",)
        TAGS_FIELD_NUMBER: _ClassVar[int]
        tags: _containers.RepeatedCompositeFieldContainer[_tag_pb2.Tag]
        def __init__(self, tags: _Optional[_Iterable[_Union[_tag_pb2.Tag, _Mapping]]] = ...) -> None: ...
    WIDGET_COMMONS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    widget_commons: _widget_commons_pb2.WidgetCommons
    data: PaymentSummaryWidget.Data
    def __init__(self, widget_commons: _Optional[_Union[_widget_commons_pb2.WidgetCommons, _Mapping]] = ..., data: _Optional[_Union[PaymentSummaryWidget.Data, _Mapping]] = ...) -> None: ...
