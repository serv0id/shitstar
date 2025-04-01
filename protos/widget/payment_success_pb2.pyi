from base import actions_pb2 as _actions_pb2
from base import widget_commons_pb2 as _widget_commons_pb2
from feature.branding import brand_pb2 as _brand_pb2
from feature.image import illustration_pb2 as _illustration_pb2
from feature.quiz import title_icon_combo_pb2 as _title_icon_combo_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PaymentSuccessWidget(_message.Message):
    __slots__ = ("widget_commons", "data")
    class Data(_message.Message):
        __slots__ = ("logo", "title", "sub_title", "sw_info", "is_plan_active", "illustration", "offers_info")
        LOGO_FIELD_NUMBER: _ClassVar[int]
        TITLE_FIELD_NUMBER: _ClassVar[int]
        SUB_TITLE_FIELD_NUMBER: _ClassVar[int]
        SW_INFO_FIELD_NUMBER: _ClassVar[int]
        IS_PLAN_ACTIVE_FIELD_NUMBER: _ClassVar[int]
        ILLUSTRATION_FIELD_NUMBER: _ClassVar[int]
        OFFERS_INFO_FIELD_NUMBER: _ClassVar[int]
        logo: _brand_pb2.Brand
        title: str
        sub_title: str
        sw_info: PaymentSuccessWidget.StartWatchingInfo
        is_plan_active: bool
        illustration: _illustration_pb2.Illustration
        offers_info: PaymentSuccessWidget.OffersInfo
        def __init__(self, logo: _Optional[_Union[_brand_pb2.Brand, str]] = ..., title: _Optional[str] = ..., sub_title: _Optional[str] = ..., sw_info: _Optional[_Union[PaymentSuccessWidget.StartWatchingInfo, _Mapping]] = ..., is_plan_active: bool = ..., illustration: _Optional[_Union[_illustration_pb2.Illustration, _Mapping]] = ..., offers_info: _Optional[_Union[PaymentSuccessWidget.OffersInfo, _Mapping]] = ...) -> None: ...
    class StartWatchingInfo(_message.Message):
        __slots__ = ("cta", "actions")
        CTA_FIELD_NUMBER: _ClassVar[int]
        ACTIONS_FIELD_NUMBER: _ClassVar[int]
        cta: str
        actions: _actions_pb2.Actions
        def __init__(self, cta: _Optional[str] = ..., actions: _Optional[_Union[_actions_pb2.Actions, _Mapping]] = ...) -> None: ...
    class OffersInfo(_message.Message):
        __slots__ = ("title", "sub_title", "top_separator")
        TITLE_FIELD_NUMBER: _ClassVar[int]
        SUB_TITLE_FIELD_NUMBER: _ClassVar[int]
        TOP_SEPARATOR_FIELD_NUMBER: _ClassVar[int]
        title: _title_icon_combo_pb2.TitleIconCombo
        sub_title: str
        top_separator: _illustration_pb2.Illustration
        def __init__(self, title: _Optional[_Union[_title_icon_combo_pb2.TitleIconCombo, _Mapping]] = ..., sub_title: _Optional[str] = ..., top_separator: _Optional[_Union[_illustration_pb2.Illustration, _Mapping]] = ...) -> None: ...
    WIDGET_COMMONS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    widget_commons: _widget_commons_pb2.WidgetCommons
    data: PaymentSuccessWidget.Data
    def __init__(self, widget_commons: _Optional[_Union[_widget_commons_pb2.WidgetCommons, _Mapping]] = ..., data: _Optional[_Union[PaymentSuccessWidget.Data, _Mapping]] = ...) -> None: ...
