from feature.payment import validations_pb2 as _validations_pb2
from feature.payment import restrictions_pb2 as _restrictions_pb2
from feature.image import image_pb2 as _image_pb2
from base import actions_pb2 as _actions_pb2
from base import widget_commons_pb2 as _widget_commons_pb2
from widget import payment_method_commons_pb2 as _payment_method_commons_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PaymentMethodCardsWidget(_message.Message):
    __slots__ = ("widget_commons", "title", "card_number", "validity", "cvv", "cta", "payment_method_meta", "auto_triggered_actions", "card_type", "actions")
    class Input(_message.Message):
        __slots__ = ("title", "placeholder", "validations", "restrictions", "image")
        TITLE_FIELD_NUMBER: _ClassVar[int]
        PLACEHOLDER_FIELD_NUMBER: _ClassVar[int]
        VALIDATIONS_FIELD_NUMBER: _ClassVar[int]
        RESTRICTIONS_FIELD_NUMBER: _ClassVar[int]
        IMAGE_FIELD_NUMBER: _ClassVar[int]
        title: str
        placeholder: str
        validations: _containers.RepeatedCompositeFieldContainer[_validations_pb2.Validation]
        restrictions: _containers.RepeatedCompositeFieldContainer[_restrictions_pb2.Restriction]
        image: _image_pb2.Image
        def __init__(self, title: _Optional[str] = ..., placeholder: _Optional[str] = ..., validations: _Optional[_Iterable[_Union[_validations_pb2.Validation, _Mapping]]] = ..., restrictions: _Optional[_Iterable[_Union[_restrictions_pb2.Restriction, _Mapping]]] = ..., image: _Optional[_Union[_image_pb2.Image, _Mapping]] = ...) -> None: ...
    class Cta(_message.Message):
        __slots__ = ("text", "icon_name", "action", "actions")
        TEXT_FIELD_NUMBER: _ClassVar[int]
        ICON_NAME_FIELD_NUMBER: _ClassVar[int]
        ACTION_FIELD_NUMBER: _ClassVar[int]
        ACTIONS_FIELD_NUMBER: _ClassVar[int]
        text: str
        icon_name: str
        action: _actions_pb2.Actions
        actions: _containers.RepeatedCompositeFieldContainer[_actions_pb2.Actions.Action]
        def __init__(self, text: _Optional[str] = ..., icon_name: _Optional[str] = ..., action: _Optional[_Union[_actions_pb2.Actions, _Mapping]] = ..., actions: _Optional[_Iterable[_Union[_actions_pb2.Actions.Action, _Mapping]]] = ...) -> None: ...
    class CardType(_message.Message):
        __slots__ = ("card", "spaces", "regexExp", "max_length", "min_length", "cvv_length", "image")
        CARD_FIELD_NUMBER: _ClassVar[int]
        SPACES_FIELD_NUMBER: _ClassVar[int]
        REGEXEXP_FIELD_NUMBER: _ClassVar[int]
        MAX_LENGTH_FIELD_NUMBER: _ClassVar[int]
        MIN_LENGTH_FIELD_NUMBER: _ClassVar[int]
        CVV_LENGTH_FIELD_NUMBER: _ClassVar[int]
        IMAGE_FIELD_NUMBER: _ClassVar[int]
        card: str
        spaces: _containers.RepeatedScalarFieldContainer[int]
        regexExp: str
        max_length: int
        min_length: int
        cvv_length: int
        image: _image_pb2.Image
        def __init__(self, card: _Optional[str] = ..., spaces: _Optional[_Iterable[int]] = ..., regexExp: _Optional[str] = ..., max_length: _Optional[int] = ..., min_length: _Optional[int] = ..., cvv_length: _Optional[int] = ..., image: _Optional[_Union[_image_pb2.Image, _Mapping]] = ...) -> None: ...
    WIDGET_COMMONS_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    CARD_NUMBER_FIELD_NUMBER: _ClassVar[int]
    VALIDITY_FIELD_NUMBER: _ClassVar[int]
    CVV_FIELD_NUMBER: _ClassVar[int]
    CTA_FIELD_NUMBER: _ClassVar[int]
    PAYMENT_METHOD_META_FIELD_NUMBER: _ClassVar[int]
    AUTO_TRIGGERED_ACTIONS_FIELD_NUMBER: _ClassVar[int]
    CARD_TYPE_FIELD_NUMBER: _ClassVar[int]
    ACTIONS_FIELD_NUMBER: _ClassVar[int]
    widget_commons: _widget_commons_pb2.WidgetCommons
    title: str
    card_number: PaymentMethodCardsWidget.Input
    validity: PaymentMethodCardsWidget.Input
    cvv: PaymentMethodCardsWidget.Input
    cta: PaymentMethodCardsWidget.Cta
    payment_method_meta: _payment_method_commons_pb2.PaymentMethodCommonsWidget
    auto_triggered_actions: _containers.RepeatedCompositeFieldContainer[_actions_pb2.Actions.Action]
    card_type: _containers.RepeatedCompositeFieldContainer[PaymentMethodCardsWidget.CardType]
    actions: _actions_pb2.Actions
    def __init__(self, widget_commons: _Optional[_Union[_widget_commons_pb2.WidgetCommons, _Mapping]] = ..., title: _Optional[str] = ..., card_number: _Optional[_Union[PaymentMethodCardsWidget.Input, _Mapping]] = ..., validity: _Optional[_Union[PaymentMethodCardsWidget.Input, _Mapping]] = ..., cvv: _Optional[_Union[PaymentMethodCardsWidget.Input, _Mapping]] = ..., cta: _Optional[_Union[PaymentMethodCardsWidget.Cta, _Mapping]] = ..., payment_method_meta: _Optional[_Union[_payment_method_commons_pb2.PaymentMethodCommonsWidget, _Mapping]] = ..., auto_triggered_actions: _Optional[_Iterable[_Union[_actions_pb2.Actions.Action, _Mapping]]] = ..., card_type: _Optional[_Iterable[_Union[PaymentMethodCardsWidget.CardType, _Mapping]]] = ..., actions: _Optional[_Union[_actions_pb2.Actions, _Mapping]] = ...) -> None: ...
