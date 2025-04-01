from base import space_data_commons_pb2 as _space_data_commons_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TabbedFeedSpaceData(_message.Message):
    __slots__ = ("space_data_commons", "data", "hide_tabbed_headers")
    class TabbedName(_message.Message):
        __slots__ = ("name",)
        NAME_FIELD_NUMBER: _ClassVar[int]
        name: str
        def __init__(self, name: _Optional[str] = ...) -> None: ...
    SPACE_DATA_COMMONS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    HIDE_TABBED_HEADERS_FIELD_NUMBER: _ClassVar[int]
    space_data_commons: _space_data_commons_pb2.SpaceDataCommons
    data: _containers.RepeatedCompositeFieldContainer[TabbedFeedSpaceData.TabbedName]
    hide_tabbed_headers: bool
    def __init__(self, space_data_commons: _Optional[_Union[_space_data_commons_pb2.SpaceDataCommons, _Mapping]] = ..., data: _Optional[_Iterable[_Union[TabbedFeedSpaceData.TabbedName, _Mapping]]] = ..., hide_tabbed_headers: bool = ...) -> None: ...
