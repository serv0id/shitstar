from base import space_data_commons_pb2 as _space_data_commons_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AdaptiveTraySpaceData(_message.Message):
    __slots__ = ("space_data_commons", "data")
    class LandscapePortraitData(_message.Message):
        __slots__ = ("landscape_trays", "portrait_trays", "portrait_header_trays", "side_sheet_trays", "portrait_footer_trays")
        LANDSCAPE_TRAYS_FIELD_NUMBER: _ClassVar[int]
        PORTRAIT_TRAYS_FIELD_NUMBER: _ClassVar[int]
        PORTRAIT_HEADER_TRAYS_FIELD_NUMBER: _ClassVar[int]
        SIDE_SHEET_TRAYS_FIELD_NUMBER: _ClassVar[int]
        PORTRAIT_FOOTER_TRAYS_FIELD_NUMBER: _ClassVar[int]
        landscape_trays: _containers.RepeatedCompositeFieldContainer[AdaptiveTraySpaceData.TrayIndex]
        portrait_trays: _containers.RepeatedCompositeFieldContainer[AdaptiveTraySpaceData.TrayIndex]
        portrait_header_trays: _containers.RepeatedCompositeFieldContainer[AdaptiveTraySpaceData.TrayIndex]
        side_sheet_trays: _containers.RepeatedCompositeFieldContainer[AdaptiveTraySpaceData.TrayIndex]
        portrait_footer_trays: _containers.RepeatedCompositeFieldContainer[AdaptiveTraySpaceData.TrayIndex]
        def __init__(self, landscape_trays: _Optional[_Iterable[_Union[AdaptiveTraySpaceData.TrayIndex, _Mapping]]] = ..., portrait_trays: _Optional[_Iterable[_Union[AdaptiveTraySpaceData.TrayIndex, _Mapping]]] = ..., portrait_header_trays: _Optional[_Iterable[_Union[AdaptiveTraySpaceData.TrayIndex, _Mapping]]] = ..., side_sheet_trays: _Optional[_Iterable[_Union[AdaptiveTraySpaceData.TrayIndex, _Mapping]]] = ..., portrait_footer_trays: _Optional[_Iterable[_Union[AdaptiveTraySpaceData.TrayIndex, _Mapping]]] = ...) -> None: ...
    class TrayIndex(_message.Message):
        __slots__ = ("id",)
        ID_FIELD_NUMBER: _ClassVar[int]
        id: str
        def __init__(self, id: _Optional[str] = ...) -> None: ...
    SPACE_DATA_COMMONS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    space_data_commons: _space_data_commons_pb2.SpaceDataCommons
    data: AdaptiveTraySpaceData.LandscapePortraitData
    def __init__(self, space_data_commons: _Optional[_Union[_space_data_commons_pb2.SpaceDataCommons, _Mapping]] = ..., data: _Optional[_Union[AdaptiveTraySpaceData.LandscapePortraitData, _Mapping]] = ...) -> None: ...
