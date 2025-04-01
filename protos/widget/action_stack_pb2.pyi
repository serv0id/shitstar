from base import widget_commons_pb2 as _widget_commons_pb2
from composable.elements import button_tile_pb2 as _button_tile_pb2
from composable.elements import button_tile_download_pb2 as _button_tile_download_pb2
from composable.elements import button_tile_rating_pb2 as _button_tile_rating_pb2
from composable.elements import button_tile_watchlist_pb2 as _button_tile_watchlist_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ActionStackWidget(_message.Message):
    __slots__ = ("widget_commons", "data")
    class Data(_message.Message):
        __slots__ = ("tiles",)
        TILES_FIELD_NUMBER: _ClassVar[int]
        tiles: _containers.RepeatedCompositeFieldContainer[ActionStackWidget.Tile]
        def __init__(self, tiles: _Optional[_Iterable[_Union[ActionStackWidget.Tile, _Mapping]]] = ...) -> None: ...
    class Tile(_message.Message):
        __slots__ = ("tile_button", "download_button", "watchlist_button", "rating_button")
        TILE_BUTTON_FIELD_NUMBER: _ClassVar[int]
        DOWNLOAD_BUTTON_FIELD_NUMBER: _ClassVar[int]
        WATCHLIST_BUTTON_FIELD_NUMBER: _ClassVar[int]
        RATING_BUTTON_FIELD_NUMBER: _ClassVar[int]
        tile_button: _button_tile_pb2.ButtonTile
        download_button: _button_tile_download_pb2.ButtonTileDownload
        watchlist_button: _button_tile_watchlist_pb2.ButtonTileWatchlist
        rating_button: _button_tile_rating_pb2.ButtonTileRating
        def __init__(self, tile_button: _Optional[_Union[_button_tile_pb2.ButtonTile, _Mapping]] = ..., download_button: _Optional[_Union[_button_tile_download_pb2.ButtonTileDownload, _Mapping]] = ..., watchlist_button: _Optional[_Union[_button_tile_watchlist_pb2.ButtonTileWatchlist, _Mapping]] = ..., rating_button: _Optional[_Union[_button_tile_rating_pb2.ButtonTileRating, _Mapping]] = ...) -> None: ...
    WIDGET_COMMONS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    widget_commons: _widget_commons_pb2.WidgetCommons
    data: ActionStackWidget.Data
    def __init__(self, widget_commons: _Optional[_Union[_widget_commons_pb2.WidgetCommons, _Mapping]] = ..., data: _Optional[_Union[ActionStackWidget.Data, _Mapping]] = ...) -> None: ...
