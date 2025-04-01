from base import widget_commons_pb2 as _widget_commons_pb2
from base import actions_pb2 as _actions_pb2
from feature.consent import consent_type_pb2 as _consent_type_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class EmailCaptureWidget(_message.Message):
    __slots__ = ("widget_commons", "data")
    class ConsentStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        OPT_OUT: _ClassVar[EmailCaptureWidget.ConsentStatus]
        OPT_IN: _ClassVar[EmailCaptureWidget.ConsentStatus]
        ALREADY_OPTED_IN: _ClassVar[EmailCaptureWidget.ConsentStatus]
    OPT_OUT: EmailCaptureWidget.ConsentStatus
    OPT_IN: EmailCaptureWidget.ConsentStatus
    ALREADY_OPTED_IN: EmailCaptureWidget.ConsentStatus
    class Data(_message.Message):
        __slots__ = ("step_name", "title", "input_label", "placeholder", "email_regex", "regex_error_message", "error_message", "send_otp_button", "consent_text", "consent_status", "email_address", "password_input_label", "password_placeholder", "password_regex", "password_error_message", "password_regex_error_message")
        STEP_NAME_FIELD_NUMBER: _ClassVar[int]
        TITLE_FIELD_NUMBER: _ClassVar[int]
        INPUT_LABEL_FIELD_NUMBER: _ClassVar[int]
        PLACEHOLDER_FIELD_NUMBER: _ClassVar[int]
        EMAIL_REGEX_FIELD_NUMBER: _ClassVar[int]
        REGEX_ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
        ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
        SEND_OTP_BUTTON_FIELD_NUMBER: _ClassVar[int]
        CONSENT_TEXT_FIELD_NUMBER: _ClassVar[int]
        CONSENT_STATUS_FIELD_NUMBER: _ClassVar[int]
        EMAIL_ADDRESS_FIELD_NUMBER: _ClassVar[int]
        PASSWORD_INPUT_LABEL_FIELD_NUMBER: _ClassVar[int]
        PASSWORD_PLACEHOLDER_FIELD_NUMBER: _ClassVar[int]
        PASSWORD_REGEX_FIELD_NUMBER: _ClassVar[int]
        PASSWORD_ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
        PASSWORD_REGEX_ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
        step_name: str
        title: str
        input_label: str
        placeholder: str
        email_regex: str
        regex_error_message: str
        error_message: str
        send_otp_button: EmailCaptureWidget.SendOtpButton
        consent_text: str
        consent_status: EmailCaptureWidget.ConsentStatus
        email_address: str
        password_input_label: str
        password_placeholder: str
        password_regex: str
        password_error_message: str
        password_regex_error_message: str
        def __init__(self, step_name: _Optional[str] = ..., title: _Optional[str] = ..., input_label: _Optional[str] = ..., placeholder: _Optional[str] = ..., email_regex: _Optional[str] = ..., regex_error_message: _Optional[str] = ..., error_message: _Optional[str] = ..., send_otp_button: _Optional[_Union[EmailCaptureWidget.SendOtpButton, _Mapping]] = ..., consent_text: _Optional[str] = ..., consent_status: _Optional[_Union[EmailCaptureWidget.ConsentStatus, str]] = ..., email_address: _Optional[str] = ..., password_input_label: _Optional[str] = ..., password_placeholder: _Optional[str] = ..., password_regex: _Optional[str] = ..., password_error_message: _Optional[str] = ..., password_regex_error_message: _Optional[str] = ...) -> None: ...
    class SendOtpButton(_message.Message):
        __slots__ = ("text", "actions")
        TEXT_FIELD_NUMBER: _ClassVar[int]
        ACTIONS_FIELD_NUMBER: _ClassVar[int]
        text: str
        actions: _actions_pb2.Actions
        def __init__(self, text: _Optional[str] = ..., actions: _Optional[_Union[_actions_pb2.Actions, _Mapping]] = ...) -> None: ...
    WIDGET_COMMONS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    widget_commons: _widget_commons_pb2.WidgetCommons
    data: EmailCaptureWidget.Data
    def __init__(self, widget_commons: _Optional[_Union[_widget_commons_pb2.WidgetCommons, _Mapping]] = ..., data: _Optional[_Union[EmailCaptureWidget.Data, _Mapping]] = ...) -> None: ...
