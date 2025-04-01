from base import actions_pb2 as _actions_pb2
from base import template_pb2 as _template_pb2
from base import widget_commons_pb2 as _widget_commons_pb2
from feature.image import image_pb2 as _image_pb2
from action import external_navigation_pb2 as _external_navigation_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class OfferWidget(_message.Message):
    __slots__ = ("template", "widget_commons", "data")
    class OfferTitleType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        TITLE_TEXT: _ClassVar[OfferWidget.OfferTitleType]
        TITLE_HIGHLIGHTED: _ClassVar[OfferWidget.OfferTitleType]
    TITLE_TEXT: OfferWidget.OfferTitleType
    TITLE_HIGHLIGHTED: OfferWidget.OfferTitleType
    class Data(_message.Message):
        __slots__ = ("title", "sub_title", "img", "background_meta", "icon", "on_click", "actions", "tnc_meta")
        TITLE_FIELD_NUMBER: _ClassVar[int]
        SUB_TITLE_FIELD_NUMBER: _ClassVar[int]
        IMG_FIELD_NUMBER: _ClassVar[int]
        BACKGROUND_META_FIELD_NUMBER: _ClassVar[int]
        ICON_FIELD_NUMBER: _ClassVar[int]
        ON_CLICK_FIELD_NUMBER: _ClassVar[int]
        ACTIONS_FIELD_NUMBER: _ClassVar[int]
        TNC_META_FIELD_NUMBER: _ClassVar[int]
        title: OfferWidget.OfferTitle
        sub_title: OfferWidget.OfferSubtitle
        img: _image_pb2.Image
        background_meta: OfferWidget.OfferBackgroundMeta
        icon: str
        on_click: OfferWidget.OfferOnclickActions
        actions: _actions_pb2.Actions
        tnc_meta: OfferWidget.OfferTncMeta
        def __init__(self, title: _Optional[_Union[OfferWidget.OfferTitle, _Mapping]] = ..., sub_title: _Optional[_Union[OfferWidget.OfferSubtitle, _Mapping]] = ..., img: _Optional[_Union[_image_pb2.Image, _Mapping]] = ..., background_meta: _Optional[_Union[OfferWidget.OfferBackgroundMeta, _Mapping]] = ..., icon: _Optional[str] = ..., on_click: _Optional[_Union[OfferWidget.OfferOnclickActions, _Mapping]] = ..., actions: _Optional[_Union[_actions_pb2.Actions, _Mapping]] = ..., tnc_meta: _Optional[_Union[OfferWidget.OfferTncMeta, _Mapping]] = ...) -> None: ...
    class OfferTitle(_message.Message):
        __slots__ = ("value", "type")
        VALUE_FIELD_NUMBER: _ClassVar[int]
        TYPE_FIELD_NUMBER: _ClassVar[int]
        value: str
        type: OfferWidget.OfferTitleType
        def __init__(self, value: _Optional[str] = ..., type: _Optional[_Union[OfferWidget.OfferTitleType, str]] = ...) -> None: ...
    class OfferSubtitle(_message.Message):
        __slots__ = ("text", "error_text", "timer")
        TEXT_FIELD_NUMBER: _ClassVar[int]
        ERROR_TEXT_FIELD_NUMBER: _ClassVar[int]
        TIMER_FIELD_NUMBER: _ClassVar[int]
        text: str
        error_text: str
        timer: OfferWidget.OfferTimerMeta
        def __init__(self, text: _Optional[str] = ..., error_text: _Optional[str] = ..., timer: _Optional[_Union[OfferWidget.OfferTimerMeta, _Mapping]] = ...) -> None: ...
    class OfferBackgroundMeta(_message.Message):
        __slots__ = ("gradient_start", "gradient_end")
        GRADIENT_START_FIELD_NUMBER: _ClassVar[int]
        GRADIENT_END_FIELD_NUMBER: _ClassVar[int]
        gradient_start: str
        gradient_end: str
        def __init__(self, gradient_start: _Optional[str] = ..., gradient_end: _Optional[str] = ...) -> None: ...
    class OfferOnclickActions(_message.Message):
        __slots__ = ("external_navigation",)
        EXTERNAL_NAVIGATION_FIELD_NUMBER: _ClassVar[int]
        external_navigation: _external_navigation_pb2.ExternalNavigationAction
        def __init__(self, external_navigation: _Optional[_Union[_external_navigation_pb2.ExternalNavigationAction, _Mapping]] = ...) -> None: ...
    class OfferTimerMeta(_message.Message):
        __slots__ = ("expiry_time",)
        EXPIRY_TIME_FIELD_NUMBER: _ClassVar[int]
        expiry_time: str
        def __init__(self, expiry_time: _Optional[str] = ...) -> None: ...
    class OfferTncMeta(_message.Message):
        __slots__ = ("close_icon", "title_image", "title_text", "tnc_list", "cta")
        CLOSE_ICON_FIELD_NUMBER: _ClassVar[int]
        TITLE_IMAGE_FIELD_NUMBER: _ClassVar[int]
        TITLE_TEXT_FIELD_NUMBER: _ClassVar[int]
        TNC_LIST_FIELD_NUMBER: _ClassVar[int]
        CTA_FIELD_NUMBER: _ClassVar[int]
        close_icon: str
        title_image: _image_pb2.Image
        title_text: str
        tnc_list: _containers.RepeatedCompositeFieldContainer[OfferWidget.TncListItem]
        cta: OfferWidget.TncCta
        def __init__(self, close_icon: _Optional[str] = ..., title_image: _Optional[_Union[_image_pb2.Image, _Mapping]] = ..., title_text: _Optional[str] = ..., tnc_list: _Optional[_Iterable[_Union[OfferWidget.TncListItem, _Mapping]]] = ..., cta: _Optional[_Union[OfferWidget.TncCta, _Mapping]] = ...) -> None: ...
    class TncListItem(_message.Message):
        __slots__ = ("text", "link", "item_link")
        TEXT_FIELD_NUMBER: _ClassVar[int]
        LINK_FIELD_NUMBER: _ClassVar[int]
        ITEM_LINK_FIELD_NUMBER: _ClassVar[int]
        text: str
        link: str
        item_link: OfferWidget.Link
        def __init__(self, text: _Optional[str] = ..., link: _Optional[str] = ..., item_link: _Optional[_Union[OfferWidget.Link, _Mapping]] = ...) -> None: ...
    class TncCta(_message.Message):
        __slots__ = ("text", "cta_icon", "actions")
        TEXT_FIELD_NUMBER: _ClassVar[int]
        CTA_ICON_FIELD_NUMBER: _ClassVar[int]
        ACTIONS_FIELD_NUMBER: _ClassVar[int]
        text: str
        cta_icon: str
        actions: _actions_pb2.Actions
        def __init__(self, text: _Optional[str] = ..., cta_icon: _Optional[str] = ..., actions: _Optional[_Union[_actions_pb2.Actions, _Mapping]] = ...) -> None: ...
    class Link(_message.Message):
        __slots__ = ("label", "actions")
        LABEL_FIELD_NUMBER: _ClassVar[int]
        ACTIONS_FIELD_NUMBER: _ClassVar[int]
        label: str
        actions: _actions_pb2.Actions
        def __init__(self, label: _Optional[str] = ..., actions: _Optional[_Union[_actions_pb2.Actions, _Mapping]] = ...) -> None: ...
    TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    WIDGET_COMMONS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    template: _template_pb2.Template
    widget_commons: _widget_commons_pb2.WidgetCommons
    data: OfferWidget.Data
    def __init__(self, template: _Optional[_Union[_template_pb2.Template, _Mapping]] = ..., widget_commons: _Optional[_Union[_widget_commons_pb2.WidgetCommons, _Mapping]] = ..., data: _Optional[_Union[OfferWidget.Data, _Mapping]] = ...) -> None: ...
