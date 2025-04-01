from base import widget_commons_pb2 as _widget_commons_pb2
from base import actions_pb2 as _actions_pb2
from feature.consent import consent_type_pb2 as _consent_type_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class NotificationSettingsWidget(_message.Message):
    __slots__ = ("widget_commons", "data")
    class Data(_message.Message):
        __slots__ = ("app_notification", "sms_notification", "whatsapp_notification", "email_notification", "commercial_notification")
        APP_NOTIFICATION_FIELD_NUMBER: _ClassVar[int]
        SMS_NOTIFICATION_FIELD_NUMBER: _ClassVar[int]
        WHATSAPP_NOTIFICATION_FIELD_NUMBER: _ClassVar[int]
        EMAIL_NOTIFICATION_FIELD_NUMBER: _ClassVar[int]
        COMMERCIAL_NOTIFICATION_FIELD_NUMBER: _ClassVar[int]
        app_notification: NotificationSettingsWidget.ToggleSetting
        sms_notification: NotificationSettingsWidget.ToggleSetting
        whatsapp_notification: NotificationSettingsWidget.ToggleSetting
        email_notification: NotificationSettingsWidget.ToggleSetting
        commercial_notification: NotificationSettingsWidget.ToggleSetting
        def __init__(self, app_notification: _Optional[_Union[NotificationSettingsWidget.ToggleSetting, _Mapping]] = ..., sms_notification: _Optional[_Union[NotificationSettingsWidget.ToggleSetting, _Mapping]] = ..., whatsapp_notification: _Optional[_Union[NotificationSettingsWidget.ToggleSetting, _Mapping]] = ..., email_notification: _Optional[_Union[NotificationSettingsWidget.ToggleSetting, _Mapping]] = ..., commercial_notification: _Optional[_Union[NotificationSettingsWidget.ToggleSetting, _Mapping]] = ...) -> None: ...
    class ToggleSetting(_message.Message):
        __slots__ = ("icon_name", "title", "description", "is_selected", "actions", "preference_type", "preference_version", "preference_id")
        ICON_NAME_FIELD_NUMBER: _ClassVar[int]
        TITLE_FIELD_NUMBER: _ClassVar[int]
        DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
        IS_SELECTED_FIELD_NUMBER: _ClassVar[int]
        ACTIONS_FIELD_NUMBER: _ClassVar[int]
        PREFERENCE_TYPE_FIELD_NUMBER: _ClassVar[int]
        PREFERENCE_VERSION_FIELD_NUMBER: _ClassVar[int]
        PREFERENCE_ID_FIELD_NUMBER: _ClassVar[int]
        icon_name: str
        title: str
        description: str
        is_selected: bool
        actions: _actions_pb2.Actions
        preference_type: _consent_type_pb2.ConsentType
        preference_version: int
        preference_id: str
        def __init__(self, icon_name: _Optional[str] = ..., title: _Optional[str] = ..., description: _Optional[str] = ..., is_selected: bool = ..., actions: _Optional[_Union[_actions_pb2.Actions, _Mapping]] = ..., preference_type: _Optional[_Union[_consent_type_pb2.ConsentType, str]] = ..., preference_version: _Optional[int] = ..., preference_id: _Optional[str] = ...) -> None: ...
    WIDGET_COMMONS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    widget_commons: _widget_commons_pb2.WidgetCommons
    data: NotificationSettingsWidget.Data
    def __init__(self, widget_commons: _Optional[_Union[_widget_commons_pb2.WidgetCommons, _Mapping]] = ..., data: _Optional[_Union[NotificationSettingsWidget.Data, _Mapping]] = ...) -> None: ...
