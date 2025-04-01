from base import widget_commons_pb2 as _widget_commons_pb2
from base import actions_pb2 as _actions_pb2
from feature.image import image_pb2 as _image_pb2
from widget import dialog_pb2 as _dialog_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ProfileSettingsWidget(_message.Message):
    __slots__ = ("widget_commons", "data")
    class Data(_message.Message):
        __slots__ = ("app_language", "edit_profile", "title", "languages", "dialog", "actions")
        APP_LANGUAGE_FIELD_NUMBER: _ClassVar[int]
        EDIT_PROFILE_FIELD_NUMBER: _ClassVar[int]
        TITLE_FIELD_NUMBER: _ClassVar[int]
        LANGUAGES_FIELD_NUMBER: _ClassVar[int]
        DIALOG_FIELD_NUMBER: _ClassVar[int]
        ACTIONS_FIELD_NUMBER: _ClassVar[int]
        app_language: ProfileSettingsWidget.ClickableSetting
        edit_profile: ProfileSettingsWidget.ClickableSetting
        title: str
        languages: ProfileSettingsWidget.LanguageList
        dialog: _dialog_pb2.DialogWidget
        actions: _actions_pb2.Actions
        def __init__(self, app_language: _Optional[_Union[ProfileSettingsWidget.ClickableSetting, _Mapping]] = ..., edit_profile: _Optional[_Union[ProfileSettingsWidget.ClickableSetting, _Mapping]] = ..., title: _Optional[str] = ..., languages: _Optional[_Union[ProfileSettingsWidget.LanguageList, _Mapping]] = ..., dialog: _Optional[_Union[_dialog_pb2.DialogWidget, _Mapping]] = ..., actions: _Optional[_Union[_actions_pb2.Actions, _Mapping]] = ...) -> None: ...
    class LanguageList(_message.Message):
        __slots__ = ("title", "options", "profile_img", "on_click")
        TITLE_FIELD_NUMBER: _ClassVar[int]
        OPTIONS_FIELD_NUMBER: _ClassVar[int]
        PROFILE_IMG_FIELD_NUMBER: _ClassVar[int]
        ON_CLICK_FIELD_NUMBER: _ClassVar[int]
        title: str
        options: _containers.RepeatedCompositeFieldContainer[ProfileSettingsWidget.ListOption]
        profile_img: _image_pb2.Image
        on_click: _containers.RepeatedCompositeFieldContainer[_actions_pb2.Actions.Action]
        def __init__(self, title: _Optional[str] = ..., options: _Optional[_Iterable[_Union[ProfileSettingsWidget.ListOption, _Mapping]]] = ..., profile_img: _Optional[_Union[_image_pb2.Image, _Mapping]] = ..., on_click: _Optional[_Iterable[_Union[_actions_pb2.Actions.Action, _Mapping]]] = ...) -> None: ...
    class ListOption(_message.Message):
        __slots__ = ("label", "localised_label", "lang_code", "is_selected", "language_header", "language_sub_header", "coming_soon", "submit_button", "cancel_button")
        LABEL_FIELD_NUMBER: _ClassVar[int]
        LOCALISED_LABEL_FIELD_NUMBER: _ClassVar[int]
        LANG_CODE_FIELD_NUMBER: _ClassVar[int]
        IS_SELECTED_FIELD_NUMBER: _ClassVar[int]
        LANGUAGE_HEADER_FIELD_NUMBER: _ClassVar[int]
        LANGUAGE_SUB_HEADER_FIELD_NUMBER: _ClassVar[int]
        COMING_SOON_FIELD_NUMBER: _ClassVar[int]
        SUBMIT_BUTTON_FIELD_NUMBER: _ClassVar[int]
        CANCEL_BUTTON_FIELD_NUMBER: _ClassVar[int]
        label: str
        localised_label: str
        lang_code: str
        is_selected: bool
        language_header: str
        language_sub_header: str
        coming_soon: bool
        submit_button: ProfileSettingsWidget.Button
        cancel_button: ProfileSettingsWidget.Button
        def __init__(self, label: _Optional[str] = ..., localised_label: _Optional[str] = ..., lang_code: _Optional[str] = ..., is_selected: bool = ..., language_header: _Optional[str] = ..., language_sub_header: _Optional[str] = ..., coming_soon: bool = ..., submit_button: _Optional[_Union[ProfileSettingsWidget.Button, _Mapping]] = ..., cancel_button: _Optional[_Union[ProfileSettingsWidget.Button, _Mapping]] = ...) -> None: ...
    class ClickableSetting(_message.Message):
        __slots__ = ("title", "description", "selected_language", "actions")
        TITLE_FIELD_NUMBER: _ClassVar[int]
        DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
        SELECTED_LANGUAGE_FIELD_NUMBER: _ClassVar[int]
        ACTIONS_FIELD_NUMBER: _ClassVar[int]
        title: str
        description: str
        selected_language: str
        actions: _actions_pb2.Actions
        def __init__(self, title: _Optional[str] = ..., description: _Optional[str] = ..., selected_language: _Optional[str] = ..., actions: _Optional[_Union[_actions_pb2.Actions, _Mapping]] = ...) -> None: ...
    class Button(_message.Message):
        __slots__ = ("text", "actions")
        TEXT_FIELD_NUMBER: _ClassVar[int]
        ACTIONS_FIELD_NUMBER: _ClassVar[int]
        text: str
        actions: _actions_pb2.Actions
        def __init__(self, text: _Optional[str] = ..., actions: _Optional[_Union[_actions_pb2.Actions, _Mapping]] = ...) -> None: ...
    WIDGET_COMMONS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    widget_commons: _widget_commons_pb2.WidgetCommons
    data: ProfileSettingsWidget.Data
    def __init__(self, widget_commons: _Optional[_Union[_widget_commons_pb2.WidgetCommons, _Mapping]] = ..., data: _Optional[_Union[ProfileSettingsWidget.Data, _Mapping]] = ...) -> None: ...
