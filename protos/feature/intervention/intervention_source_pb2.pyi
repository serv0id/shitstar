from feature.intervention import ad_break_intervention_source_pb2 as _ad_break_intervention_source_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class InterventionSource(_message.Message):
    __slots__ = ("event_time_s", "is_skippable", "meta")
    class Meta(_message.Message):
        __slots__ = ("midroll", "ad_break")
        MIDROLL_FIELD_NUMBER: _ClassVar[int]
        AD_BREAK_FIELD_NUMBER: _ClassVar[int]
        midroll: InterventionSource.MidrollIntervention
        ad_break: _ad_break_intervention_source_pb2.AdBreakInterventionSource
        def __init__(self, midroll: _Optional[_Union[InterventionSource.MidrollIntervention, _Mapping]] = ..., ad_break: _Optional[_Union[_ad_break_intervention_source_pb2.AdBreakInterventionSource, _Mapping]] = ...) -> None: ...
    class MidrollIntervention(_message.Message):
        __slots__ = ("url",)
        URL_FIELD_NUMBER: _ClassVar[int]
        url: str
        def __init__(self, url: _Optional[str] = ...) -> None: ...
    EVENT_TIME_S_FIELD_NUMBER: _ClassVar[int]
    IS_SKIPPABLE_FIELD_NUMBER: _ClassVar[int]
    META_FIELD_NUMBER: _ClassVar[int]
    event_time_s: int
    is_skippable: bool
    meta: InterventionSource.Meta
    def __init__(self, event_time_s: _Optional[int] = ..., is_skippable: bool = ..., meta: _Optional[_Union[InterventionSource.Meta, _Mapping]] = ...) -> None: ...
