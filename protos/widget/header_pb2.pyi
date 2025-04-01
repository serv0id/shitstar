from base import actions_pb2 as _actions_pb2
from feature.image import image_pb2 as _image_pb2
from base import widget_commons_pb2 as _widget_commons_pb2
from feature.atom import button_pb2 as _button_pb2
from feature.text import text_pb2 as _text_pb2
from feature.callout_tag import callout_tag_pb2 as _callout_tag_pb2
from feature.accessibility import accessibility_pb2 as _accessibility_pb2
from widget import button_stack_pb2 as _button_stack_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class HeaderWidget(_message.Message):
    __slots__ = ("widget_commons", "data")
    class WidgetAlignment(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        DEFAULT: _ClassVar[HeaderWidget.WidgetAlignment]
        CENTER: _ClassVar[HeaderWidget.WidgetAlignment]
        LEFT: _ClassVar[HeaderWidget.WidgetAlignment]
    DEFAULT: HeaderWidget.WidgetAlignment
    CENTER: HeaderWidget.WidgetAlignment
    LEFT: HeaderWidget.WidgetAlignment
    class Data(_message.Message):
        __slots__ = ("header", "widget_alignment")
        HEADER_FIELD_NUMBER: _ClassVar[int]
        WIDGET_ALIGNMENT_FIELD_NUMBER: _ClassVar[int]
        header: HeaderWidget.Header
        widget_alignment: HeaderWidget.WidgetAlignment
        def __init__(self, header: _Optional[_Union[HeaderWidget.Header, _Mapping]] = ..., widget_alignment: _Optional[_Union[HeaderWidget.WidgetAlignment, str]] = ...) -> None: ...
    class Header(_message.Message):
        __slots__ = ("regular_tray_header", "anchored_tray_header", "branded_tray_header", "decorated_tray_header", "filter_tray_header", "surface_tray_header")
        REGULAR_TRAY_HEADER_FIELD_NUMBER: _ClassVar[int]
        ANCHORED_TRAY_HEADER_FIELD_NUMBER: _ClassVar[int]
        BRANDED_TRAY_HEADER_FIELD_NUMBER: _ClassVar[int]
        DECORATED_TRAY_HEADER_FIELD_NUMBER: _ClassVar[int]
        FILTER_TRAY_HEADER_FIELD_NUMBER: _ClassVar[int]
        SURFACE_TRAY_HEADER_FIELD_NUMBER: _ClassVar[int]
        regular_tray_header: HeaderWidget.RegularTrayHeader
        anchored_tray_header: HeaderWidget.AnchoredTrayHeader
        branded_tray_header: HeaderWidget.BrandedTrayHeader
        decorated_tray_header: HeaderWidget.DecoratedTrayHeader
        filter_tray_header: HeaderWidget.FilterTrayHeader
        surface_tray_header: HeaderWidget.SurfaceTrayHeader
        def __init__(self, regular_tray_header: _Optional[_Union[HeaderWidget.RegularTrayHeader, _Mapping]] = ..., anchored_tray_header: _Optional[_Union[HeaderWidget.AnchoredTrayHeader, _Mapping]] = ..., branded_tray_header: _Optional[_Union[HeaderWidget.BrandedTrayHeader, _Mapping]] = ..., decorated_tray_header: _Optional[_Union[HeaderWidget.DecoratedTrayHeader, _Mapping]] = ..., filter_tray_header: _Optional[_Union[HeaderWidget.FilterTrayHeader, _Mapping]] = ..., surface_tray_header: _Optional[_Union[HeaderWidget.SurfaceTrayHeader, _Mapping]] = ...) -> None: ...
    class RegularTrayHeader(_message.Message):
        __slots__ = ("title", "actions", "cta", "alt")
        TITLE_FIELD_NUMBER: _ClassVar[int]
        ACTIONS_FIELD_NUMBER: _ClassVar[int]
        CTA_FIELD_NUMBER: _ClassVar[int]
        ALT_FIELD_NUMBER: _ClassVar[int]
        title: str
        actions: _actions_pb2.Actions
        cta: _button_pb2.Button
        alt: _accessibility_pb2.Accessibility
        def __init__(self, title: _Optional[str] = ..., actions: _Optional[_Union[_actions_pb2.Actions, _Mapping]] = ..., cta: _Optional[_Union[_button_pb2.Button, _Mapping]] = ..., alt: _Optional[_Union[_accessibility_pb2.Accessibility, _Mapping]] = ...) -> None: ...
    class AnchoredTrayHeader(_message.Message):
        __slots__ = ("title", "sub_title", "image", "actions", "cta", "alt")
        TITLE_FIELD_NUMBER: _ClassVar[int]
        SUB_TITLE_FIELD_NUMBER: _ClassVar[int]
        IMAGE_FIELD_NUMBER: _ClassVar[int]
        ACTIONS_FIELD_NUMBER: _ClassVar[int]
        CTA_FIELD_NUMBER: _ClassVar[int]
        ALT_FIELD_NUMBER: _ClassVar[int]
        title: str
        sub_title: str
        image: _image_pb2.Image
        actions: _actions_pb2.Actions
        cta: _button_pb2.Button
        alt: _accessibility_pb2.Accessibility
        def __init__(self, title: _Optional[str] = ..., sub_title: _Optional[str] = ..., image: _Optional[_Union[_image_pb2.Image, _Mapping]] = ..., actions: _Optional[_Union[_actions_pb2.Actions, _Mapping]] = ..., cta: _Optional[_Union[_button_pb2.Button, _Mapping]] = ..., alt: _Optional[_Union[_accessibility_pb2.Accessibility, _Mapping]] = ...) -> None: ...
    class BrandedTrayHeader(_message.Message):
        __slots__ = ("image", "actions", "cta", "alt")
        IMAGE_FIELD_NUMBER: _ClassVar[int]
        ACTIONS_FIELD_NUMBER: _ClassVar[int]
        CTA_FIELD_NUMBER: _ClassVar[int]
        ALT_FIELD_NUMBER: _ClassVar[int]
        image: _image_pb2.Image
        actions: _actions_pb2.Actions
        cta: _button_pb2.Button
        alt: _accessibility_pb2.Accessibility
        def __init__(self, image: _Optional[_Union[_image_pb2.Image, _Mapping]] = ..., actions: _Optional[_Union[_actions_pb2.Actions, _Mapping]] = ..., cta: _Optional[_Union[_button_pb2.Button, _Mapping]] = ..., alt: _Optional[_Union[_accessibility_pb2.Accessibility, _Mapping]] = ...) -> None: ...
    class DecoratedTrayHeader(_message.Message):
        __slots__ = ("elements", "sub_title", "actions", "cta", "alt")
        ELEMENTS_FIELD_NUMBER: _ClassVar[int]
        SUB_TITLE_FIELD_NUMBER: _ClassVar[int]
        ACTIONS_FIELD_NUMBER: _ClassVar[int]
        CTA_FIELD_NUMBER: _ClassVar[int]
        ALT_FIELD_NUMBER: _ClassVar[int]
        elements: _containers.RepeatedCompositeFieldContainer[_callout_tag_pb2.CalloutTag]
        sub_title: str
        actions: _actions_pb2.Actions
        cta: _button_pb2.Button
        alt: _accessibility_pb2.Accessibility
        def __init__(self, elements: _Optional[_Iterable[_Union[_callout_tag_pb2.CalloutTag, _Mapping]]] = ..., sub_title: _Optional[str] = ..., actions: _Optional[_Union[_actions_pb2.Actions, _Mapping]] = ..., cta: _Optional[_Union[_button_pb2.Button, _Mapping]] = ..., alt: _Optional[_Union[_accessibility_pb2.Accessibility, _Mapping]] = ...) -> None: ...
    class SurfaceTrayHeader(_message.Message):
        __slots__ = ("title_text", "sub_title_text", "actions", "cta", "alt")
        TITLE_TEXT_FIELD_NUMBER: _ClassVar[int]
        SUB_TITLE_TEXT_FIELD_NUMBER: _ClassVar[int]
        ACTIONS_FIELD_NUMBER: _ClassVar[int]
        CTA_FIELD_NUMBER: _ClassVar[int]
        ALT_FIELD_NUMBER: _ClassVar[int]
        title_text: _text_pb2.Text
        sub_title_text: _text_pb2.Text
        actions: _actions_pb2.Actions
        cta: _button_pb2.Button
        alt: _accessibility_pb2.Accessibility
        def __init__(self, title_text: _Optional[_Union[_text_pb2.Text, _Mapping]] = ..., sub_title_text: _Optional[_Union[_text_pb2.Text, _Mapping]] = ..., actions: _Optional[_Union[_actions_pb2.Actions, _Mapping]] = ..., cta: _Optional[_Union[_button_pb2.Button, _Mapping]] = ..., alt: _Optional[_Union[_accessibility_pb2.Accessibility, _Mapping]] = ...) -> None: ...
    class FilterTrayHeader(_message.Message):
        __slots__ = ("header", "items")
        class Item(_message.Message):
            __slots__ = ("is_selected", "button_stack")
            IS_SELECTED_FIELD_NUMBER: _ClassVar[int]
            BUTTON_STACK_FIELD_NUMBER: _ClassVar[int]
            is_selected: bool
            button_stack: _button_stack_pb2.ButtonStackWidget
            def __init__(self, is_selected: bool = ..., button_stack: _Optional[_Union[_button_stack_pb2.ButtonStackWidget, _Mapping]] = ...) -> None: ...
        HEADER_FIELD_NUMBER: _ClassVar[int]
        ITEMS_FIELD_NUMBER: _ClassVar[int]
        header: HeaderWidget.Header
        items: _containers.RepeatedCompositeFieldContainer[HeaderWidget.FilterTrayHeader.Item]
        def __init__(self, header: _Optional[_Union[HeaderWidget.Header, _Mapping]] = ..., items: _Optional[_Iterable[_Union[HeaderWidget.FilterTrayHeader.Item, _Mapping]]] = ...) -> None: ...
    WIDGET_COMMONS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    widget_commons: _widget_commons_pb2.WidgetCommons
    data: HeaderWidget.Data
    def __init__(self, widget_commons: _Optional[_Union[_widget_commons_pb2.WidgetCommons, _Mapping]] = ..., data: _Optional[_Union[HeaderWidget.Data, _Mapping]] = ...) -> None: ...
