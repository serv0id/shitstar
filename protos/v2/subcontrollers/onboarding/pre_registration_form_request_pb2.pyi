from v2.subcontrollers.onboarding import submit_consent_request_pb2 as _submit_consent_request_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PreRegistrationFormRequest(_message.Message):
    __slots__ = ("full_name", "phone_number", "country_prefix", "email", "consent_ids", "initiate_by", "source", "submit_consent_request")
    class InitiateBy(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        PHONE_OTP: _ClassVar[PreRegistrationFormRequest.InitiateBy]
        PHONE_IVR: _ClassVar[PreRegistrationFormRequest.InitiateBy]
    PHONE_OTP: PreRegistrationFormRequest.InitiateBy
    PHONE_IVR: PreRegistrationFormRequest.InitiateBy
    class Source(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        LOGIN: _ClassVar[PreRegistrationFormRequest.Source]
        PRE_LAUNCH: _ClassVar[PreRegistrationFormRequest.Source]
    LOGIN: PreRegistrationFormRequest.Source
    PRE_LAUNCH: PreRegistrationFormRequest.Source
    FULL_NAME_FIELD_NUMBER: _ClassVar[int]
    PHONE_NUMBER_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_PREFIX_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    CONSENT_IDS_FIELD_NUMBER: _ClassVar[int]
    INITIATE_BY_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    SUBMIT_CONSENT_REQUEST_FIELD_NUMBER: _ClassVar[int]
    full_name: str
    phone_number: str
    country_prefix: str
    email: str
    consent_ids: _containers.RepeatedScalarFieldContainer[int]
    initiate_by: PreRegistrationFormRequest.InitiateBy
    source: PreRegistrationFormRequest.Source
    submit_consent_request: _submit_consent_request_pb2.SubmitConsentRequest
    def __init__(self, full_name: _Optional[str] = ..., phone_number: _Optional[str] = ..., country_prefix: _Optional[str] = ..., email: _Optional[str] = ..., consent_ids: _Optional[_Iterable[int]] = ..., initiate_by: _Optional[_Union[PreRegistrationFormRequest.InitiateBy, str]] = ..., source: _Optional[_Union[PreRegistrationFormRequest.Source, str]] = ..., submit_consent_request: _Optional[_Union[_submit_consent_request_pb2.SubmitConsentRequest, _Mapping]] = ...) -> None: ...
