from feature.intervention import preroll_intervention_pb2 as _preroll_intervention_pb2
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

class Intervention(_message.Message):
    __slots__ = ("event_time_s", "is_skippable", "meta", "repeat")
    class Meta(_message.Message):
        __slots__ = ("preroll", "action_handler", "refresh", "playback_action", "widget_visibility", "compose_display")
        PREROLL_FIELD_NUMBER: _ClassVar[int]
        ACTION_HANDLER_FIELD_NUMBER: _ClassVar[int]
        REFRESH_FIELD_NUMBER: _ClassVar[int]
        PLAYBACK_ACTION_FIELD_NUMBER: _ClassVar[int]
        WIDGET_VISIBILITY_FIELD_NUMBER: _ClassVar[int]
        COMPOSE_DISPLAY_FIELD_NUMBER: _ClassVar[int]
        preroll: _preroll_intervention_pb2.PrerollIntervention
        action_handler: _action_intervention_pb2.ActionHandlerIntervention
        refresh: _any_pb2.Any
        playback_action: _any_pb2.Any
        widget_visibility: _widget_visibility_intervention_pb2.WidgetVisibilityIntervention
        compose_display: _compose_display_intervention_pb2.ComposeDisplayIntervention
        def __init__(self, preroll: _Optional[_Union[_preroll_intervention_pb2.PrerollIntervention, _Mapping]] = ..., action_handler: _Optional[_Union[_action_intervention_pb2.ActionHandlerIntervention, _Mapping]] = ..., refresh: _Optional[_Union[_any_pb2.Any, _Mapping]] = ..., playback_action: _Optional[_Union[_any_pb2.Any, _Mapping]] = ..., widget_visibility: _Optional[_Union[_widget_visibility_intervention_pb2.WidgetVisibilityIntervention, _Mapping]] = ..., compose_display: _Optional[_Union[_compose_display_intervention_pb2.ComposeDisplayIntervention, _Mapping]] = ...) -> None: ...
    class Repeat(_message.Message):
        __slots__ = ("duration_time_s",)
        DURATION_TIME_S_FIELD_NUMBER: _ClassVar[int]
        duration_time_s: int
        def __init__(self, duration_time_s: _Optional[int] = ...) -> None: ...
    EVENT_TIME_S_FIELD_NUMBER: _ClassVar[int]
    IS_SKIPPABLE_FIELD_NUMBER: _ClassVar[int]
    META_FIELD_NUMBER: _ClassVar[int]
    REPEAT_FIELD_NUMBER: _ClassVar[int]
    event_time_s: int
    is_skippable: bool
    meta: Intervention.Meta
    repeat: Intervention.Repeat
    def __init__(self, event_time_s: _Optional[int] = ..., is_skippable: bool = ..., meta: _Optional[_Union[Intervention.Meta, _Mapping]] = ..., repeat: _Optional[_Union[Intervention.Repeat, _Mapping]] = ...) -> None: ...
