from base import template_pb2 as _template_pb2
from base import widget_commons_pb2 as _widget_commons_pb2
from widget import cast_icon_pb2 as _cast_icon_pb2
from widget import logo_pb2 as _logo_pb2
from widget import subscription_logo_pb2 as _subscription_logo_pb2
from widget import help_settings_button_pb2 as _help_settings_button_pb2
from widget import subscription_nudge_pb2 as _subscription_nudge_pb2
from feature.atom import button_pb2 as _button_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class BrandedLogoHeaderWidget(_message.Message):
    __slots__ = ("template", "widget_commons", "data")
    class Data(_message.Message):
        __slots__ = ("logo", "widgets", "subscription_logo", "cast_button")
        LOGO_FIELD_NUMBER: _ClassVar[int]
        WIDGETS_FIELD_NUMBER: _ClassVar[int]
        SUBSCRIPTION_LOGO_FIELD_NUMBER: _ClassVar[int]
        CAST_BUTTON_FIELD_NUMBER: _ClassVar[int]
        logo: _logo_pb2.LogoWidget
        widgets: _containers.RepeatedCompositeFieldContainer[BrandedLogoHeaderWidget.Widget]
        subscription_logo: _subscription_logo_pb2.SubscriptionLogoWidget
        cast_button: _button_pb2.Button
        def __init__(self, logo: _Optional[_Union[_logo_pb2.LogoWidget, _Mapping]] = ..., widgets: _Optional[_Iterable[_Union[BrandedLogoHeaderWidget.Widget, _Mapping]]] = ..., subscription_logo: _Optional[_Union[_subscription_logo_pb2.SubscriptionLogoWidget, _Mapping]] = ..., cast_button: _Optional[_Union[_button_pb2.Button, _Mapping]] = ...) -> None: ...
    class Widget(_message.Message):
        __slots__ = ("cast_icon", "help_settings_button", "subscription_nudge")
        CAST_ICON_FIELD_NUMBER: _ClassVar[int]
        HELP_SETTINGS_BUTTON_FIELD_NUMBER: _ClassVar[int]
        SUBSCRIPTION_NUDGE_FIELD_NUMBER: _ClassVar[int]
        cast_icon: _cast_icon_pb2.CastIconButtonWidget
        help_settings_button: _help_settings_button_pb2.HelpSettingsButtonWidget
        subscription_nudge: _subscription_nudge_pb2.SubscriptionNudgeWidget
        def __init__(self, cast_icon: _Optional[_Union[_cast_icon_pb2.CastIconButtonWidget, _Mapping]] = ..., help_settings_button: _Optional[_Union[_help_settings_button_pb2.HelpSettingsButtonWidget, _Mapping]] = ..., subscription_nudge: _Optional[_Union[_subscription_nudge_pb2.SubscriptionNudgeWidget, _Mapping]] = ...) -> None: ...
    TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    WIDGET_COMMONS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    template: _template_pb2.Template
    widget_commons: _widget_commons_pb2.WidgetCommons
    data: BrandedLogoHeaderWidget.Data
    def __init__(self, template: _Optional[_Union[_template_pb2.Template, _Mapping]] = ..., widget_commons: _Optional[_Union[_widget_commons_pb2.WidgetCommons, _Mapping]] = ..., data: _Optional[_Union[BrandedLogoHeaderWidget.Data, _Mapping]] = ...) -> None: ...
