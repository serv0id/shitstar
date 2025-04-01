from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class AvailableQuality(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    AVAILABLE_QUALITY_UNSPECIFIED: _ClassVar[AvailableQuality]
    AVAILABLE_QUALITY_SD: _ClassVar[AvailableQuality]
    AVAILABLE_QUALITY_HD: _ClassVar[AvailableQuality]
    AVAILABLE_QUALITY_FULL_HD: _ClassVar[AvailableQuality]
AVAILABLE_QUALITY_UNSPECIFIED: AvailableQuality
AVAILABLE_QUALITY_SD: AvailableQuality
AVAILABLE_QUALITY_HD: AvailableQuality
AVAILABLE_QUALITY_FULL_HD: AvailableQuality
