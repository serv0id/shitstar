from feature.accessibility import accessibility_pb2 as _accessibility_pb2
from composable.elements import composable_pb2 as _composable_pb2
from composable.elements import text_pb2 as _text_pb2
from composable.base import commons_pb2 as _commons_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TimerMini(_message.Message):
    __slots__ = ("composable_commons", "data", "view", "accessibility")
    class TimerData(_message.Message):
        __slots__ = ("timer_end_timestamp", "format")
        class TimerFormat(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            DAYS: _ClassVar[TimerMini.TimerData.TimerFormat]
            HOURS_MINUTES_SECONDS: _ClassVar[TimerMini.TimerData.TimerFormat]
            MINUTES_SECONDS: _ClassVar[TimerMini.TimerData.TimerFormat]
            SECONDS: _ClassVar[TimerMini.TimerData.TimerFormat]
        DAYS: TimerMini.TimerData.TimerFormat
        HOURS_MINUTES_SECONDS: TimerMini.TimerData.TimerFormat
        MINUTES_SECONDS: TimerMini.TimerData.TimerFormat
        SECONDS: TimerMini.TimerData.TimerFormat
        TIMER_END_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
        FORMAT_FIELD_NUMBER: _ClassVar[int]
        timer_end_timestamp: int
        format: TimerMini.TimerData.TimerFormat
        def __init__(self, timer_end_timestamp: _Optional[int] = ..., format: _Optional[_Union[TimerMini.TimerData.TimerFormat, str]] = ...) -> None: ...
    class TimerView(_message.Message):
        __slots__ = ("prefix", "days", "hours", "minutes", "seconds")
        PREFIX_FIELD_NUMBER: _ClassVar[int]
        DAYS_FIELD_NUMBER: _ClassVar[int]
        HOURS_FIELD_NUMBER: _ClassVar[int]
        MINUTES_FIELD_NUMBER: _ClassVar[int]
        SECONDS_FIELD_NUMBER: _ClassVar[int]
        prefix: _composable_pb2.Composable
        days: _text_pb2.Text
        hours: _text_pb2.Text
        minutes: _text_pb2.Text
        seconds: _text_pb2.Text
        def __init__(self, prefix: _Optional[_Union[_composable_pb2.Composable, _Mapping]] = ..., days: _Optional[_Union[_text_pb2.Text, _Mapping]] = ..., hours: _Optional[_Union[_text_pb2.Text, _Mapping]] = ..., minutes: _Optional[_Union[_text_pb2.Text, _Mapping]] = ..., seconds: _Optional[_Union[_text_pb2.Text, _Mapping]] = ...) -> None: ...
    COMPOSABLE_COMMONS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    VIEW_FIELD_NUMBER: _ClassVar[int]
    ACCESSIBILITY_FIELD_NUMBER: _ClassVar[int]
    composable_commons: _commons_pb2.ComposableCommons
    data: TimerMini.TimerData
    view: TimerMini.TimerView
    accessibility: _accessibility_pb2.Accessibility
    def __init__(self, composable_commons: _Optional[_Union[_commons_pb2.ComposableCommons, _Mapping]] = ..., data: _Optional[_Union[TimerMini.TimerData, _Mapping]] = ..., view: _Optional[_Union[TimerMini.TimerView, _Mapping]] = ..., accessibility: _Optional[_Union[_accessibility_pb2.Accessibility, _Mapping]] = ...) -> None: ...
