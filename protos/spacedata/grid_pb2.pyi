from base import space_data_commons_pb2 as _space_data_commons_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GridSpaceData(_message.Message):
    __slots__ = ("space_data_commons", "grid_title", "column_number", "more_grid_items_url")
    SPACE_DATA_COMMONS_FIELD_NUMBER: _ClassVar[int]
    GRID_TITLE_FIELD_NUMBER: _ClassVar[int]
    COLUMN_NUMBER_FIELD_NUMBER: _ClassVar[int]
    MORE_GRID_ITEMS_URL_FIELD_NUMBER: _ClassVar[int]
    space_data_commons: _space_data_commons_pb2.SpaceDataCommons
    grid_title: str
    column_number: int
    more_grid_items_url: str
    def __init__(self, space_data_commons: _Optional[_Union[_space_data_commons_pb2.SpaceDataCommons, _Mapping]] = ..., grid_title: _Optional[str] = ..., column_number: _Optional[int] = ..., more_grid_items_url: _Optional[str] = ...) -> None: ...
