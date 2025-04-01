from v2.subcontrollers.onboarding import submit_consent_request_pb2 as _submit_consent_request_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class InitiatePhoneLoginRequest(_message.Message):
    __slots__ = ("initiate_by", "source", "submit_consent_request", "mode", "is_consent_given", "recaptcha_token", "phone_number", "encrypted_identifier", "email_address")
    class InitiateBy(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        PHONE_OTP: _ClassVar[InitiatePhoneLoginRequest.InitiateBy]
        PHONE_IVR: _ClassVar[InitiatePhoneLoginRequest.InitiateBy]
        PHONE_SNA: _ClassVar[InitiatePhoneLoginRequest.InitiateBy]
        EMAIL_OTP: _ClassVar[InitiatePhoneLoginRequest.InitiateBy]
    PHONE_OTP: InitiatePhoneLoginRequest.InitiateBy
    PHONE_IVR: InitiatePhoneLoginRequest.InitiateBy
    PHONE_SNA: InitiatePhoneLoginRequest.InitiateBy
    EMAIL_OTP: InitiatePhoneLoginRequest.InitiateBy
    class Source(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        LOGIN: _ClassVar[InitiatePhoneLoginRequest.Source]
        PRE_LAUNCH: _ClassVar[InitiatePhoneLoginRequest.Source]
        SKIPPABLE_LOGIN: _ClassVar[InitiatePhoneLoginRequest.Source]
    LOGIN: InitiatePhoneLoginRequest.Source
    PRE_LAUNCH: InitiatePhoneLoginRequest.Source
    SKIPPABLE_LOGIN: InitiatePhoneLoginRequest.Source
    class Mode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        MANUAL: _ClassVar[InitiatePhoneLoginRequest.Mode]
        AUTO: _ClassVar[InitiatePhoneLoginRequest.Mode]
    MANUAL: InitiatePhoneLoginRequest.Mode
    AUTO: InitiatePhoneLoginRequest.Mode
    INITIATE_BY_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    SUBMIT_CONSENT_REQUEST_FIELD_NUMBER: _ClassVar[int]
    MODE_FIELD_NUMBER: _ClassVar[int]
    IS_CONSENT_GIVEN_FIELD_NUMBER: _ClassVar[int]
    RECAPTCHA_TOKEN_FIELD_NUMBER: _ClassVar[int]
    PHONE_NUMBER_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTED_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    EMAIL_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    initiate_by: InitiatePhoneLoginRequest.InitiateBy
    source: InitiatePhoneLoginRequest.Source
    submit_consent_request: _submit_consent_request_pb2.SubmitConsentRequest
    mode: InitiatePhoneLoginRequest.Mode
    is_consent_given: bool
    recaptcha_token: str
    phone_number: str
    encrypted_identifier: str
    email_address: str
    def __init__(self, initiate_by: _Optional[_Union[InitiatePhoneLoginRequest.InitiateBy, str]] = ..., source: _Optional[_Union[InitiatePhoneLoginRequest.Source, str]] = ..., submit_consent_request: _Optional[_Union[_submit_consent_request_pb2.SubmitConsentRequest, _Mapping]] = ..., mode: _Optional[_Union[InitiatePhoneLoginRequest.Mode, str]] = ..., is_consent_given: bool = ..., recaptcha_token: _Optional[str] = ..., phone_number: _Optional[str] = ..., encrypted_identifier: _Optional[str] = ..., email_address: _Optional[str] = ...) -> None: ...
