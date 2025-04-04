from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class CastingDisconnectionReason(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CASTING_DISCONNECTION_REASON_UNSPECIFIED: _ClassVar[CastingDisconnectionReason]
    CASTING_DISCONNECTION_REASON_DISCONNECT_BUTTON: _ClassVar[CastingDisconnectionReason]
    CASTING_DISCONNECTION_REASON_NETWORK_CHANGE: _ClassVar[CastingDisconnectionReason]
    CASTING_DISCONNECTION_REASON_DEVICE_LOST: _ClassVar[CastingDisconnectionReason]
    CASTING_DISCONNECTION_REASON_ERROR: _ClassVar[CastingDisconnectionReason]
CASTING_DISCONNECTION_REASON_UNSPECIFIED: CastingDisconnectionReason
CASTING_DISCONNECTION_REASON_DISCONNECT_BUTTON: CastingDisconnectionReason
CASTING_DISCONNECTION_REASON_NETWORK_CHANGE: CastingDisconnectionReason
CASTING_DISCONNECTION_REASON_DEVICE_LOST: CastingDisconnectionReason
CASTING_DISCONNECTION_REASON_ERROR: CastingDisconnectionReason
