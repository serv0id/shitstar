from base import actions_pb2 as _actions_pb2
from feature.accessibility import accessibility_pb2 as _accessibility_pb2
from composable.elements import icon_pb2 as _icon_pb2
from composable.elements import button_pb2 as _button_pb2
from composable.base import corner_radius_pb2 as _corner_radius_pb2
from composable.base import commons_pb2 as _commons_pb2
from composable.base import edges_pb2 as _edges_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ButtonIcon(_message.Message):
    __slots__ = ("composable_commons", "view")
    COMPOSABLE_COMMONS_FIELD_NUMBER: _ClassVar[int]
    VIEW_FIELD_NUMBER: _ClassVar[int]
    composable_commons: _commons_pb2.ComposableCommons
    view: ButtonIconView
    def __init__(self, composable_commons: _Optional[_Union[_commons_pb2.ComposableCommons, _Mapping]] = ..., view: _Optional[_Union[ButtonIconView, _Mapping]] = ...) -> None: ...

class ButtonIconView(_message.Message):
    __slots__ = ("icon", "type", "corner_radius", "padding", "accessibility", "actions")
    ICON_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    CORNER_RADIUS_FIELD_NUMBER: _ClassVar[int]
    PADDING_FIELD_NUMBER: _ClassVar[int]
    ACCESSIBILITY_FIELD_NUMBER: _ClassVar[int]
    ACTIONS_FIELD_NUMBER: _ClassVar[int]
    icon: _icon_pb2.Icon
    type: _button_pb2.ButtonType
    corner_radius: _corner_radius_pb2.CornerRadius
    padding: _edges_pb2.Edges
    accessibility: _accessibility_pb2.Accessibility
    actions: _actions_pb2.Actions
    def __init__(self, icon: _Optional[_Union[_icon_pb2.Icon, _Mapping]] = ..., type: _Optional[_Union[_button_pb2.ButtonType, str]] = ..., corner_radius: _Optional[_Union[_corner_radius_pb2.CornerRadius, _Mapping]] = ..., padding: _Optional[_Union[_edges_pb2.Edges, _Mapping]] = ..., accessibility: _Optional[_Union[_accessibility_pb2.Accessibility, _Mapping]] = ..., actions: _Optional[_Union[_actions_pb2.Actions, _Mapping]] = ...) -> None: ...
