from base import widget_commons_pb2 as _widget_commons_pb2
from feature.image import image_pb2 as _image_pb2
from feature.text import text_pb2 as _text_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TimerWidget(_message.Message):
    __slots__ = ("widget_commons", "data")
    class TimerEndBehaviour(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NONE: _ClassVar[TimerWidget.TimerEndBehaviour]
        STOP: _ClassVar[TimerWidget.TimerEndBehaviour]
        HIDE: _ClassVar[TimerWidget.TimerEndBehaviour]
    NONE: TimerWidget.TimerEndBehaviour
    STOP: TimerWidget.TimerEndBehaviour
    HIDE: TimerWidget.TimerEndBehaviour
    class Data(_message.Message):
        __slots__ = ("timer_end_timestamp", "end_behaviour", "timer")
        TIMER_END_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
        END_BEHAVIOUR_FIELD_NUMBER: _ClassVar[int]
        TIMER_FIELD_NUMBER: _ClassVar[int]
        timer_end_timestamp: int
        end_behaviour: TimerWidget.TimerEndBehaviour
        timer: TimerWidget.Timer
        def __init__(self, timer_end_timestamp: _Optional[int] = ..., end_behaviour: _Optional[_Union[TimerWidget.TimerEndBehaviour, str]] = ..., timer: _Optional[_Union[TimerWidget.Timer, _Mapping]] = ...) -> None: ...
    class Timer(_message.Message):
        __slots__ = ("top_flip_timer", "masthead_timer", "horizontal_timer")
        TOP_FLIP_TIMER_FIELD_NUMBER: _ClassVar[int]
        MASTHEAD_TIMER_FIELD_NUMBER: _ClassVar[int]
        HORIZONTAL_TIMER_FIELD_NUMBER: _ClassVar[int]
        top_flip_timer: TimerWidget.TopFlipTimer
        masthead_timer: TimerWidget.MastheadTimer
        horizontal_timer: TimerWidget.HorizontalTimer
        def __init__(self, top_flip_timer: _Optional[_Union[TimerWidget.TopFlipTimer, _Mapping]] = ..., masthead_timer: _Optional[_Union[TimerWidget.MastheadTimer, _Mapping]] = ..., horizontal_timer: _Optional[_Union[TimerWidget.HorizontalTimer, _Mapping]] = ...) -> None: ...
    class TopFlipTimer(_message.Message):
        __slots__ = ("hour_placeholder_text", "min_placeholder_text", "sec_placeholder_text")
        HOUR_PLACEHOLDER_TEXT_FIELD_NUMBER: _ClassVar[int]
        MIN_PLACEHOLDER_TEXT_FIELD_NUMBER: _ClassVar[int]
        SEC_PLACEHOLDER_TEXT_FIELD_NUMBER: _ClassVar[int]
        hour_placeholder_text: str
        min_placeholder_text: str
        sec_placeholder_text: str
        def __init__(self, hour_placeholder_text: _Optional[str] = ..., min_placeholder_text: _Optional[str] = ..., sec_placeholder_text: _Optional[str] = ...) -> None: ...
    class MastheadTimer(_message.Message):
        __slots__ = ("image",)
        IMAGE_FIELD_NUMBER: _ClassVar[int]
        image: _image_pb2.Image
        def __init__(self, image: _Optional[_Union[_image_pb2.Image, _Mapping]] = ...) -> None: ...
    class HorizontalTimer(_message.Message):
        __slots__ = ("image", "hour_placeholder_text", "min_placeholder_text", "sec_placeholder_text", "prefix_text")
        IMAGE_FIELD_NUMBER: _ClassVar[int]
        HOUR_PLACEHOLDER_TEXT_FIELD_NUMBER: _ClassVar[int]
        MIN_PLACEHOLDER_TEXT_FIELD_NUMBER: _ClassVar[int]
        SEC_PLACEHOLDER_TEXT_FIELD_NUMBER: _ClassVar[int]
        PREFIX_TEXT_FIELD_NUMBER: _ClassVar[int]
        image: _image_pb2.Image
        hour_placeholder_text: str
        min_placeholder_text: str
        sec_placeholder_text: str
        prefix_text: _text_pb2.Text
        def __init__(self, image: _Optional[_Union[_image_pb2.Image, _Mapping]] = ..., hour_placeholder_text: _Optional[str] = ..., min_placeholder_text: _Optional[str] = ..., sec_placeholder_text: _Optional[str] = ..., prefix_text: _Optional[_Union[_text_pb2.Text, _Mapping]] = ...) -> None: ...
    WIDGET_COMMONS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    widget_commons: _widget_commons_pb2.WidgetCommons
    data: TimerWidget.Data
    def __init__(self, widget_commons: _Optional[_Union[_widget_commons_pb2.WidgetCommons, _Mapping]] = ..., data: _Optional[_Union[TimerWidget.Data, _Mapping]] = ...) -> None: ...
