from base import template_pb2 as _template_pb2
from base import widget_commons_pb2 as _widget_commons_pb2
from widget import cw_card_pb2 as _cw_card_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CentreAlignedTrayWidget(_message.Message):
    __slots__ = ("template", "widget_commons", "data")
    class Data(_message.Message):
        __slots__ = ("item_template_name", "items")
        ITEM_TEMPLATE_NAME_FIELD_NUMBER: _ClassVar[int]
        ITEMS_FIELD_NUMBER: _ClassVar[int]
        item_template_name: str
        items: _containers.RepeatedCompositeFieldContainer[CentreAlignedTrayWidget.Item]
        def __init__(self, item_template_name: _Optional[str] = ..., items: _Optional[_Iterable[_Union[CentreAlignedTrayWidget.Item, _Mapping]]] = ...) -> None: ...
    class Item(_message.Message):
        __slots__ = ("cw_card",)
        CW_CARD_FIELD_NUMBER: _ClassVar[int]
        cw_card: _cw_card_pb2.CWCardWidget
        def __init__(self, cw_card: _Optional[_Union[_cw_card_pb2.CWCardWidget, _Mapping]] = ...) -> None: ...
    TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    WIDGET_COMMONS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    template: _template_pb2.Template
    widget_commons: _widget_commons_pb2.WidgetCommons
    data: CentreAlignedTrayWidget.Data
    def __init__(self, template: _Optional[_Union[_template_pb2.Template, _Mapping]] = ..., widget_commons: _Optional[_Union[_widget_commons_pb2.WidgetCommons, _Mapping]] = ..., data: _Optional[_Union[CentreAlignedTrayWidget.Data, _Mapping]] = ...) -> None: ...
