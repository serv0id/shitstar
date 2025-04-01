from base import widget_commons_pb2 as _widget_commons_pb2
from widget import payment_method_commons_pb2 as _payment_method_commons_pb2
from feature.payment import validations_pb2 as _validations_pb2
from feature.payment import restrictions_pb2 as _restrictions_pb2
from feature.image import image_pb2 as _image_pb2
from base import actions_pb2 as _actions_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PaymentMethodNetBankingWidget(_message.Message):
    __slots__ = ("widget_commons", "bank_list", "search", "payment_method_meta", "banks")
    class Banklist(_message.Message):
        __slots__ = ("name", "logo", "link")
        NAME_FIELD_NUMBER: _ClassVar[int]
        LOGO_FIELD_NUMBER: _ClassVar[int]
        LINK_FIELD_NUMBER: _ClassVar[int]
        name: str
        logo: str
        link: str
        def __init__(self, name: _Optional[str] = ..., logo: _Optional[str] = ..., link: _Optional[str] = ...) -> None: ...
    class SearchOption(_message.Message):
        __slots__ = ("icon_name", "text", "heading", "input")
        ICON_NAME_FIELD_NUMBER: _ClassVar[int]
        TEXT_FIELD_NUMBER: _ClassVar[int]
        HEADING_FIELD_NUMBER: _ClassVar[int]
        INPUT_FIELD_NUMBER: _ClassVar[int]
        icon_name: str
        text: str
        heading: str
        input: PaymentMethodNetBankingWidget.Input
        def __init__(self, icon_name: _Optional[str] = ..., text: _Optional[str] = ..., heading: _Optional[str] = ..., input: _Optional[_Union[PaymentMethodNetBankingWidget.Input, _Mapping]] = ...) -> None: ...
    class BankOption(_message.Message):
        __slots__ = ("name", "full_name", "short_name", "bank_code", "callout", "image", "actions")
        NAME_FIELD_NUMBER: _ClassVar[int]
        FULL_NAME_FIELD_NUMBER: _ClassVar[int]
        SHORT_NAME_FIELD_NUMBER: _ClassVar[int]
        BANK_CODE_FIELD_NUMBER: _ClassVar[int]
        CALLOUT_FIELD_NUMBER: _ClassVar[int]
        IMAGE_FIELD_NUMBER: _ClassVar[int]
        ACTIONS_FIELD_NUMBER: _ClassVar[int]
        name: str
        full_name: str
        short_name: str
        bank_code: str
        callout: str
        image: _image_pb2.Image
        actions: _containers.RepeatedCompositeFieldContainer[_actions_pb2.Actions.Action]
        def __init__(self, name: _Optional[str] = ..., full_name: _Optional[str] = ..., short_name: _Optional[str] = ..., bank_code: _Optional[str] = ..., callout: _Optional[str] = ..., image: _Optional[_Union[_image_pb2.Image, _Mapping]] = ..., actions: _Optional[_Iterable[_Union[_actions_pb2.Actions.Action, _Mapping]]] = ...) -> None: ...
    class Input(_message.Message):
        __slots__ = ("title", "placeholder", "icon_name")
        TITLE_FIELD_NUMBER: _ClassVar[int]
        PLACEHOLDER_FIELD_NUMBER: _ClassVar[int]
        ICON_NAME_FIELD_NUMBER: _ClassVar[int]
        title: str
        placeholder: str
        icon_name: str
        def __init__(self, title: _Optional[str] = ..., placeholder: _Optional[str] = ..., icon_name: _Optional[str] = ...) -> None: ...
    WIDGET_COMMONS_FIELD_NUMBER: _ClassVar[int]
    BANK_LIST_FIELD_NUMBER: _ClassVar[int]
    SEARCH_FIELD_NUMBER: _ClassVar[int]
    PAYMENT_METHOD_META_FIELD_NUMBER: _ClassVar[int]
    BANKS_FIELD_NUMBER: _ClassVar[int]
    widget_commons: _widget_commons_pb2.WidgetCommons
    bank_list: _containers.RepeatedCompositeFieldContainer[PaymentMethodNetBankingWidget.Banklist]
    search: PaymentMethodNetBankingWidget.SearchOption
    payment_method_meta: _payment_method_commons_pb2.PaymentMethodCommonsWidget
    banks: _containers.RepeatedCompositeFieldContainer[PaymentMethodNetBankingWidget.BankOption]
    def __init__(self, widget_commons: _Optional[_Union[_widget_commons_pb2.WidgetCommons, _Mapping]] = ..., bank_list: _Optional[_Iterable[_Union[PaymentMethodNetBankingWidget.Banklist, _Mapping]]] = ..., search: _Optional[_Union[PaymentMethodNetBankingWidget.SearchOption, _Mapping]] = ..., payment_method_meta: _Optional[_Union[_payment_method_commons_pb2.PaymentMethodCommonsWidget, _Mapping]] = ..., banks: _Optional[_Iterable[_Union[PaymentMethodNetBankingWidget.BankOption, _Mapping]]] = ...) -> None: ...
