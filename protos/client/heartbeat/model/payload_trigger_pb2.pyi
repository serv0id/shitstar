from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class PayloadTrigger(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PAYLOAD_TRIGGER_UNSPECIFIED: _ClassVar[PayloadTrigger]
    PAYLOAD_TRIGGER_PERIODIC: _ClassVar[PayloadTrigger]
    PAYLOAD_TRIGGER_PAUSE: _ClassVar[PayloadTrigger]
    PAYLOAD_TRIGGER_END: _ClassVar[PayloadTrigger]
    PAYLOAD_TRIGGER_ERROR: _ClassVar[PayloadTrigger]
PAYLOAD_TRIGGER_UNSPECIFIED: PayloadTrigger
PAYLOAD_TRIGGER_PERIODIC: PayloadTrigger
PAYLOAD_TRIGGER_PAUSE: PayloadTrigger
PAYLOAD_TRIGGER_END: PayloadTrigger
PAYLOAD_TRIGGER_ERROR: PayloadTrigger
