from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class LoginMethod(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PHONE_OTP: _ClassVar[LoginMethod]
    PHONE_IVR: _ClassVar[LoginMethod]
    PHONE_SNA: _ClassVar[LoginMethod]
    EMAIL_OTP: _ClassVar[LoginMethod]
PHONE_OTP: LoginMethod
PHONE_IVR: LoginMethod
PHONE_SNA: LoginMethod
EMAIL_OTP: LoginMethod
