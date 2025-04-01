from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class ConsentStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ALREADY_OPTED: _ClassVar[ConsentStatus]
    OPT_OUT: _ClassVar[ConsentStatus]
    OPT_IN: _ClassVar[ConsentStatus]
ALREADY_OPTED: ConsentStatus
OPT_OUT: ConsentStatus
OPT_IN: ConsentStatus
