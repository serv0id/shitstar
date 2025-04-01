from base import actions_pb2 as _actions_pb2
from base import widget_commons_pb2 as _widget_commons_pb2
from feature.image import image_pb2 as _image_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ReAuthenticationWidget(_message.Message):
    __slots__ = ("widget_commons", "data")
    class Data(_message.Message):
        __slots__ = ("illustration", "title", "desc", "pin_size", "resend_otp", "verify_via_call", "time_text", "submit", "error_message", "resend_disable_duration_sec", "submit_btn_label", "recaptcha_enabled")
        ILLUSTRATION_FIELD_NUMBER: _ClassVar[int]
        TITLE_FIELD_NUMBER: _ClassVar[int]
        DESC_FIELD_NUMBER: _ClassVar[int]
        PIN_SIZE_FIELD_NUMBER: _ClassVar[int]
        RESEND_OTP_FIELD_NUMBER: _ClassVar[int]
        VERIFY_VIA_CALL_FIELD_NUMBER: _ClassVar[int]
        TIME_TEXT_FIELD_NUMBER: _ClassVar[int]
        SUBMIT_FIELD_NUMBER: _ClassVar[int]
        ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
        RESEND_DISABLE_DURATION_SEC_FIELD_NUMBER: _ClassVar[int]
        SUBMIT_BTN_LABEL_FIELD_NUMBER: _ClassVar[int]
        RECAPTCHA_ENABLED_FIELD_NUMBER: _ClassVar[int]
        illustration: _image_pb2.Image
        title: str
        desc: str
        pin_size: int
        resend_otp: ReAuthenticationWidget.CTA
        verify_via_call: ReAuthenticationWidget.CTA
        time_text: str
        submit: _actions_pb2.Actions
        error_message: str
        resend_disable_duration_sec: int
        submit_btn_label: str
        recaptcha_enabled: bool
        def __init__(self, illustration: _Optional[_Union[_image_pb2.Image, _Mapping]] = ..., title: _Optional[str] = ..., desc: _Optional[str] = ..., pin_size: _Optional[int] = ..., resend_otp: _Optional[_Union[ReAuthenticationWidget.CTA, _Mapping]] = ..., verify_via_call: _Optional[_Union[ReAuthenticationWidget.CTA, _Mapping]] = ..., time_text: _Optional[str] = ..., submit: _Optional[_Union[_actions_pb2.Actions, _Mapping]] = ..., error_message: _Optional[str] = ..., resend_disable_duration_sec: _Optional[int] = ..., submit_btn_label: _Optional[str] = ..., recaptcha_enabled: bool = ...) -> None: ...
    class CTA(_message.Message):
        __slots__ = ("label", "action", "icon_name")
        LABEL_FIELD_NUMBER: _ClassVar[int]
        ACTION_FIELD_NUMBER: _ClassVar[int]
        ICON_NAME_FIELD_NUMBER: _ClassVar[int]
        label: str
        action: _actions_pb2.Actions
        icon_name: str
        def __init__(self, label: _Optional[str] = ..., action: _Optional[_Union[_actions_pb2.Actions, _Mapping]] = ..., icon_name: _Optional[str] = ...) -> None: ...
    WIDGET_COMMONS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    widget_commons: _widget_commons_pb2.WidgetCommons
    data: ReAuthenticationWidget.Data
    def __init__(self, widget_commons: _Optional[_Union[_widget_commons_pb2.WidgetCommons, _Mapping]] = ..., data: _Optional[_Union[ReAuthenticationWidget.Data, _Mapping]] = ...) -> None: ...
