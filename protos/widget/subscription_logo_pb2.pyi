from base import actions_pb2 as _actions_pb2
from base import widget_commons_pb2 as _widget_commons_pb2
from feature.branding import brand_pb2 as _brand_pb2
from widget import logo_pb2 as _logo_pb2
from feature.quiz import title_icon_combo_pb2 as _title_icon_combo_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SubscriptionLogoWidget(_message.Message):
    __slots__ = ("widget_commons", "data")
    class Data(_message.Message):
        __slots__ = ("actions", "icon_name", "subs_nudge", "variant", "image_alt")
        ACTIONS_FIELD_NUMBER: _ClassVar[int]
        ICON_NAME_FIELD_NUMBER: _ClassVar[int]
        SUBS_NUDGE_FIELD_NUMBER: _ClassVar[int]
        VARIANT_FIELD_NUMBER: _ClassVar[int]
        IMAGE_ALT_FIELD_NUMBER: _ClassVar[int]
        actions: _actions_pb2.Actions
        icon_name: _brand_pb2.Brand
        subs_nudge: SubscriptionLogoWidget.SubsNudge
        variant: _logo_pb2.LogoVariant
        image_alt: str
        def __init__(self, actions: _Optional[_Union[_actions_pb2.Actions, _Mapping]] = ..., icon_name: _Optional[_Union[_brand_pb2.Brand, str]] = ..., subs_nudge: _Optional[_Union[SubscriptionLogoWidget.SubsNudge, _Mapping]] = ..., variant: _Optional[_Union[_logo_pb2.LogoVariant, str]] = ..., image_alt: _Optional[str] = ...) -> None: ...
    class SubsNudge(_message.Message):
        __slots__ = ("label", "actions", "nudge_text", "text", "animation")
        LABEL_FIELD_NUMBER: _ClassVar[int]
        ACTIONS_FIELD_NUMBER: _ClassVar[int]
        NUDGE_TEXT_FIELD_NUMBER: _ClassVar[int]
        TEXT_FIELD_NUMBER: _ClassVar[int]
        ANIMATION_FIELD_NUMBER: _ClassVar[int]
        label: str
        actions: _actions_pb2.Actions
        nudge_text: str
        text: str
        animation: SubscriptionLogoWidget.NudgeAnimation
        def __init__(self, label: _Optional[str] = ..., actions: _Optional[_Union[_actions_pb2.Actions, _Mapping]] = ..., nudge_text: _Optional[str] = ..., text: _Optional[str] = ..., animation: _Optional[_Union[SubscriptionLogoWidget.NudgeAnimation, _Mapping]] = ...) -> None: ...
    class NudgeAnimation(_message.Message):
        __slots__ = ("slide_up",)
        SLIDE_UP_FIELD_NUMBER: _ClassVar[int]
        slide_up: _containers.RepeatedCompositeFieldContainer[_title_icon_combo_pb2.TitleIconCombo]
        def __init__(self, slide_up: _Optional[_Iterable[_Union[_title_icon_combo_pb2.TitleIconCombo, _Mapping]]] = ...) -> None: ...
    WIDGET_COMMONS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    widget_commons: _widget_commons_pb2.WidgetCommons
    data: SubscriptionLogoWidget.Data
    def __init__(self, widget_commons: _Optional[_Union[_widget_commons_pb2.WidgetCommons, _Mapping]] = ..., data: _Optional[_Union[SubscriptionLogoWidget.Data, _Mapping]] = ...) -> None: ...
