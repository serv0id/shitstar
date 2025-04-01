from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PurchaseType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    WEB: _ClassVar[PurchaseType]
    WEB_VIEW: _ClassVar[PurchaseType]
    IAP: _ClassVar[PurchaseType]
WEB: PurchaseType
WEB_VIEW: PurchaseType
IAP: PurchaseType

class PurchaseAction(_message.Message):
    __slots__ = ("purchase_type", "commercial_pack_id", "payment_url", "payment_success_widget_url", "replace_page", "web_view_meta", "promo_code")
    class WebViewMeta(_message.Message):
        __slots__ = ("headers", "cookies", "override_cookies")
        class HeadersEntry(_message.Message):
            __slots__ = ("key", "value")
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: str
            value: str
            def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
        class OverrideCookiesEntry(_message.Message):
            __slots__ = ("key", "value")
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: str
            value: str
            def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
        HEADERS_FIELD_NUMBER: _ClassVar[int]
        COOKIES_FIELD_NUMBER: _ClassVar[int]
        OVERRIDE_COOKIES_FIELD_NUMBER: _ClassVar[int]
        headers: _containers.ScalarMap[str, str]
        cookies: _containers.RepeatedScalarFieldContainer[str]
        override_cookies: _containers.ScalarMap[str, str]
        def __init__(self, headers: _Optional[_Mapping[str, str]] = ..., cookies: _Optional[_Iterable[str]] = ..., override_cookies: _Optional[_Mapping[str, str]] = ...) -> None: ...
    PURCHASE_TYPE_FIELD_NUMBER: _ClassVar[int]
    COMMERCIAL_PACK_ID_FIELD_NUMBER: _ClassVar[int]
    PAYMENT_URL_FIELD_NUMBER: _ClassVar[int]
    PAYMENT_SUCCESS_WIDGET_URL_FIELD_NUMBER: _ClassVar[int]
    REPLACE_PAGE_FIELD_NUMBER: _ClassVar[int]
    WEB_VIEW_META_FIELD_NUMBER: _ClassVar[int]
    PROMO_CODE_FIELD_NUMBER: _ClassVar[int]
    purchase_type: PurchaseType
    commercial_pack_id: str
    payment_url: str
    payment_success_widget_url: str
    replace_page: bool
    web_view_meta: PurchaseAction.WebViewMeta
    promo_code: str
    def __init__(self, purchase_type: _Optional[_Union[PurchaseType, str]] = ..., commercial_pack_id: _Optional[str] = ..., payment_url: _Optional[str] = ..., payment_success_widget_url: _Optional[str] = ..., replace_page: bool = ..., web_view_meta: _Optional[_Union[PurchaseAction.WebViewMeta, _Mapping]] = ..., promo_code: _Optional[str] = ...) -> None: ...
