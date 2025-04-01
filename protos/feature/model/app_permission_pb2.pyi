from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class AppPermission(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    NONE: _ClassVar[AppPermission]
    PUSH_NOTIFICATION: _ClassVar[AppPermission]
NONE: AppPermission
PUSH_NOTIFICATION: AppPermission
