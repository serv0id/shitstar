from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class CastingConnectionState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CASTING_CONNECTION_STATE_UNSPECIFIED: _ClassVar[CastingConnectionState]
    CASTING_CONNECTION_STATE_NOT_CONNECTED: _ClassVar[CastingConnectionState]
    CASTING_CONNECTION_STATE_STARTED: _ClassVar[CastingConnectionState]
    CASTING_CONNECTION_STATE_START_FAILED: _ClassVar[CastingConnectionState]
    CASTING_CONNECTION_STATE_RESUMED: _ClassVar[CastingConnectionState]
    CASTING_CONNECTION_STATE_RESUME_FAILED: _ClassVar[CastingConnectionState]
    CASTING_CONNECTION_STATE_ENDED: _ClassVar[CastingConnectionState]
    CASTING_CONNECTION_STATE_SUSPENDED: _ClassVar[CastingConnectionState]
CASTING_CONNECTION_STATE_UNSPECIFIED: CastingConnectionState
CASTING_CONNECTION_STATE_NOT_CONNECTED: CastingConnectionState
CASTING_CONNECTION_STATE_STARTED: CastingConnectionState
CASTING_CONNECTION_STATE_START_FAILED: CastingConnectionState
CASTING_CONNECTION_STATE_RESUMED: CastingConnectionState
CASTING_CONNECTION_STATE_RESUME_FAILED: CastingConnectionState
CASTING_CONNECTION_STATE_ENDED: CastingConnectionState
CASTING_CONNECTION_STATE_SUSPENDED: CastingConnectionState
