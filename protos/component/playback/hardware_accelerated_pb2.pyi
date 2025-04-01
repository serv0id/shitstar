from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class HardwareAccelerated(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    HARDWARE_ACCELERATED_UNSPECIFIED: _ClassVar[HardwareAccelerated]
    HARDWARE_ACCELERATED_SUPPORTED: _ClassVar[HardwareAccelerated]
    HARDWARE_ACCELERATED_NOT_SUPPORTED: _ClassVar[HardwareAccelerated]
HARDWARE_ACCELERATED_UNSPECIFIED: HardwareAccelerated
HARDWARE_ACCELERATED_SUPPORTED: HardwareAccelerated
HARDWARE_ACCELERATED_NOT_SUPPORTED: HardwareAccelerated
