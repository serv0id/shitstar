from base import template_pb2 as _template_pb2
from base import widget_commons_pb2 as _widget_commons_pb2
from widget import previous_logins_pb2 as _previous_logins_pb2
from widget import login_with_phone_pb2 as _login_with_phone_pb2
from widget import login_with_qr_pb2 as _login_with_qr_pb2
from widget import hero_pb2 as _hero_pb2
from widget import divider_pb2 as _divider_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class LoginContainerWidget(_message.Message):
    __slots__ = ("template", "widget_commons", "data")
    class ContentAlignment(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        DEFAULT: _ClassVar[LoginContainerWidget.ContentAlignment]
        RIGHT: _ClassVar[LoginContainerWidget.ContentAlignment]
    DEFAULT: LoginContainerWidget.ContentAlignment
    RIGHT: LoginContainerWidget.ContentAlignment
    class Data(_message.Message):
        __slots__ = ("title", "sub_title", "widgets", "help_rich_text", "content_alignment", "recaptcha_enabled", "recaptcha_v2_enabled")
        TITLE_FIELD_NUMBER: _ClassVar[int]
        SUB_TITLE_FIELD_NUMBER: _ClassVar[int]
        WIDGETS_FIELD_NUMBER: _ClassVar[int]
        HELP_RICH_TEXT_FIELD_NUMBER: _ClassVar[int]
        CONTENT_ALIGNMENT_FIELD_NUMBER: _ClassVar[int]
        RECAPTCHA_ENABLED_FIELD_NUMBER: _ClassVar[int]
        RECAPTCHA_V2_ENABLED_FIELD_NUMBER: _ClassVar[int]
        title: str
        sub_title: str
        widgets: _containers.RepeatedCompositeFieldContainer[LoginContainerWidget.LoginContainerWidgets]
        help_rich_text: str
        content_alignment: LoginContainerWidget.ContentAlignment
        recaptcha_enabled: bool
        recaptcha_v2_enabled: bool
        def __init__(self, title: _Optional[str] = ..., sub_title: _Optional[str] = ..., widgets: _Optional[_Iterable[_Union[LoginContainerWidget.LoginContainerWidgets, _Mapping]]] = ..., help_rich_text: _Optional[str] = ..., content_alignment: _Optional[_Union[LoginContainerWidget.ContentAlignment, str]] = ..., recaptcha_enabled: bool = ..., recaptcha_v2_enabled: bool = ...) -> None: ...
    class LoginContainerWidgets(_message.Message):
        __slots__ = ("previous_logins", "login_with_phone", "login_with_qr", "hero_widget", "divider")
        PREVIOUS_LOGINS_FIELD_NUMBER: _ClassVar[int]
        LOGIN_WITH_PHONE_FIELD_NUMBER: _ClassVar[int]
        LOGIN_WITH_QR_FIELD_NUMBER: _ClassVar[int]
        HERO_WIDGET_FIELD_NUMBER: _ClassVar[int]
        DIVIDER_FIELD_NUMBER: _ClassVar[int]
        previous_logins: _previous_logins_pb2.PreviousLoginsWidget
        login_with_phone: _login_with_phone_pb2.LoginWithPhoneWidget
        login_with_qr: _login_with_qr_pb2.LoginWithQrWidget
        hero_widget: _hero_pb2.HeroWidget
        divider: _divider_pb2.DividerWidget
        def __init__(self, previous_logins: _Optional[_Union[_previous_logins_pb2.PreviousLoginsWidget, _Mapping]] = ..., login_with_phone: _Optional[_Union[_login_with_phone_pb2.LoginWithPhoneWidget, _Mapping]] = ..., login_with_qr: _Optional[_Union[_login_with_qr_pb2.LoginWithQrWidget, _Mapping]] = ..., hero_widget: _Optional[_Union[_hero_pb2.HeroWidget, _Mapping]] = ..., divider: _Optional[_Union[_divider_pb2.DividerWidget, _Mapping]] = ...) -> None: ...
    TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    WIDGET_COMMONS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    template: _template_pb2.Template
    widget_commons: _widget_commons_pb2.WidgetCommons
    data: LoginContainerWidget.Data
    def __init__(self, template: _Optional[_Union[_template_pb2.Template, _Mapping]] = ..., widget_commons: _Optional[_Union[_widget_commons_pb2.WidgetCommons, _Mapping]] = ..., data: _Optional[_Union[LoginContainerWidget.Data, _Mapping]] = ...) -> None: ...
