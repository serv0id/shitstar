from base import actions_pb2 as _actions_pb2
from base import template_pb2 as _template_pb2
from base import widget_commons_pb2 as _widget_commons_pb2
from feature.image import image_pb2 as _image_pb2
from widget import logo_pb2 as _logo_pb2
from feature.accessibility import accessibility_pb2 as _accessibility_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class LocaleSelectionHeaderWidget(_message.Message):
    __slots__ = ("template", "widget_commons", "data")
    class Data(_message.Message):
        __slots__ = ("image_btn", "logo", "language_selector", "login_info", "header", "animation_enabled")
        IMAGE_BTN_FIELD_NUMBER: _ClassVar[int]
        LOGO_FIELD_NUMBER: _ClassVar[int]
        LANGUAGE_SELECTOR_FIELD_NUMBER: _ClassVar[int]
        LOGIN_INFO_FIELD_NUMBER: _ClassVar[int]
        HEADER_FIELD_NUMBER: _ClassVar[int]
        ANIMATION_ENABLED_FIELD_NUMBER: _ClassVar[int]
        image_btn: LocaleSelectionHeaderWidget.ImageButton
        logo: _logo_pb2.LogoWidget
        language_selector: LocaleSelectionHeaderWidget.LanguageSelector
        login_info: LocaleSelectionHeaderWidget.LoginInfo
        header: LocaleSelectionHeaderWidget.Header
        animation_enabled: bool
        def __init__(self, image_btn: _Optional[_Union[LocaleSelectionHeaderWidget.ImageButton, _Mapping]] = ..., logo: _Optional[_Union[_logo_pb2.LogoWidget, _Mapping]] = ..., language_selector: _Optional[_Union[LocaleSelectionHeaderWidget.LanguageSelector, _Mapping]] = ..., login_info: _Optional[_Union[LocaleSelectionHeaderWidget.LoginInfo, _Mapping]] = ..., header: _Optional[_Union[LocaleSelectionHeaderWidget.Header, _Mapping]] = ..., animation_enabled: bool = ...) -> None: ...
    class ImageButton(_message.Message):
        __slots__ = ("icon_name", "actions", "alt", "action", "confirmation")
        ICON_NAME_FIELD_NUMBER: _ClassVar[int]
        ACTIONS_FIELD_NUMBER: _ClassVar[int]
        ALT_FIELD_NUMBER: _ClassVar[int]
        ACTION_FIELD_NUMBER: _ClassVar[int]
        CONFIRMATION_FIELD_NUMBER: _ClassVar[int]
        icon_name: str
        actions: _actions_pb2.Actions
        alt: _accessibility_pb2.Accessibility
        action: _actions_pb2.Actions
        confirmation: LocaleSelectionHeaderWidget.ConfirmationMeta
        def __init__(self, icon_name: _Optional[str] = ..., actions: _Optional[_Union[_actions_pb2.Actions, _Mapping]] = ..., alt: _Optional[_Union[_accessibility_pb2.Accessibility, _Mapping]] = ..., action: _Optional[_Union[_actions_pb2.Actions, _Mapping]] = ..., confirmation: _Optional[_Union[LocaleSelectionHeaderWidget.ConfirmationMeta, _Mapping]] = ...) -> None: ...
    class LoginInfo(_message.Message):
        __slots__ = ("label", "actions")
        LABEL_FIELD_NUMBER: _ClassVar[int]
        ACTIONS_FIELD_NUMBER: _ClassVar[int]
        label: str
        actions: _actions_pb2.Actions
        def __init__(self, label: _Optional[str] = ..., actions: _Optional[_Union[_actions_pb2.Actions, _Mapping]] = ...) -> None: ...
    class Cta(_message.Message):
        __slots__ = ("text", "icon_name", "actions")
        TEXT_FIELD_NUMBER: _ClassVar[int]
        ICON_NAME_FIELD_NUMBER: _ClassVar[int]
        ACTIONS_FIELD_NUMBER: _ClassVar[int]
        text: str
        icon_name: str
        actions: _actions_pb2.Actions
        def __init__(self, text: _Optional[str] = ..., icon_name: _Optional[str] = ..., actions: _Optional[_Union[_actions_pb2.Actions, _Mapping]] = ...) -> None: ...
    class Detail(_message.Message):
        __slots__ = ("description", "links")
        DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
        LINKS_FIELD_NUMBER: _ClassVar[int]
        description: str
        links: _containers.RepeatedCompositeFieldContainer[LocaleSelectionHeaderWidget.Link]
        def __init__(self, description: _Optional[str] = ..., links: _Optional[_Iterable[_Union[LocaleSelectionHeaderWidget.Link, _Mapping]]] = ...) -> None: ...
    class Link(_message.Message):
        __slots__ = ("key", "label", "url")
        KEY_FIELD_NUMBER: _ClassVar[int]
        LABEL_FIELD_NUMBER: _ClassVar[int]
        URL_FIELD_NUMBER: _ClassVar[int]
        key: str
        label: str
        url: str
        def __init__(self, key: _Optional[str] = ..., label: _Optional[str] = ..., url: _Optional[str] = ...) -> None: ...
    class ConfirmationMeta(_message.Message):
        __slots__ = ("img", "title", "details", "primary_cta", "secondary_cta", "is_closable", "actions")
        IMG_FIELD_NUMBER: _ClassVar[int]
        TITLE_FIELD_NUMBER: _ClassVar[int]
        DETAILS_FIELD_NUMBER: _ClassVar[int]
        PRIMARY_CTA_FIELD_NUMBER: _ClassVar[int]
        SECONDARY_CTA_FIELD_NUMBER: _ClassVar[int]
        IS_CLOSABLE_FIELD_NUMBER: _ClassVar[int]
        ACTIONS_FIELD_NUMBER: _ClassVar[int]
        img: _image_pb2.Image
        title: str
        details: _containers.RepeatedCompositeFieldContainer[LocaleSelectionHeaderWidget.Detail]
        primary_cta: LocaleSelectionHeaderWidget.Cta
        secondary_cta: LocaleSelectionHeaderWidget.Cta
        is_closable: bool
        actions: _actions_pb2.Actions
        def __init__(self, img: _Optional[_Union[_image_pb2.Image, _Mapping]] = ..., title: _Optional[str] = ..., details: _Optional[_Iterable[_Union[LocaleSelectionHeaderWidget.Detail, _Mapping]]] = ..., primary_cta: _Optional[_Union[LocaleSelectionHeaderWidget.Cta, _Mapping]] = ..., secondary_cta: _Optional[_Union[LocaleSelectionHeaderWidget.Cta, _Mapping]] = ..., is_closable: bool = ..., actions: _Optional[_Union[_actions_pb2.Actions, _Mapping]] = ...) -> None: ...
    class LanguageSelector(_message.Message):
        __slots__ = ("icon_name", "items", "heading", "actions")
        ICON_NAME_FIELD_NUMBER: _ClassVar[int]
        ITEMS_FIELD_NUMBER: _ClassVar[int]
        HEADING_FIELD_NUMBER: _ClassVar[int]
        ACTIONS_FIELD_NUMBER: _ClassVar[int]
        icon_name: str
        items: _containers.RepeatedCompositeFieldContainer[LocaleSelectionHeaderWidget.LanguageOption]
        heading: str
        actions: _actions_pb2.Actions
        def __init__(self, icon_name: _Optional[str] = ..., items: _Optional[_Iterable[_Union[LocaleSelectionHeaderWidget.LanguageOption, _Mapping]]] = ..., heading: _Optional[str] = ..., actions: _Optional[_Union[_actions_pb2.Actions, _Mapping]] = ...) -> None: ...
    class LanguageOption(_message.Message):
        __slots__ = ("label", "localised_label", "lang_code", "is_selected", "actions")
        LABEL_FIELD_NUMBER: _ClassVar[int]
        LOCALISED_LABEL_FIELD_NUMBER: _ClassVar[int]
        LANG_CODE_FIELD_NUMBER: _ClassVar[int]
        IS_SELECTED_FIELD_NUMBER: _ClassVar[int]
        ACTIONS_FIELD_NUMBER: _ClassVar[int]
        label: str
        localised_label: str
        lang_code: str
        is_selected: bool
        actions: _actions_pb2.Actions
        def __init__(self, label: _Optional[str] = ..., localised_label: _Optional[str] = ..., lang_code: _Optional[str] = ..., is_selected: bool = ..., actions: _Optional[_Union[_actions_pb2.Actions, _Mapping]] = ...) -> None: ...
    class TitleHeader(_message.Message):
        __slots__ = ("text",)
        TEXT_FIELD_NUMBER: _ClassVar[int]
        text: str
        def __init__(self, text: _Optional[str] = ...) -> None: ...
    class LogoHeader(_message.Message):
        __slots__ = ("logo",)
        LOGO_FIELD_NUMBER: _ClassVar[int]
        logo: _logo_pb2.LogoWidget
        def __init__(self, logo: _Optional[_Union[_logo_pb2.LogoWidget, _Mapping]] = ...) -> None: ...
    class Header(_message.Message):
        __slots__ = ("title_header", "logo_header")
        TITLE_HEADER_FIELD_NUMBER: _ClassVar[int]
        LOGO_HEADER_FIELD_NUMBER: _ClassVar[int]
        title_header: LocaleSelectionHeaderWidget.TitleHeader
        logo_header: LocaleSelectionHeaderWidget.LogoHeader
        def __init__(self, title_header: _Optional[_Union[LocaleSelectionHeaderWidget.TitleHeader, _Mapping]] = ..., logo_header: _Optional[_Union[LocaleSelectionHeaderWidget.LogoHeader, _Mapping]] = ...) -> None: ...
    TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    WIDGET_COMMONS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    template: _template_pb2.Template
    widget_commons: _widget_commons_pb2.WidgetCommons
    data: LocaleSelectionHeaderWidget.Data
    def __init__(self, template: _Optional[_Union[_template_pb2.Template, _Mapping]] = ..., widget_commons: _Optional[_Union[_widget_commons_pb2.WidgetCommons, _Mapping]] = ..., data: _Optional[_Union[LocaleSelectionHeaderWidget.Data, _Mapping]] = ...) -> None: ...
