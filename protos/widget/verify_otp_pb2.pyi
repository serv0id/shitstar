from base import template_pb2 as _template_pb2
from base import widget_commons_pb2 as _widget_commons_pb2
from base import actions_pb2 as _actions_pb2
from feature.login_method import login_method_pb2 as _login_method_pb2
from feature.atom import button_pb2 as _button_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class VerifyOtpWidget(_message.Message):
    __slots__ = ("template", "widget_commons", "data")
    class OTPSource(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        DEFAULT: _ClassVar[VerifyOtpWidget.OTPSource]
        PHONE: _ClassVar[VerifyOtpWidget.OTPSource]
        EMAIL: _ClassVar[VerifyOtpWidget.OTPSource]
    DEFAULT: VerifyOtpWidget.OTPSource
    PHONE: VerifyOtpWidget.OTPSource
    EMAIL: VerifyOtpWidget.OTPSource
    class Data(_message.Message):
        __slots__ = ("title", "otp_length", "resend_otp_info_text", "resend_disable_duration_sec", "resend_otp", "resend_otp_ivr", "verify_otp_button", "help_rich_text", "phone_number", "is_error", "error_message", "widget_title", "edit_button_text", "email_address", "step_name", "otp_source", "consent_text", "skip_button", "recaptcha_enabled", "login_data", "sub_title", "resend_otp_email", "back_button", "resend_otp_info_pre_text", "resend_otp_info_post_text", "resent_toast_text", "help_rich_button")
        TITLE_FIELD_NUMBER: _ClassVar[int]
        OTP_LENGTH_FIELD_NUMBER: _ClassVar[int]
        RESEND_OTP_INFO_TEXT_FIELD_NUMBER: _ClassVar[int]
        RESEND_DISABLE_DURATION_SEC_FIELD_NUMBER: _ClassVar[int]
        RESEND_OTP_FIELD_NUMBER: _ClassVar[int]
        RESEND_OTP_IVR_FIELD_NUMBER: _ClassVar[int]
        VERIFY_OTP_BUTTON_FIELD_NUMBER: _ClassVar[int]
        HELP_RICH_TEXT_FIELD_NUMBER: _ClassVar[int]
        PHONE_NUMBER_FIELD_NUMBER: _ClassVar[int]
        IS_ERROR_FIELD_NUMBER: _ClassVar[int]
        ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
        WIDGET_TITLE_FIELD_NUMBER: _ClassVar[int]
        EDIT_BUTTON_TEXT_FIELD_NUMBER: _ClassVar[int]
        EMAIL_ADDRESS_FIELD_NUMBER: _ClassVar[int]
        STEP_NAME_FIELD_NUMBER: _ClassVar[int]
        OTP_SOURCE_FIELD_NUMBER: _ClassVar[int]
        CONSENT_TEXT_FIELD_NUMBER: _ClassVar[int]
        SKIP_BUTTON_FIELD_NUMBER: _ClassVar[int]
        RECAPTCHA_ENABLED_FIELD_NUMBER: _ClassVar[int]
        LOGIN_DATA_FIELD_NUMBER: _ClassVar[int]
        SUB_TITLE_FIELD_NUMBER: _ClassVar[int]
        RESEND_OTP_EMAIL_FIELD_NUMBER: _ClassVar[int]
        BACK_BUTTON_FIELD_NUMBER: _ClassVar[int]
        RESEND_OTP_INFO_PRE_TEXT_FIELD_NUMBER: _ClassVar[int]
        RESEND_OTP_INFO_POST_TEXT_FIELD_NUMBER: _ClassVar[int]
        RESENT_TOAST_TEXT_FIELD_NUMBER: _ClassVar[int]
        HELP_RICH_BUTTON_FIELD_NUMBER: _ClassVar[int]
        title: str
        otp_length: int
        resend_otp_info_text: str
        resend_disable_duration_sec: int
        resend_otp: VerifyOtpWidget.Button
        resend_otp_ivr: VerifyOtpWidget.Button
        verify_otp_button: VerifyOtpWidget.Button
        help_rich_text: str
        phone_number: str
        is_error: bool
        error_message: str
        widget_title: str
        edit_button_text: str
        email_address: str
        step_name: str
        otp_source: VerifyOtpWidget.OTPSource
        consent_text: str
        skip_button: VerifyOtpWidget.SkipCTA
        recaptcha_enabled: bool
        login_data: VerifyOtpWidget.LoginData
        sub_title: str
        resend_otp_email: _button_pb2.Button
        back_button: _button_pb2.Button
        resend_otp_info_pre_text: str
        resend_otp_info_post_text: str
        resent_toast_text: str
        help_rich_button: _button_pb2.Button
        def __init__(self, title: _Optional[str] = ..., otp_length: _Optional[int] = ..., resend_otp_info_text: _Optional[str] = ..., resend_disable_duration_sec: _Optional[int] = ..., resend_otp: _Optional[_Union[VerifyOtpWidget.Button, _Mapping]] = ..., resend_otp_ivr: _Optional[_Union[VerifyOtpWidget.Button, _Mapping]] = ..., verify_otp_button: _Optional[_Union[VerifyOtpWidget.Button, _Mapping]] = ..., help_rich_text: _Optional[str] = ..., phone_number: _Optional[str] = ..., is_error: bool = ..., error_message: _Optional[str] = ..., widget_title: _Optional[str] = ..., edit_button_text: _Optional[str] = ..., email_address: _Optional[str] = ..., step_name: _Optional[str] = ..., otp_source: _Optional[_Union[VerifyOtpWidget.OTPSource, str]] = ..., consent_text: _Optional[str] = ..., skip_button: _Optional[_Union[VerifyOtpWidget.SkipCTA, _Mapping]] = ..., recaptcha_enabled: bool = ..., login_data: _Optional[_Union[VerifyOtpWidget.LoginData, _Mapping]] = ..., sub_title: _Optional[str] = ..., resend_otp_email: _Optional[_Union[_button_pb2.Button, _Mapping]] = ..., back_button: _Optional[_Union[_button_pb2.Button, _Mapping]] = ..., resend_otp_info_pre_text: _Optional[str] = ..., resend_otp_info_post_text: _Optional[str] = ..., resent_toast_text: _Optional[str] = ..., help_rich_button: _Optional[_Union[_button_pb2.Button, _Mapping]] = ...) -> None: ...
    class Button(_message.Message):
        __slots__ = ("text", "actions", "icon_name")
        TEXT_FIELD_NUMBER: _ClassVar[int]
        ACTIONS_FIELD_NUMBER: _ClassVar[int]
        ICON_NAME_FIELD_NUMBER: _ClassVar[int]
        text: str
        actions: _actions_pb2.Actions
        icon_name: str
        def __init__(self, text: _Optional[str] = ..., actions: _Optional[_Union[_actions_pb2.Actions, _Mapping]] = ..., icon_name: _Optional[str] = ...) -> None: ...
    class SkipCTA(_message.Message):
        __slots__ = ("text", "icon_name", "actions")
        TEXT_FIELD_NUMBER: _ClassVar[int]
        ICON_NAME_FIELD_NUMBER: _ClassVar[int]
        ACTIONS_FIELD_NUMBER: _ClassVar[int]
        text: str
        icon_name: str
        actions: _actions_pb2.Actions
        def __init__(self, text: _Optional[str] = ..., icon_name: _Optional[str] = ..., actions: _Optional[_Union[_actions_pb2.Actions, _Mapping]] = ...) -> None: ...
    class LoginData(_message.Message):
        __slots__ = ("login_method",)
        LOGIN_METHOD_FIELD_NUMBER: _ClassVar[int]
        login_method: _login_method_pb2.LoginMethod
        def __init__(self, login_method: _Optional[_Union[_login_method_pb2.LoginMethod, str]] = ...) -> None: ...
    TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    WIDGET_COMMONS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    template: _template_pb2.Template
    widget_commons: _widget_commons_pb2.WidgetCommons
    data: VerifyOtpWidget.Data
    def __init__(self, template: _Optional[_Union[_template_pb2.Template, _Mapping]] = ..., widget_commons: _Optional[_Union[_widget_commons_pb2.WidgetCommons, _Mapping]] = ..., data: _Optional[_Union[VerifyOtpWidget.Data, _Mapping]] = ...) -> None: ...
