from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class StreamType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    UNKNOWN: _ClassVar[StreamType]
    STREAM_VOD: _ClassVar[StreamType]
    STREAM_LIVE: _ClassVar[StreamType]
    STREAM_SIMULCAST: _ClassVar[StreamType]
UNKNOWN: StreamType
STREAM_VOD: StreamType
STREAM_LIVE: StreamType
STREAM_SIMULCAST: StreamType
