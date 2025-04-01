from composable.elements import button_pb2 as _button_pb2
from composable.elements import button_icon_pb2 as _button_icon_pb2
from composable.elements import button_toggle_pb2 as _button_toggle_pb2
from composable.base import commons_pb2 as _commons_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ButtonStack(_message.Message):
    __slots__ = ("composable_commons", "view")
    COMPOSABLE_COMMONS_FIELD_NUMBER: _ClassVar[int]
    VIEW_FIELD_NUMBER: _ClassVar[int]
    composable_commons: _commons_pb2.ComposableCommons
    view: ButtonStackView
    def __init__(self, composable_commons: _Optional[_Union[_commons_pb2.ComposableCommons, _Mapping]] = ..., view: _Optional[_Union[ButtonStackView, _Mapping]] = ...) -> None: ...

class ButtonStackView(_message.Message):
    __slots__ = ("alignment", "padding", "shows_loading", "primary", "secondary", "secondaryButtonRatio")
    class StackAlignment(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        VERTICAL: _ClassVar[ButtonStackView.StackAlignment]
        HORIZONTAL: _ClassVar[ButtonStackView.StackAlignment]
    VERTICAL: ButtonStackView.StackAlignment
    HORIZONTAL: ButtonStackView.StackAlignment
    class ButtonPadding(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        REGULAR: _ClassVar[ButtonStackView.ButtonPadding]
        LARGE: _ClassVar[ButtonStackView.ButtonPadding]
        NONE: _ClassVar[ButtonStackView.ButtonPadding]
    REGULAR: ButtonStackView.ButtonPadding
    LARGE: ButtonStackView.ButtonPadding
    NONE: ButtonStackView.ButtonPadding
    class HorizontalAlignmentRatio(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STANDARD: _ClassVar[ButtonStackView.HorizontalAlignmentRatio]
        RIGHT_CONSTRAINED: _ClassVar[ButtonStackView.HorizontalAlignmentRatio]
        LEFT_CONSTRAINED: _ClassVar[ButtonStackView.HorizontalAlignmentRatio]
    STANDARD: ButtonStackView.HorizontalAlignmentRatio
    RIGHT_CONSTRAINED: ButtonStackView.HorizontalAlignmentRatio
    LEFT_CONSTRAINED: ButtonStackView.HorizontalAlignmentRatio
    class CTA(_message.Message):
        __slots__ = ("button", "button_toggle", "button_icon")
        BUTTON_FIELD_NUMBER: _ClassVar[int]
        BUTTON_TOGGLE_FIELD_NUMBER: _ClassVar[int]
        BUTTON_ICON_FIELD_NUMBER: _ClassVar[int]
        button: _button_pb2.Button
        button_toggle: _button_toggle_pb2.ButtonToggle
        button_icon: _button_icon_pb2.ButtonIcon
        def __init__(self, button: _Optional[_Union[_button_pb2.Button, _Mapping]] = ..., button_toggle: _Optional[_Union[_button_toggle_pb2.ButtonToggle, _Mapping]] = ..., button_icon: _Optional[_Union[_button_icon_pb2.ButtonIcon, _Mapping]] = ...) -> None: ...
    ALIGNMENT_FIELD_NUMBER: _ClassVar[int]
    PADDING_FIELD_NUMBER: _ClassVar[int]
    SHOWS_LOADING_FIELD_NUMBER: _ClassVar[int]
    PRIMARY_FIELD_NUMBER: _ClassVar[int]
    SECONDARY_FIELD_NUMBER: _ClassVar[int]
    SECONDARYBUTTONRATIO_FIELD_NUMBER: _ClassVar[int]
    alignment: ButtonStackView.StackAlignment
    padding: ButtonStackView.ButtonPadding
    shows_loading: bool
    primary: ButtonStackView.CTA
    secondary: ButtonStackView.CTA
    secondaryButtonRatio: float
    def __init__(self, alignment: _Optional[_Union[ButtonStackView.StackAlignment, str]] = ..., padding: _Optional[_Union[ButtonStackView.ButtonPadding, str]] = ..., shows_loading: bool = ..., primary: _Optional[_Union[ButtonStackView.CTA, _Mapping]] = ..., secondary: _Optional[_Union[ButtonStackView.CTA, _Mapping]] = ..., secondaryButtonRatio: _Optional[float] = ...) -> None: ...
