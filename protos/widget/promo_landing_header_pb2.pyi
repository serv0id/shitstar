from feature.image import image_pb2 as _image_pb2
from base import widget_commons_pb2 as _widget_commons_pb2
from base import actions_pb2 as _actions_pb2
from widget import languages_selection_pb2 as _languages_selection_pb2
from widget import logo_pb2 as _logo_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PromoLandingHeaderWidget(_message.Message):
    __slots__ = ("widget_commons", "data")
    class Data(_message.Message):
        __slots__ = ("login_btn", "language_selection", "language_selector", "brand_logo")
        LOGIN_BTN_FIELD_NUMBER: _ClassVar[int]
        LANGUAGE_SELECTION_FIELD_NUMBER: _ClassVar[int]
        LANGUAGE_SELECTOR_FIELD_NUMBER: _ClassVar[int]
        BRAND_LOGO_FIELD_NUMBER: _ClassVar[int]
        login_btn: PromoLandingHeaderWidget.Button
        language_selection: _languages_selection_pb2.LanguagesSelectionWidget
        language_selector: PromoLandingHeaderWidget.LanguageSelector
        brand_logo: _logo_pb2.LogoWidget
        def __init__(self, login_btn: _Optional[_Union[PromoLandingHeaderWidget.Button, _Mapping]] = ..., language_selection: _Optional[_Union[_languages_selection_pb2.LanguagesSelectionWidget, _Mapping]] = ..., language_selector: _Optional[_Union[PromoLandingHeaderWidget.LanguageSelector, _Mapping]] = ..., brand_logo: _Optional[_Union[_logo_pb2.LogoWidget, _Mapping]] = ...) -> None: ...
    class Button(_message.Message):
        __slots__ = ("text", "actions", "icon")
        TEXT_FIELD_NUMBER: _ClassVar[int]
        ACTIONS_FIELD_NUMBER: _ClassVar[int]
        ICON_FIELD_NUMBER: _ClassVar[int]
        text: str
        actions: _actions_pb2.Actions
        icon: str
        def __init__(self, text: _Optional[str] = ..., actions: _Optional[_Union[_actions_pb2.Actions, _Mapping]] = ..., icon: _Optional[str] = ...) -> None: ...
    class LanguageSelector(_message.Message):
        __slots__ = ("choose_language_text", "languages")
        CHOOSE_LANGUAGE_TEXT_FIELD_NUMBER: _ClassVar[int]
        LANGUAGES_FIELD_NUMBER: _ClassVar[int]
        choose_language_text: str
        languages: _containers.RepeatedCompositeFieldContainer[PromoLandingHeaderWidget.LanguageOption]
        def __init__(self, choose_language_text: _Optional[str] = ..., languages: _Optional[_Iterable[_Union[PromoLandingHeaderWidget.LanguageOption, _Mapping]]] = ...) -> None: ...
    class LanguageOption(_message.Message):
        __slots__ = ("iso", "flag", "label", "is_selected", "change_lang_action")
        ISO_FIELD_NUMBER: _ClassVar[int]
        FLAG_FIELD_NUMBER: _ClassVar[int]
        LABEL_FIELD_NUMBER: _ClassVar[int]
        IS_SELECTED_FIELD_NUMBER: _ClassVar[int]
        CHANGE_LANG_ACTION_FIELD_NUMBER: _ClassVar[int]
        iso: str
        flag: _image_pb2.Image
        label: str
        is_selected: bool
        change_lang_action: _actions_pb2.Actions
        def __init__(self, iso: _Optional[str] = ..., flag: _Optional[_Union[_image_pb2.Image, _Mapping]] = ..., label: _Optional[str] = ..., is_selected: bool = ..., change_lang_action: _Optional[_Union[_actions_pb2.Actions, _Mapping]] = ...) -> None: ...
    WIDGET_COMMONS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    widget_commons: _widget_commons_pb2.WidgetCommons
    data: PromoLandingHeaderWidget.Data
    def __init__(self, widget_commons: _Optional[_Union[_widget_commons_pb2.WidgetCommons, _Mapping]] = ..., data: _Optional[_Union[PromoLandingHeaderWidget.Data, _Mapping]] = ...) -> None: ...
