from base import widget_commons_pb2 as _widget_commons_pb2
from base import actions_pb2 as _actions_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PackInfoLRWidget(_message.Message):
    __slots__ = ("widget_commons", "data")
    class Data(_message.Message):
        __slots__ = ("pack_list", "auto_trigger_actions", "text")
        PACK_LIST_FIELD_NUMBER: _ClassVar[int]
        AUTO_TRIGGER_ACTIONS_FIELD_NUMBER: _ClassVar[int]
        TEXT_FIELD_NUMBER: _ClassVar[int]
        pack_list: _containers.RepeatedCompositeFieldContainer[PackInfoLRWidget.Pack]
        auto_trigger_actions: _actions_pb2.Actions
        text: PackInfoLRWidget.PurchaseDisclaimer
        def __init__(self, pack_list: _Optional[_Iterable[_Union[PackInfoLRWidget.Pack, _Mapping]]] = ..., auto_trigger_actions: _Optional[_Union[_actions_pb2.Actions, _Mapping]] = ..., text: _Optional[_Union[PackInfoLRWidget.PurchaseDisclaimer, _Mapping]] = ...) -> None: ...
    class Pack(_message.Message):
        __slots__ = ("is_selected", "title", "sub_title", "label", "offer", "price", "is_disabled", "actions", "filter_meta", "original_price_text", "price_proration_text")
        IS_SELECTED_FIELD_NUMBER: _ClassVar[int]
        TITLE_FIELD_NUMBER: _ClassVar[int]
        SUB_TITLE_FIELD_NUMBER: _ClassVar[int]
        LABEL_FIELD_NUMBER: _ClassVar[int]
        OFFER_FIELD_NUMBER: _ClassVar[int]
        PRICE_FIELD_NUMBER: _ClassVar[int]
        IS_DISABLED_FIELD_NUMBER: _ClassVar[int]
        ACTIONS_FIELD_NUMBER: _ClassVar[int]
        FILTER_META_FIELD_NUMBER: _ClassVar[int]
        ORIGINAL_PRICE_TEXT_FIELD_NUMBER: _ClassVar[int]
        PRICE_PRORATION_TEXT_FIELD_NUMBER: _ClassVar[int]
        is_selected: bool
        title: str
        sub_title: str
        label: str
        offer: PackInfoLRWidget.Offer
        price: PackInfoLRWidget.Price
        is_disabled: bool
        actions: _actions_pb2.Actions
        filter_meta: PackInfoLRWidget.FilterMeta
        original_price_text: str
        price_proration_text: str
        def __init__(self, is_selected: bool = ..., title: _Optional[str] = ..., sub_title: _Optional[str] = ..., label: _Optional[str] = ..., offer: _Optional[_Union[PackInfoLRWidget.Offer, _Mapping]] = ..., price: _Optional[_Union[PackInfoLRWidget.Price, _Mapping]] = ..., is_disabled: bool = ..., actions: _Optional[_Union[_actions_pb2.Actions, _Mapping]] = ..., filter_meta: _Optional[_Union[PackInfoLRWidget.FilterMeta, _Mapping]] = ..., original_price_text: _Optional[str] = ..., price_proration_text: _Optional[str] = ...) -> None: ...
    class Price(_message.Message):
        __slots__ = ("amount", "currency", "interval")
        AMOUNT_FIELD_NUMBER: _ClassVar[int]
        CURRENCY_FIELD_NUMBER: _ClassVar[int]
        INTERVAL_FIELD_NUMBER: _ClassVar[int]
        amount: str
        currency: str
        interval: str
        def __init__(self, amount: _Optional[str] = ..., currency: _Optional[str] = ..., interval: _Optional[str] = ...) -> None: ...
    class PurchaseDisclaimer(_message.Message):
        __slots__ = ("text_message",)
        TEXT_MESSAGE_FIELD_NUMBER: _ClassVar[int]
        text_message: str
        def __init__(self, text_message: _Optional[str] = ...) -> None: ...
    class Offer(_message.Message):
        __slots__ = ("strike_through_text", "info")
        STRIKE_THROUGH_TEXT_FIELD_NUMBER: _ClassVar[int]
        INFO_FIELD_NUMBER: _ClassVar[int]
        strike_through_text: str
        info: str
        def __init__(self, strike_through_text: _Optional[str] = ..., info: _Optional[str] = ...) -> None: ...
    class FilterMeta(_message.Message):
        __slots__ = ("identifier",)
        IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
        identifier: str
        def __init__(self, identifier: _Optional[str] = ...) -> None: ...
    WIDGET_COMMONS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    widget_commons: _widget_commons_pb2.WidgetCommons
    data: PackInfoLRWidget.Data
    def __init__(self, widget_commons: _Optional[_Union[_widget_commons_pb2.WidgetCommons, _Mapping]] = ..., data: _Optional[_Union[PackInfoLRWidget.Data, _Mapping]] = ...) -> None: ...
