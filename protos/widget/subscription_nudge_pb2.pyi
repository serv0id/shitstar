from base import actions_pb2 as _actions_pb2
from base import widget_commons_pb2 as _widget_commons_pb2
from feature.quiz import title_icon_combo_pb2 as _title_icon_combo_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SubscriptionNudgeWidget(_message.Message):
    __slots__ = ("widget_commons", "data")
    class Data(_message.Message):
        __slots__ = ("nudge_text", "actions", "text", "animation")
        NUDGE_TEXT_FIELD_NUMBER: _ClassVar[int]
        ACTIONS_FIELD_NUMBER: _ClassVar[int]
        TEXT_FIELD_NUMBER: _ClassVar[int]
        ANIMATION_FIELD_NUMBER: _ClassVar[int]
        nudge_text: str
        actions: _actions_pb2.Actions
        text: str
        animation: SubscriptionNudgeWidget.NudgeAnimation
        def __init__(self, nudge_text: _Optional[str] = ..., actions: _Optional[_Union[_actions_pb2.Actions, _Mapping]] = ..., text: _Optional[str] = ..., animation: _Optional[_Union[SubscriptionNudgeWidget.NudgeAnimation, _Mapping]] = ...) -> None: ...
    class NudgeAnimation(_message.Message):
        __slots__ = ("slide_up",)
        SLIDE_UP_FIELD_NUMBER: _ClassVar[int]
        slide_up: _containers.RepeatedCompositeFieldContainer[_title_icon_combo_pb2.TitleIconCombo]
        def __init__(self, slide_up: _Optional[_Iterable[_Union[_title_icon_combo_pb2.TitleIconCombo, _Mapping]]] = ...) -> None: ...
    WIDGET_COMMONS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    widget_commons: _widget_commons_pb2.WidgetCommons
    data: SubscriptionNudgeWidget.Data
    def __init__(self, widget_commons: _Optional[_Union[_widget_commons_pb2.WidgetCommons, _Mapping]] = ..., data: _Optional[_Union[SubscriptionNudgeWidget.Data, _Mapping]] = ...) -> None: ...
