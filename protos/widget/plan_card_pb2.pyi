from base import widget_commons_pb2 as _widget_commons_pb2
from base import actions_pb2 as _actions_pb2
from feature.image import image_pb2 as _image_pb2
from feature.accessibility import accessibility_pb2 as _accessibility_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PlanCardWidget(_message.Message):
    __slots__ = ("widget_commons", "data")
    class Theme(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        DEFAULT_THEME: _ClassVar[PlanCardWidget.Theme]
        PRIMARY: _ClassVar[PlanCardWidget.Theme]
        SECONDARY: _ClassVar[PlanCardWidget.Theme]
    DEFAULT_THEME: PlanCardWidget.Theme
    PRIMARY: PlanCardWidget.Theme
    SECONDARY: PlanCardWidget.Theme
    class SubtextType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        DEFAULT: _ClassVar[PlanCardWidget.SubtextType]
        HIGHLIGHT: _ClassVar[PlanCardWidget.SubtextType]
    DEFAULT: PlanCardWidget.SubtextType
    HIGHLIGHT: PlanCardWidget.SubtextType
    class Data(_message.Message):
        __slots__ = ("is_expandable", "is_expanded", "tag", "header", "body", "color", "price_details", "theme", "alt")
        IS_EXPANDABLE_FIELD_NUMBER: _ClassVar[int]
        IS_EXPANDED_FIELD_NUMBER: _ClassVar[int]
        TAG_FIELD_NUMBER: _ClassVar[int]
        HEADER_FIELD_NUMBER: _ClassVar[int]
        BODY_FIELD_NUMBER: _ClassVar[int]
        COLOR_FIELD_NUMBER: _ClassVar[int]
        PRICE_DETAILS_FIELD_NUMBER: _ClassVar[int]
        THEME_FIELD_NUMBER: _ClassVar[int]
        ALT_FIELD_NUMBER: _ClassVar[int]
        is_expandable: bool
        is_expanded: bool
        tag: str
        header: PlanCardWidget.Header
        body: PlanCardWidget.Body
        color: PlanCardWidget.Color
        price_details: str
        theme: PlanCardWidget.Theme
        alt: _accessibility_pb2.Accessibility
        def __init__(self, is_expandable: bool = ..., is_expanded: bool = ..., tag: _Optional[str] = ..., header: _Optional[_Union[PlanCardWidget.Header, _Mapping]] = ..., body: _Optional[_Union[PlanCardWidget.Body, _Mapping]] = ..., color: _Optional[_Union[PlanCardWidget.Color, _Mapping]] = ..., price_details: _Optional[str] = ..., theme: _Optional[_Union[PlanCardWidget.Theme, str]] = ..., alt: _Optional[_Union[_accessibility_pb2.Accessibility, _Mapping]] = ...) -> None: ...
    class Header(_message.Message):
        __slots__ = ("title", "subtitle", "info")
        TITLE_FIELD_NUMBER: _ClassVar[int]
        SUBTITLE_FIELD_NUMBER: _ClassVar[int]
        INFO_FIELD_NUMBER: _ClassVar[int]
        title: str
        subtitle: str
        info: PlanCardWidget.InfoText
        def __init__(self, title: _Optional[str] = ..., subtitle: _Optional[str] = ..., info: _Optional[_Union[PlanCardWidget.InfoText, _Mapping]] = ...) -> None: ...
    class Body(_message.Message):
        __slots__ = ("usps", "selectors", "alt_usps", "alt_actions_usps")
        USPS_FIELD_NUMBER: _ClassVar[int]
        SELECTORS_FIELD_NUMBER: _ClassVar[int]
        ALT_USPS_FIELD_NUMBER: _ClassVar[int]
        ALT_ACTIONS_USPS_FIELD_NUMBER: _ClassVar[int]
        usps: _containers.RepeatedCompositeFieldContainer[PlanCardWidget.USP]
        selectors: _containers.RepeatedCompositeFieldContainer[PlanCardWidget.Selector]
        alt_usps: _accessibility_pb2.Accessibility
        alt_actions_usps: _containers.RepeatedCompositeFieldContainer[_actions_pb2.AccessibilityAction]
        def __init__(self, usps: _Optional[_Iterable[_Union[PlanCardWidget.USP, _Mapping]]] = ..., selectors: _Optional[_Iterable[_Union[PlanCardWidget.Selector, _Mapping]]] = ..., alt_usps: _Optional[_Union[_accessibility_pb2.Accessibility, _Mapping]] = ..., alt_actions_usps: _Optional[_Iterable[_Union[_actions_pb2.AccessibilityAction, _Mapping]]] = ...) -> None: ...
    class InfoText(_message.Message):
        __slots__ = ("text", "text_placeholder", "sub_text")
        TEXT_FIELD_NUMBER: _ClassVar[int]
        TEXT_PLACEHOLDER_FIELD_NUMBER: _ClassVar[int]
        SUB_TEXT_FIELD_NUMBER: _ClassVar[int]
        text: str
        text_placeholder: str
        sub_text: str
        def __init__(self, text: _Optional[str] = ..., text_placeholder: _Optional[str] = ..., sub_text: _Optional[str] = ...) -> None: ...
    class USP(_message.Message):
        __slots__ = ("expanded_image", "collapsed_image", "description", "name")
        EXPANDED_IMAGE_FIELD_NUMBER: _ClassVar[int]
        COLLAPSED_IMAGE_FIELD_NUMBER: _ClassVar[int]
        DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        expanded_image: _image_pb2.Image
        collapsed_image: _image_pb2.Image
        description: str
        name: str
        def __init__(self, expanded_image: _Optional[_Union[_image_pb2.Image, _Mapping]] = ..., collapsed_image: _Optional[_Union[_image_pb2.Image, _Mapping]] = ..., description: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...
    class Selector(_message.Message):
        __slots__ = ("is_selected", "identifier", "tag", "title", "subtitle", "sub_text", "actions", "price_details", "alt_selected", "alt_unselected", "alt_actions")
        IS_SELECTED_FIELD_NUMBER: _ClassVar[int]
        IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
        TAG_FIELD_NUMBER: _ClassVar[int]
        TITLE_FIELD_NUMBER: _ClassVar[int]
        SUBTITLE_FIELD_NUMBER: _ClassVar[int]
        SUB_TEXT_FIELD_NUMBER: _ClassVar[int]
        ACTIONS_FIELD_NUMBER: _ClassVar[int]
        PRICE_DETAILS_FIELD_NUMBER: _ClassVar[int]
        ALT_SELECTED_FIELD_NUMBER: _ClassVar[int]
        ALT_UNSELECTED_FIELD_NUMBER: _ClassVar[int]
        ALT_ACTIONS_FIELD_NUMBER: _ClassVar[int]
        is_selected: bool
        identifier: str
        tag: str
        title: str
        subtitle: PlanCardWidget.InfoText
        sub_text: PlanCardWidget.Subtext
        actions: _containers.RepeatedCompositeFieldContainer[_actions_pb2.Actions.Action]
        price_details: str
        alt_selected: _accessibility_pb2.Accessibility
        alt_unselected: _accessibility_pb2.Accessibility
        alt_actions: _containers.RepeatedCompositeFieldContainer[_actions_pb2.AccessibilityAction]
        def __init__(self, is_selected: bool = ..., identifier: _Optional[str] = ..., tag: _Optional[str] = ..., title: _Optional[str] = ..., subtitle: _Optional[_Union[PlanCardWidget.InfoText, _Mapping]] = ..., sub_text: _Optional[_Union[PlanCardWidget.Subtext, _Mapping]] = ..., actions: _Optional[_Iterable[_Union[_actions_pb2.Actions.Action, _Mapping]]] = ..., price_details: _Optional[str] = ..., alt_selected: _Optional[_Union[_accessibility_pb2.Accessibility, _Mapping]] = ..., alt_unselected: _Optional[_Union[_accessibility_pb2.Accessibility, _Mapping]] = ..., alt_actions: _Optional[_Iterable[_Union[_actions_pb2.AccessibilityAction, _Mapping]]] = ...) -> None: ...
    class Subtext(_message.Message):
        __slots__ = ("value", "type")
        VALUE_FIELD_NUMBER: _ClassVar[int]
        TYPE_FIELD_NUMBER: _ClassVar[int]
        value: str
        type: PlanCardWidget.SubtextType
        def __init__(self, value: _Optional[str] = ..., type: _Optional[_Union[PlanCardWidget.SubtextType, str]] = ...) -> None: ...
    class Color(_message.Message):
        __slots__ = ("primary_color", "secondary_color")
        PRIMARY_COLOR_FIELD_NUMBER: _ClassVar[int]
        SECONDARY_COLOR_FIELD_NUMBER: _ClassVar[int]
        primary_color: str
        secondary_color: str
        def __init__(self, primary_color: _Optional[str] = ..., secondary_color: _Optional[str] = ...) -> None: ...
    WIDGET_COMMONS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    widget_commons: _widget_commons_pb2.WidgetCommons
    data: PlanCardWidget.Data
    def __init__(self, widget_commons: _Optional[_Union[_widget_commons_pb2.WidgetCommons, _Mapping]] = ..., data: _Optional[_Union[PlanCardWidget.Data, _Mapping]] = ...) -> None: ...
