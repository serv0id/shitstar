from base import widget_commons_pb2 as _widget_commons_pb2
from widget import settings_tab_pb2 as _settings_tab_pb2
from widget import dialog_pb2 as _dialog_pb2
from base import actions_pb2 as _actions_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TabGroupWidget(_message.Message):
    __slots__ = ("widget_commons", "data")
    class Data(_message.Message):
        __slots__ = ("tabs", "logout_button", "title", "recaptcha_enabled")
        TABS_FIELD_NUMBER: _ClassVar[int]
        LOGOUT_BUTTON_FIELD_NUMBER: _ClassVar[int]
        TITLE_FIELD_NUMBER: _ClassVar[int]
        RECAPTCHA_ENABLED_FIELD_NUMBER: _ClassVar[int]
        tabs: _containers.RepeatedCompositeFieldContainer[_settings_tab_pb2.SettingsTabWidget]
        logout_button: TabGroupWidget.Button
        title: str
        recaptcha_enabled: bool
        def __init__(self, tabs: _Optional[_Iterable[_Union[_settings_tab_pb2.SettingsTabWidget, _Mapping]]] = ..., logout_button: _Optional[_Union[TabGroupWidget.Button, _Mapping]] = ..., title: _Optional[str] = ..., recaptcha_enabled: bool = ...) -> None: ...
    class Button(_message.Message):
        __slots__ = ("text", "actions", "dialog")
        TEXT_FIELD_NUMBER: _ClassVar[int]
        ACTIONS_FIELD_NUMBER: _ClassVar[int]
        DIALOG_FIELD_NUMBER: _ClassVar[int]
        text: str
        actions: _actions_pb2.Actions
        dialog: _dialog_pb2.DialogWidget
        def __init__(self, text: _Optional[str] = ..., actions: _Optional[_Union[_actions_pb2.Actions, _Mapping]] = ..., dialog: _Optional[_Union[_dialog_pb2.DialogWidget, _Mapping]] = ...) -> None: ...
    WIDGET_COMMONS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    widget_commons: _widget_commons_pb2.WidgetCommons
    data: TabGroupWidget.Data
    def __init__(self, widget_commons: _Optional[_Union[_widget_commons_pb2.WidgetCommons, _Mapping]] = ..., data: _Optional[_Union[TabGroupWidget.Data, _Mapping]] = ...) -> None: ...
