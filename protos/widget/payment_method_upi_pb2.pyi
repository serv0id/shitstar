from feature.image import image_pb2 as _image_pb2
from feature.payment import validations_pb2 as _validations_pb2
from feature.payment import restrictions_pb2 as _restrictions_pb2
from base import actions_pb2 as _actions_pb2
from base import widget_commons_pb2 as _widget_commons_pb2
from widget import payment_method_commons_pb2 as _payment_method_commons_pb2
from widget import divider_pb2 as _divider_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PaymentMethodUpiWidget(_message.Message):
    __slots__ = ("widget_commons", "title", "vpa", "cta", "qr_meta", "app_timer", "divider", "fallback_qr_meta", "payment_method_meta", "auto_triggered_actions", "divider_widget")
    class Input(_message.Message):
        __slots__ = ("title", "placeholder", "validations", "restrictions", "image", "auto_triggered_actions", "suggestions")
        TITLE_FIELD_NUMBER: _ClassVar[int]
        PLACEHOLDER_FIELD_NUMBER: _ClassVar[int]
        VALIDATIONS_FIELD_NUMBER: _ClassVar[int]
        RESTRICTIONS_FIELD_NUMBER: _ClassVar[int]
        IMAGE_FIELD_NUMBER: _ClassVar[int]
        AUTO_TRIGGERED_ACTIONS_FIELD_NUMBER: _ClassVar[int]
        SUGGESTIONS_FIELD_NUMBER: _ClassVar[int]
        title: str
        placeholder: str
        validations: _containers.RepeatedCompositeFieldContainer[_validations_pb2.Validation]
        restrictions: _containers.RepeatedCompositeFieldContainer[_restrictions_pb2.Restriction]
        image: _image_pb2.Image
        auto_triggered_actions: _containers.RepeatedCompositeFieldContainer[_actions_pb2.Actions.Action]
        suggestions: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, title: _Optional[str] = ..., placeholder: _Optional[str] = ..., validations: _Optional[_Iterable[_Union[_validations_pb2.Validation, _Mapping]]] = ..., restrictions: _Optional[_Iterable[_Union[_restrictions_pb2.Restriction, _Mapping]]] = ..., image: _Optional[_Union[_image_pb2.Image, _Mapping]] = ..., auto_triggered_actions: _Optional[_Iterable[_Union[_actions_pb2.Actions.Action, _Mapping]]] = ..., suggestions: _Optional[_Iterable[str]] = ...) -> None: ...
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
    class QRMeta(_message.Message):
        __slots__ = ("title", "sub_title", "image", "timer", "links", "cta", "auto_triggered_actions")
        TITLE_FIELD_NUMBER: _ClassVar[int]
        SUB_TITLE_FIELD_NUMBER: _ClassVar[int]
        IMAGE_FIELD_NUMBER: _ClassVar[int]
        TIMER_FIELD_NUMBER: _ClassVar[int]
        LINKS_FIELD_NUMBER: _ClassVar[int]
        CTA_FIELD_NUMBER: _ClassVar[int]
        AUTO_TRIGGERED_ACTIONS_FIELD_NUMBER: _ClassVar[int]
        title: str
        sub_title: str
        image: _image_pb2.Image
        timer: PaymentMethodUpiWidget.Timer
        links: _containers.RepeatedCompositeFieldContainer[PaymentMethodUpiWidget.Link]
        cta: PaymentMethodUpiWidget.Cta
        auto_triggered_actions: _containers.RepeatedCompositeFieldContainer[_actions_pb2.Actions.Action]
        def __init__(self, title: _Optional[str] = ..., sub_title: _Optional[str] = ..., image: _Optional[_Union[_image_pb2.Image, _Mapping]] = ..., timer: _Optional[_Union[PaymentMethodUpiWidget.Timer, _Mapping]] = ..., links: _Optional[_Iterable[_Union[PaymentMethodUpiWidget.Link, _Mapping]]] = ..., cta: _Optional[_Union[PaymentMethodUpiWidget.Cta, _Mapping]] = ..., auto_triggered_actions: _Optional[_Iterable[_Union[_actions_pb2.Actions.Action, _Mapping]]] = ...) -> None: ...
    class AppTimer(_message.Message):
        __slots__ = ("timer", "title", "sub_title", "warning", "auto_triggered_actions")
        TIMER_FIELD_NUMBER: _ClassVar[int]
        TITLE_FIELD_NUMBER: _ClassVar[int]
        SUB_TITLE_FIELD_NUMBER: _ClassVar[int]
        WARNING_FIELD_NUMBER: _ClassVar[int]
        AUTO_TRIGGERED_ACTIONS_FIELD_NUMBER: _ClassVar[int]
        timer: PaymentMethodUpiWidget.Timer
        title: str
        sub_title: str
        warning: str
        auto_triggered_actions: _containers.RepeatedCompositeFieldContainer[_actions_pb2.Actions.Action]
        def __init__(self, timer: _Optional[_Union[PaymentMethodUpiWidget.Timer, _Mapping]] = ..., title: _Optional[str] = ..., sub_title: _Optional[str] = ..., warning: _Optional[str] = ..., auto_triggered_actions: _Optional[_Iterable[_Union[_actions_pb2.Actions.Action, _Mapping]]] = ...) -> None: ...
    class Link(_message.Message):
        __slots__ = ("label", "url", "key")
        LABEL_FIELD_NUMBER: _ClassVar[int]
        URL_FIELD_NUMBER: _ClassVar[int]
        KEY_FIELD_NUMBER: _ClassVar[int]
        label: str
        url: str
        key: str
        def __init__(self, label: _Optional[str] = ..., url: _Optional[str] = ..., key: _Optional[str] = ...) -> None: ...
    class Timer(_message.Message):
        __slots__ = ("text", "sub_text", "timeoutInMS", "icon", "polling_inverval_in_MS", "success_action", "timeout_action", "key")
        TEXT_FIELD_NUMBER: _ClassVar[int]
        SUB_TEXT_FIELD_NUMBER: _ClassVar[int]
        TIMEOUTINMS_FIELD_NUMBER: _ClassVar[int]
        ICON_FIELD_NUMBER: _ClassVar[int]
        POLLING_INVERVAL_IN_MS_FIELD_NUMBER: _ClassVar[int]
        SUCCESS_ACTION_FIELD_NUMBER: _ClassVar[int]
        TIMEOUT_ACTION_FIELD_NUMBER: _ClassVar[int]
        KEY_FIELD_NUMBER: _ClassVar[int]
        text: str
        sub_text: str
        timeoutInMS: int
        icon: str
        polling_inverval_in_MS: int
        success_action: _actions_pb2.Actions
        timeout_action: _actions_pb2.Actions
        key: str
        def __init__(self, text: _Optional[str] = ..., sub_text: _Optional[str] = ..., timeoutInMS: _Optional[int] = ..., icon: _Optional[str] = ..., polling_inverval_in_MS: _Optional[int] = ..., success_action: _Optional[_Union[_actions_pb2.Actions, _Mapping]] = ..., timeout_action: _Optional[_Union[_actions_pb2.Actions, _Mapping]] = ..., key: _Optional[str] = ...) -> None: ...
    WIDGET_COMMONS_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    VPA_FIELD_NUMBER: _ClassVar[int]
    CTA_FIELD_NUMBER: _ClassVar[int]
    QR_META_FIELD_NUMBER: _ClassVar[int]
    APP_TIMER_FIELD_NUMBER: _ClassVar[int]
    DIVIDER_FIELD_NUMBER: _ClassVar[int]
    FALLBACK_QR_META_FIELD_NUMBER: _ClassVar[int]
    PAYMENT_METHOD_META_FIELD_NUMBER: _ClassVar[int]
    AUTO_TRIGGERED_ACTIONS_FIELD_NUMBER: _ClassVar[int]
    DIVIDER_WIDGET_FIELD_NUMBER: _ClassVar[int]
    widget_commons: _widget_commons_pb2.WidgetCommons
    title: str
    vpa: PaymentMethodUpiWidget.Input
    cta: PaymentMethodUpiWidget.Cta
    qr_meta: PaymentMethodUpiWidget.QRMeta
    app_timer: PaymentMethodUpiWidget.AppTimer
    divider: str
    fallback_qr_meta: PaymentMethodUpiWidget.QRMeta
    payment_method_meta: _payment_method_commons_pb2.PaymentMethodCommonsWidget
    auto_triggered_actions: _containers.RepeatedCompositeFieldContainer[_actions_pb2.Actions.Action]
    divider_widget: _divider_pb2.DividerWidget
    def __init__(self, widget_commons: _Optional[_Union[_widget_commons_pb2.WidgetCommons, _Mapping]] = ..., title: _Optional[str] = ..., vpa: _Optional[_Union[PaymentMethodUpiWidget.Input, _Mapping]] = ..., cta: _Optional[_Union[PaymentMethodUpiWidget.Cta, _Mapping]] = ..., qr_meta: _Optional[_Union[PaymentMethodUpiWidget.QRMeta, _Mapping]] = ..., app_timer: _Optional[_Union[PaymentMethodUpiWidget.AppTimer, _Mapping]] = ..., divider: _Optional[str] = ..., fallback_qr_meta: _Optional[_Union[PaymentMethodUpiWidget.QRMeta, _Mapping]] = ..., payment_method_meta: _Optional[_Union[_payment_method_commons_pb2.PaymentMethodCommonsWidget, _Mapping]] = ..., auto_triggered_actions: _Optional[_Iterable[_Union[_actions_pb2.Actions.Action, _Mapping]]] = ..., divider_widget: _Optional[_Union[_divider_pb2.DividerWidget, _Mapping]] = ...) -> None: ...
