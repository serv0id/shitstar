from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class Orientation(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ORIENTATION_UNSPECIFIED: _ClassVar[Orientation]
    ORIENTATION_PORTRAIT: _ClassVar[Orientation]
    ORIENTATION_LANDSCAPE: _ClassVar[Orientation]
ORIENTATION_UNSPECIFIED: Orientation
ORIENTATION_PORTRAIT: Orientation
ORIENTATION_LANDSCAPE: Orientation
