from base import widget_commons_pb2 as _widget_commons_pb2
from feature.image import image_pb2 as _image_pb2
from feature.payment import payment_gateway_pb2 as _payment_gateway_pb2
from base import actions_pb2 as _actions_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class QrPaymentWidget(_message.Message):
    __slots__ = ("widget_commons", "data")
    class Data(_message.Message):
        __slots__ = ("title", "qr_meta", "fallback_qr_meta", "status_widget_url", "gateways", "pollingInterval", "pollingExpiryTime")
        TITLE_FIELD_NUMBER: _ClassVar[int]
        QR_META_FIELD_NUMBER: _ClassVar[int]
        FALLBACK_QR_META_FIELD_NUMBER: _ClassVar[int]
        STATUS_WIDGET_URL_FIELD_NUMBER: _ClassVar[int]
        GATEWAYS_FIELD_NUMBER: _ClassVar[int]
        POLLINGINTERVAL_FIELD_NUMBER: _ClassVar[int]
        POLLINGEXPIRYTIME_FIELD_NUMBER: _ClassVar[int]
        title: str
        qr_meta: QRMeta
        fallback_qr_meta: FallbackQrMeta
        status_widget_url: str
        gateways: _containers.RepeatedCompositeFieldContainer[_payment_gateway_pb2.PaymentGateway]
        pollingInterval: int
        pollingExpiryTime: int
        def __init__(self, title: _Optional[str] = ..., qr_meta: _Optional[_Union[QRMeta, _Mapping]] = ..., fallback_qr_meta: _Optional[_Union[FallbackQrMeta, _Mapping]] = ..., status_widget_url: _Optional[str] = ..., gateways: _Optional[_Iterable[_Union[_payment_gateway_pb2.PaymentGateway, _Mapping]]] = ..., pollingInterval: _Optional[int] = ..., pollingExpiryTime: _Optional[int] = ...) -> None: ...
    WIDGET_COMMONS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    widget_commons: _widget_commons_pb2.WidgetCommons
    data: QrPaymentWidget.Data
    def __init__(self, widget_commons: _Optional[_Union[_widget_commons_pb2.WidgetCommons, _Mapping]] = ..., data: _Optional[_Union[QrPaymentWidget.Data, _Mapping]] = ...) -> None: ...

class QRMeta(_message.Message):
    __slots__ = ("title", "sub_title", "timer_expiry_text", "image", "pollingInterval", "loading_image", "paragraphs", "loading_caption", "caption", "auto_triggered_actions", "cta")
    class Cta(_message.Message):
        __slots__ = ("text", "icon_name", "actions")
        TEXT_FIELD_NUMBER: _ClassVar[int]
        ICON_NAME_FIELD_NUMBER: _ClassVar[int]
        ACTIONS_FIELD_NUMBER: _ClassVar[int]
        text: str
        icon_name: str
        actions: _containers.RepeatedCompositeFieldContainer[_actions_pb2.Actions.Action]
        def __init__(self, text: _Optional[str] = ..., icon_name: _Optional[str] = ..., actions: _Optional[_Iterable[_Union[_actions_pb2.Actions.Action, _Mapping]]] = ...) -> None: ...
    TITLE_FIELD_NUMBER: _ClassVar[int]
    SUB_TITLE_FIELD_NUMBER: _ClassVar[int]
    TIMER_EXPIRY_TEXT_FIELD_NUMBER: _ClassVar[int]
    IMAGE_FIELD_NUMBER: _ClassVar[int]
    POLLINGINTERVAL_FIELD_NUMBER: _ClassVar[int]
    LOADING_IMAGE_FIELD_NUMBER: _ClassVar[int]
    PARAGRAPHS_FIELD_NUMBER: _ClassVar[int]
    LOADING_CAPTION_FIELD_NUMBER: _ClassVar[int]
    CAPTION_FIELD_NUMBER: _ClassVar[int]
    AUTO_TRIGGERED_ACTIONS_FIELD_NUMBER: _ClassVar[int]
    CTA_FIELD_NUMBER: _ClassVar[int]
    title: str
    sub_title: str
    timer_expiry_text: str
    image: _image_pb2.Image
    pollingInterval: int
    loading_image: _image_pb2.Image
    paragraphs: Description
    loading_caption: ImageCaption
    caption: ImageCaption
    auto_triggered_actions: _containers.RepeatedCompositeFieldContainer[_actions_pb2.Actions.Action]
    cta: QRMeta.Cta
    def __init__(self, title: _Optional[str] = ..., sub_title: _Optional[str] = ..., timer_expiry_text: _Optional[str] = ..., image: _Optional[_Union[_image_pb2.Image, _Mapping]] = ..., pollingInterval: _Optional[int] = ..., loading_image: _Optional[_Union[_image_pb2.Image, _Mapping]] = ..., paragraphs: _Optional[_Union[Description, _Mapping]] = ..., loading_caption: _Optional[_Union[ImageCaption, _Mapping]] = ..., caption: _Optional[_Union[ImageCaption, _Mapping]] = ..., auto_triggered_actions: _Optional[_Iterable[_Union[_actions_pb2.Actions.Action, _Mapping]]] = ..., cta: _Optional[_Union[QRMeta.Cta, _Mapping]] = ...) -> None: ...

class FallbackQrMeta(_message.Message):
    __slots__ = ("title", "sub_title", "fallback_data", "header", "qr_image", "paragraphs", "caption", "auto_triggered_actions")
    TITLE_FIELD_NUMBER: _ClassVar[int]
    SUB_TITLE_FIELD_NUMBER: _ClassVar[int]
    FALLBACK_DATA_FIELD_NUMBER: _ClassVar[int]
    HEADER_FIELD_NUMBER: _ClassVar[int]
    QR_IMAGE_FIELD_NUMBER: _ClassVar[int]
    PARAGRAPHS_FIELD_NUMBER: _ClassVar[int]
    CAPTION_FIELD_NUMBER: _ClassVar[int]
    AUTO_TRIGGERED_ACTIONS_FIELD_NUMBER: _ClassVar[int]
    title: str
    sub_title: str
    fallback_data: str
    header: str
    qr_image: _image_pb2.Image
    paragraphs: Description
    caption: ImageCaption
    auto_triggered_actions: _containers.RepeatedCompositeFieldContainer[_actions_pb2.Actions.Action]
    def __init__(self, title: _Optional[str] = ..., sub_title: _Optional[str] = ..., fallback_data: _Optional[str] = ..., header: _Optional[str] = ..., qr_image: _Optional[_Union[_image_pb2.Image, _Mapping]] = ..., paragraphs: _Optional[_Union[Description, _Mapping]] = ..., caption: _Optional[_Union[ImageCaption, _Mapping]] = ..., auto_triggered_actions: _Optional[_Iterable[_Union[_actions_pb2.Actions.Action, _Mapping]]] = ...) -> None: ...

class Description(_message.Message):
    __slots__ = ("text", "links")
    TEXT_FIELD_NUMBER: _ClassVar[int]
    LINKS_FIELD_NUMBER: _ClassVar[int]
    text: str
    links: _containers.RepeatedCompositeFieldContainer[Link]
    def __init__(self, text: _Optional[str] = ..., links: _Optional[_Iterable[_Union[Link, _Mapping]]] = ...) -> None: ...

class Link(_message.Message):
    __slots__ = ("key", "label", "url")
    KEY_FIELD_NUMBER: _ClassVar[int]
    LABEL_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    key: str
    label: str
    url: str
    def __init__(self, key: _Optional[str] = ..., label: _Optional[str] = ..., url: _Optional[str] = ...) -> None: ...

class ImageCaption(_message.Message):
    __slots__ = ("type", "text", "sub_text", "timeout_duration", "key")
    class CaptionType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[ImageCaption.CaptionType]
        TIMER: _ClassVar[ImageCaption.CaptionType]
        LOADER: _ClassVar[ImageCaption.CaptionType]
    UNSPECIFIED: ImageCaption.CaptionType
    TIMER: ImageCaption.CaptionType
    LOADER: ImageCaption.CaptionType
    TYPE_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    SUB_TEXT_FIELD_NUMBER: _ClassVar[int]
    TIMEOUT_DURATION_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    type: ImageCaption.CaptionType
    text: str
    sub_text: str
    timeout_duration: int
    key: str
    def __init__(self, type: _Optional[_Union[ImageCaption.CaptionType, str]] = ..., text: _Optional[str] = ..., sub_text: _Optional[str] = ..., timeout_duration: _Optional[int] = ..., key: _Optional[str] = ...) -> None: ...
