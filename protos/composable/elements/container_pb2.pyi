from composable.elements import composable_pb2 as _composable_pb2
from feature.color import color_pb2 as _color_pb2
from composable.base import commons_pb2 as _commons_pb2
from composable.tokens import dls_tokens_pb2 as _dls_tokens_pb2
from base import actions_pb2 as _actions_pb2
from composable.base import corner_radius_pb2 as _corner_radius_pb2
from composable.base import layout_traits_pb2 as _layout_traits_pb2
from composable.base import dimension_constraint_pb2 as _dimension_constraint_pb2
from composable.base import edges_pb2 as _edges_pb2
from composable.base import border_pb2 as _border_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Container(_message.Message):
    __slots__ = ("composable_commons", "layout", "layout_sizing_horizontal", "layout_sizing_vertical", "width_constraint", "height_constraint", "primary_axis_alignment", "counter_axis_alignment", "gap", "padding", "background_color", "border", "corner_radius", "children", "actions")
    class Layout(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        HORIZONTAL: _ClassVar[Container.Layout]
        VERTICAL: _ClassVar[Container.Layout]
    HORIZONTAL: Container.Layout
    VERTICAL: Container.Layout
    class PrimaryAxisAlignment(_message.Message):
        __slots__ = ("alignment",)
        class Alignment(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            MIN: _ClassVar[Container.PrimaryAxisAlignment.Alignment]
            MAX: _ClassVar[Container.PrimaryAxisAlignment.Alignment]
            CENTER: _ClassVar[Container.PrimaryAxisAlignment.Alignment]
            SPACE_BETWEEN: _ClassVar[Container.PrimaryAxisAlignment.Alignment]
        MIN: Container.PrimaryAxisAlignment.Alignment
        MAX: Container.PrimaryAxisAlignment.Alignment
        CENTER: Container.PrimaryAxisAlignment.Alignment
        SPACE_BETWEEN: Container.PrimaryAxisAlignment.Alignment
        ALIGNMENT_FIELD_NUMBER: _ClassVar[int]
        alignment: Container.PrimaryAxisAlignment.Alignment
        def __init__(self, alignment: _Optional[_Union[Container.PrimaryAxisAlignment.Alignment, str]] = ...) -> None: ...
    class CounterAxisAlignment(_message.Message):
        __slots__ = ("alignment",)
        class Alignment(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            MIN: _ClassVar[Container.CounterAxisAlignment.Alignment]
            MAX: _ClassVar[Container.CounterAxisAlignment.Alignment]
            CENTER: _ClassVar[Container.CounterAxisAlignment.Alignment]
        MIN: Container.CounterAxisAlignment.Alignment
        MAX: Container.CounterAxisAlignment.Alignment
        CENTER: Container.CounterAxisAlignment.Alignment
        ALIGNMENT_FIELD_NUMBER: _ClassVar[int]
        alignment: Container.CounterAxisAlignment.Alignment
        def __init__(self, alignment: _Optional[_Union[Container.CounterAxisAlignment.Alignment, str]] = ...) -> None: ...
    COMPOSABLE_COMMONS_FIELD_NUMBER: _ClassVar[int]
    LAYOUT_FIELD_NUMBER: _ClassVar[int]
    LAYOUT_SIZING_HORIZONTAL_FIELD_NUMBER: _ClassVar[int]
    LAYOUT_SIZING_VERTICAL_FIELD_NUMBER: _ClassVar[int]
    WIDTH_CONSTRAINT_FIELD_NUMBER: _ClassVar[int]
    HEIGHT_CONSTRAINT_FIELD_NUMBER: _ClassVar[int]
    PRIMARY_AXIS_ALIGNMENT_FIELD_NUMBER: _ClassVar[int]
    COUNTER_AXIS_ALIGNMENT_FIELD_NUMBER: _ClassVar[int]
    GAP_FIELD_NUMBER: _ClassVar[int]
    PADDING_FIELD_NUMBER: _ClassVar[int]
    BACKGROUND_COLOR_FIELD_NUMBER: _ClassVar[int]
    BORDER_FIELD_NUMBER: _ClassVar[int]
    CORNER_RADIUS_FIELD_NUMBER: _ClassVar[int]
    CHILDREN_FIELD_NUMBER: _ClassVar[int]
    ACTIONS_FIELD_NUMBER: _ClassVar[int]
    composable_commons: _commons_pb2.ComposableCommons
    layout: Container.Layout
    layout_sizing_horizontal: Container.Layout
    layout_sizing_vertical: Container.Layout
    width_constraint: _dimension_constraint_pb2.DimensionConstraint
    height_constraint: _dimension_constraint_pb2.DimensionConstraint
    primary_axis_alignment: Container.PrimaryAxisAlignment
    counter_axis_alignment: Container.CounterAxisAlignment
    gap: _dls_tokens_pb2.DLSSpacings
    padding: _edges_pb2.Edges
    background_color: _color_pb2.Color
    border: _border_pb2.Border
    corner_radius: _corner_radius_pb2.CornerRadius
    children: _containers.RepeatedCompositeFieldContainer[_composable_pb2.Composable]
    actions: _actions_pb2.Actions
    def __init__(self, composable_commons: _Optional[_Union[_commons_pb2.ComposableCommons, _Mapping]] = ..., layout: _Optional[_Union[Container.Layout, str]] = ..., layout_sizing_horizontal: _Optional[_Union[Container.Layout, str]] = ..., layout_sizing_vertical: _Optional[_Union[Container.Layout, str]] = ..., width_constraint: _Optional[_Union[_dimension_constraint_pb2.DimensionConstraint, _Mapping]] = ..., height_constraint: _Optional[_Union[_dimension_constraint_pb2.DimensionConstraint, _Mapping]] = ..., primary_axis_alignment: _Optional[_Union[Container.PrimaryAxisAlignment, _Mapping]] = ..., counter_axis_alignment: _Optional[_Union[Container.CounterAxisAlignment, _Mapping]] = ..., gap: _Optional[_Union[_dls_tokens_pb2.DLSSpacings, str]] = ..., padding: _Optional[_Union[_edges_pb2.Edges, _Mapping]] = ..., background_color: _Optional[_Union[_color_pb2.Color, _Mapping]] = ..., border: _Optional[_Union[_border_pb2.Border, _Mapping]] = ..., corner_radius: _Optional[_Union[_corner_radius_pb2.CornerRadius, _Mapping]] = ..., children: _Optional[_Iterable[_Union[_composable_pb2.Composable, _Mapping]]] = ..., actions: _Optional[_Union[_actions_pb2.Actions, _Mapping]] = ...) -> None: ...
