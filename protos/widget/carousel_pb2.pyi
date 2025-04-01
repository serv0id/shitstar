from base import actions_pb2 as _actions_pb2
from base import template_pb2 as _template_pb2
from base import widget_commons_pb2 as _widget_commons_pb2
from feature.image import image_pb2 as _image_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CarouselWidget(_message.Message):
    __slots__ = ("widget_commons", "data")
    class Data(_message.Message):
        __slots__ = ("items", "transition_type", "animation_lottie")
        ITEMS_FIELD_NUMBER: _ClassVar[int]
        TRANSITION_TYPE_FIELD_NUMBER: _ClassVar[int]
        ANIMATION_LOTTIE_FIELD_NUMBER: _ClassVar[int]
        items: _containers.RepeatedCompositeFieldContainer[CarouselWidget.CarouselItem]
        transition_type: CarouselWidget.TransitionType
        animation_lottie: str
        def __init__(self, items: _Optional[_Iterable[_Union[CarouselWidget.CarouselItem, _Mapping]]] = ..., transition_type: _Optional[_Union[CarouselWidget.TransitionType, _Mapping]] = ..., animation_lottie: _Optional[str] = ...) -> None: ...
    class TransitionType(_message.Message):
        __slots__ = ("auto_swipe",)
        AUTO_SWIPE_FIELD_NUMBER: _ClassVar[int]
        auto_swipe: CarouselWidget.AutoSwipe
        def __init__(self, auto_swipe: _Optional[_Union[CarouselWidget.AutoSwipe, _Mapping]] = ...) -> None: ...
    class AutoSwipe(_message.Message):
        __slots__ = ("auto_swipe_duration",)
        AUTO_SWIPE_DURATION_FIELD_NUMBER: _ClassVar[int]
        auto_swipe_duration: int
        def __init__(self, auto_swipe_duration: _Optional[int] = ...) -> None: ...
    class CarouselItem(_message.Message):
        __slots__ = ("actions", "offer_item")
        ACTIONS_FIELD_NUMBER: _ClassVar[int]
        OFFER_ITEM_FIELD_NUMBER: _ClassVar[int]
        actions: _containers.RepeatedCompositeFieldContainer[_actions_pb2.Actions.Action]
        offer_item: CarouselWidget.CarouselOfferItem
        def __init__(self, actions: _Optional[_Iterable[_Union[_actions_pb2.Actions.Action, _Mapping]]] = ..., offer_item: _Optional[_Union[CarouselWidget.CarouselOfferItem, _Mapping]] = ...) -> None: ...
    class CarouselOfferItem(_message.Message):
        __slots__ = ("title", "sub_title", "logo", "background_meta", "icon")
        TITLE_FIELD_NUMBER: _ClassVar[int]
        SUB_TITLE_FIELD_NUMBER: _ClassVar[int]
        LOGO_FIELD_NUMBER: _ClassVar[int]
        BACKGROUND_META_FIELD_NUMBER: _ClassVar[int]
        ICON_FIELD_NUMBER: _ClassVar[int]
        title: CarouselWidget.Title
        sub_title: CarouselWidget.SubTitle
        logo: _image_pb2.Image
        background_meta: CarouselWidget.BackgroundMeta
        icon: str
        def __init__(self, title: _Optional[_Union[CarouselWidget.Title, _Mapping]] = ..., sub_title: _Optional[_Union[CarouselWidget.SubTitle, _Mapping]] = ..., logo: _Optional[_Union[_image_pb2.Image, _Mapping]] = ..., background_meta: _Optional[_Union[CarouselWidget.BackgroundMeta, _Mapping]] = ..., icon: _Optional[str] = ...) -> None: ...
    class Title(_message.Message):
        __slots__ = ("value",)
        VALUE_FIELD_NUMBER: _ClassVar[int]
        value: str
        def __init__(self, value: _Optional[str] = ...) -> None: ...
    class SubTitle(_message.Message):
        __slots__ = ("value",)
        VALUE_FIELD_NUMBER: _ClassVar[int]
        value: str
        def __init__(self, value: _Optional[str] = ...) -> None: ...
    class BackgroundMeta(_message.Message):
        __slots__ = ("gradient",)
        GRADIENT_FIELD_NUMBER: _ClassVar[int]
        gradient: CarouselWidget.Gradient
        def __init__(self, gradient: _Optional[_Union[CarouselWidget.Gradient, _Mapping]] = ...) -> None: ...
    class Gradient(_message.Message):
        __slots__ = ("gradient_start", "gradient_end")
        GRADIENT_START_FIELD_NUMBER: _ClassVar[int]
        GRADIENT_END_FIELD_NUMBER: _ClassVar[int]
        gradient_start: str
        gradient_end: str
        def __init__(self, gradient_start: _Optional[str] = ..., gradient_end: _Optional[str] = ...) -> None: ...
    WIDGET_COMMONS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    widget_commons: _widget_commons_pb2.WidgetCommons
    data: CarouselWidget.Data
    def __init__(self, widget_commons: _Optional[_Union[_widget_commons_pb2.WidgetCommons, _Mapping]] = ..., data: _Optional[_Union[CarouselWidget.Data, _Mapping]] = ...) -> None: ...
