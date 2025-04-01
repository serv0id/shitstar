from base import template_pb2 as _template_pb2
from widget import header_pb2 as _header_pb2
from base import widget_commons_pb2 as _widget_commons_pb2
from widget import rectangle_studio_card_pb2 as _rectangle_studio_card_pb2
from widget import square_studio_card_pb2 as _square_studio_card_pb2
from feature.accessibility import accessibility_pb2 as _accessibility_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ScaleToFitTrayWidget(_message.Message):
    __slots__ = ("template", "widget_commons", "data")
    class Data(_message.Message):
        __slots__ = ("item_template_name", "items_per_row", "items", "header", "alt")
        ITEM_TEMPLATE_NAME_FIELD_NUMBER: _ClassVar[int]
        ITEMS_PER_ROW_FIELD_NUMBER: _ClassVar[int]
        ITEMS_FIELD_NUMBER: _ClassVar[int]
        HEADER_FIELD_NUMBER: _ClassVar[int]
        ALT_FIELD_NUMBER: _ClassVar[int]
        item_template_name: str
        items_per_row: int
        items: _containers.RepeatedCompositeFieldContainer[ScaleToFitTrayWidget.Item]
        header: _header_pb2.HeaderWidget
        alt: _accessibility_pb2.Accessibility
        def __init__(self, item_template_name: _Optional[str] = ..., items_per_row: _Optional[int] = ..., items: _Optional[_Iterable[_Union[ScaleToFitTrayWidget.Item, _Mapping]]] = ..., header: _Optional[_Union[_header_pb2.HeaderWidget, _Mapping]] = ..., alt: _Optional[_Union[_accessibility_pb2.Accessibility, _Mapping]] = ...) -> None: ...
    class Item(_message.Message):
        __slots__ = ("rectangle_studio_card", "square_studio_card")
        RECTANGLE_STUDIO_CARD_FIELD_NUMBER: _ClassVar[int]
        SQUARE_STUDIO_CARD_FIELD_NUMBER: _ClassVar[int]
        rectangle_studio_card: _rectangle_studio_card_pb2.RectangleStudioCardWidget
        square_studio_card: _square_studio_card_pb2.SquareStudioCardWidget
        def __init__(self, rectangle_studio_card: _Optional[_Union[_rectangle_studio_card_pb2.RectangleStudioCardWidget, _Mapping]] = ..., square_studio_card: _Optional[_Union[_square_studio_card_pb2.SquareStudioCardWidget, _Mapping]] = ...) -> None: ...
    TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    WIDGET_COMMONS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    template: _template_pb2.Template
    widget_commons: _widget_commons_pb2.WidgetCommons
    data: ScaleToFitTrayWidget.Data
    def __init__(self, template: _Optional[_Union[_template_pb2.Template, _Mapping]] = ..., widget_commons: _Optional[_Union[_widget_commons_pb2.WidgetCommons, _Mapping]] = ..., data: _Optional[_Union[ScaleToFitTrayWidget.Data, _Mapping]] = ...) -> None: ...
