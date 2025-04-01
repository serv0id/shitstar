from base import widget_commons_pb2 as _widget_commons_pb2
from widget import email_capture_pb2 as _email_capture_pb2
from widget import verify_otp_pb2 as _verify_otp_pb2
from base import actions_pb2 as _actions_pb2
from feature.image import image_pb2 as _image_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class EmailCaptureContainerWidget(_message.Message):
    __slots__ = ("widget_commons", "data")
    class Source(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        DEFAULT: _ClassVar[EmailCaptureContainerWidget.Source]
        EMAIL_CAPTURE: _ClassVar[EmailCaptureContainerWidget.Source]
        EMAIL_UPDATE: _ClassVar[EmailCaptureContainerWidget.Source]
        EMAIL_NEW: _ClassVar[EmailCaptureContainerWidget.Source]
    DEFAULT: EmailCaptureContainerWidget.Source
    EMAIL_CAPTURE: EmailCaptureContainerWidget.Source
    EMAIL_UPDATE: EmailCaptureContainerWidget.Source
    EMAIL_NEW: EmailCaptureContainerWidget.Source
    class Data(_message.Message):
        __slots__ = ("widgets", "help_rich_text", "skip_cta", "is_back_enabled", "hero_image", "source")
        WIDGETS_FIELD_NUMBER: _ClassVar[int]
        HELP_RICH_TEXT_FIELD_NUMBER: _ClassVar[int]
        SKIP_CTA_FIELD_NUMBER: _ClassVar[int]
        IS_BACK_ENABLED_FIELD_NUMBER: _ClassVar[int]
        HERO_IMAGE_FIELD_NUMBER: _ClassVar[int]
        SOURCE_FIELD_NUMBER: _ClassVar[int]
        widgets: _containers.RepeatedCompositeFieldContainer[EmailCaptureContainerWidget.EmailCaptureContainerWidgets]
        help_rich_text: str
        skip_cta: EmailCaptureContainerWidget.SkipCTA
        is_back_enabled: bool
        hero_image: _image_pb2.Image
        source: EmailCaptureContainerWidget.Source
        def __init__(self, widgets: _Optional[_Iterable[_Union[EmailCaptureContainerWidget.EmailCaptureContainerWidgets, _Mapping]]] = ..., help_rich_text: _Optional[str] = ..., skip_cta: _Optional[_Union[EmailCaptureContainerWidget.SkipCTA, _Mapping]] = ..., is_back_enabled: bool = ..., hero_image: _Optional[_Union[_image_pb2.Image, _Mapping]] = ..., source: _Optional[_Union[EmailCaptureContainerWidget.Source, str]] = ...) -> None: ...
    class SkipCTA(_message.Message):
        __slots__ = ("text", "icon_name", "actions")
        TEXT_FIELD_NUMBER: _ClassVar[int]
        ICON_NAME_FIELD_NUMBER: _ClassVar[int]
        ACTIONS_FIELD_NUMBER: _ClassVar[int]
        text: str
        icon_name: str
        actions: _actions_pb2.Actions
        def __init__(self, text: _Optional[str] = ..., icon_name: _Optional[str] = ..., actions: _Optional[_Union[_actions_pb2.Actions, _Mapping]] = ...) -> None: ...
    class EmailCaptureContainerWidgets(_message.Message):
        __slots__ = ("email_capture", "verify_otp")
        EMAIL_CAPTURE_FIELD_NUMBER: _ClassVar[int]
        VERIFY_OTP_FIELD_NUMBER: _ClassVar[int]
        email_capture: _email_capture_pb2.EmailCaptureWidget
        verify_otp: _verify_otp_pb2.VerifyOtpWidget
        def __init__(self, email_capture: _Optional[_Union[_email_capture_pb2.EmailCaptureWidget, _Mapping]] = ..., verify_otp: _Optional[_Union[_verify_otp_pb2.VerifyOtpWidget, _Mapping]] = ...) -> None: ...
    WIDGET_COMMONS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    widget_commons: _widget_commons_pb2.WidgetCommons
    data: EmailCaptureContainerWidget.Data
    def __init__(self, widget_commons: _Optional[_Union[_widget_commons_pb2.WidgetCommons, _Mapping]] = ..., data: _Optional[_Union[EmailCaptureContainerWidget.Data, _Mapping]] = ...) -> None: ...
