from feature.instrumentation import instrumentation_context_pb2 as _instrumentation_context_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class HSTrackAction(_message.Message):
    __slots__ = ("name", "override_context", "priority")
    class HSTrackActionPriority(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        DEFAULT: _ClassVar[HSTrackAction.HSTrackActionPriority]
        NORMAL: _ClassVar[HSTrackAction.HSTrackActionPriority]
        HIGH: _ClassVar[HSTrackAction.HSTrackActionPriority]
        HIGH_WITH_CALLBACK: _ClassVar[HSTrackAction.HSTrackActionPriority]
    DEFAULT: HSTrackAction.HSTrackActionPriority
    NORMAL: HSTrackAction.HSTrackActionPriority
    HIGH: HSTrackAction.HSTrackActionPriority
    HIGH_WITH_CALLBACK: HSTrackAction.HSTrackActionPriority
    NAME_FIELD_NUMBER: _ClassVar[int]
    OVERRIDE_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    PRIORITY_FIELD_NUMBER: _ClassVar[int]
    name: str
    override_context: _instrumentation_context_pb2.InstrumentationContext
    priority: HSTrackAction.HSTrackActionPriority
    def __init__(self, name: _Optional[str] = ..., override_context: _Optional[_Union[_instrumentation_context_pb2.InstrumentationContext, _Mapping]] = ..., priority: _Optional[_Union[HSTrackAction.HSTrackActionPriority, str]] = ...) -> None: ...
