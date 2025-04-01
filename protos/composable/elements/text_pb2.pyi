from feature.accessibility import accessibility_pb2 as _accessibility_pb2
from feature.color import color_pb2 as _color_pb2
from composable.tokens import dls_tokens_pb2 as _dls_tokens_pb2
from base import actions_pb2 as _actions_pb2
from composable.base import commons_pb2 as _commons_pb2
from composable.base import layout_traits_pb2 as _layout_traits_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Text(_message.Message):
    __slots__ = ("label", "typography", "color", "accessibility", "alignment", "composable_commons", "actions", "width")
    class Alignment(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        LEFT: _ClassVar[Text.Alignment]
        CENTER: _ClassVar[Text.Alignment]
        RIGHT: _ClassVar[Text.Alignment]
        JUSTIFIED: _ClassVar[Text.Alignment]
    LEFT: Text.Alignment
    CENTER: Text.Alignment
    RIGHT: Text.Alignment
    JUSTIFIED: Text.Alignment
    LABEL_FIELD_NUMBER: _ClassVar[int]
    TYPOGRAPHY_FIELD_NUMBER: _ClassVar[int]
    COLOR_FIELD_NUMBER: _ClassVar[int]
    ACCESSIBILITY_FIELD_NUMBER: _ClassVar[int]
    ALIGNMENT_FIELD_NUMBER: _ClassVar[int]
    COMPOSABLE_COMMONS_FIELD_NUMBER: _ClassVar[int]
    ACTIONS_FIELD_NUMBER: _ClassVar[int]
    WIDTH_FIELD_NUMBER: _ClassVar[int]
    label: str
    typography: _dls_tokens_pb2.DLSTypography
    color: _color_pb2.Color
    accessibility: _accessibility_pb2.Accessibility
    alignment: Text.Alignment
    composable_commons: _commons_pb2.ComposableCommons
    actions: _actions_pb2.Actions
    width: _layout_traits_pb2.LayoutHugFill
    def __init__(self, label: _Optional[str] = ..., typography: _Optional[_Union[_dls_tokens_pb2.DLSTypography, str]] = ..., color: _Optional[_Union[_color_pb2.Color, _Mapping]] = ..., accessibility: _Optional[_Union[_accessibility_pb2.Accessibility, _Mapping]] = ..., alignment: _Optional[_Union[Text.Alignment, str]] = ..., composable_commons: _Optional[_Union[_commons_pb2.ComposableCommons, _Mapping]] = ..., actions: _Optional[_Union[_actions_pb2.Actions, _Mapping]] = ..., width: _Optional[_Union[_layout_traits_pb2.LayoutHugFill, str]] = ...) -> None: ...
