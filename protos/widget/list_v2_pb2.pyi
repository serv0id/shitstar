from base import widget_commons_pb2 as _widget_commons_pb2
from base import actions_pb2 as _actions_pb2
from feature.image import image_pb2 as _image_pb2
from feature.atom import button_pb2 as _button_pb2
from widget import list_item_v2_pb2 as _list_item_v2_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ListV2Widget(_message.Message):
    __slots__ = ("widget_commons", "data")
    class ListViewType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        Default: _ClassVar[ListV2Widget.ListViewType]
        Card: _ClassVar[ListV2Widget.ListViewType]
    Default: ListV2Widget.ListViewType
    Card: ListV2Widget.ListViewType
    class Data(_message.Message):
        __slots__ = ("list_header", "list_item", "list_view_type")
        LIST_HEADER_FIELD_NUMBER: _ClassVar[int]
        LIST_ITEM_FIELD_NUMBER: _ClassVar[int]
        LIST_VIEW_TYPE_FIELD_NUMBER: _ClassVar[int]
        list_header: ListV2Widget.ListHeader
        list_item: _containers.RepeatedCompositeFieldContainer[ListV2Widget.ListItem]
        list_view_type: ListV2Widget.ListViewType
        def __init__(self, list_header: _Optional[_Union[ListV2Widget.ListHeader, _Mapping]] = ..., list_item: _Optional[_Iterable[_Union[ListV2Widget.ListItem, _Mapping]]] = ..., list_view_type: _Optional[_Union[ListV2Widget.ListViewType, str]] = ...) -> None: ...
    class ListItem(_message.Message):
        __slots__ = ("list_item_widget",)
        LIST_ITEM_WIDGET_FIELD_NUMBER: _ClassVar[int]
        list_item_widget: _list_item_v2_pb2.ListItemV2Widget
        def __init__(self, list_item_widget: _Optional[_Union[_list_item_v2_pb2.ListItemV2Widget, _Mapping]] = ...) -> None: ...
    class ListHeader(_message.Message):
        __slots__ = ("toggle_state_header", "title_bar_header")
        class ToggleStateHeader(_message.Message):
            __slots__ = ("title", "primary_button", "secondary_button")
            TITLE_FIELD_NUMBER: _ClassVar[int]
            PRIMARY_BUTTON_FIELD_NUMBER: _ClassVar[int]
            SECONDARY_BUTTON_FIELD_NUMBER: _ClassVar[int]
            title: str
            primary_button: _button_pb2.Button
            secondary_button: _button_pb2.Button
            def __init__(self, title: _Optional[str] = ..., primary_button: _Optional[_Union[_button_pb2.Button, _Mapping]] = ..., secondary_button: _Optional[_Union[_button_pb2.Button, _Mapping]] = ...) -> None: ...
        class TitleBarHeader(_message.Message):
            __slots__ = ("title", "button")
            TITLE_FIELD_NUMBER: _ClassVar[int]
            BUTTON_FIELD_NUMBER: _ClassVar[int]
            title: str
            button: _button_pb2.Button
            def __init__(self, title: _Optional[str] = ..., button: _Optional[_Union[_button_pb2.Button, _Mapping]] = ...) -> None: ...
        TOGGLE_STATE_HEADER_FIELD_NUMBER: _ClassVar[int]
        TITLE_BAR_HEADER_FIELD_NUMBER: _ClassVar[int]
        toggle_state_header: ListV2Widget.ListHeader.ToggleStateHeader
        title_bar_header: ListV2Widget.ListHeader.TitleBarHeader
        def __init__(self, toggle_state_header: _Optional[_Union[ListV2Widget.ListHeader.ToggleStateHeader, _Mapping]] = ..., title_bar_header: _Optional[_Union[ListV2Widget.ListHeader.TitleBarHeader, _Mapping]] = ...) -> None: ...
    WIDGET_COMMONS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    widget_commons: _widget_commons_pb2.WidgetCommons
    data: ListV2Widget.Data
    def __init__(self, widget_commons: _Optional[_Union[_widget_commons_pb2.WidgetCommons, _Mapping]] = ..., data: _Optional[_Union[ListV2Widget.Data, _Mapping]] = ...) -> None: ...
