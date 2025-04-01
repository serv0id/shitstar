from widget import header_pb2 as _header_pb2
from widget import hero_gec_pb2 as _hero_gec_pb2
from base import widget_commons_pb2 as _widget_commons_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class VerticalContentCardCollectionWidget(_message.Message):
    __slots__ = ("widget_commons", "data")
    class Data(_message.Message):
        __slots__ = ("header", "items")
        HEADER_FIELD_NUMBER: _ClassVar[int]
        ITEMS_FIELD_NUMBER: _ClassVar[int]
        header: _header_pb2.HeaderWidget
        items: _containers.RepeatedCompositeFieldContainer[VerticalContentCardCollectionWidget.Item]
        def __init__(self, header: _Optional[_Union[_header_pb2.HeaderWidget, _Mapping]] = ..., items: _Optional[_Iterable[_Union[VerticalContentCardCollectionWidget.Item, _Mapping]]] = ...) -> None: ...
    class Item(_message.Message):
        __slots__ = ("hero_gec",)
        HERO_GEC_FIELD_NUMBER: _ClassVar[int]
        hero_gec: _hero_gec_pb2.HeroGECWidget
        def __init__(self, hero_gec: _Optional[_Union[_hero_gec_pb2.HeroGECWidget, _Mapping]] = ...) -> None: ...
    WIDGET_COMMONS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    widget_commons: _widget_commons_pb2.WidgetCommons
    data: VerticalContentCardCollectionWidget.Data
    def __init__(self, widget_commons: _Optional[_Union[_widget_commons_pb2.WidgetCommons, _Mapping]] = ..., data: _Optional[_Union[VerticalContentCardCollectionWidget.Data, _Mapping]] = ...) -> None: ...
