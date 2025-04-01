from base import template_pb2 as _template_pb2
from base import widget_commons_pb2 as _widget_commons_pb2
from base import actions_pb2 as _actions_pb2
from widget import dialog_pb2 as _dialog_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DeviceManagerWidget(_message.Message):
    __slots__ = ("widget_commons", "data")
    class DeviceType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNRECOGNZED: _ClassVar[DeviceManagerWidget.DeviceType]
        TV: _ClassVar[DeviceManagerWidget.DeviceType]
        WEB: _ClassVar[DeviceManagerWidget.DeviceType]
        MOBILE: _ClassVar[DeviceManagerWidget.DeviceType]
    UNRECOGNZED: DeviceManagerWidget.DeviceType
    TV: DeviceManagerWidget.DeviceType
    WEB: DeviceManagerWidget.DeviceType
    MOBILE: DeviceManagerWidget.DeviceType
    class Data(_message.Message):
        __slots__ = ("device_lists", "message")
        DEVICE_LISTS_FIELD_NUMBER: _ClassVar[int]
        MESSAGE_FIELD_NUMBER: _ClassVar[int]
        device_lists: _containers.RepeatedCompositeFieldContainer[DeviceManagerWidget.DeviceList]
        message: str
        def __init__(self, device_lists: _Optional[_Iterable[_Union[DeviceManagerWidget.DeviceList, _Mapping]]] = ..., message: _Optional[str] = ...) -> None: ...
    class DeviceList(_message.Message):
        __slots__ = ("title", "devices_info", "dialog")
        TITLE_FIELD_NUMBER: _ClassVar[int]
        DEVICES_INFO_FIELD_NUMBER: _ClassVar[int]
        DIALOG_FIELD_NUMBER: _ClassVar[int]
        title: str
        devices_info: _containers.RepeatedCompositeFieldContainer[DeviceManagerWidget.DeviceInfoItems]
        dialog: _dialog_pb2.DialogWidget
        def __init__(self, title: _Optional[str] = ..., devices_info: _Optional[_Iterable[_Union[DeviceManagerWidget.DeviceInfoItems, _Mapping]]] = ..., dialog: _Optional[_Union[_dialog_pb2.DialogWidget, _Mapping]] = ...) -> None: ...
    class DeviceInfoItems(_message.Message):
        __slots__ = ("device_name", "device_location", "is_active", "device_status", "device_type", "logout_button", "session_id", "device_id")
        DEVICE_NAME_FIELD_NUMBER: _ClassVar[int]
        DEVICE_LOCATION_FIELD_NUMBER: _ClassVar[int]
        IS_ACTIVE_FIELD_NUMBER: _ClassVar[int]
        DEVICE_STATUS_FIELD_NUMBER: _ClassVar[int]
        DEVICE_TYPE_FIELD_NUMBER: _ClassVar[int]
        LOGOUT_BUTTON_FIELD_NUMBER: _ClassVar[int]
        SESSION_ID_FIELD_NUMBER: _ClassVar[int]
        DEVICE_ID_FIELD_NUMBER: _ClassVar[int]
        device_name: str
        device_location: str
        is_active: bool
        device_status: str
        device_type: DeviceManagerWidget.DeviceType
        logout_button: DeviceManagerWidget.LogoutButton
        session_id: str
        device_id: str
        def __init__(self, device_name: _Optional[str] = ..., device_location: _Optional[str] = ..., is_active: bool = ..., device_status: _Optional[str] = ..., device_type: _Optional[_Union[DeviceManagerWidget.DeviceType, str]] = ..., logout_button: _Optional[_Union[DeviceManagerWidget.LogoutButton, _Mapping]] = ..., session_id: _Optional[str] = ..., device_id: _Optional[str] = ...) -> None: ...
    class LogoutButton(_message.Message):
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
    data: DeviceManagerWidget.Data
    def __init__(self, widget_commons: _Optional[_Union[_widget_commons_pb2.WidgetCommons, _Mapping]] = ..., data: _Optional[_Union[DeviceManagerWidget.Data, _Mapping]] = ...) -> None: ...
