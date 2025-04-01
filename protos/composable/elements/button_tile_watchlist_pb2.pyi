from base import actions_pb2 as _actions_pb2
from composable.elements import button_tile_pb2 as _button_tile_pb2
from composable.elements import image_pb2 as _image_pb2
from composable.base import commons_pb2 as _commons_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ButtonTileWatchlist(_message.Message):
    __slots__ = ("states", "info", "actions", "thumbnail", "composable_commons")
    class WatchlistButtonStates(_message.Message):
        __slots__ = ("default", "added")
        DEFAULT_FIELD_NUMBER: _ClassVar[int]
        ADDED_FIELD_NUMBER: _ClassVar[int]
        default: _button_tile_pb2.ButtonTileView
        added: _button_tile_pb2.ButtonTileView
        def __init__(self, default: _Optional[_Union[_button_tile_pb2.ButtonTileView, _Mapping]] = ..., added: _Optional[_Union[_button_tile_pb2.ButtonTileView, _Mapping]] = ...) -> None: ...
    class WatchlistInfo(_message.Message):
        __slots__ = ("content_id", "is_watchlisted", "timestamp", "content_title")
        CONTENT_ID_FIELD_NUMBER: _ClassVar[int]
        IS_WATCHLISTED_FIELD_NUMBER: _ClassVar[int]
        TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
        CONTENT_TITLE_FIELD_NUMBER: _ClassVar[int]
        content_id: str
        is_watchlisted: bool
        timestamp: int
        content_title: str
        def __init__(self, content_id: _Optional[str] = ..., is_watchlisted: bool = ..., timestamp: _Optional[int] = ..., content_title: _Optional[str] = ...) -> None: ...
    STATES_FIELD_NUMBER: _ClassVar[int]
    INFO_FIELD_NUMBER: _ClassVar[int]
    ACTIONS_FIELD_NUMBER: _ClassVar[int]
    THUMBNAIL_FIELD_NUMBER: _ClassVar[int]
    COMPOSABLE_COMMONS_FIELD_NUMBER: _ClassVar[int]
    states: ButtonTileWatchlist.WatchlistButtonStates
    info: ButtonTileWatchlist.WatchlistInfo
    actions: _actions_pb2.Actions
    thumbnail: _image_pb2.Image.Source
    composable_commons: _commons_pb2.ComposableCommons
    def __init__(self, states: _Optional[_Union[ButtonTileWatchlist.WatchlistButtonStates, _Mapping]] = ..., info: _Optional[_Union[ButtonTileWatchlist.WatchlistInfo, _Mapping]] = ..., actions: _Optional[_Union[_actions_pb2.Actions, _Mapping]] = ..., thumbnail: _Optional[_Union[_image_pb2.Image.Source, _Mapping]] = ..., composable_commons: _Optional[_Union[_commons_pb2.ComposableCommons, _Mapping]] = ...) -> None: ...
