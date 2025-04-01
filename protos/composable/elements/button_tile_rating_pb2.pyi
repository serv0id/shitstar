from base import actions_pb2 as _actions_pb2
from composable.elements import button_tile_pb2 as _button_tile_pb2
from google.protobuf import any_pb2 as _any_pb2
from composable.base import commons_pb2 as _commons_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ButtonTileRating(_message.Message):
    __slots__ = ("states", "tooltip_action_menu_widget", "content_id", "composable_commons", "actions", "is_rated")
    class RatingButtonStates(_message.Message):
        __slots__ = ("default", "rated")
        DEFAULT_FIELD_NUMBER: _ClassVar[int]
        RATED_FIELD_NUMBER: _ClassVar[int]
        default: _button_tile_pb2.ButtonTileView
        rated: _button_tile_pb2.ButtonTileView
        def __init__(self, default: _Optional[_Union[_button_tile_pb2.ButtonTileView, _Mapping]] = ..., rated: _Optional[_Union[_button_tile_pb2.ButtonTileView, _Mapping]] = ...) -> None: ...
    STATES_FIELD_NUMBER: _ClassVar[int]
    TOOLTIP_ACTION_MENU_WIDGET_FIELD_NUMBER: _ClassVar[int]
    CONTENT_ID_FIELD_NUMBER: _ClassVar[int]
    COMPOSABLE_COMMONS_FIELD_NUMBER: _ClassVar[int]
    ACTIONS_FIELD_NUMBER: _ClassVar[int]
    IS_RATED_FIELD_NUMBER: _ClassVar[int]
    states: ButtonTileRating.RatingButtonStates
    tooltip_action_menu_widget: _any_pb2.Any
    content_id: str
    composable_commons: _commons_pb2.ComposableCommons
    actions: _actions_pb2.Actions
    is_rated: bool
    def __init__(self, states: _Optional[_Union[ButtonTileRating.RatingButtonStates, _Mapping]] = ..., tooltip_action_menu_widget: _Optional[_Union[_any_pb2.Any, _Mapping]] = ..., content_id: _Optional[str] = ..., composable_commons: _Optional[_Union[_commons_pb2.ComposableCommons, _Mapping]] = ..., actions: _Optional[_Union[_actions_pb2.Actions, _Mapping]] = ..., is_rated: bool = ...) -> None: ...
