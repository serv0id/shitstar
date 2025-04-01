from base import widget_commons_pb2 as _widget_commons_pb2
from feature.trackers import url_trackers_pb2 as _url_trackers_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class NoFillAdWidget(_message.Message):
    __slots__ = ("widget_commons", "data")
    class Data(_message.Message):
        __slots__ = ("tracker",)
        TRACKER_FIELD_NUMBER: _ClassVar[int]
        tracker: _url_trackers_pb2.UrlTrackers
        def __init__(self, tracker: _Optional[_Union[_url_trackers_pb2.UrlTrackers, _Mapping]] = ...) -> None: ...
    WIDGET_COMMONS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    widget_commons: _widget_commons_pb2.WidgetCommons
    data: NoFillAdWidget.Data
    def __init__(self, widget_commons: _Optional[_Union[_widget_commons_pb2.WidgetCommons, _Mapping]] = ..., data: _Optional[_Union[NoFillAdWidget.Data, _Mapping]] = ...) -> None: ...
