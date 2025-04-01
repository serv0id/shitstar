from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class JourneyType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    JOURNEY_TYPE_UNSPECIFIED: _ClassVar[JourneyType]
    JOURNEY_TYPE_NORMAL: _ClassVar[JourneyType]
    JOURNEY_TYPE_RETRY_MANUAL: _ClassVar[JourneyType]
    JOURNEY_TYPE_RETRY_AUTO: _ClassVar[JourneyType]
JOURNEY_TYPE_UNSPECIFIED: JourneyType
JOURNEY_TYPE_NORMAL: JourneyType
JOURNEY_TYPE_RETRY_MANUAL: JourneyType
JOURNEY_TYPE_RETRY_AUTO: JourneyType
