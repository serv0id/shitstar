from base import template_pb2 as _template_pb2
from base import widget_commons_pb2 as _widget_commons_pb2
from base import actions_pb2 as _actions_pb2
from widget import logo_pb2 as _logo_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SubscriptionsHeaderWidget(_message.Message):
    __slots__ = ("template", "widget_commons", "data")
    class Data(_message.Message):
        __slots__ = ("help_setting_button", "subscriptions", "logo")
        HELP_SETTING_BUTTON_FIELD_NUMBER: _ClassVar[int]
        SUBSCRIPTIONS_FIELD_NUMBER: _ClassVar[int]
        LOGO_FIELD_NUMBER: _ClassVar[int]
        help_setting_button: SubscriptionsHeaderWidget.HelpSettingButton
        subscriptions: _containers.RepeatedCompositeFieldContainer[SubscriptionsHeaderWidget.SubscriptionDetail]
        logo: _logo_pb2.LogoWidget
        def __init__(self, help_setting_button: _Optional[_Union[SubscriptionsHeaderWidget.HelpSettingButton, _Mapping]] = ..., subscriptions: _Optional[_Iterable[_Union[SubscriptionsHeaderWidget.SubscriptionDetail, _Mapping]]] = ..., logo: _Optional[_Union[_logo_pb2.LogoWidget, _Mapping]] = ...) -> None: ...
    class HelpSettingButton(_message.Message):
        __slots__ = ("text", "actions")
        TEXT_FIELD_NUMBER: _ClassVar[int]
        ACTIONS_FIELD_NUMBER: _ClassVar[int]
        text: str
        actions: _actions_pb2.Actions
        def __init__(self, text: _Optional[str] = ..., actions: _Optional[_Union[_actions_pb2.Actions, _Mapping]] = ...) -> None: ...
    class SubscriptionDetail(_message.Message):
        __slots__ = ("id", "plan_name", "mobile_number", "number_of_logged_in_devices", "device_logged_in_text", "manage_button")
        ID_FIELD_NUMBER: _ClassVar[int]
        PLAN_NAME_FIELD_NUMBER: _ClassVar[int]
        MOBILE_NUMBER_FIELD_NUMBER: _ClassVar[int]
        NUMBER_OF_LOGGED_IN_DEVICES_FIELD_NUMBER: _ClassVar[int]
        DEVICE_LOGGED_IN_TEXT_FIELD_NUMBER: _ClassVar[int]
        MANAGE_BUTTON_FIELD_NUMBER: _ClassVar[int]
        id: str
        plan_name: str
        mobile_number: str
        number_of_logged_in_devices: int
        device_logged_in_text: str
        manage_button: SubscriptionsHeaderWidget.ManageButton
        def __init__(self, id: _Optional[str] = ..., plan_name: _Optional[str] = ..., mobile_number: _Optional[str] = ..., number_of_logged_in_devices: _Optional[int] = ..., device_logged_in_text: _Optional[str] = ..., manage_button: _Optional[_Union[SubscriptionsHeaderWidget.ManageButton, _Mapping]] = ...) -> None: ...
    class ManageButton(_message.Message):
        __slots__ = ("text", "actions")
        TEXT_FIELD_NUMBER: _ClassVar[int]
        ACTIONS_FIELD_NUMBER: _ClassVar[int]
        text: str
        actions: _actions_pb2.Actions
        def __init__(self, text: _Optional[str] = ..., actions: _Optional[_Union[_actions_pb2.Actions, _Mapping]] = ...) -> None: ...
    TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    WIDGET_COMMONS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    template: _template_pb2.Template
    widget_commons: _widget_commons_pb2.WidgetCommons
    data: SubscriptionsHeaderWidget.Data
    def __init__(self, template: _Optional[_Union[_template_pb2.Template, _Mapping]] = ..., widget_commons: _Optional[_Union[_widget_commons_pb2.WidgetCommons, _Mapping]] = ..., data: _Optional[_Union[SubscriptionsHeaderWidget.Data, _Mapping]] = ...) -> None: ...
