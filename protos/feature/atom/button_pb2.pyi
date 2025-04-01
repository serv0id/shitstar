from base import actions_pb2 as _actions_pb2
from feature.accessibility import accessibility_pb2 as _accessibility_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Button(_message.Message):
    __slots__ = ("button_type", "data", "actions", "selected_state_data", "selected_state_actions", "is_selected")
    class ButtonType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        DEFAULT: _ClassVar[Button.ButtonType]
        INVERSE: _ClassVar[Button.ButtonType]
        SUBTLE: _ClassVar[Button.ButtonType]
        GHOST: _ClassVar[Button.ButtonType]
        ICON: _ClassVar[Button.ButtonType]
        CHIP: _ClassVar[Button.ButtonType]
        TRANSLUCENT: _ClassVar[Button.ButtonType]
        ICON_SUBTLE: _ClassVar[Button.ButtonType]
    DEFAULT: Button.ButtonType
    INVERSE: Button.ButtonType
    SUBTLE: Button.ButtonType
    GHOST: Button.ButtonType
    ICON: Button.ButtonType
    CHIP: Button.ButtonType
    TRANSLUCENT: Button.ButtonType
    ICON_SUBTLE: Button.ButtonType
    class Data(_message.Message):
        __slots__ = ("text", "sub_text", "leading_icon", "trailing_icon", "alt")
        TEXT_FIELD_NUMBER: _ClassVar[int]
        SUB_TEXT_FIELD_NUMBER: _ClassVar[int]
        LEADING_ICON_FIELD_NUMBER: _ClassVar[int]
        TRAILING_ICON_FIELD_NUMBER: _ClassVar[int]
        ALT_FIELD_NUMBER: _ClassVar[int]
        text: str
        sub_text: str
        leading_icon: str
        trailing_icon: str
        alt: _accessibility_pb2.Accessibility
        def __init__(self, text: _Optional[str] = ..., sub_text: _Optional[str] = ..., leading_icon: _Optional[str] = ..., trailing_icon: _Optional[str] = ..., alt: _Optional[_Union[_accessibility_pb2.Accessibility, _Mapping]] = ...) -> None: ...
    BUTTON_TYPE_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    ACTIONS_FIELD_NUMBER: _ClassVar[int]
    SELECTED_STATE_DATA_FIELD_NUMBER: _ClassVar[int]
    SELECTED_STATE_ACTIONS_FIELD_NUMBER: _ClassVar[int]
    IS_SELECTED_FIELD_NUMBER: _ClassVar[int]
    button_type: Button.ButtonType
    data: Button.Data
    actions: _actions_pb2.Actions
    selected_state_data: Button.Data
    selected_state_actions: _actions_pb2.Actions
    is_selected: bool
    def __init__(self, button_type: _Optional[_Union[Button.ButtonType, str]] = ..., data: _Optional[_Union[Button.Data, _Mapping]] = ..., actions: _Optional[_Union[_actions_pb2.Actions, _Mapping]] = ..., selected_state_data: _Optional[_Union[Button.Data, _Mapping]] = ..., selected_state_actions: _Optional[_Union[_actions_pb2.Actions, _Mapping]] = ..., is_selected: bool = ...) -> None: ...
