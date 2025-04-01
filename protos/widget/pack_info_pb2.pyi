from base import template_pb2 as _template_pb2
from base import widget_commons_pb2 as _widget_commons_pb2
from base import actions_pb2 as _actions_pb2
from feature.image import image_pb2 as _image_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PackInfoWidget(_message.Message):
    __slots__ = ("template", "widget_commons", "data")
    class Data(_message.Message):
        __slots__ = ("pack_list", "payment_mode_consent", "filter_data", "partner_info", "pack_unavailable_info", "secondary_cta", "tertiary_cta")
        PACK_LIST_FIELD_NUMBER: _ClassVar[int]
        PAYMENT_MODE_CONSENT_FIELD_NUMBER: _ClassVar[int]
        FILTER_DATA_FIELD_NUMBER: _ClassVar[int]
        PARTNER_INFO_FIELD_NUMBER: _ClassVar[int]
        PACK_UNAVAILABLE_INFO_FIELD_NUMBER: _ClassVar[int]
        SECONDARY_CTA_FIELD_NUMBER: _ClassVar[int]
        TERTIARY_CTA_FIELD_NUMBER: _ClassVar[int]
        pack_list: _containers.RepeatedCompositeFieldContainer[PackInfoWidget.Pack]
        payment_mode_consent: PackInfoWidget.PaymentModeConsent
        filter_data: _containers.RepeatedCompositeFieldContainer[PackInfoWidget.FilterItem]
        partner_info: PackInfoWidget.PartnerInfo
        pack_unavailable_info: str
        secondary_cta: PackInfoWidget.CTA
        tertiary_cta: PackInfoWidget.CTA
        def __init__(self, pack_list: _Optional[_Iterable[_Union[PackInfoWidget.Pack, _Mapping]]] = ..., payment_mode_consent: _Optional[_Union[PackInfoWidget.PaymentModeConsent, _Mapping]] = ..., filter_data: _Optional[_Iterable[_Union[PackInfoWidget.FilterItem, _Mapping]]] = ..., partner_info: _Optional[_Union[PackInfoWidget.PartnerInfo, _Mapping]] = ..., pack_unavailable_info: _Optional[str] = ..., secondary_cta: _Optional[_Union[PackInfoWidget.CTA, _Mapping]] = ..., tertiary_cta: _Optional[_Union[PackInfoWidget.CTA, _Mapping]] = ...) -> None: ...
    class Pack(_message.Message):
        __slots__ = ("is_selected", "title", "sub_title", "label", "offer", "filter_meta", "is_disabled", "actions", "savings_text", "price", "pack_details_text", "subscribe", "upgrade", "continue_watching", "text")
        IS_SELECTED_FIELD_NUMBER: _ClassVar[int]
        TITLE_FIELD_NUMBER: _ClassVar[int]
        SUB_TITLE_FIELD_NUMBER: _ClassVar[int]
        LABEL_FIELD_NUMBER: _ClassVar[int]
        OFFER_FIELD_NUMBER: _ClassVar[int]
        FILTER_META_FIELD_NUMBER: _ClassVar[int]
        IS_DISABLED_FIELD_NUMBER: _ClassVar[int]
        ACTIONS_FIELD_NUMBER: _ClassVar[int]
        SAVINGS_TEXT_FIELD_NUMBER: _ClassVar[int]
        PRICE_FIELD_NUMBER: _ClassVar[int]
        PACK_DETAILS_TEXT_FIELD_NUMBER: _ClassVar[int]
        SUBSCRIBE_FIELD_NUMBER: _ClassVar[int]
        UPGRADE_FIELD_NUMBER: _ClassVar[int]
        CONTINUE_WATCHING_FIELD_NUMBER: _ClassVar[int]
        TEXT_FIELD_NUMBER: _ClassVar[int]
        is_selected: bool
        title: str
        sub_title: str
        label: str
        offer: PackInfoWidget.Offer
        filter_meta: PackInfoWidget.FilterMeta
        is_disabled: bool
        actions: _actions_pb2.Actions
        savings_text: str
        price: PackInfoWidget.Price
        pack_details_text: str
        subscribe: PackInfoWidget.SubscribeInfo
        upgrade: PackInfoWidget.UpgradeInfo
        continue_watching: PackInfoWidget.CWInfo
        text: PackInfoWidget.PurchaseDisclaimer
        def __init__(self, is_selected: bool = ..., title: _Optional[str] = ..., sub_title: _Optional[str] = ..., label: _Optional[str] = ..., offer: _Optional[_Union[PackInfoWidget.Offer, _Mapping]] = ..., filter_meta: _Optional[_Union[PackInfoWidget.FilterMeta, _Mapping]] = ..., is_disabled: bool = ..., actions: _Optional[_Union[_actions_pb2.Actions, _Mapping]] = ..., savings_text: _Optional[str] = ..., price: _Optional[_Union[PackInfoWidget.Price, _Mapping]] = ..., pack_details_text: _Optional[str] = ..., subscribe: _Optional[_Union[PackInfoWidget.SubscribeInfo, _Mapping]] = ..., upgrade: _Optional[_Union[PackInfoWidget.UpgradeInfo, _Mapping]] = ..., continue_watching: _Optional[_Union[PackInfoWidget.CWInfo, _Mapping]] = ..., text: _Optional[_Union[PackInfoWidget.PurchaseDisclaimer, _Mapping]] = ...) -> None: ...
    class FilterMeta(_message.Message):
        __slots__ = ("filter_key", "identifier")
        FILTER_KEY_FIELD_NUMBER: _ClassVar[int]
        IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
        filter_key: str
        identifier: str
        def __init__(self, filter_key: _Optional[str] = ..., identifier: _Optional[str] = ...) -> None: ...
    class FilterItem(_message.Message):
        __slots__ = ("is_selected", "title", "filter_meta", "actions", "offer_lottie")
        IS_SELECTED_FIELD_NUMBER: _ClassVar[int]
        TITLE_FIELD_NUMBER: _ClassVar[int]
        FILTER_META_FIELD_NUMBER: _ClassVar[int]
        ACTIONS_FIELD_NUMBER: _ClassVar[int]
        OFFER_LOTTIE_FIELD_NUMBER: _ClassVar[int]
        is_selected: bool
        title: str
        filter_meta: PackInfoWidget.FilterMeta
        actions: _actions_pb2.Actions
        offer_lottie: _image_pb2.Image
        def __init__(self, is_selected: bool = ..., title: _Optional[str] = ..., filter_meta: _Optional[_Union[PackInfoWidget.FilterMeta, _Mapping]] = ..., actions: _Optional[_Union[_actions_pb2.Actions, _Mapping]] = ..., offer_lottie: _Optional[_Union[_image_pb2.Image, _Mapping]] = ...) -> None: ...
    class PaymentModeConsent(_message.Message):
        __slots__ = ("paytm", "iap_upgrade")
        PAYTM_FIELD_NUMBER: _ClassVar[int]
        IAP_UPGRADE_FIELD_NUMBER: _ClassVar[int]
        paytm: PackInfoWidget.PaytmMode
        iap_upgrade: PackInfoWidget.IAPUpgradeMode
        def __init__(self, paytm: _Optional[_Union[PackInfoWidget.PaytmMode, _Mapping]] = ..., iap_upgrade: _Optional[_Union[PackInfoWidget.IAPUpgradeMode, _Mapping]] = ...) -> None: ...
    class PaytmMode(_message.Message):
        __slots__ = ("value",)
        VALUE_FIELD_NUMBER: _ClassVar[int]
        value: str
        def __init__(self, value: _Optional[str] = ...) -> None: ...
    class IAPUpgradeMode(_message.Message):
        __slots__ = ("value",)
        VALUE_FIELD_NUMBER: _ClassVar[int]
        value: str
        def __init__(self, value: _Optional[str] = ...) -> None: ...
    class Price(_message.Message):
        __slots__ = ("amount", "currency", "interval")
        AMOUNT_FIELD_NUMBER: _ClassVar[int]
        CURRENCY_FIELD_NUMBER: _ClassVar[int]
        INTERVAL_FIELD_NUMBER: _ClassVar[int]
        amount: str
        currency: str
        interval: str
        def __init__(self, amount: _Optional[str] = ..., currency: _Optional[str] = ..., interval: _Optional[str] = ...) -> None: ...
    class Offer(_message.Message):
        __slots__ = ("strike_through_text", "info")
        STRIKE_THROUGH_TEXT_FIELD_NUMBER: _ClassVar[int]
        INFO_FIELD_NUMBER: _ClassVar[int]
        strike_through_text: str
        info: str
        def __init__(self, strike_through_text: _Optional[str] = ..., info: _Optional[str] = ...) -> None: ...
    class SubscribeInfo(_message.Message):
        __slots__ = ("cta", "actions")
        CTA_FIELD_NUMBER: _ClassVar[int]
        ACTIONS_FIELD_NUMBER: _ClassVar[int]
        cta: str
        actions: _actions_pb2.Actions
        def __init__(self, cta: _Optional[str] = ..., actions: _Optional[_Union[_actions_pb2.Actions, _Mapping]] = ...) -> None: ...
    class UpgradeInfo(_message.Message):
        __slots__ = ("cta", "deduction", "deduction_details", "actions")
        CTA_FIELD_NUMBER: _ClassVar[int]
        DEDUCTION_FIELD_NUMBER: _ClassVar[int]
        DEDUCTION_DETAILS_FIELD_NUMBER: _ClassVar[int]
        ACTIONS_FIELD_NUMBER: _ClassVar[int]
        cta: str
        deduction: PackInfoWidget.PriceDeduction
        deduction_details: _containers.RepeatedCompositeFieldContainer[PackInfoWidget.DeductionDetail]
        actions: _actions_pb2.Actions
        def __init__(self, cta: _Optional[str] = ..., deduction: _Optional[_Union[PackInfoWidget.PriceDeduction, _Mapping]] = ..., deduction_details: _Optional[_Iterable[_Union[PackInfoWidget.DeductionDetail, _Mapping]]] = ..., actions: _Optional[_Union[_actions_pb2.Actions, _Mapping]] = ...) -> None: ...
    class PriceDeduction(_message.Message):
        __slots__ = ("label", "currency", "new_price", "old_price")
        LABEL_FIELD_NUMBER: _ClassVar[int]
        CURRENCY_FIELD_NUMBER: _ClassVar[int]
        NEW_PRICE_FIELD_NUMBER: _ClassVar[int]
        OLD_PRICE_FIELD_NUMBER: _ClassVar[int]
        label: str
        currency: str
        new_price: str
        old_price: str
        def __init__(self, label: _Optional[str] = ..., currency: _Optional[str] = ..., new_price: _Optional[str] = ..., old_price: _Optional[str] = ...) -> None: ...
    class DeductionDetail(_message.Message):
        __slots__ = ("info", "price")
        INFO_FIELD_NUMBER: _ClassVar[int]
        PRICE_FIELD_NUMBER: _ClassVar[int]
        info: str
        price: str
        def __init__(self, info: _Optional[str] = ..., price: _Optional[str] = ...) -> None: ...
    class CWInfo(_message.Message):
        __slots__ = ("cta", "actions")
        CTA_FIELD_NUMBER: _ClassVar[int]
        ACTIONS_FIELD_NUMBER: _ClassVar[int]
        cta: str
        actions: _actions_pb2.Actions
        def __init__(self, cta: _Optional[str] = ..., actions: _Optional[_Union[_actions_pb2.Actions, _Mapping]] = ...) -> None: ...
    class PurchaseDisclaimer(_message.Message):
        __slots__ = ("text_message",)
        TEXT_MESSAGE_FIELD_NUMBER: _ClassVar[int]
        text_message: str
        def __init__(self, text_message: _Optional[str] = ...) -> None: ...
    class PartnerInfo(_message.Message):
        __slots__ = ("rich_text", "image")
        RICH_TEXT_FIELD_NUMBER: _ClassVar[int]
        IMAGE_FIELD_NUMBER: _ClassVar[int]
        rich_text: str
        image: _image_pb2.Image
        def __init__(self, rich_text: _Optional[str] = ..., image: _Optional[_Union[_image_pb2.Image, _Mapping]] = ...) -> None: ...
    class CTA(_message.Message):
        __slots__ = ("label", "actions")
        LABEL_FIELD_NUMBER: _ClassVar[int]
        ACTIONS_FIELD_NUMBER: _ClassVar[int]
        label: str
        actions: _actions_pb2.Actions
        def __init__(self, label: _Optional[str] = ..., actions: _Optional[_Union[_actions_pb2.Actions, _Mapping]] = ...) -> None: ...
    TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    WIDGET_COMMONS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    template: _template_pb2.Template
    widget_commons: _widget_commons_pb2.WidgetCommons
    data: PackInfoWidget.Data
    def __init__(self, template: _Optional[_Union[_template_pb2.Template, _Mapping]] = ..., widget_commons: _Optional[_Union[_widget_commons_pb2.WidgetCommons, _Mapping]] = ..., data: _Optional[_Union[PackInfoWidget.Data, _Mapping]] = ...) -> None: ...
