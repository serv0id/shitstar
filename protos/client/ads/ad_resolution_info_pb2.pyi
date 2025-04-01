from client.ads import info_pb2 as _info_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AdResolutionInfo(_message.Message):
    __slots__ = ("info", "resolution_time_ms", "is_resolved")
    INFO_FIELD_NUMBER: _ClassVar[int]
    RESOLUTION_TIME_MS_FIELD_NUMBER: _ClassVar[int]
    IS_RESOLVED_FIELD_NUMBER: _ClassVar[int]
    info: _info_pb2.Info
    resolution_time_ms: int
    is_resolved: bool
    def __init__(self, info: _Optional[_Union[_info_pb2.Info, _Mapping]] = ..., resolution_time_ms: _Optional[int] = ..., is_resolved: bool = ...) -> None: ...
