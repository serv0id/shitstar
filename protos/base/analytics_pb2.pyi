from google.protobuf import any_pb2 as _any_pb2
from feature.instrumentation import instrumentation_context_pb2 as _instrumentation_context_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Instrumentation(_message.Message):
    __slots__ = ("context", "override_referrer", "impression_events", "instrumentation_context", "instrumentation_context_v2")
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    OVERRIDE_REFERRER_FIELD_NUMBER: _ClassVar[int]
    IMPRESSION_EVENTS_FIELD_NUMBER: _ClassVar[int]
    INSTRUMENTATION_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    INSTRUMENTATION_CONTEXT_V2_FIELD_NUMBER: _ClassVar[int]
    context: _any_pb2.Any
    override_referrer: bool
    impression_events: _containers.RepeatedCompositeFieldContainer[ImpressionEvent]
    instrumentation_context: InstrumentationContext
    instrumentation_context_v2: _instrumentation_context_pb2.InstrumentationContext
    def __init__(self, context: _Optional[_Union[_any_pb2.Any, _Mapping]] = ..., override_referrer: bool = ..., impression_events: _Optional[_Iterable[_Union[ImpressionEvent, _Mapping]]] = ..., instrumentation_context: _Optional[_Union[InstrumentationContext, _Mapping]] = ..., instrumentation_context_v2: _Optional[_Union[_instrumentation_context_pb2.InstrumentationContext, _Mapping]] = ...) -> None: ...

class InstrumentationContext(_message.Message):
    __slots__ = ("url", "value")
    URL_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    url: str
    value: bytes
    def __init__(self, url: _Optional[str] = ..., value: _Optional[bytes] = ...) -> None: ...

class ImpressionEvent(_message.Message):
    __slots__ = ("event_name",)
    EVENT_NAME_FIELD_NUMBER: _ClassVar[int]
    event_name: str
    def __init__(self, event_name: _Optional[str] = ...) -> None: ...
