from base import widget_commons_pb2 as _widget_commons_pb2
from widget import button_stack_pb2 as _button_stack_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FeedCTAWidget(_message.Message):
    __slots__ = ("widget_commons", "data")
    class Data(_message.Message):
        __slots__ = ("button",)
        BUTTON_FIELD_NUMBER: _ClassVar[int]
        button: _button_stack_pb2.ButtonStackWidget
        def __init__(self, button: _Optional[_Union[_button_stack_pb2.ButtonStackWidget, _Mapping]] = ...) -> None: ...
    WIDGET_COMMONS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    widget_commons: _widget_commons_pb2.WidgetCommons
    data: FeedCTAWidget.Data
    def __init__(self, widget_commons: _Optional[_Union[_widget_commons_pb2.WidgetCommons, _Mapping]] = ..., data: _Optional[_Union[FeedCTAWidget.Data, _Mapping]] = ...) -> None: ...
