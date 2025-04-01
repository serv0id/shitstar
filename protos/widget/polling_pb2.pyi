from base import template_pb2 as _template_pb2
from base import widget_commons_pb2 as _widget_commons_pb2
from base import actions_pb2 as _actions_pb2
from widget import tab_pb2 as _tab_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PollingData(_message.Message):
    __slots__ = ("active", "polling_frequency", "polling_url")
    ACTIVE_FIELD_NUMBER: _ClassVar[int]
    POLLING_FREQUENCY_FIELD_NUMBER: _ClassVar[int]
    POLLING_URL_FIELD_NUMBER: _ClassVar[int]
    active: bool
    polling_frequency: int
    polling_url: str
    def __init__(self, active: bool = ..., polling_frequency: _Optional[int] = ..., polling_url: _Optional[str] = ...) -> None: ...

class PollingTabWidget(_message.Message):
    __slots__ = ("widget_commons", "data")
    class Data(_message.Message):
        __slots__ = ("tab", "polling")
        TAB_FIELD_NUMBER: _ClassVar[int]
        POLLING_FIELD_NUMBER: _ClassVar[int]
        tab: _tab_pb2.TabWidget
        polling: PollingData
        def __init__(self, tab: _Optional[_Union[_tab_pb2.TabWidget, _Mapping]] = ..., polling: _Optional[_Union[PollingData, _Mapping]] = ...) -> None: ...
    WIDGET_COMMONS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    widget_commons: _widget_commons_pb2.WidgetCommons
    data: PollingTabWidget.Data
    def __init__(self, widget_commons: _Optional[_Union[_widget_commons_pb2.WidgetCommons, _Mapping]] = ..., data: _Optional[_Union[PollingTabWidget.Data, _Mapping]] = ...) -> None: ...
