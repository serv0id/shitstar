from base import widget_commons_pb2 as _widget_commons_pb2
from base import actions_pb2 as _actions_pb2
from feature.atom import button_pb2 as _button_pb2
from feature.branding import brand_pb2 as _brand_pb2
from feature.consent import consent_type_pb2 as _consent_type_pb2
from feature.image import image_pb2 as _image_pb2
from widget import dialog_pb2 as _dialog_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DisclaimerConsentWidget(_message.Message):
    __slots__ = ("widget_commons", "data")
    class Data(_message.Message):
        __slots__ = ("logo", "title", "disclaimer_rich_text", "channel_logos", "continue_button", "consent_id", "consent_type", "consent_version", "disclaimer_rich_sub_text", "studio_logos", "loading_text", "is_auto_submit", "auto_navigation_wait", "close_button", "is_force_consent", "change_language")
        LOGO_FIELD_NUMBER: _ClassVar[int]
        TITLE_FIELD_NUMBER: _ClassVar[int]
        DISCLAIMER_RICH_TEXT_FIELD_NUMBER: _ClassVar[int]
        CHANNEL_LOGOS_FIELD_NUMBER: _ClassVar[int]
        CONTINUE_BUTTON_FIELD_NUMBER: _ClassVar[int]
        CONSENT_ID_FIELD_NUMBER: _ClassVar[int]
        CONSENT_TYPE_FIELD_NUMBER: _ClassVar[int]
        CONSENT_VERSION_FIELD_NUMBER: _ClassVar[int]
        DISCLAIMER_RICH_SUB_TEXT_FIELD_NUMBER: _ClassVar[int]
        STUDIO_LOGOS_FIELD_NUMBER: _ClassVar[int]
        LOADING_TEXT_FIELD_NUMBER: _ClassVar[int]
        IS_AUTO_SUBMIT_FIELD_NUMBER: _ClassVar[int]
        AUTO_NAVIGATION_WAIT_FIELD_NUMBER: _ClassVar[int]
        CLOSE_BUTTON_FIELD_NUMBER: _ClassVar[int]
        IS_FORCE_CONSENT_FIELD_NUMBER: _ClassVar[int]
        CHANGE_LANGUAGE_FIELD_NUMBER: _ClassVar[int]
        logo: _brand_pb2.Brand
        title: str
        disclaimer_rich_text: str
        channel_logos: _containers.RepeatedCompositeFieldContainer[DisclaimerConsentWidget.ChannelLogo]
        continue_button: DisclaimerConsentWidget.ContinueButton
        consent_id: str
        consent_type: _consent_type_pb2.ConsentType
        consent_version: int
        disclaimer_rich_sub_text: str
        studio_logos: _containers.RepeatedCompositeFieldContainer[_image_pb2.Image]
        loading_text: str
        is_auto_submit: bool
        auto_navigation_wait: int
        close_button: DisclaimerConsentWidget.CloseButton
        is_force_consent: bool
        change_language: _button_pb2.Button
        def __init__(self, logo: _Optional[_Union[_brand_pb2.Brand, str]] = ..., title: _Optional[str] = ..., disclaimer_rich_text: _Optional[str] = ..., channel_logos: _Optional[_Iterable[_Union[DisclaimerConsentWidget.ChannelLogo, _Mapping]]] = ..., continue_button: _Optional[_Union[DisclaimerConsentWidget.ContinueButton, _Mapping]] = ..., consent_id: _Optional[str] = ..., consent_type: _Optional[_Union[_consent_type_pb2.ConsentType, str]] = ..., consent_version: _Optional[int] = ..., disclaimer_rich_sub_text: _Optional[str] = ..., studio_logos: _Optional[_Iterable[_Union[_image_pb2.Image, _Mapping]]] = ..., loading_text: _Optional[str] = ..., is_auto_submit: bool = ..., auto_navigation_wait: _Optional[int] = ..., close_button: _Optional[_Union[DisclaimerConsentWidget.CloseButton, _Mapping]] = ..., is_force_consent: bool = ..., change_language: _Optional[_Union[_button_pb2.Button, _Mapping]] = ...) -> None: ...
    class ChannelLogo(_message.Message):
        __slots__ = ("src", "alt")
        SRC_FIELD_NUMBER: _ClassVar[int]
        ALT_FIELD_NUMBER: _ClassVar[int]
        src: str
        alt: str
        def __init__(self, src: _Optional[str] = ..., alt: _Optional[str] = ...) -> None: ...
    class ContinueButton(_message.Message):
        __slots__ = ("text", "actions")
        TEXT_FIELD_NUMBER: _ClassVar[int]
        ACTIONS_FIELD_NUMBER: _ClassVar[int]
        text: str
        actions: _actions_pb2.Actions
        def __init__(self, text: _Optional[str] = ..., actions: _Optional[_Union[_actions_pb2.Actions, _Mapping]] = ...) -> None: ...
    class CloseButton(_message.Message):
        __slots__ = ("text", "actions", "dialog")
        TEXT_FIELD_NUMBER: _ClassVar[int]
        ACTIONS_FIELD_NUMBER: _ClassVar[int]
        DIALOG_FIELD_NUMBER: _ClassVar[int]
        text: str
        actions: _actions_pb2.Actions
        dialog: _dialog_pb2.DialogWidget
        def __init__(self, text: _Optional[str] = ..., actions: _Optional[_Union[_actions_pb2.Actions, _Mapping]] = ..., dialog: _Optional[_Union[_dialog_pb2.DialogWidget, _Mapping]] = ...) -> None: ...
    WIDGET_COMMONS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    widget_commons: _widget_commons_pb2.WidgetCommons
    data: DisclaimerConsentWidget.Data
    def __init__(self, widget_commons: _Optional[_Union[_widget_commons_pb2.WidgetCommons, _Mapping]] = ..., data: _Optional[_Union[DisclaimerConsentWidget.Data, _Mapping]] = ...) -> None: ...
