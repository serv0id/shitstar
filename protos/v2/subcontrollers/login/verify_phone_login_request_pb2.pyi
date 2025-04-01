from v2.commons import login_initiate_by_pb2 as _login_initiate_by_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class VerifyPhoneLoginRequest(_message.Message):
    __slots__ = ("verification_code", "mode", "consent_status", "login_device_meta", "source", "initiate_by", "phone_number", "encrypted_identifier", "email_address")
    class Mode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        MANUAL: _ClassVar[VerifyPhoneLoginRequest.Mode]
        AUTO: _ClassVar[VerifyPhoneLoginRequest.Mode]
    MANUAL: VerifyPhoneLoginRequest.Mode
    AUTO: VerifyPhoneLoginRequest.Mode
    class ConsentStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ALREADY_OPTED: _ClassVar[VerifyPhoneLoginRequest.ConsentStatus]
        OPT_OUT: _ClassVar[VerifyPhoneLoginRequest.ConsentStatus]
        OPT_IN: _ClassVar[VerifyPhoneLoginRequest.ConsentStatus]
    ALREADY_OPTED: VerifyPhoneLoginRequest.ConsentStatus
    OPT_OUT: VerifyPhoneLoginRequest.ConsentStatus
    OPT_IN: VerifyPhoneLoginRequest.ConsentStatus
    class Source(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        LOGIN: _ClassVar[VerifyPhoneLoginRequest.Source]
        PRE_LAUNCH: _ClassVar[VerifyPhoneLoginRequest.Source]
        SKIPPABLE_LOGIN: _ClassVar[VerifyPhoneLoginRequest.Source]
    LOGIN: VerifyPhoneLoginRequest.Source
    PRE_LAUNCH: VerifyPhoneLoginRequest.Source
    SKIPPABLE_LOGIN: VerifyPhoneLoginRequest.Source
    class LoginDeviceMeta(_message.Message):
        __slots__ = ("device_name",)
        DEVICE_NAME_FIELD_NUMBER: _ClassVar[int]
        device_name: str
        def __init__(self, device_name: _Optional[str] = ...) -> None: ...
    VERIFICATION_CODE_FIELD_NUMBER: _ClassVar[int]
    MODE_FIELD_NUMBER: _ClassVar[int]
    CONSENT_STATUS_FIELD_NUMBER: _ClassVar[int]
    LOGIN_DEVICE_META_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    INITIATE_BY_FIELD_NUMBER: _ClassVar[int]
    PHONE_NUMBER_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTED_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    EMAIL_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    verification_code: str
    mode: VerifyPhoneLoginRequest.Mode
    consent_status: VerifyPhoneLoginRequest.ConsentStatus
    login_device_meta: VerifyPhoneLoginRequest.LoginDeviceMeta
    source: VerifyPhoneLoginRequest.Source
    initiate_by: _login_initiate_by_pb2.LoginInitiateBy
    phone_number: str
    encrypted_identifier: str
    email_address: str
    def __init__(self, verification_code: _Optional[str] = ..., mode: _Optional[_Union[VerifyPhoneLoginRequest.Mode, str]] = ..., consent_status: _Optional[_Union[VerifyPhoneLoginRequest.ConsentStatus, str]] = ..., login_device_meta: _Optional[_Union[VerifyPhoneLoginRequest.LoginDeviceMeta, _Mapping]] = ..., source: _Optional[_Union[VerifyPhoneLoginRequest.Source, str]] = ..., initiate_by: _Optional[_Union[_login_initiate_by_pb2.LoginInitiateBy, str]] = ..., phone_number: _Optional[str] = ..., encrypted_identifier: _Optional[str] = ..., email_address: _Optional[str] = ...) -> None: ...
