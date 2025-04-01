from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class Orientation(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    DEFAULT: _ClassVar[Orientation]
    PORTRAIT: _ClassVar[Orientation]
    LANDSCAPE: _ClassVar[Orientation]
DEFAULT: Orientation
PORTRAIT: Orientation
LANDSCAPE: Orientation
