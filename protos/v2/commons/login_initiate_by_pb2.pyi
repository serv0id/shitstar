from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class LoginInitiateBy(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PHONE_OTP: _ClassVar[LoginInitiateBy]
    PHONE_IVR: _ClassVar[LoginInitiateBy]
    PHONE_SNA: _ClassVar[LoginInitiateBy]
PHONE_OTP: LoginInitiateBy
PHONE_IVR: LoginInitiateBy
PHONE_SNA: LoginInitiateBy
