from base import widget_commons_pb2 as _widget_commons_pb2
from feature.search import badge_pb2 as _badge_pb2
from widget import horizontal_content_card_pb2 as _horizontal_content_card_pb2
from widget import vertical_content_poster_pb2 as _vertical_content_poster_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class KlotskiGridWidget(_message.Message):
    __slots__ = ("widget_commons", "data")
    class BlockType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        DEFAULT_TYPE: _ClassVar[KlotskiGridWidget.BlockType]
        VERTICAL: _ClassVar[KlotskiGridWidget.BlockType]
        HORIZONTAL: _ClassVar[KlotskiGridWidget.BlockType]
    DEFAULT_TYPE: KlotskiGridWidget.BlockType
    VERTICAL: KlotskiGridWidget.BlockType
    HORIZONTAL: KlotskiGridWidget.BlockType
    class WidgetAlignment(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        DEFAULT: _ClassVar[KlotskiGridWidget.WidgetAlignment]
        LEFT: _ClassVar[KlotskiGridWidget.WidgetAlignment]
        RIGHT: _ClassVar[KlotskiGridWidget.WidgetAlignment]
    DEFAULT: KlotskiGridWidget.WidgetAlignment
    LEFT: KlotskiGridWidget.WidgetAlignment
    RIGHT: KlotskiGridWidget.WidgetAlignment
    class Data(_message.Message):
        __slots__ = ("type", "parallel_unit_number", "blocks", "klotski_title")
        TYPE_FIELD_NUMBER: _ClassVar[int]
        PARALLEL_UNIT_NUMBER_FIELD_NUMBER: _ClassVar[int]
        BLOCKS_FIELD_NUMBER: _ClassVar[int]
        KLOTSKI_TITLE_FIELD_NUMBER: _ClassVar[int]
        type: KlotskiGridWidget.BlockType
        parallel_unit_number: int
        blocks: _containers.RepeatedCompositeFieldContainer[KlotskiGridWidget.BlockWidget]
        klotski_title: str
        def __init__(self, type: _Optional[_Union[KlotskiGridWidget.BlockType, str]] = ..., parallel_unit_number: _Optional[int] = ..., blocks: _Optional[_Iterable[_Union[KlotskiGridWidget.BlockWidget, _Mapping]]] = ..., klotski_title: _Optional[str] = ...) -> None: ...
    class BlockWidget(_message.Message):
        __slots__ = ("vertical_unit_number", "single_items", "alignment")
        VERTICAL_UNIT_NUMBER_FIELD_NUMBER: _ClassVar[int]
        SINGLE_ITEMS_FIELD_NUMBER: _ClassVar[int]
        ALIGNMENT_FIELD_NUMBER: _ClassVar[int]
        vertical_unit_number: int
        single_items: _containers.RepeatedCompositeFieldContainer[KlotskiGridWidget.SingleItemWidget]
        alignment: KlotskiGridWidget.WidgetAlignment
        def __init__(self, vertical_unit_number: _Optional[int] = ..., single_items: _Optional[_Iterable[_Union[KlotskiGridWidget.SingleItemWidget, _Mapping]]] = ..., alignment: _Optional[_Union[KlotskiGridWidget.WidgetAlignment, str]] = ...) -> None: ...
    class SingleItemWidget(_message.Message):
        __slots__ = ("width_unit", "height_unit", "x_position_unit", "y_position_unit", "item", "badge")
        WIDTH_UNIT_FIELD_NUMBER: _ClassVar[int]
        HEIGHT_UNIT_FIELD_NUMBER: _ClassVar[int]
        X_POSITION_UNIT_FIELD_NUMBER: _ClassVar[int]
        Y_POSITION_UNIT_FIELD_NUMBER: _ClassVar[int]
        ITEM_FIELD_NUMBER: _ClassVar[int]
        BADGE_FIELD_NUMBER: _ClassVar[int]
        width_unit: int
        height_unit: int
        x_position_unit: int
        y_position_unit: int
        item: KlotskiGridWidget.Item
        badge: _badge_pb2.Badge
        def __init__(self, width_unit: _Optional[int] = ..., height_unit: _Optional[int] = ..., x_position_unit: _Optional[int] = ..., y_position_unit: _Optional[int] = ..., item: _Optional[_Union[KlotskiGridWidget.Item, _Mapping]] = ..., badge: _Optional[_Union[_badge_pb2.Badge, _Mapping]] = ...) -> None: ...
    class Item(_message.Message):
        __slots__ = ("horizontal_content_card", "vertical_content_poster")
        HORIZONTAL_CONTENT_CARD_FIELD_NUMBER: _ClassVar[int]
        VERTICAL_CONTENT_POSTER_FIELD_NUMBER: _ClassVar[int]
        horizontal_content_card: _horizontal_content_card_pb2.HorizontalContentCardWidget
        vertical_content_poster: _vertical_content_poster_pb2.VerticalContentPosterWidget
        def __init__(self, horizontal_content_card: _Optional[_Union[_horizontal_content_card_pb2.HorizontalContentCardWidget, _Mapping]] = ..., vertical_content_poster: _Optional[_Union[_vertical_content_poster_pb2.VerticalContentPosterWidget, _Mapping]] = ...) -> None: ...
    WIDGET_COMMONS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    widget_commons: _widget_commons_pb2.WidgetCommons
    data: KlotskiGridWidget.Data
    def __init__(self, widget_commons: _Optional[_Union[_widget_commons_pb2.WidgetCommons, _Mapping]] = ..., data: _Optional[_Union[KlotskiGridWidget.Data, _Mapping]] = ...) -> None: ...
