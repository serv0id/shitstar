from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class ContentSpread(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    SPREAD_UNSPECIFIED: _ClassVar[ContentSpread]
    SPREAD_START: _ClassVar[ContentSpread]
    SPREAD_END: _ClassVar[ContentSpread]
    SPREAD_EVEN: _ClassVar[ContentSpread]
SPREAD_UNSPECIFIED: ContentSpread
SPREAD_START: ContentSpread
SPREAD_END: ContentSpread
SPREAD_EVEN: ContentSpread
