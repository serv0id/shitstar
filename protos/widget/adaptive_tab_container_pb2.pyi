from base import widget_commons_pb2 as _widget_commons_pb2
from widget import tab_pb2 as _tab_pb2
from base import actions_pb2 as _actions_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AdaptiveTabContainerWidget(_message.Message):
    __slots__ = ("widget_commons", "data")
    class Data(_message.Message):
        __slots__ = ("portrait_tabs", "landscape_tabs", "side_sheet_tabs")
        PORTRAIT_TABS_FIELD_NUMBER: _ClassVar[int]
        LANDSCAPE_TABS_FIELD_NUMBER: _ClassVar[int]
        SIDE_SHEET_TABS_FIELD_NUMBER: _ClassVar[int]
        portrait_tabs: _containers.RepeatedCompositeFieldContainer[_tab_pb2.TabWidget]
        landscape_tabs: _containers.RepeatedCompositeFieldContainer[_tab_pb2.TabWidget]
        side_sheet_tabs: _containers.RepeatedCompositeFieldContainer[_tab_pb2.TabWidget]
        def __init__(self, portrait_tabs: _Optional[_Iterable[_Union[_tab_pb2.TabWidget, _Mapping]]] = ..., landscape_tabs: _Optional[_Iterable[_Union[_tab_pb2.TabWidget, _Mapping]]] = ..., side_sheet_tabs: _Optional[_Iterable[_Union[_tab_pb2.TabWidget, _Mapping]]] = ...) -> None: ...
    WIDGET_COMMONS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    widget_commons: _widget_commons_pb2.WidgetCommons
    data: AdaptiveTabContainerWidget.Data
    def __init__(self, widget_commons: _Optional[_Union[_widget_commons_pb2.WidgetCommons, _Mapping]] = ..., data: _Optional[_Union[AdaptiveTabContainerWidget.Data, _Mapping]] = ...) -> None: ...
