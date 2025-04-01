from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class StreamMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    STREAM_MODE_UNSPECIFIED: _ClassVar[StreamMode]
    STREAM_MODE_VERTICAL: _ClassVar[StreamMode]
    STREAM_MODE_STANDARD: _ClassVar[StreamMode]
    STREAM_MODE_VR: _ClassVar[StreamMode]
STREAM_MODE_UNSPECIFIED: StreamMode
STREAM_MODE_VERTICAL: StreamMode
STREAM_MODE_STANDARD: StreamMode
STREAM_MODE_VR: StreamMode
