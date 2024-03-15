from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class ArrowPosition(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    POSITION_UNSPECIFIED: _ClassVar[ArrowPosition]
    POSITION_START: _ClassVar[ArrowPosition]
    POSITION_END: _ClassVar[ArrowPosition]
    POSITION_CENTER: _ClassVar[ArrowPosition]
POSITION_UNSPECIFIED: ArrowPosition
POSITION_START: ArrowPosition
POSITION_END: ArrowPosition
POSITION_CENTER: ArrowPosition
