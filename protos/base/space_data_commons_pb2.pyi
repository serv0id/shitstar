from base import analytics_pb2 as _analytics_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SpaceDataCommons(_message.Message):
    __slots__ = ("instrumentation",)
    INSTRUMENTATION_FIELD_NUMBER: _ClassVar[int]
    instrumentation: _analytics_pb2.Instrumentation
    def __init__(self, instrumentation: _Optional[_Union[_analytics_pb2.Instrumentation, _Mapping]] = ...) -> None: ...
