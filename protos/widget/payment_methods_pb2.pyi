from base import actions_pb2 as _actions_pb2
from base import template_pb2 as _template_pb2
from base import widget_commons_pb2 as _widget_commons_pb2
from feature.image import image_pb2 as _image_pb2
from feature.payment import payment_gateway_pb2 as _payment_gateway_pb2
from widget import payment_method_cards_pb2 as _payment_method_cards_pb2
from widget import payment_method_net_banking_pb2 as _payment_method_net_banking_pb2
from widget import payment_method_wallets_pb2 as _payment_method_wallets_pb2
from widget import payment_method_quick_pay_pb2 as _payment_method_quick_pay_pb2
from widget import payment_method_upi_pb2 as _payment_method_upi_pb2
from widget import text_list_pb2 as _text_list_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PaymentMethodsWidget(_message.Message):
    __slots__ = ("widget_commons", "data")
    class Data(_message.Message):
        __slots__ = ("payment_methods", "selected_method_meta", "footer", "on_success", "on_error", "offer_success_meta", "error_metas", "cancel_payment")
        class PaymentMethod(_message.Message):
            __slots__ = ("method_name", "method_image", "method_features", "method_info", "gateways", "is_expanded", "cards", "wallets", "upi", "net_banking", "quick_pay")
            METHOD_NAME_FIELD_NUMBER: _ClassVar[int]
            METHOD_IMAGE_FIELD_NUMBER: _ClassVar[int]
            METHOD_FEATURES_FIELD_NUMBER: _ClassVar[int]
            METHOD_INFO_FIELD_NUMBER: _ClassVar[int]
            GATEWAYS_FIELD_NUMBER: _ClassVar[int]
            IS_EXPANDED_FIELD_NUMBER: _ClassVar[int]
            CARDS_FIELD_NUMBER: _ClassVar[int]
            WALLETS_FIELD_NUMBER: _ClassVar[int]
            UPI_FIELD_NUMBER: _ClassVar[int]
            NET_BANKING_FIELD_NUMBER: _ClassVar[int]
            QUICK_PAY_FIELD_NUMBER: _ClassVar[int]
            method_name: str
            method_image: _image_pb2.Image
            method_features: _text_list_pb2.TextListWidget
            method_info: _text_list_pb2.TextListWidget
            gateways: _containers.RepeatedCompositeFieldContainer[_payment_gateway_pb2.PaymentGateway]
            is_expanded: bool
            cards: _payment_method_cards_pb2.PaymentMethodCardsWidget
            wallets: _payment_method_wallets_pb2.PaymentMethodWalletsWidget
            upi: _payment_method_upi_pb2.PaymentMethodUpiWidget
            net_banking: _payment_method_net_banking_pb2.PaymentMethodNetBankingWidget
            quick_pay: _payment_method_quick_pay_pb2.PaymentMethodQuickPayWidget
            def __init__(self, method_name: _Optional[str] = ..., method_image: _Optional[_Union[_image_pb2.Image, _Mapping]] = ..., method_features: _Optional[_Union[_text_list_pb2.TextListWidget, _Mapping]] = ..., method_info: _Optional[_Union[_text_list_pb2.TextListWidget, _Mapping]] = ..., gateways: _Optional[_Iterable[_Union[_payment_gateway_pb2.PaymentGateway, _Mapping]]] = ..., is_expanded: bool = ..., cards: _Optional[_Union[_payment_method_cards_pb2.PaymentMethodCardsWidget, _Mapping]] = ..., wallets: _Optional[_Union[_payment_method_wallets_pb2.PaymentMethodWalletsWidget, _Mapping]] = ..., upi: _Optional[_Union[_payment_method_upi_pb2.PaymentMethodUpiWidget, _Mapping]] = ..., net_banking: _Optional[_Union[_payment_method_net_banking_pb2.PaymentMethodNetBankingWidget, _Mapping]] = ..., quick_pay: _Optional[_Union[_payment_method_quick_pay_pb2.PaymentMethodQuickPayWidget, _Mapping]] = ...) -> None: ...
        class SelectedMethodMeta(_message.Message):
            __slots__ = ("title",)
            TITLE_FIELD_NUMBER: _ClassVar[int]
            title: str
            def __init__(self, title: _Optional[str] = ...) -> None: ...
        class Footer(_message.Message):
            __slots__ = ("icon", "text", "sub_text", "details")
            ICON_FIELD_NUMBER: _ClassVar[int]
            TEXT_FIELD_NUMBER: _ClassVar[int]
            SUB_TEXT_FIELD_NUMBER: _ClassVar[int]
            DETAILS_FIELD_NUMBER: _ClassVar[int]
            icon: str
            text: str
            sub_text: str
            details: _containers.RepeatedCompositeFieldContainer[PaymentMethodsWidget.Data.Detail]
            def __init__(self, icon: _Optional[str] = ..., text: _Optional[str] = ..., sub_text: _Optional[str] = ..., details: _Optional[_Iterable[_Union[PaymentMethodsWidget.Data.Detail, _Mapping]]] = ...) -> None: ...
        class PaymentSuccessMeta(_message.Message):
            __slots__ = ("fetch_url", "image", "title", "sub_title", "cta")
            FETCH_URL_FIELD_NUMBER: _ClassVar[int]
            IMAGE_FIELD_NUMBER: _ClassVar[int]
            TITLE_FIELD_NUMBER: _ClassVar[int]
            SUB_TITLE_FIELD_NUMBER: _ClassVar[int]
            CTA_FIELD_NUMBER: _ClassVar[int]
            fetch_url: str
            image: _image_pb2.Image
            title: str
            sub_title: str
            cta: PaymentMethodsWidget.Data.Cta
            def __init__(self, fetch_url: _Optional[str] = ..., image: _Optional[_Union[_image_pb2.Image, _Mapping]] = ..., title: _Optional[str] = ..., sub_title: _Optional[str] = ..., cta: _Optional[_Union[PaymentMethodsWidget.Data.Cta, _Mapping]] = ...) -> None: ...
        class PaymentErrorMeta(_message.Message):
            __slots__ = ("timer_expired", "default_error")
            class TimerExpiry(_message.Message):
                __slots__ = ("image", "title", "sub_title", "primary_cta", "secondary_cta")
                IMAGE_FIELD_NUMBER: _ClassVar[int]
                TITLE_FIELD_NUMBER: _ClassVar[int]
                SUB_TITLE_FIELD_NUMBER: _ClassVar[int]
                PRIMARY_CTA_FIELD_NUMBER: _ClassVar[int]
                SECONDARY_CTA_FIELD_NUMBER: _ClassVar[int]
                image: _image_pb2.Image
                title: str
                sub_title: str
                primary_cta: PaymentMethodsWidget.Data.Cta
                secondary_cta: PaymentMethodsWidget.Data.Cta
                def __init__(self, image: _Optional[_Union[_image_pb2.Image, _Mapping]] = ..., title: _Optional[str] = ..., sub_title: _Optional[str] = ..., primary_cta: _Optional[_Union[PaymentMethodsWidget.Data.Cta, _Mapping]] = ..., secondary_cta: _Optional[_Union[PaymentMethodsWidget.Data.Cta, _Mapping]] = ...) -> None: ...
            class DefaultError(_message.Message):
                __slots__ = ("image", "title", "sub_titles", "primary_cta", "secondary_cta")
                IMAGE_FIELD_NUMBER: _ClassVar[int]
                TITLE_FIELD_NUMBER: _ClassVar[int]
                SUB_TITLES_FIELD_NUMBER: _ClassVar[int]
                PRIMARY_CTA_FIELD_NUMBER: _ClassVar[int]
                SECONDARY_CTA_FIELD_NUMBER: _ClassVar[int]
                image: _image_pb2.Image
                title: str
                sub_titles: _containers.RepeatedScalarFieldContainer[str]
                primary_cta: PaymentMethodsWidget.Data.Cta
                secondary_cta: PaymentMethodsWidget.Data.Cta
                def __init__(self, image: _Optional[_Union[_image_pb2.Image, _Mapping]] = ..., title: _Optional[str] = ..., sub_titles: _Optional[_Iterable[str]] = ..., primary_cta: _Optional[_Union[PaymentMethodsWidget.Data.Cta, _Mapping]] = ..., secondary_cta: _Optional[_Union[PaymentMethodsWidget.Data.Cta, _Mapping]] = ...) -> None: ...
            TIMER_EXPIRED_FIELD_NUMBER: _ClassVar[int]
            DEFAULT_ERROR_FIELD_NUMBER: _ClassVar[int]
            timer_expired: PaymentMethodsWidget.Data.PaymentErrorMeta.TimerExpiry
            default_error: PaymentMethodsWidget.Data.PaymentErrorMeta.DefaultError
            def __init__(self, timer_expired: _Optional[_Union[PaymentMethodsWidget.Data.PaymentErrorMeta.TimerExpiry, _Mapping]] = ..., default_error: _Optional[_Union[PaymentMethodsWidget.Data.PaymentErrorMeta.DefaultError, _Mapping]] = ...) -> None: ...
        class OfferSuccesMeta(_message.Message):
            __slots__ = ("type", "text", "icon")
            TYPE_FIELD_NUMBER: _ClassVar[int]
            TEXT_FIELD_NUMBER: _ClassVar[int]
            ICON_FIELD_NUMBER: _ClassVar[int]
            type: str
            text: str
            icon: str
            def __init__(self, type: _Optional[str] = ..., text: _Optional[str] = ..., icon: _Optional[str] = ...) -> None: ...
        class PaymentCancelMeta(_message.Message):
            __slots__ = ("img", "title", "details", "primary_cta", "secondary_cta", "is_closable")
            IMG_FIELD_NUMBER: _ClassVar[int]
            TITLE_FIELD_NUMBER: _ClassVar[int]
            DETAILS_FIELD_NUMBER: _ClassVar[int]
            PRIMARY_CTA_FIELD_NUMBER: _ClassVar[int]
            SECONDARY_CTA_FIELD_NUMBER: _ClassVar[int]
            IS_CLOSABLE_FIELD_NUMBER: _ClassVar[int]
            img: _image_pb2.Image
            title: str
            details: _containers.RepeatedCompositeFieldContainer[PaymentMethodsWidget.Data.Detail]
            primary_cta: PaymentMethodsWidget.Data.Cta
            secondary_cta: PaymentMethodsWidget.Data.Cta
            is_closable: bool
            def __init__(self, img: _Optional[_Union[_image_pb2.Image, _Mapping]] = ..., title: _Optional[str] = ..., details: _Optional[_Iterable[_Union[PaymentMethodsWidget.Data.Detail, _Mapping]]] = ..., primary_cta: _Optional[_Union[PaymentMethodsWidget.Data.Cta, _Mapping]] = ..., secondary_cta: _Optional[_Union[PaymentMethodsWidget.Data.Cta, _Mapping]] = ..., is_closable: bool = ...) -> None: ...
        class Cta(_message.Message):
            __slots__ = ("text", "icon_name", "action")
            TEXT_FIELD_NUMBER: _ClassVar[int]
            ICON_NAME_FIELD_NUMBER: _ClassVar[int]
            ACTION_FIELD_NUMBER: _ClassVar[int]
            text: str
            icon_name: str
            action: _actions_pb2.Actions
            def __init__(self, text: _Optional[str] = ..., icon_name: _Optional[str] = ..., action: _Optional[_Union[_actions_pb2.Actions, _Mapping]] = ...) -> None: ...
        class Detail(_message.Message):
            __slots__ = ("description", "links")
            DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
            LINKS_FIELD_NUMBER: _ClassVar[int]
            description: str
            links: _containers.RepeatedCompositeFieldContainer[PaymentMethodsWidget.Data.Link]
            def __init__(self, description: _Optional[str] = ..., links: _Optional[_Iterable[_Union[PaymentMethodsWidget.Data.Link, _Mapping]]] = ...) -> None: ...
        class Link(_message.Message):
            __slots__ = ("key", "label", "url")
            KEY_FIELD_NUMBER: _ClassVar[int]
            LABEL_FIELD_NUMBER: _ClassVar[int]
            URL_FIELD_NUMBER: _ClassVar[int]
            key: str
            label: str
            url: str
            def __init__(self, key: _Optional[str] = ..., label: _Optional[str] = ..., url: _Optional[str] = ...) -> None: ...
        PAYMENT_METHODS_FIELD_NUMBER: _ClassVar[int]
        SELECTED_METHOD_META_FIELD_NUMBER: _ClassVar[int]
        FOOTER_FIELD_NUMBER: _ClassVar[int]
        ON_SUCCESS_FIELD_NUMBER: _ClassVar[int]
        ON_ERROR_FIELD_NUMBER: _ClassVar[int]
        OFFER_SUCCESS_META_FIELD_NUMBER: _ClassVar[int]
        ERROR_METAS_FIELD_NUMBER: _ClassVar[int]
        CANCEL_PAYMENT_FIELD_NUMBER: _ClassVar[int]
        payment_methods: _containers.RepeatedCompositeFieldContainer[PaymentMethodsWidget.Data.PaymentMethod]
        selected_method_meta: PaymentMethodsWidget.Data.SelectedMethodMeta
        footer: PaymentMethodsWidget.Data.Footer
        on_success: PaymentMethodsWidget.Data.PaymentSuccessMeta
        on_error: PaymentMethodsWidget.Data.PaymentErrorMeta
        offer_success_meta: _containers.RepeatedCompositeFieldContainer[PaymentMethodsWidget.Data.OfferSuccesMeta]
        error_metas: _containers.RepeatedCompositeFieldContainer[PaymentMethodsWidget.Data.PaymentErrorMeta]
        cancel_payment: PaymentMethodsWidget.Data.PaymentCancelMeta
        def __init__(self, payment_methods: _Optional[_Iterable[_Union[PaymentMethodsWidget.Data.PaymentMethod, _Mapping]]] = ..., selected_method_meta: _Optional[_Union[PaymentMethodsWidget.Data.SelectedMethodMeta, _Mapping]] = ..., footer: _Optional[_Union[PaymentMethodsWidget.Data.Footer, _Mapping]] = ..., on_success: _Optional[_Union[PaymentMethodsWidget.Data.PaymentSuccessMeta, _Mapping]] = ..., on_error: _Optional[_Union[PaymentMethodsWidget.Data.PaymentErrorMeta, _Mapping]] = ..., offer_success_meta: _Optional[_Iterable[_Union[PaymentMethodsWidget.Data.OfferSuccesMeta, _Mapping]]] = ..., error_metas: _Optional[_Iterable[_Union[PaymentMethodsWidget.Data.PaymentErrorMeta, _Mapping]]] = ..., cancel_payment: _Optional[_Union[PaymentMethodsWidget.Data.PaymentCancelMeta, _Mapping]] = ...) -> None: ...
    WIDGET_COMMONS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    widget_commons: _widget_commons_pb2.WidgetCommons
    data: PaymentMethodsWidget.Data
    def __init__(self, widget_commons: _Optional[_Union[_widget_commons_pb2.WidgetCommons, _Mapping]] = ..., data: _Optional[_Union[PaymentMethodsWidget.Data, _Mapping]] = ...) -> None: ...
