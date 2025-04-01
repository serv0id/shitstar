from feature.image import image_pb2 as _image_pb2
from base import actions_pb2 as _actions_pb2
from base import widget_commons_pb2 as _widget_commons_pb2
from widget import payment_method_commons_pb2 as _payment_method_commons_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PaymentMethodGiapWidget(_message.Message):
    __slots__ = ("widget_commons", "title", "cta", "payment_method_meta")
    class Cta(_message.Message):
        __slots__ = ("text", "image", "actions")
        TEXT_FIELD_NUMBER: _ClassVar[int]
        IMAGE_FIELD_NUMBER: _ClassVar[int]
        ACTIONS_FIELD_NUMBER: _ClassVar[int]
        text: str
        image: _image_pb2.Image
        actions: _actions_pb2.Actions
        def __init__(self, text: _Optional[str] = ..., image: _Optional[_Union[_image_pb2.Image, _Mapping]] = ..., actions: _Optional[_Union[_actions_pb2.Actions, _Mapping]] = ...) -> None: ...
    WIDGET_COMMONS_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    CTA_FIELD_NUMBER: _ClassVar[int]
    PAYMENT_METHOD_META_FIELD_NUMBER: _ClassVar[int]
    widget_commons: _widget_commons_pb2.WidgetCommons
    title: str
    cta: PaymentMethodGiapWidget.Cta
    payment_method_meta: _payment_method_commons_pb2.PaymentMethodCommonsWidget
    def __init__(self, widget_commons: _Optional[_Union[_widget_commons_pb2.WidgetCommons, _Mapping]] = ..., title: _Optional[str] = ..., cta: _Optional[_Union[PaymentMethodGiapWidget.Cta, _Mapping]] = ..., payment_method_meta: _Optional[_Union[_payment_method_commons_pb2.PaymentMethodCommonsWidget, _Mapping]] = ...) -> None: ...
