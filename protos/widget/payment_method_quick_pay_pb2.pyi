from base import widget_commons_pb2 as _widget_commons_pb2
from widget import payment_method_commons_pb2 as _payment_method_commons_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PaymentMethodQuickPayWidget(_message.Message):
    __slots__ = ("widget_commons", "quick_pay_arr", "payment_method_meta")
    class QuickPay(_message.Message):
        __slots__ = ("paytm_quick_pay",)
        PAYTM_QUICK_PAY_FIELD_NUMBER: _ClassVar[int]
        paytm_quick_pay: PaymentMethodQuickPayWidget.PaytmQuickPay
        def __init__(self, paytm_quick_pay: _Optional[_Union[PaymentMethodQuickPayWidget.PaytmQuickPay, _Mapping]] = ...) -> None: ...
    class PaytmQuickPay(_message.Message):
        __slots__ = ("vendorName", "phoneNumber", "walletBalance", "cta", "isBalanceSufficiecnt")
        VENDORNAME_FIELD_NUMBER: _ClassVar[int]
        PHONENUMBER_FIELD_NUMBER: _ClassVar[int]
        WALLETBALANCE_FIELD_NUMBER: _ClassVar[int]
        CTA_FIELD_NUMBER: _ClassVar[int]
        ISBALANCESUFFICIECNT_FIELD_NUMBER: _ClassVar[int]
        vendorName: str
        phoneNumber: str
        walletBalance: str
        cta: str
        isBalanceSufficiecnt: bool
        def __init__(self, vendorName: _Optional[str] = ..., phoneNumber: _Optional[str] = ..., walletBalance: _Optional[str] = ..., cta: _Optional[str] = ..., isBalanceSufficiecnt: bool = ...) -> None: ...
    WIDGET_COMMONS_FIELD_NUMBER: _ClassVar[int]
    QUICK_PAY_ARR_FIELD_NUMBER: _ClassVar[int]
    PAYMENT_METHOD_META_FIELD_NUMBER: _ClassVar[int]
    widget_commons: _widget_commons_pb2.WidgetCommons
    quick_pay_arr: _containers.RepeatedCompositeFieldContainer[PaymentMethodQuickPayWidget.QuickPay]
    payment_method_meta: _payment_method_commons_pb2.PaymentMethodCommonsWidget
    def __init__(self, widget_commons: _Optional[_Union[_widget_commons_pb2.WidgetCommons, _Mapping]] = ..., quick_pay_arr: _Optional[_Iterable[_Union[PaymentMethodQuickPayWidget.QuickPay, _Mapping]]] = ..., payment_method_meta: _Optional[_Union[_payment_method_commons_pb2.PaymentMethodCommonsWidget, _Mapping]] = ...) -> None: ...
