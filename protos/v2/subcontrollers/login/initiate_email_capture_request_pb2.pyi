from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class InitiateEmailCaptureRequest(_message.Message):
    __slots__ = ("email_address", "consent_status", "password", "recaptcha_token")
    class ConsentStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        OPT_OUT: _ClassVar[InitiateEmailCaptureRequest.ConsentStatus]
        OPT_IN: _ClassVar[InitiateEmailCaptureRequest.ConsentStatus]
        ALREADY_OPTED_IN: _ClassVar[InitiateEmailCaptureRequest.ConsentStatus]
    OPT_OUT: InitiateEmailCaptureRequest.ConsentStatus
    OPT_IN: InitiateEmailCaptureRequest.ConsentStatus
    ALREADY_OPTED_IN: InitiateEmailCaptureRequest.ConsentStatus
    EMAIL_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    CONSENT_STATUS_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    RECAPTCHA_TOKEN_FIELD_NUMBER: _ClassVar[int]
    email_address: str
    consent_status: InitiateEmailCaptureRequest.ConsentStatus
    password: str
    recaptcha_token: str
    def __init__(self, email_address: _Optional[str] = ..., consent_status: _Optional[_Union[InitiateEmailCaptureRequest.ConsentStatus, str]] = ..., password: _Optional[str] = ..., recaptcha_token: _Optional[str] = ...) -> None: ...
