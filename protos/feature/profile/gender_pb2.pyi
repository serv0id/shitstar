from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class Gender(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    UNKNOWN: _ClassVar[Gender]
    MALE: _ClassVar[Gender]
    FEMALE: _ClassVar[Gender]
    OTHER: _ClassVar[Gender]
    PREFER_NOT_TO_SAY: _ClassVar[Gender]
UNKNOWN: Gender
MALE: Gender
FEMALE: Gender
OTHER: Gender
PREFER_NOT_TO_SAY: Gender
