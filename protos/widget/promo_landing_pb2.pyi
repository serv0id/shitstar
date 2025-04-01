from base import widget_commons_pb2 as _widget_commons_pb2
from base import actions_pb2 as _actions_pb2
from feature.image import image_pb2 as _image_pb2
from feature.branding import brand_pb2 as _brand_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PromoLandingWidget(_message.Message):
    __slots__ = ("widget_commons", "data")
    class Data(_message.Message):
        __slots__ = ("login_btn", "promo_detail", "footer")
        LOGIN_BTN_FIELD_NUMBER: _ClassVar[int]
        PROMO_DETAIL_FIELD_NUMBER: _ClassVar[int]
        FOOTER_FIELD_NUMBER: _ClassVar[int]
        login_btn: PromoLandingWidget.Button
        promo_detail: PromoLandingWidget.PromoDetail
        footer: PromoLandingWidget.Footer
        def __init__(self, login_btn: _Optional[_Union[PromoLandingWidget.Button, _Mapping]] = ..., promo_detail: _Optional[_Union[PromoLandingWidget.PromoDetail, _Mapping]] = ..., footer: _Optional[_Union[PromoLandingWidget.Footer, _Mapping]] = ...) -> None: ...
    class PromoDetail(_message.Message):
        __slots__ = ("image", "title", "promo_btn", "sub_title", "logo", "download_btn", "bg_img", "image_alt")
        IMAGE_FIELD_NUMBER: _ClassVar[int]
        TITLE_FIELD_NUMBER: _ClassVar[int]
        PROMO_BTN_FIELD_NUMBER: _ClassVar[int]
        SUB_TITLE_FIELD_NUMBER: _ClassVar[int]
        LOGO_FIELD_NUMBER: _ClassVar[int]
        DOWNLOAD_BTN_FIELD_NUMBER: _ClassVar[int]
        BG_IMG_FIELD_NUMBER: _ClassVar[int]
        IMAGE_ALT_FIELD_NUMBER: _ClassVar[int]
        image: _image_pb2.Image
        title: str
        promo_btn: PromoLandingWidget.Button
        sub_title: str
        logo: _brand_pb2.Brand
        download_btn: PromoLandingWidget.Button
        bg_img: _image_pb2.Image
        image_alt: str
        def __init__(self, image: _Optional[_Union[_image_pb2.Image, _Mapping]] = ..., title: _Optional[str] = ..., promo_btn: _Optional[_Union[PromoLandingWidget.Button, _Mapping]] = ..., sub_title: _Optional[str] = ..., logo: _Optional[_Union[_brand_pb2.Brand, str]] = ..., download_btn: _Optional[_Union[PromoLandingWidget.Button, _Mapping]] = ..., bg_img: _Optional[_Union[_image_pb2.Image, _Mapping]] = ..., image_alt: _Optional[str] = ...) -> None: ...
    class Button(_message.Message):
        __slots__ = ("text", "actions")
        TEXT_FIELD_NUMBER: _ClassVar[int]
        ACTIONS_FIELD_NUMBER: _ClassVar[int]
        text: str
        actions: _actions_pb2.Actions
        def __init__(self, text: _Optional[str] = ..., actions: _Optional[_Union[_actions_pb2.Actions, _Mapping]] = ...) -> None: ...
    class Footer(_message.Message):
        __slots__ = ("icon", "title", "sub_title")
        ICON_FIELD_NUMBER: _ClassVar[int]
        TITLE_FIELD_NUMBER: _ClassVar[int]
        SUB_TITLE_FIELD_NUMBER: _ClassVar[int]
        icon: str
        title: str
        sub_title: str
        def __init__(self, icon: _Optional[str] = ..., title: _Optional[str] = ..., sub_title: _Optional[str] = ...) -> None: ...
    WIDGET_COMMONS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    widget_commons: _widget_commons_pb2.WidgetCommons
    data: PromoLandingWidget.Data
    def __init__(self, widget_commons: _Optional[_Union[_widget_commons_pb2.WidgetCommons, _Mapping]] = ..., data: _Optional[_Union[PromoLandingWidget.Data, _Mapping]] = ...) -> None: ...
