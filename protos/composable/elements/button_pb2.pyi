from base import actions_pb2 as _actions_pb2
from feature.accessibility import accessibility_pb2 as _accessibility_pb2
from composable.elements import icon_pb2 as _icon_pb2
from feature.cw import cw_info_pb2 as _cw_info_pb2
from composable.elements import text_pb2 as _text_pb2
from feature.color import color_pb2 as _color_pb2
from composable.base import commons_pb2 as _commons_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ButtonType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    BRAND: _ClassVar[ButtonType]
    INVERSE: _ClassVar[ButtonType]
    SUBTLE: _ClassVar[ButtonType]
    TRANSLUCENT: _ClassVar[ButtonType]
    TRANSPARENT: _ClassVar[ButtonType]
BRAND: ButtonType
INVERSE: ButtonType
SUBTLE: ButtonType
TRANSLUCENT: ButtonType
TRANSPARENT: ButtonType

class Button(_message.Message):
    __slots__ = ("composable_commons", "view")
    COMPOSABLE_COMMONS_FIELD_NUMBER: _ClassVar[int]
    VIEW_FIELD_NUMBER: _ClassVar[int]
    composable_commons: _commons_pb2.ComposableCommons
    view: ButtonView
    def __init__(self, composable_commons: _Optional[_Union[_commons_pb2.ComposableCommons, _Mapping]] = ..., view: _Optional[_Union[ButtonView, _Mapping]] = ...) -> None: ...

class ProgressInfo(_message.Message):
    __slots__ = ("cw_info", "progress")
    CW_INFO_FIELD_NUMBER: _ClassVar[int]
    PROGRESS_FIELD_NUMBER: _ClassVar[int]
    cw_info: _cw_info_pb2.CwInfo
    progress: Progress
    def __init__(self, cw_info: _Optional[_Union[_cw_info_pb2.CwInfo, _Mapping]] = ..., progress: _Optional[_Union[Progress, _Mapping]] = ...) -> None: ...

class Progress(_message.Message):
    __slots__ = ("ratio",)
    RATIO_FIELD_NUMBER: _ClassVar[int]
    ratio: float
    def __init__(self, ratio: _Optional[float] = ...) -> None: ...

class ButtonView(_message.Message):
    __slots__ = ("label", "sub_label", "leading_icon", "trailing_icon", "type", "accessibility", "seekbarColor", "actions", "progress")
    LABEL_FIELD_NUMBER: _ClassVar[int]
    SUB_LABEL_FIELD_NUMBER: _ClassVar[int]
    LEADING_ICON_FIELD_NUMBER: _ClassVar[int]
    TRAILING_ICON_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    ACCESSIBILITY_FIELD_NUMBER: _ClassVar[int]
    SEEKBARCOLOR_FIELD_NUMBER: _ClassVar[int]
    ACTIONS_FIELD_NUMBER: _ClassVar[int]
    PROGRESS_FIELD_NUMBER: _ClassVar[int]
    label: _text_pb2.Text
    sub_label: _text_pb2.Text
    leading_icon: _icon_pb2.Icon
    trailing_icon: _icon_pb2.Icon
    type: ButtonType
    accessibility: _accessibility_pb2.Accessibility
    seekbarColor: _color_pb2.Color
    actions: _actions_pb2.Actions
    progress: ProgressInfo
    def __init__(self, label: _Optional[_Union[_text_pb2.Text, _Mapping]] = ..., sub_label: _Optional[_Union[_text_pb2.Text, _Mapping]] = ..., leading_icon: _Optional[_Union[_icon_pb2.Icon, _Mapping]] = ..., trailing_icon: _Optional[_Union[_icon_pb2.Icon, _Mapping]] = ..., type: _Optional[_Union[ButtonType, str]] = ..., accessibility: _Optional[_Union[_accessibility_pb2.Accessibility, _Mapping]] = ..., seekbarColor: _Optional[_Union[_color_pb2.Color, _Mapping]] = ..., actions: _Optional[_Union[_actions_pb2.Actions, _Mapping]] = ..., progress: _Optional[_Union[ProgressInfo, _Mapping]] = ...) -> None: ...
