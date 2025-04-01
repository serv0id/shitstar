from base import widget_commons_pb2 as _widget_commons_pb2
from feature.quiz import title_pb2 as _title_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class QuizInterimResultWidget(_message.Message):
    __slots__ = ("widget_commons", "data")
    class Data(_message.Message):
        __slots__ = ("is_right_anwser", "background_color_hex", "results", "extra_reminder", "duration_in_seconds")
        IS_RIGHT_ANWSER_FIELD_NUMBER: _ClassVar[int]
        BACKGROUND_COLOR_HEX_FIELD_NUMBER: _ClassVar[int]
        RESULTS_FIELD_NUMBER: _ClassVar[int]
        EXTRA_REMINDER_FIELD_NUMBER: _ClassVar[int]
        DURATION_IN_SECONDS_FIELD_NUMBER: _ClassVar[int]
        is_right_anwser: bool
        background_color_hex: str
        results: _title_pb2.Title
        extra_reminder: _title_pb2.Title
        duration_in_seconds: int
        def __init__(self, is_right_anwser: bool = ..., background_color_hex: _Optional[str] = ..., results: _Optional[_Union[_title_pb2.Title, _Mapping]] = ..., extra_reminder: _Optional[_Union[_title_pb2.Title, _Mapping]] = ..., duration_in_seconds: _Optional[int] = ...) -> None: ...
    WIDGET_COMMONS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    widget_commons: _widget_commons_pb2.WidgetCommons
    data: QuizInterimResultWidget.Data
    def __init__(self, widget_commons: _Optional[_Union[_widget_commons_pb2.WidgetCommons, _Mapping]] = ..., data: _Optional[_Union[QuizInterimResultWidget.Data, _Mapping]] = ...) -> None: ...
