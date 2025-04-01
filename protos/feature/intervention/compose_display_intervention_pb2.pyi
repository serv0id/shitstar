from base import actions_pb2 as _actions_pb2
from feature.commons import widget_wrapper_pb2 as _widget_wrapper_pb2
from base import orientation_pb2 as _orientation_pb2
from feature.commons import alignment_pb2 as _alignment_pb2
from feature.player import player_layer_pb2 as _player_layer_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ComposeDisplayIntervention(_message.Message):
    __slots__ = ("operation",)
    class FetchSource(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        DEFAULT: _ClassVar[ComposeDisplayIntervention.FetchSource]
        CACHE_ONLY: _ClassVar[ComposeDisplayIntervention.FetchSource]
        EMBEDDED: _ClassVar[ComposeDisplayIntervention.FetchSource]
    DEFAULT: ComposeDisplayIntervention.FetchSource
    CACHE_ONLY: ComposeDisplayIntervention.FetchSource
    EMBEDDED: ComposeDisplayIntervention.FetchSource
    class Operation(_message.Message):
        __slots__ = ("should_perform_operation_action", "add_widget", "remove_widget")
        SHOULD_PERFORM_OPERATION_ACTION_FIELD_NUMBER: _ClassVar[int]
        ADD_WIDGET_FIELD_NUMBER: _ClassVar[int]
        REMOVE_WIDGET_FIELD_NUMBER: _ClassVar[int]
        should_perform_operation_action: _actions_pb2.WrapperAction
        add_widget: ComposeDisplayIntervention.AddWidget
        remove_widget: ComposeDisplayIntervention.RemoveWidget
        def __init__(self, should_perform_operation_action: _Optional[_Union[_actions_pb2.WrapperAction, _Mapping]] = ..., add_widget: _Optional[_Union[ComposeDisplayIntervention.AddWidget, _Mapping]] = ..., remove_widget: _Optional[_Union[ComposeDisplayIntervention.RemoveWidget, _Mapping]] = ...) -> None: ...
    class AddWidget(_message.Message):
        __slots__ = ("widget", "fetch_source", "modifier")
        WIDGET_FIELD_NUMBER: _ClassVar[int]
        FETCH_SOURCE_FIELD_NUMBER: _ClassVar[int]
        MODIFIER_FIELD_NUMBER: _ClassVar[int]
        widget: ComposeDisplayIntervention.Widget
        fetch_source: ComposeDisplayIntervention.FetchSource
        modifier: ComposeDisplayIntervention.Modifier
        def __init__(self, widget: _Optional[_Union[ComposeDisplayIntervention.Widget, _Mapping]] = ..., fetch_source: _Optional[_Union[ComposeDisplayIntervention.FetchSource, str]] = ..., modifier: _Optional[_Union[ComposeDisplayIntervention.Modifier, _Mapping]] = ...) -> None: ...
    class RemoveWidget(_message.Message):
        __slots__ = ("widget",)
        WIDGET_FIELD_NUMBER: _ClassVar[int]
        widget: ComposeDisplayIntervention.Widget
        def __init__(self, widget: _Optional[_Union[ComposeDisplayIntervention.Widget, _Mapping]] = ...) -> None: ...
    class Widget(_message.Message):
        __slots__ = ("widget_url", "widget_data")
        WIDGET_URL_FIELD_NUMBER: _ClassVar[int]
        WIDGET_DATA_FIELD_NUMBER: _ClassVar[int]
        widget_url: str
        widget_data: _widget_wrapper_pb2.WidgetWrapper
        def __init__(self, widget_url: _Optional[str] = ..., widget_data: _Optional[_Union[_widget_wrapper_pb2.WidgetWrapper, _Mapping]] = ...) -> None: ...
    class Modifier(_message.Message):
        __slots__ = ("player_layer", "orientation", "alignment")
        PLAYER_LAYER_FIELD_NUMBER: _ClassVar[int]
        ORIENTATION_FIELD_NUMBER: _ClassVar[int]
        ALIGNMENT_FIELD_NUMBER: _ClassVar[int]
        player_layer: _player_layer_pb2.PlayerLayer
        orientation: _orientation_pb2.Orientation
        alignment: _alignment_pb2.Alignment
        def __init__(self, player_layer: _Optional[_Union[_player_layer_pb2.PlayerLayer, str]] = ..., orientation: _Optional[_Union[_orientation_pb2.Orientation, str]] = ..., alignment: _Optional[_Union[_alignment_pb2.Alignment, str]] = ...) -> None: ...
    OPERATION_FIELD_NUMBER: _ClassVar[int]
    operation: ComposeDisplayIntervention.Operation
    def __init__(self, operation: _Optional[_Union[ComposeDisplayIntervention.Operation, _Mapping]] = ...) -> None: ...
