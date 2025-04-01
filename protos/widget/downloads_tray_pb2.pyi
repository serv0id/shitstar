from base import widget_commons_pb2 as _widget_commons_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DownloadsTrayWidget(_message.Message):
    __slots__ = ("widget_commons", "data")
    class Data(_message.Message):
        __slots__ = ("header",)
        HEADER_FIELD_NUMBER: _ClassVar[int]
        header: DownloadsTrayWidget.Header
        def __init__(self, header: _Optional[_Union[DownloadsTrayWidget.Header, _Mapping]] = ...) -> None: ...
    class Header(_message.Message):
        __slots__ = ("title", "end_icon_name")
        TITLE_FIELD_NUMBER: _ClassVar[int]
        END_ICON_NAME_FIELD_NUMBER: _ClassVar[int]
        title: str
        end_icon_name: str
        def __init__(self, title: _Optional[str] = ..., end_icon_name: _Optional[str] = ...) -> None: ...
    WIDGET_COMMONS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    widget_commons: _widget_commons_pb2.WidgetCommons
    data: DownloadsTrayWidget.Data
    def __init__(self, widget_commons: _Optional[_Union[_widget_commons_pb2.WidgetCommons, _Mapping]] = ..., data: _Optional[_Union[DownloadsTrayWidget.Data, _Mapping]] = ...) -> None: ...
