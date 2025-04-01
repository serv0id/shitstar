from base import actions_pb2 as _actions_pb2
from base import widget_commons_pb2 as _widget_commons_pb2
from feature.branding import brand_pb2 as _brand_pb2
from feature.image import image_pb2 as _image_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SubscriptionDisclaimer(_message.Message):
    __slots__ = ("widget_commons", "data")
    class SubtitleType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        DEFAULT: _ClassVar[SubscriptionDisclaimer.SubtitleType]
        ERROR: _ClassVar[SubscriptionDisclaimer.SubtitleType]
    DEFAULT: SubscriptionDisclaimer.SubtitleType
    ERROR: SubscriptionDisclaimer.SubtitleType
    class Data(_message.Message):
        __slots__ = ("logo", "bg_image_list", "title", "paragraphs", "primary_cta", "secondary_cta", "partner_image", "qr_image", "subtitle")
        LOGO_FIELD_NUMBER: _ClassVar[int]
        BG_IMAGE_LIST_FIELD_NUMBER: _ClassVar[int]
        TITLE_FIELD_NUMBER: _ClassVar[int]
        PARAGRAPHS_FIELD_NUMBER: _ClassVar[int]
        PRIMARY_CTA_FIELD_NUMBER: _ClassVar[int]
        SECONDARY_CTA_FIELD_NUMBER: _ClassVar[int]
        PARTNER_IMAGE_FIELD_NUMBER: _ClassVar[int]
        QR_IMAGE_FIELD_NUMBER: _ClassVar[int]
        SUBTITLE_FIELD_NUMBER: _ClassVar[int]
        logo: _brand_pb2.Brand
        bg_image_list: _containers.RepeatedCompositeFieldContainer[_image_pb2.Image]
        title: str
        paragraphs: _containers.RepeatedCompositeFieldContainer[SubscriptionDisclaimer.Description]
        primary_cta: SubscriptionDisclaimer.Cta
        secondary_cta: SubscriptionDisclaimer.Cta
        partner_image: _image_pb2.Image
        qr_image: _image_pb2.Image
        subtitle: SubscriptionDisclaimer.Subtitle
        def __init__(self, logo: _Optional[_Union[_brand_pb2.Brand, str]] = ..., bg_image_list: _Optional[_Iterable[_Union[_image_pb2.Image, _Mapping]]] = ..., title: _Optional[str] = ..., paragraphs: _Optional[_Iterable[_Union[SubscriptionDisclaimer.Description, _Mapping]]] = ..., primary_cta: _Optional[_Union[SubscriptionDisclaimer.Cta, _Mapping]] = ..., secondary_cta: _Optional[_Union[SubscriptionDisclaimer.Cta, _Mapping]] = ..., partner_image: _Optional[_Union[_image_pb2.Image, _Mapping]] = ..., qr_image: _Optional[_Union[_image_pb2.Image, _Mapping]] = ..., subtitle: _Optional[_Union[SubscriptionDisclaimer.Subtitle, _Mapping]] = ...) -> None: ...
    class Description(_message.Message):
        __slots__ = ("text", "pay_link")
        TEXT_FIELD_NUMBER: _ClassVar[int]
        PAY_LINK_FIELD_NUMBER: _ClassVar[int]
        text: str
        pay_link: str
        def __init__(self, text: _Optional[str] = ..., pay_link: _Optional[str] = ...) -> None: ...
    class Subtitle(_message.Message):
        __slots__ = ("text", "type")
        TEXT_FIELD_NUMBER: _ClassVar[int]
        TYPE_FIELD_NUMBER: _ClassVar[int]
        text: str
        type: SubscriptionDisclaimer.SubtitleType
        def __init__(self, text: _Optional[str] = ..., type: _Optional[_Union[SubscriptionDisclaimer.SubtitleType, str]] = ...) -> None: ...
    class Cta(_message.Message):
        __slots__ = ("text", "actions")
        TEXT_FIELD_NUMBER: _ClassVar[int]
        ACTIONS_FIELD_NUMBER: _ClassVar[int]
        text: str
        actions: _actions_pb2.Actions
        def __init__(self, text: _Optional[str] = ..., actions: _Optional[_Union[_actions_pb2.Actions, _Mapping]] = ...) -> None: ...
    WIDGET_COMMONS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    widget_commons: _widget_commons_pb2.WidgetCommons
    data: SubscriptionDisclaimer.Data
    def __init__(self, widget_commons: _Optional[_Union[_widget_commons_pb2.WidgetCommons, _Mapping]] = ..., data: _Optional[_Union[SubscriptionDisclaimer.Data, _Mapping]] = ...) -> None: ...
