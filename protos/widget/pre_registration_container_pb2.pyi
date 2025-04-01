from base import widget_commons_pb2 as _widget_commons_pb2
from feature.branding import brand_pb2 as _brand_pb2
from widget import logo_pb2 as _logo_pb2
from widget import pre_registration_form_pb2 as _pre_registration_form_pb2
from widget import verify_otp_pb2 as _verify_otp_pb2
from widget import pre_registration_success_pb2 as _pre_registration_success_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PreRegistrationContainerWidget(_message.Message):
    __slots__ = ("widget_commons", "data")
    class Data(_message.Message):
        __slots__ = ("logo", "widgets", "brand_details")
        LOGO_FIELD_NUMBER: _ClassVar[int]
        WIDGETS_FIELD_NUMBER: _ClassVar[int]
        BRAND_DETAILS_FIELD_NUMBER: _ClassVar[int]
        logo: _brand_pb2.Brand
        widgets: _containers.RepeatedCompositeFieldContainer[PreRegistrationContainerWidget.PreRegistrationWidgets]
        brand_details: _logo_pb2.LogoWidget
        def __init__(self, logo: _Optional[_Union[_brand_pb2.Brand, str]] = ..., widgets: _Optional[_Iterable[_Union[PreRegistrationContainerWidget.PreRegistrationWidgets, _Mapping]]] = ..., brand_details: _Optional[_Union[_logo_pb2.LogoWidget, _Mapping]] = ...) -> None: ...
    class PreRegistrationWidgets(_message.Message):
        __slots__ = ("pre_registration_form", "verify_otp", "pre_registration_success")
        PRE_REGISTRATION_FORM_FIELD_NUMBER: _ClassVar[int]
        VERIFY_OTP_FIELD_NUMBER: _ClassVar[int]
        PRE_REGISTRATION_SUCCESS_FIELD_NUMBER: _ClassVar[int]
        pre_registration_form: _pre_registration_form_pb2.PreRegistrationFormWidget
        verify_otp: _verify_otp_pb2.VerifyOtpWidget
        pre_registration_success: _pre_registration_success_pb2.PreRegistrationSuccessWidget
        def __init__(self, pre_registration_form: _Optional[_Union[_pre_registration_form_pb2.PreRegistrationFormWidget, _Mapping]] = ..., verify_otp: _Optional[_Union[_verify_otp_pb2.VerifyOtpWidget, _Mapping]] = ..., pre_registration_success: _Optional[_Union[_pre_registration_success_pb2.PreRegistrationSuccessWidget, _Mapping]] = ...) -> None: ...
    WIDGET_COMMONS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    widget_commons: _widget_commons_pb2.WidgetCommons
    data: PreRegistrationContainerWidget.Data
    def __init__(self, widget_commons: _Optional[_Union[_widget_commons_pb2.WidgetCommons, _Mapping]] = ..., data: _Optional[_Union[PreRegistrationContainerWidget.Data, _Mapping]] = ...) -> None: ...
