from base import widget_commons_pb2 as _widget_commons_pb2
from widget import cancel_subscription_pb2 as _cancel_subscription_pb2
from base import actions_pb2 as _actions_pb2
from widget import dialog_pb2 as _dialog_pb2
from feature.atom import button_pb2 as _button_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SettingsLRWidget(_message.Message):
    __slots__ = ("widget_commons", "data")
    class Data(_message.Message):
        __slots__ = ("items", "logout_button", "debug_playback_button")
        ITEMS_FIELD_NUMBER: _ClassVar[int]
        LOGOUT_BUTTON_FIELD_NUMBER: _ClassVar[int]
        DEBUG_PLAYBACK_BUTTON_FIELD_NUMBER: _ClassVar[int]
        items: _containers.RepeatedCompositeFieldContainer[SettingsLRWidget.Item]
        logout_button: SettingsLRWidget.LogoutButton
        debug_playback_button: _button_pb2.Button
        def __init__(self, items: _Optional[_Iterable[_Union[SettingsLRWidget.Item, _Mapping]]] = ..., logout_button: _Optional[_Union[SettingsLRWidget.LogoutButton, _Mapping]] = ..., debug_playback_button: _Optional[_Union[_button_pb2.Button, _Mapping]] = ...) -> None: ...
    class Item(_message.Message):
        __slots__ = ("setting", "cancel_subscription", "footer")
        SETTING_FIELD_NUMBER: _ClassVar[int]
        CANCEL_SUBSCRIPTION_FIELD_NUMBER: _ClassVar[int]
        FOOTER_FIELD_NUMBER: _ClassVar[int]
        setting: SettingsLRWidget.Setting
        cancel_subscription: _cancel_subscription_pb2.CancelSubscriptionWidget
        footer: SettingsLRWidget.Footer
        def __init__(self, setting: _Optional[_Union[SettingsLRWidget.Setting, _Mapping]] = ..., cancel_subscription: _Optional[_Union[_cancel_subscription_pb2.CancelSubscriptionWidget, _Mapping]] = ..., footer: _Optional[_Union[SettingsLRWidget.Footer, _Mapping]] = ...) -> None: ...
    class LogoutButton(_message.Message):
        __slots__ = ("text", "actions", "dialog")
        TEXT_FIELD_NUMBER: _ClassVar[int]
        ACTIONS_FIELD_NUMBER: _ClassVar[int]
        DIALOG_FIELD_NUMBER: _ClassVar[int]
        text: str
        actions: _actions_pb2.Actions
        dialog: _dialog_pb2.DialogWidget
        def __init__(self, text: _Optional[str] = ..., actions: _Optional[_Union[_actions_pb2.Actions, _Mapping]] = ..., dialog: _Optional[_Union[_dialog_pb2.DialogWidget, _Mapping]] = ...) -> None: ...
    class Setting(_message.Message):
        __slots__ = ("title", "sub_text")
        TITLE_FIELD_NUMBER: _ClassVar[int]
        SUB_TEXT_FIELD_NUMBER: _ClassVar[int]
        title: str
        sub_text: SettingsLRWidget.SubText
        def __init__(self, title: _Optional[str] = ..., sub_text: _Optional[_Union[SettingsLRWidget.SubText, _Mapping]] = ...) -> None: ...
    class SubText(_message.Message):
        __slots__ = ("text", "list", "link_text")
        TEXT_FIELD_NUMBER: _ClassVar[int]
        LIST_FIELD_NUMBER: _ClassVar[int]
        LINK_TEXT_FIELD_NUMBER: _ClassVar[int]
        text: str
        list: _containers.RepeatedCompositeFieldContainer[SettingsLRWidget.ListItem]
        link_text: SettingsLRWidget.LinkText
        def __init__(self, text: _Optional[str] = ..., list: _Optional[_Iterable[_Union[SettingsLRWidget.ListItem, _Mapping]]] = ..., link_text: _Optional[_Union[SettingsLRWidget.LinkText, _Mapping]] = ...) -> None: ...
    class LinkText(_message.Message):
        __slots__ = ("label", "link")
        LABEL_FIELD_NUMBER: _ClassVar[int]
        LINK_FIELD_NUMBER: _ClassVar[int]
        label: str
        link: str
        def __init__(self, label: _Optional[str] = ..., link: _Optional[str] = ...) -> None: ...
    class ListItem(_message.Message):
        __slots__ = ("bullet", "text")
        BULLET_FIELD_NUMBER: _ClassVar[int]
        TEXT_FIELD_NUMBER: _ClassVar[int]
        bullet: str
        text: str
        def __init__(self, bullet: _Optional[str] = ..., text: _Optional[str] = ...) -> None: ...
    class Footer(_message.Message):
        __slots__ = ("text", "description", "app_version_text")
        TEXT_FIELD_NUMBER: _ClassVar[int]
        DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
        APP_VERSION_TEXT_FIELD_NUMBER: _ClassVar[int]
        text: _containers.RepeatedCompositeFieldContainer[SettingsLRWidget.LinkText]
        description: str
        app_version_text: str
        def __init__(self, text: _Optional[_Iterable[_Union[SettingsLRWidget.LinkText, _Mapping]]] = ..., description: _Optional[str] = ..., app_version_text: _Optional[str] = ...) -> None: ...
    WIDGET_COMMONS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    widget_commons: _widget_commons_pb2.WidgetCommons
    data: SettingsLRWidget.Data
    def __init__(self, widget_commons: _Optional[_Union[_widget_commons_pb2.WidgetCommons, _Mapping]] = ..., data: _Optional[_Union[SettingsLRWidget.Data, _Mapping]] = ...) -> None: ...
