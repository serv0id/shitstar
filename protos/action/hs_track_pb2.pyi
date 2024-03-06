from feature.instrumentation import instrumentation_context_pb2 as _instrumentation_context_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class HSTrackAction(_message.Message):
    __slots__ = ["name", "override_context"]
    NAME_FIELD_NUMBER: _ClassVar[int]
    OVERRIDE_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    name: str
    override_context: _instrumentation_context_pb2.InstrumentationContext
    def __init__(self, name: _Optional[str] = ..., override_context: _Optional[_Union[_instrumentation_context_pb2.InstrumentationContext, _Mapping]] = ...) -> None: ...
