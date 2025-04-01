from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ResendOtpProperties(_message.Message):
    __slots__ = ("verification_type", "source")
    class VerificationType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        VERIFICATION_TYPE_UNSPECIFIED: _ClassVar[ResendOtpProperties.VerificationType]
        VERIFICATION_TYPE_SMS: _ClassVar[ResendOtpProperties.VerificationType]
        VERIFICATION_TYPE_CALL: _ClassVar[ResendOtpProperties.VerificationType]
        VERIFICATION_TYPE_EMAIL: _ClassVar[ResendOtpProperties.VerificationType]
    VERIFICATION_TYPE_UNSPECIFIED: ResendOtpProperties.VerificationType
    VERIFICATION_TYPE_SMS: ResendOtpProperties.VerificationType
    VERIFICATION_TYPE_CALL: ResendOtpProperties.VerificationType
    VERIFICATION_TYPE_EMAIL: ResendOtpProperties.VerificationType
    class ResendOtpSource(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        RESEND_OTP_SOURCE_UNSPECIFIED: _ClassVar[ResendOtpProperties.ResendOtpSource]
        RESEND_OTP_SOURCE_ONBOARDING: _ClassVar[ResendOtpProperties.ResendOtpSource]
        RESEND_OTP_SOURCE_PARENTAL_LOCK: _ClassVar[ResendOtpProperties.ResendOtpSource]
        RESEND_OTP_SOURCE_LOG_OUT_ALL_DEVICES: _ClassVar[ResendOtpProperties.ResendOtpSource]
        RESEND_OTP_SOURCE_EMAIL_CAPTURE: _ClassVar[ResendOtpProperties.ResendOtpSource]
        RESEND_OTP_SOURCE_PREREG: _ClassVar[ResendOtpProperties.ResendOtpSource]
        RESEND_OTP_SOURCE_DELETE_ACCOUNT: _ClassVar[ResendOtpProperties.ResendOtpSource]
        RESEND_OTP_SOURCE_LOGIN_EXP_WATCH: _ClassVar[ResendOtpProperties.ResendOtpSource]
        RESEND_OTP_SOURCE_EMAIL_OTP_LOGIN: _ClassVar[ResendOtpProperties.ResendOtpSource]
        RESEND_OTP_SOURCE_UPDATE_EMAIL_OTP: _ClassVar[ResendOtpProperties.ResendOtpSource]
    RESEND_OTP_SOURCE_UNSPECIFIED: ResendOtpProperties.ResendOtpSource
    RESEND_OTP_SOURCE_ONBOARDING: ResendOtpProperties.ResendOtpSource
    RESEND_OTP_SOURCE_PARENTAL_LOCK: ResendOtpProperties.ResendOtpSource
    RESEND_OTP_SOURCE_LOG_OUT_ALL_DEVICES: ResendOtpProperties.ResendOtpSource
    RESEND_OTP_SOURCE_EMAIL_CAPTURE: ResendOtpProperties.ResendOtpSource
    RESEND_OTP_SOURCE_PREREG: ResendOtpProperties.ResendOtpSource
    RESEND_OTP_SOURCE_DELETE_ACCOUNT: ResendOtpProperties.ResendOtpSource
    RESEND_OTP_SOURCE_LOGIN_EXP_WATCH: ResendOtpProperties.ResendOtpSource
    RESEND_OTP_SOURCE_EMAIL_OTP_LOGIN: ResendOtpProperties.ResendOtpSource
    RESEND_OTP_SOURCE_UPDATE_EMAIL_OTP: ResendOtpProperties.ResendOtpSource
    VERIFICATION_TYPE_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    verification_type: ResendOtpProperties.VerificationType
    source: ResendOtpProperties.ResendOtpSource
    def __init__(self, verification_type: _Optional[_Union[ResendOtpProperties.VerificationType, str]] = ..., source: _Optional[_Union[ResendOtpProperties.ResendOtpSource, str]] = ...) -> None: ...
