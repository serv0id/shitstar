from base import widget_commons_pb2 as _widget_commons_pb2
from widget import promo_landing_pb2 as _promo_landing_pb2
from widget import promo_landing_container_pb2 as _promo_landing_container_pb2
from widget import login_with_phone_pb2 as _login_with_phone_pb2
from widget import login_container_pb2 as _login_container_pb2
from widget import faq_pb2 as _faq_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class UserRegistrationContainerWidget(_message.Message):
    __slots__ = ("widget_commons", "data")
    class Data(_message.Message):
        __slots__ = ("promo_landing", "login_with_phone", "promo_landing_container", "login_container", "faq")
        PROMO_LANDING_FIELD_NUMBER: _ClassVar[int]
        LOGIN_WITH_PHONE_FIELD_NUMBER: _ClassVar[int]
        PROMO_LANDING_CONTAINER_FIELD_NUMBER: _ClassVar[int]
        LOGIN_CONTAINER_FIELD_NUMBER: _ClassVar[int]
        FAQ_FIELD_NUMBER: _ClassVar[int]
        promo_landing: _promo_landing_pb2.PromoLandingWidget
        login_with_phone: _login_with_phone_pb2.LoginWithPhoneWidget
        promo_landing_container: _promo_landing_container_pb2.PromoLandingContainerWidget
        login_container: _login_container_pb2.LoginContainerWidget
        faq: _faq_pb2.FAQWidget
        def __init__(self, promo_landing: _Optional[_Union[_promo_landing_pb2.PromoLandingWidget, _Mapping]] = ..., login_with_phone: _Optional[_Union[_login_with_phone_pb2.LoginWithPhoneWidget, _Mapping]] = ..., promo_landing_container: _Optional[_Union[_promo_landing_container_pb2.PromoLandingContainerWidget, _Mapping]] = ..., login_container: _Optional[_Union[_login_container_pb2.LoginContainerWidget, _Mapping]] = ..., faq: _Optional[_Union[_faq_pb2.FAQWidget, _Mapping]] = ...) -> None: ...
    WIDGET_COMMONS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    widget_commons: _widget_commons_pb2.WidgetCommons
    data: UserRegistrationContainerWidget.Data
    def __init__(self, widget_commons: _Optional[_Union[_widget_commons_pb2.WidgetCommons, _Mapping]] = ..., data: _Optional[_Union[UserRegistrationContainerWidget.Data, _Mapping]] = ...) -> None: ...
