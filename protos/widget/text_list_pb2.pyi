from base import template_pb2 as _template_pb2
from base import widget_commons_pb2 as _widget_commons_pb2
from feature.image import image_pb2 as _image_pb2
from base import actions_pb2 as _actions_pb2
from feature.accessibility import accessibility_pb2 as _accessibility_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TextListWidget(_message.Message):
    __slots__ = ("template", "widget_commons", "data")
    class TextType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNDEFINED: _ClassVar[TextListWidget.TextType]
        DISCLAIMER: _ClassVar[TextListWidget.TextType]
        OFFER: _ClassVar[TextListWidget.TextType]
        WARNING: _ClassVar[TextListWidget.TextType]
        HEADING: _ClassVar[TextListWidget.TextType]
    UNDEFINED: TextListWidget.TextType
    DISCLAIMER: TextListWidget.TextType
    OFFER: TextListWidget.TextType
    WARNING: TextListWidget.TextType
    HEADING: TextListWidget.TextType
    class Data(_message.Message):
        __slots__ = ("info", "toggle_button", "secondary_button", "alt_info")
        INFO_FIELD_NUMBER: _ClassVar[int]
        TOGGLE_BUTTON_FIELD_NUMBER: _ClassVar[int]
        SECONDARY_BUTTON_FIELD_NUMBER: _ClassVar[int]
        ALT_INFO_FIELD_NUMBER: _ClassVar[int]
        info: _containers.RepeatedCompositeFieldContainer[TextListWidget.Text]
        toggle_button: TextListWidget.Toggle
        secondary_button: TextListWidget.Button
        alt_info: _accessibility_pb2.Accessibility
        def __init__(self, info: _Optional[_Iterable[_Union[TextListWidget.Text, _Mapping]]] = ..., toggle_button: _Optional[_Union[TextListWidget.Toggle, _Mapping]] = ..., secondary_button: _Optional[_Union[TextListWidget.Button, _Mapping]] = ..., alt_info: _Optional[_Union[_accessibility_pb2.Accessibility, _Mapping]] = ...) -> None: ...
    class Text(_message.Message):
        __slots__ = ("text_type", "links", "info_text", "rich_text", "icon_text")
        class InfoText(_message.Message):
            __slots__ = ("value",)
            VALUE_FIELD_NUMBER: _ClassVar[int]
            value: str
            def __init__(self, value: _Optional[str] = ...) -> None: ...
        class RichText(_message.Message):
            __slots__ = ("value", "asset")
            VALUE_FIELD_NUMBER: _ClassVar[int]
            ASSET_FIELD_NUMBER: _ClassVar[int]
            value: str
            asset: TextListWidget.Text.Asset
            def __init__(self, value: _Optional[str] = ..., asset: _Optional[_Union[TextListWidget.Text.Asset, _Mapping]] = ...) -> None: ...
        class IconText(_message.Message):
            __slots__ = ("icon", "value")
            ICON_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            icon: str
            value: str
            def __init__(self, icon: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
        class Asset(_message.Message):
            __slots__ = ("image",)
            IMAGE_FIELD_NUMBER: _ClassVar[int]
            image: _image_pb2.Image
            def __init__(self, image: _Optional[_Union[_image_pb2.Image, _Mapping]] = ...) -> None: ...
        TEXT_TYPE_FIELD_NUMBER: _ClassVar[int]
        LINKS_FIELD_NUMBER: _ClassVar[int]
        INFO_TEXT_FIELD_NUMBER: _ClassVar[int]
        RICH_TEXT_FIELD_NUMBER: _ClassVar[int]
        ICON_TEXT_FIELD_NUMBER: _ClassVar[int]
        text_type: TextListWidget.TextType
        links: _containers.RepeatedCompositeFieldContainer[TextListWidget.Link]
        info_text: TextListWidget.Text.InfoText
        rich_text: TextListWidget.Text.RichText
        icon_text: TextListWidget.Text.IconText
        def __init__(self, text_type: _Optional[_Union[TextListWidget.TextType, str]] = ..., links: _Optional[_Iterable[_Union[TextListWidget.Link, _Mapping]]] = ..., info_text: _Optional[_Union[TextListWidget.Text.InfoText, _Mapping]] = ..., rich_text: _Optional[_Union[TextListWidget.Text.RichText, _Mapping]] = ..., icon_text: _Optional[_Union[TextListWidget.Text.IconText, _Mapping]] = ...) -> None: ...
    class Toggle(_message.Message):
        __slots__ = ("collapsed_button", "expanded_button")
        COLLAPSED_BUTTON_FIELD_NUMBER: _ClassVar[int]
        EXPANDED_BUTTON_FIELD_NUMBER: _ClassVar[int]
        collapsed_button: TextListWidget.Button
        expanded_button: TextListWidget.Button
        def __init__(self, collapsed_button: _Optional[_Union[TextListWidget.Button, _Mapping]] = ..., expanded_button: _Optional[_Union[TextListWidget.Button, _Mapping]] = ...) -> None: ...
    class Button(_message.Message):
        __slots__ = ("label", "icon", "items_to_be_displayed", "is_default", "actions", "base_actions")
        LABEL_FIELD_NUMBER: _ClassVar[int]
        ICON_FIELD_NUMBER: _ClassVar[int]
        ITEMS_TO_BE_DISPLAYED_FIELD_NUMBER: _ClassVar[int]
        IS_DEFAULT_FIELD_NUMBER: _ClassVar[int]
        ACTIONS_FIELD_NUMBER: _ClassVar[int]
        BASE_ACTIONS_FIELD_NUMBER: _ClassVar[int]
        label: str
        icon: str
        items_to_be_displayed: int
        is_default: bool
        actions: _actions_pb2.Actions.Action
        base_actions: _actions_pb2.Actions
        def __init__(self, label: _Optional[str] = ..., icon: _Optional[str] = ..., items_to_be_displayed: _Optional[int] = ..., is_default: bool = ..., actions: _Optional[_Union[_actions_pb2.Actions.Action, _Mapping]] = ..., base_actions: _Optional[_Union[_actions_pb2.Actions, _Mapping]] = ...) -> None: ...
    class Link(_message.Message):
        __slots__ = ("label", "url", "key", "link_action")
        LABEL_FIELD_NUMBER: _ClassVar[int]
        URL_FIELD_NUMBER: _ClassVar[int]
        KEY_FIELD_NUMBER: _ClassVar[int]
        LINK_ACTION_FIELD_NUMBER: _ClassVar[int]
        label: str
        url: str
        key: str
        link_action: TextListWidget.LinkClickAction
        def __init__(self, label: _Optional[str] = ..., url: _Optional[str] = ..., key: _Optional[str] = ..., link_action: _Optional[_Union[TextListWidget.LinkClickAction, _Mapping]] = ...) -> None: ...
    class LinkClickAction(_message.Message):
        __slots__ = ("url", "actions")
        URL_FIELD_NUMBER: _ClassVar[int]
        ACTIONS_FIELD_NUMBER: _ClassVar[int]
        url: str
        actions: _actions_pb2.Actions.Action
        def __init__(self, url: _Optional[str] = ..., actions: _Optional[_Union[_actions_pb2.Actions.Action, _Mapping]] = ...) -> None: ...
    TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    WIDGET_COMMONS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    template: _template_pb2.Template
    widget_commons: _widget_commons_pb2.WidgetCommons
    data: TextListWidget.Data
    def __init__(self, template: _Optional[_Union[_template_pb2.Template, _Mapping]] = ..., widget_commons: _Optional[_Union[_widget_commons_pb2.WidgetCommons, _Mapping]] = ..., data: _Optional[_Union[TextListWidget.Data, _Mapping]] = ...) -> None: ...
