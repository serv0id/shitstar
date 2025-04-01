from feature.intervention import interventions_pb2 as _interventions_pb2
from feature.intervention import action_intervention_pb2 as _action_intervention_pb2
from feature.intervention import refresh_intervention_pb2 as _refresh_intervention_pb2
from feature.intervention import widget_visibility_intervention_pb2 as _widget_visibility_intervention_pb2
from feature.intervention import compose_display_intervention_pb2 as _compose_display_intervention_pb2
from google.protobuf import any_pb2 as _any_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class EventIntervention(_message.Message):
    __slots__ = ("event_name", "meta", "repeat")
    class Meta(_message.Message):
        __slots__ = ("action_handler", "compose_display", "refresh")
        ACTION_HANDLER_FIELD_NUMBER: _ClassVar[int]
        COMPOSE_DISPLAY_FIELD_NUMBER: _ClassVar[int]
        REFRESH_FIELD_NUMBER: _ClassVar[int]
        action_handler: _action_intervention_pb2.ActionHandlerIntervention
        compose_display: _compose_display_intervention_pb2.ComposeDisplayIntervention
        refresh: _any_pb2.Any
        def __init__(self, action_handler: _Optional[_Union[_action_intervention_pb2.ActionHandlerIntervention, _Mapping]] = ..., compose_display: _Optional[_Union[_compose_display_intervention_pb2.ComposeDisplayIntervention, _Mapping]] = ..., refresh: _Optional[_Union[_any_pb2.Any, _Mapping]] = ...) -> None: ...
    class Repeat(_message.Message):
        __slots__ = ("max_repetition_count",)
        MAX_REPETITION_COUNT_FIELD_NUMBER: _ClassVar[int]
        max_repetition_count: int
        def __init__(self, max_repetition_count: _Optional[int] = ...) -> None: ...
    EVENT_NAME_FIELD_NUMBER: _ClassVar[int]
    META_FIELD_NUMBER: _ClassVar[int]
    REPEAT_FIELD_NUMBER: _ClassVar[int]
    event_name: str
    meta: EventIntervention.Meta
    repeat: EventIntervention.Repeat
    def __init__(self, event_name: _Optional[str] = ..., meta: _Optional[_Union[EventIntervention.Meta, _Mapping]] = ..., repeat: _Optional[_Union[EventIntervention.Repeat, _Mapping]] = ...) -> None: ...
