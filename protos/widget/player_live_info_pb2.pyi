from base import widget_commons_pb2 as _widget_commons_pb2
from feature.live import live_info_pb2 as _live_info_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ConcurrencyWidget(_message.Message):
    __slots__ = ("widget_commons", "data")
    class Data(_message.Message):
        __slots__ = ("live_data",)
        LIVE_DATA_FIELD_NUMBER: _ClassVar[int]
        live_data: _live_info_pb2.LiveInfo
        def __init__(self, live_data: _Optional[_Union[_live_info_pb2.LiveInfo, _Mapping]] = ...) -> None: ...
    WIDGET_COMMONS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    widget_commons: _widget_commons_pb2.WidgetCommons
    data: ConcurrencyWidget.Data
    def __init__(self, widget_commons: _Optional[_Union[_widget_commons_pb2.WidgetCommons, _Mapping]] = ..., data: _Optional[_Union[ConcurrencyWidget.Data, _Mapping]] = ...) -> None: ...
