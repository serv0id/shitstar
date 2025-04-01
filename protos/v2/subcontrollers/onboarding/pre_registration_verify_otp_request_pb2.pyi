from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class PreRegistrationVerifyOtpRequest(_message.Message):
    __slots__ = ("phone_number", "verification_code", "email", "full_name", "consent_ids", "is_consent_given")
    PHONE_NUMBER_FIELD_NUMBER: _ClassVar[int]
    VERIFICATION_CODE_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    FULL_NAME_FIELD_NUMBER: _ClassVar[int]
    CONSENT_IDS_FIELD_NUMBER: _ClassVar[int]
    IS_CONSENT_GIVEN_FIELD_NUMBER: _ClassVar[int]
    phone_number: str
    verification_code: str
    email: str
    full_name: str
    consent_ids: _containers.RepeatedScalarFieldContainer[int]
    is_consent_given: bool
    def __init__(self, phone_number: _Optional[str] = ..., verification_code: _Optional[str] = ..., email: _Optional[str] = ..., full_name: _Optional[str] = ..., consent_ids: _Optional[_Iterable[int]] = ..., is_consent_given: bool = ...) -> None: ...
