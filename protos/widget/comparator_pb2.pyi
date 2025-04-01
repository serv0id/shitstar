from base import template_pb2 as _template_pb2
from base import widget_commons_pb2 as _widget_commons_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PlanComparatorWidget(_message.Message):
    __slots__ = ("template", "widget_commons", "data")
    class Data(_message.Message):
        __slots__ = ("heading", "item_list")
        HEADING_FIELD_NUMBER: _ClassVar[int]
        ITEM_LIST_FIELD_NUMBER: _ClassVar[int]
        heading: _containers.RepeatedCompositeFieldContainer[PlanComparatorWidget.PlanHeading]
        item_list: _containers.RepeatedCompositeFieldContainer[PlanComparatorWidget.ComparatorRow]
        def __init__(self, heading: _Optional[_Iterable[_Union[PlanComparatorWidget.PlanHeading, _Mapping]]] = ..., item_list: _Optional[_Iterable[_Union[PlanComparatorWidget.ComparatorRow, _Mapping]]] = ...) -> None: ...
    class PlanHeading(_message.Message):
        __slots__ = ("heading", "sub_heading", "is_selected", "identifier")
        HEADING_FIELD_NUMBER: _ClassVar[int]
        SUB_HEADING_FIELD_NUMBER: _ClassVar[int]
        IS_SELECTED_FIELD_NUMBER: _ClassVar[int]
        IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
        heading: str
        sub_heading: str
        is_selected: bool
        identifier: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, heading: _Optional[str] = ..., sub_heading: _Optional[str] = ..., is_selected: bool = ..., identifier: _Optional[_Iterable[str]] = ...) -> None: ...
    class ComparatorRow(_message.Message):
        __slots__ = ("usp", "item_value")
        USP_FIELD_NUMBER: _ClassVar[int]
        ITEM_VALUE_FIELD_NUMBER: _ClassVar[int]
        usp: PlanComparatorWidget.TextItem
        item_value: _containers.RepeatedCompositeFieldContainer[PlanComparatorWidget.ComparatorCol]
        def __init__(self, usp: _Optional[_Union[PlanComparatorWidget.TextItem, _Mapping]] = ..., item_value: _Optional[_Iterable[_Union[PlanComparatorWidget.ComparatorCol, _Mapping]]] = ...) -> None: ...
    class ComparatorCol(_message.Message):
        __slots__ = ("is_selected", "identifier", "icon_name", "text")
        IS_SELECTED_FIELD_NUMBER: _ClassVar[int]
        IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
        ICON_NAME_FIELD_NUMBER: _ClassVar[int]
        TEXT_FIELD_NUMBER: _ClassVar[int]
        is_selected: bool
        identifier: _containers.RepeatedScalarFieldContainer[str]
        icon_name: str
        text: PlanComparatorWidget.TextItem
        def __init__(self, is_selected: bool = ..., identifier: _Optional[_Iterable[str]] = ..., icon_name: _Optional[str] = ..., text: _Optional[_Union[PlanComparatorWidget.TextItem, _Mapping]] = ...) -> None: ...
    class TextItem(_message.Message):
        __slots__ = ("title", "sub_title")
        TITLE_FIELD_NUMBER: _ClassVar[int]
        SUB_TITLE_FIELD_NUMBER: _ClassVar[int]
        title: str
        sub_title: PlanComparatorWidget.Subtitle
        def __init__(self, title: _Optional[str] = ..., sub_title: _Optional[_Union[PlanComparatorWidget.Subtitle, _Mapping]] = ...) -> None: ...
    class Subtitle(_message.Message):
        __slots__ = ("text", "is_highlighted")
        TEXT_FIELD_NUMBER: _ClassVar[int]
        IS_HIGHLIGHTED_FIELD_NUMBER: _ClassVar[int]
        text: str
        is_highlighted: bool
        def __init__(self, text: _Optional[str] = ..., is_highlighted: bool = ...) -> None: ...
    TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    WIDGET_COMMONS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    template: _template_pb2.Template
    widget_commons: _widget_commons_pb2.WidgetCommons
    data: PlanComparatorWidget.Data
    def __init__(self, template: _Optional[_Union[_template_pb2.Template, _Mapping]] = ..., widget_commons: _Optional[_Union[_widget_commons_pb2.WidgetCommons, _Mapping]] = ..., data: _Optional[_Union[PlanComparatorWidget.Data, _Mapping]] = ...) -> None: ...
