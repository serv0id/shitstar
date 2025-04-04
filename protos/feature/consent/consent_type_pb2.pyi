from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class ConsentType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    UNKNOWN: _ClassVar[ConsentType]
    PPTOU: _ClassVar[ConsentType]
    NOTIFICATION: _ClassVar[ConsentType]
    SMS: _ClassVar[ConsentType]
    WHATSAPP: _ClassVar[ConsentType]
    EMAIL: _ClassVar[ConsentType]
UNKNOWN: ConsentType
PPTOU: ConsentType
NOTIFICATION: ConsentType
SMS: ConsentType
WHATSAPP: ConsentType
EMAIL: ConsentType
