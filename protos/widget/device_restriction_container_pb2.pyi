from base import widget_commons_pb2 as _widget_commons_pb2
from widget import hero_pb2 as _hero_pb2
from widget import device_manager_pb2 as _device_manager_pb2
from widget import mini_banner_pb2 as _mini_banner_pb2
from widget import divider_pb2 as _divider_pb2
from base import actions_pb2 as _actions_pb2
from widget import dialog_pb2 as _dialog_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DeviceRestrictionContainerWidget(_message.Message):
    __slots__ = ("widget_commons", "data")
    class Data(_message.Message):
        __slots__ = ("back_button", "hero", "child_widget")
        BACK_BUTTON_FIELD_NUMBER: _ClassVar[int]
        HERO_FIELD_NUMBER: _ClassVar[int]
        CHILD_WIDGET_FIELD_NUMBER: _ClassVar[int]
        back_button: DeviceRestrictionContainerWidget.BackButton
        hero: _hero_pb2.HeroWidget
        child_widget: _containers.RepeatedCompositeFieldContainer[DeviceRestrictionContainerWidget.ChildWidget]
        def __init__(self, back_button: _Optional[_Union[DeviceRestrictionContainerWidget.BackButton, _Mapping]] = ..., hero: _Optional[_Union[_hero_pb2.HeroWidget, _Mapping]] = ..., child_widget: _Optional[_Iterable[_Union[DeviceRestrictionContainerWidget.ChildWidget, _Mapping]]] = ...) -> None: ...
    class ChildWidget(_message.Message):
        __slots__ = ("device_manager", "divider", "mini_banner")
        DEVICE_MANAGER_FIELD_NUMBER: _ClassVar[int]
        DIVIDER_FIELD_NUMBER: _ClassVar[int]
        MINI_BANNER_FIELD_NUMBER: _ClassVar[int]
        device_manager: _device_manager_pb2.DeviceManagerWidget
        divider: _divider_pb2.DividerWidget
        mini_banner: _mini_banner_pb2.MiniBannerWidget
        def __init__(self, device_manager: _Optional[_Union[_device_manager_pb2.DeviceManagerWidget, _Mapping]] = ..., divider: _Optional[_Union[_divider_pb2.DividerWidget, _Mapping]] = ..., mini_banner: _Optional[_Union[_mini_banner_pb2.MiniBannerWidget, _Mapping]] = ...) -> None: ...
    class BackButton(_message.Message):
        __slots__ = ("icon", "actions", "dialog")
        ICON_FIELD_NUMBER: _ClassVar[int]
        ACTIONS_FIELD_NUMBER: _ClassVar[int]
        DIALOG_FIELD_NUMBER: _ClassVar[int]
        icon: str
        actions: _actions_pb2.Actions
        dialog: _dialog_pb2.DialogWidget
        def __init__(self, icon: _Optional[str] = ..., actions: _Optional[_Union[_actions_pb2.Actions, _Mapping]] = ..., dialog: _Optional[_Union[_dialog_pb2.DialogWidget, _Mapping]] = ...) -> None: ...
    WIDGET_COMMONS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    widget_commons: _widget_commons_pb2.WidgetCommons
    data: DeviceRestrictionContainerWidget.Data
    def __init__(self, widget_commons: _Optional[_Union[_widget_commons_pb2.WidgetCommons, _Mapping]] = ..., data: _Optional[_Union[DeviceRestrictionContainerWidget.Data, _Mapping]] = ...) -> None: ...
