from base import template_pb2 as _template_pb2
from base import widget_commons_pb2 as _widget_commons_pb2
from widget import tab_pb2 as _tab_pb2
from widget import polling_pb2 as _polling_pb2
from base import actions_pb2 as _actions_pb2
from feature.item import selectable_item_pb2 as _selectable_item_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CategoryPickerWidget(_message.Message):
    __slots__ = ("template", "widget_commons", "data")
    class CategoryPickerLayout(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        DEFAULT: _ClassVar[CategoryPickerWidget.CategoryPickerLayout]
        VERTICAL: _ClassVar[CategoryPickerWidget.CategoryPickerLayout]
        HORIZONTAL: _ClassVar[CategoryPickerWidget.CategoryPickerLayout]
    DEFAULT: CategoryPickerWidget.CategoryPickerLayout
    VERTICAL: CategoryPickerWidget.CategoryPickerLayout
    HORIZONTAL: CategoryPickerWidget.CategoryPickerLayout
    class Data(_message.Message):
        __slots__ = ("tabs", "dropdown", "load_more_url", "category_layout")
        TABS_FIELD_NUMBER: _ClassVar[int]
        DROPDOWN_FIELD_NUMBER: _ClassVar[int]
        LOAD_MORE_URL_FIELD_NUMBER: _ClassVar[int]
        CATEGORY_LAYOUT_FIELD_NUMBER: _ClassVar[int]
        tabs: _containers.RepeatedCompositeFieldContainer[CategoryPickerWidget.Widget]
        dropdown: DropdownData
        load_more_url: str
        category_layout: CategoryPickerWidget.CategoryPickerLayout
        def __init__(self, tabs: _Optional[_Iterable[_Union[CategoryPickerWidget.Widget, _Mapping]]] = ..., dropdown: _Optional[_Union[DropdownData, _Mapping]] = ..., load_more_url: _Optional[str] = ..., category_layout: _Optional[_Union[CategoryPickerWidget.CategoryPickerLayout, str]] = ...) -> None: ...
    class Widget(_message.Message):
        __slots__ = ("tab", "polling_tab")
        TAB_FIELD_NUMBER: _ClassVar[int]
        POLLING_TAB_FIELD_NUMBER: _ClassVar[int]
        tab: _tab_pb2.TabWidget
        polling_tab: _polling_pb2.PollingTabWidget
        def __init__(self, tab: _Optional[_Union[_tab_pb2.TabWidget, _Mapping]] = ..., polling_tab: _Optional[_Union[_polling_pb2.PollingTabWidget, _Mapping]] = ...) -> None: ...
    TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    WIDGET_COMMONS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    template: _template_pb2.Template
    widget_commons: _widget_commons_pb2.WidgetCommons
    data: CategoryPickerWidget.Data
    def __init__(self, template: _Optional[_Union[_template_pb2.Template, _Mapping]] = ..., widget_commons: _Optional[_Union[_widget_commons_pb2.WidgetCommons, _Mapping]] = ..., data: _Optional[_Union[CategoryPickerWidget.Data, _Mapping]] = ...) -> None: ...

class DropdownData(_message.Message):
    __slots__ = ("selected_item_id", "items", "actions")
    SELECTED_ITEM_ID_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    ACTIONS_FIELD_NUMBER: _ClassVar[int]
    selected_item_id: str
    items: _containers.RepeatedCompositeFieldContainer[_selectable_item_pb2.SelectableItem]
    actions: _actions_pb2.Actions
    def __init__(self, selected_item_id: _Optional[str] = ..., items: _Optional[_Iterable[_Union[_selectable_item_pb2.SelectableItem, _Mapping]]] = ..., actions: _Optional[_Union[_actions_pb2.Actions, _Mapping]] = ...) -> None: ...
