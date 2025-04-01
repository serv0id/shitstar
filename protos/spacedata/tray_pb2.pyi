from base import space_data_commons_pb2 as _space_data_commons_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TraySpaceData(_message.Message):
    __slots__ = ("space_data_commons", "next_space_url", "tabs", "tab_layout")
    class TabsLayout(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        DEFAULT: _ClassVar[TraySpaceData.TabsLayout]
        VERTICAL: _ClassVar[TraySpaceData.TabsLayout]
        HORIZONTAL: _ClassVar[TraySpaceData.TabsLayout]
    DEFAULT: TraySpaceData.TabsLayout
    VERTICAL: TraySpaceData.TabsLayout
    HORIZONTAL: TraySpaceData.TabsLayout
    class Tab(_message.Message):
        __slots__ = ("title", "id")
        TITLE_FIELD_NUMBER: _ClassVar[int]
        ID_FIELD_NUMBER: _ClassVar[int]
        title: str
        id: str
        def __init__(self, title: _Optional[str] = ..., id: _Optional[str] = ...) -> None: ...
    SPACE_DATA_COMMONS_FIELD_NUMBER: _ClassVar[int]
    NEXT_SPACE_URL_FIELD_NUMBER: _ClassVar[int]
    TABS_FIELD_NUMBER: _ClassVar[int]
    TAB_LAYOUT_FIELD_NUMBER: _ClassVar[int]
    space_data_commons: _space_data_commons_pb2.SpaceDataCommons
    next_space_url: str
    tabs: _containers.RepeatedCompositeFieldContainer[TraySpaceData.Tab]
    tab_layout: TraySpaceData.TabsLayout
    def __init__(self, space_data_commons: _Optional[_Union[_space_data_commons_pb2.SpaceDataCommons, _Mapping]] = ..., next_space_url: _Optional[str] = ..., tabs: _Optional[_Iterable[_Union[TraySpaceData.Tab, _Mapping]]] = ..., tab_layout: _Optional[_Union[TraySpaceData.TabsLayout, str]] = ...) -> None: ...
