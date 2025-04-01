from composable.elements import button_pb2 as _button_pb2
from composable.elements import button_icon_pb2 as _button_icon_pb2
from composable.base import commons_pb2 as _commons_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ToggleEventType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    UNSPECIFIED: _ClassVar[ToggleEventType]
    REMIND_ME: _ClassVar[ToggleEventType]
UNSPECIFIED: ToggleEventType
REMIND_ME: ToggleEventType

class ButtonToggle(_message.Message):
    __slots__ = ("composable_commons", "toggle_off_button", "toggle_on_button", "is_toggled_on", "event_type", "identifier")
    class ToggleView(_message.Message):
        __slots__ = ("button_view", "icon_view")
        BUTTON_VIEW_FIELD_NUMBER: _ClassVar[int]
        ICON_VIEW_FIELD_NUMBER: _ClassVar[int]
        button_view: _button_pb2.ButtonView
        icon_view: _button_icon_pb2.ButtonIconView
        def __init__(self, button_view: _Optional[_Union[_button_pb2.ButtonView, _Mapping]] = ..., icon_view: _Optional[_Union[_button_icon_pb2.ButtonIconView, _Mapping]] = ...) -> None: ...
    COMPOSABLE_COMMONS_FIELD_NUMBER: _ClassVar[int]
    TOGGLE_OFF_BUTTON_FIELD_NUMBER: _ClassVar[int]
    TOGGLE_ON_BUTTON_FIELD_NUMBER: _ClassVar[int]
    IS_TOGGLED_ON_FIELD_NUMBER: _ClassVar[int]
    EVENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    composable_commons: _commons_pb2.ComposableCommons
    toggle_off_button: ButtonToggle.ToggleView
    toggle_on_button: ButtonToggle.ToggleView
    is_toggled_on: bool
    event_type: ToggleEventType
    identifier: str
    def __init__(self, composable_commons: _Optional[_Union[_commons_pb2.ComposableCommons, _Mapping]] = ..., toggle_off_button: _Optional[_Union[ButtonToggle.ToggleView, _Mapping]] = ..., toggle_on_button: _Optional[_Union[ButtonToggle.ToggleView, _Mapping]] = ..., is_toggled_on: bool = ..., event_type: _Optional[_Union[ToggleEventType, str]] = ..., identifier: _Optional[str] = ...) -> None: ...
