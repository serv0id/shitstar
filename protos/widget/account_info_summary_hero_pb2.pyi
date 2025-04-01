from base import widget_commons_pb2 as _widget_commons_pb2
from feature.image import image_pb2 as _image_pb2
from widget import logo_pb2 as _logo_pb2
from base import actions_pb2 as _actions_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AccountInfoSummaryHeroWidget(_message.Message):
    __slots__ = ("widget_commons", "data")
    class Data(_message.Message):
        __slots__ = ("hero_img", "account_info_summary")
        HERO_IMG_FIELD_NUMBER: _ClassVar[int]
        ACCOUNT_INFO_SUMMARY_FIELD_NUMBER: _ClassVar[int]
        hero_img: _image_pb2.Image
        account_info_summary: AccountInfoSummaryHeroWidget.AccountInfoSummary
        def __init__(self, hero_img: _Optional[_Union[_image_pb2.Image, _Mapping]] = ..., account_info_summary: _Optional[_Union[AccountInfoSummaryHeroWidget.AccountInfoSummary, _Mapping]] = ...) -> None: ...
    class AccountInfoSummary(_message.Message):
        __slots__ = ("title", "subtitle", "primary_cta", "secondary_cta", "logo")
        TITLE_FIELD_NUMBER: _ClassVar[int]
        SUBTITLE_FIELD_NUMBER: _ClassVar[int]
        PRIMARY_CTA_FIELD_NUMBER: _ClassVar[int]
        SECONDARY_CTA_FIELD_NUMBER: _ClassVar[int]
        LOGO_FIELD_NUMBER: _ClassVar[int]
        title: str
        subtitle: str
        primary_cta: AccountInfoSummaryHeroWidget.IconLabelButton
        secondary_cta: AccountInfoSummaryHeroWidget.IconLabelButton
        logo: _logo_pb2.LogoWidget
        def __init__(self, title: _Optional[str] = ..., subtitle: _Optional[str] = ..., primary_cta: _Optional[_Union[AccountInfoSummaryHeroWidget.IconLabelButton, _Mapping]] = ..., secondary_cta: _Optional[_Union[AccountInfoSummaryHeroWidget.IconLabelButton, _Mapping]] = ..., logo: _Optional[_Union[_logo_pb2.LogoWidget, _Mapping]] = ...) -> None: ...
    class IconLabelButton(_message.Message):
        __slots__ = ("icon_name", "label", "actions")
        ICON_NAME_FIELD_NUMBER: _ClassVar[int]
        LABEL_FIELD_NUMBER: _ClassVar[int]
        ACTIONS_FIELD_NUMBER: _ClassVar[int]
        icon_name: str
        label: str
        actions: _actions_pb2.Actions
        def __init__(self, icon_name: _Optional[str] = ..., label: _Optional[str] = ..., actions: _Optional[_Union[_actions_pb2.Actions, _Mapping]] = ...) -> None: ...
    WIDGET_COMMONS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    widget_commons: _widget_commons_pb2.WidgetCommons
    data: AccountInfoSummaryHeroWidget.Data
    def __init__(self, widget_commons: _Optional[_Union[_widget_commons_pb2.WidgetCommons, _Mapping]] = ..., data: _Optional[_Union[AccountInfoSummaryHeroWidget.Data, _Mapping]] = ...) -> None: ...
