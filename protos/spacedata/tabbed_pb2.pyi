from base import space_data_commons_pb2 as _space_data_commons_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TabbedSpaceData(_message.Message):
    __slots__ = ("space_data_commons", "tabs")
    class Tab(_message.Message):
        __slots__ = ("title", "widget_id")
        TITLE_FIELD_NUMBER: _ClassVar[int]
        WIDGET_ID_FIELD_NUMBER: _ClassVar[int]
        title: str
        widget_id: str
        def __init__(self, title: _Optional[str] = ..., widget_id: _Optional[str] = ...) -> None: ...
    SPACE_DATA_COMMONS_FIELD_NUMBER: _ClassVar[int]
    TABS_FIELD_NUMBER: _ClassVar[int]
    space_data_commons: _space_data_commons_pb2.SpaceDataCommons
    tabs: _containers.RepeatedCompositeFieldContainer[TabbedSpaceData.Tab]
    def __init__(self, space_data_commons: _Optional[_Union[_space_data_commons_pb2.SpaceDataCommons, _Mapping]] = ..., tabs: _Optional[_Iterable[_Union[TabbedSpaceData.Tab, _Mapping]]] = ...) -> None: ...
