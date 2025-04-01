from base import actions_pb2 as _actions_pb2
from base import widget_commons_pb2 as _widget_commons_pb2
from feature.branding import brand_pb2 as _brand_pb2
from feature.atom import button_pb2 as _button_pb2
from feature.image import image_pb2 as _image_pb2
from feature.subscription import paywall_impression_pb2 as _paywall_impression_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ConsumptionPaywallWidget(_message.Message):
    __slots__ = ("widget_commons", "data")
    class Data(_message.Message):
        __slots__ = ("logo", "title", "description", "cta", "help_rich_text", "help_info", "bg_image", "paywall_impression", "back_button", "linkout_data")
        LOGO_FIELD_NUMBER: _ClassVar[int]
        TITLE_FIELD_NUMBER: _ClassVar[int]
        DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
        CTA_FIELD_NUMBER: _ClassVar[int]
        HELP_RICH_TEXT_FIELD_NUMBER: _ClassVar[int]
        HELP_INFO_FIELD_NUMBER: _ClassVar[int]
        BG_IMAGE_FIELD_NUMBER: _ClassVar[int]
        PAYWALL_IMPRESSION_FIELD_NUMBER: _ClassVar[int]
        BACK_BUTTON_FIELD_NUMBER: _ClassVar[int]
        LINKOUT_DATA_FIELD_NUMBER: _ClassVar[int]
        logo: _brand_pb2.Brand
        title: str
        description: ConsumptionPaywallWidget.Description
        cta: ConsumptionPaywallWidget.Cta
        help_rich_text: str
        help_info: ConsumptionPaywallWidget.HelpInfo
        bg_image: _image_pb2.Image
        paywall_impression: _paywall_impression_pb2.PaywallImpressionPayload
        back_button: _button_pb2.Button
        linkout_data: ConsumptionPaywallWidget.LinkoutData
        def __init__(self, logo: _Optional[_Union[_brand_pb2.Brand, str]] = ..., title: _Optional[str] = ..., description: _Optional[_Union[ConsumptionPaywallWidget.Description, _Mapping]] = ..., cta: _Optional[_Union[ConsumptionPaywallWidget.Cta, _Mapping]] = ..., help_rich_text: _Optional[str] = ..., help_info: _Optional[_Union[ConsumptionPaywallWidget.HelpInfo, _Mapping]] = ..., bg_image: _Optional[_Union[_image_pb2.Image, _Mapping]] = ..., paywall_impression: _Optional[_Union[_paywall_impression_pb2.PaywallImpressionPayload, _Mapping]] = ..., back_button: _Optional[_Union[_button_pb2.Button, _Mapping]] = ..., linkout_data: _Optional[_Union[ConsumptionPaywallWidget.LinkoutData, _Mapping]] = ...) -> None: ...
    class LinkoutData(_message.Message):
        __slots__ = ("text", "link", "icon", "actions")
        TEXT_FIELD_NUMBER: _ClassVar[int]
        LINK_FIELD_NUMBER: _ClassVar[int]
        ICON_FIELD_NUMBER: _ClassVar[int]
        ACTIONS_FIELD_NUMBER: _ClassVar[int]
        text: str
        link: str
        icon: str
        actions: _actions_pb2.Actions
        def __init__(self, text: _Optional[str] = ..., link: _Optional[str] = ..., icon: _Optional[str] = ..., actions: _Optional[_Union[_actions_pb2.Actions, _Mapping]] = ...) -> None: ...
    class Description(_message.Message):
        __slots__ = ("text", "pay_link")
        TEXT_FIELD_NUMBER: _ClassVar[int]
        PAY_LINK_FIELD_NUMBER: _ClassVar[int]
        text: str
        pay_link: str
        def __init__(self, text: _Optional[str] = ..., pay_link: _Optional[str] = ...) -> None: ...
    class Cta(_message.Message):
        __slots__ = ("text", "actions")
        TEXT_FIELD_NUMBER: _ClassVar[int]
        ACTIONS_FIELD_NUMBER: _ClassVar[int]
        text: str
        actions: _actions_pb2.Actions
        def __init__(self, text: _Optional[str] = ..., actions: _Optional[_Union[_actions_pb2.Actions, _Mapping]] = ...) -> None: ...
    class HelpInfo(_message.Message):
        __slots__ = ("text", "actions")
        TEXT_FIELD_NUMBER: _ClassVar[int]
        ACTIONS_FIELD_NUMBER: _ClassVar[int]
        text: str
        actions: _actions_pb2.Actions
        def __init__(self, text: _Optional[str] = ..., actions: _Optional[_Union[_actions_pb2.Actions, _Mapping]] = ...) -> None: ...
    WIDGET_COMMONS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    widget_commons: _widget_commons_pb2.WidgetCommons
    data: ConsumptionPaywallWidget.Data
    def __init__(self, widget_commons: _Optional[_Union[_widget_commons_pb2.WidgetCommons, _Mapping]] = ..., data: _Optional[_Union[ConsumptionPaywallWidget.Data, _Mapping]] = ...) -> None: ...
