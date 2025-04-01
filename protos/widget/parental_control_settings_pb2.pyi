from base import widget_commons_pb2 as _widget_commons_pb2
from base import actions_pb2 as _actions_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ParentalControlSettingsWidget(_message.Message):
    __slots__ = ("widget_commons", "data")
    class Data(_message.Message):
        __slots__ = ("parental_lock", "viewing_restrictions", "change_parental_lock_pin", "title", "actions", "recaptcha_enabled")
        PARENTAL_LOCK_FIELD_NUMBER: _ClassVar[int]
        VIEWING_RESTRICTIONS_FIELD_NUMBER: _ClassVar[int]
        CHANGE_PARENTAL_LOCK_PIN_FIELD_NUMBER: _ClassVar[int]
        TITLE_FIELD_NUMBER: _ClassVar[int]
        ACTIONS_FIELD_NUMBER: _ClassVar[int]
        RECAPTCHA_ENABLED_FIELD_NUMBER: _ClassVar[int]
        parental_lock: ParentalControlSettingsWidget.ToggleSetting
        viewing_restrictions: ParentalControlSettingsWidget.ClickableSetting
        change_parental_lock_pin: ParentalControlSettingsWidget.ClickableSetting
        title: str
        actions: _actions_pb2.Actions
        recaptcha_enabled: bool
        def __init__(self, parental_lock: _Optional[_Union[ParentalControlSettingsWidget.ToggleSetting, _Mapping]] = ..., viewing_restrictions: _Optional[_Union[ParentalControlSettingsWidget.ClickableSetting, _Mapping]] = ..., change_parental_lock_pin: _Optional[_Union[ParentalControlSettingsWidget.ClickableSetting, _Mapping]] = ..., title: _Optional[str] = ..., actions: _Optional[_Union[_actions_pb2.Actions, _Mapping]] = ..., recaptcha_enabled: bool = ...) -> None: ...
    class ToggleSetting(_message.Message):
        __slots__ = ("icon_name", "title", "description", "is_selected", "actions", "status_label", "enabled_label", "disabled_label", "turn_off_action", "turn_on_action")
        ICON_NAME_FIELD_NUMBER: _ClassVar[int]
        TITLE_FIELD_NUMBER: _ClassVar[int]
        DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
        IS_SELECTED_FIELD_NUMBER: _ClassVar[int]
        ACTIONS_FIELD_NUMBER: _ClassVar[int]
        STATUS_LABEL_FIELD_NUMBER: _ClassVar[int]
        ENABLED_LABEL_FIELD_NUMBER: _ClassVar[int]
        DISABLED_LABEL_FIELD_NUMBER: _ClassVar[int]
        TURN_OFF_ACTION_FIELD_NUMBER: _ClassVar[int]
        TURN_ON_ACTION_FIELD_NUMBER: _ClassVar[int]
        icon_name: str
        title: str
        description: str
        is_selected: bool
        actions: _actions_pb2.Actions
        status_label: str
        enabled_label: str
        disabled_label: str
        turn_off_action: _actions_pb2.Actions
        turn_on_action: _actions_pb2.Actions
        def __init__(self, icon_name: _Optional[str] = ..., title: _Optional[str] = ..., description: _Optional[str] = ..., is_selected: bool = ..., actions: _Optional[_Union[_actions_pb2.Actions, _Mapping]] = ..., status_label: _Optional[str] = ..., enabled_label: _Optional[str] = ..., disabled_label: _Optional[str] = ..., turn_off_action: _Optional[_Union[_actions_pb2.Actions, _Mapping]] = ..., turn_on_action: _Optional[_Union[_actions_pb2.Actions, _Mapping]] = ...) -> None: ...
    class ClickableSetting(_message.Message):
        __slots__ = ("title", "description", "actions")
        TITLE_FIELD_NUMBER: _ClassVar[int]
        DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
        ACTIONS_FIELD_NUMBER: _ClassVar[int]
        title: str
        description: str
        actions: _actions_pb2.Actions
        def __init__(self, title: _Optional[str] = ..., description: _Optional[str] = ..., actions: _Optional[_Union[_actions_pb2.Actions, _Mapping]] = ...) -> None: ...
    WIDGET_COMMONS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    widget_commons: _widget_commons_pb2.WidgetCommons
    data: ParentalControlSettingsWidget.Data
    def __init__(self, widget_commons: _Optional[_Union[_widget_commons_pb2.WidgetCommons, _Mapping]] = ..., data: _Optional[_Union[ParentalControlSettingsWidget.Data, _Mapping]] = ...) -> None: ...
