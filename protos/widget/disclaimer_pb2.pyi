from base import template_pb2 as _template_pb2
from base import widget_commons_pb2 as _widget_commons_pb2
from base import actions_pb2 as _actions_pb2
from widget import dialog_pb2 as _dialog_pb2
from feature.image import image_pb2 as _image_pb2
from feature.atom import link_pb2 as _link_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DisclaimerWidget(_message.Message):
    __slots__ = ("widget_commons", "data")
    class AlertType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        DEFAULT: _ClassVar[DisclaimerWidget.AlertType]
        WARNING: _ClassVar[DisclaimerWidget.AlertType]
    DEFAULT: DisclaimerWidget.AlertType
    WARNING: DisclaimerWidget.AlertType
    class Data(_message.Message):
        __slots__ = ("header_primary_btn", "illustration", "title", "phone_number", "list_item", "footer", "consent_text", "recaptcha_enabled", "email_address", "alert_info", "description")
        HEADER_PRIMARY_BTN_FIELD_NUMBER: _ClassVar[int]
        ILLUSTRATION_FIELD_NUMBER: _ClassVar[int]
        TITLE_FIELD_NUMBER: _ClassVar[int]
        PHONE_NUMBER_FIELD_NUMBER: _ClassVar[int]
        LIST_ITEM_FIELD_NUMBER: _ClassVar[int]
        FOOTER_FIELD_NUMBER: _ClassVar[int]
        CONSENT_TEXT_FIELD_NUMBER: _ClassVar[int]
        RECAPTCHA_ENABLED_FIELD_NUMBER: _ClassVar[int]
        EMAIL_ADDRESS_FIELD_NUMBER: _ClassVar[int]
        ALERT_INFO_FIELD_NUMBER: _ClassVar[int]
        DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
        header_primary_btn: DisclaimerWidget.Button
        illustration: _image_pb2.Image
        title: str
        phone_number: str
        list_item: _containers.RepeatedCompositeFieldContainer[DisclaimerWidget.ListItem]
        footer: DisclaimerWidget.Footer
        consent_text: str
        recaptcha_enabled: bool
        email_address: str
        alert_info: DisclaimerWidget.AlertInfo
        description: str
        def __init__(self, header_primary_btn: _Optional[_Union[DisclaimerWidget.Button, _Mapping]] = ..., illustration: _Optional[_Union[_image_pb2.Image, _Mapping]] = ..., title: _Optional[str] = ..., phone_number: _Optional[str] = ..., list_item: _Optional[_Iterable[_Union[DisclaimerWidget.ListItem, _Mapping]]] = ..., footer: _Optional[_Union[DisclaimerWidget.Footer, _Mapping]] = ..., consent_text: _Optional[str] = ..., recaptcha_enabled: bool = ..., email_address: _Optional[str] = ..., alert_info: _Optional[_Union[DisclaimerWidget.AlertInfo, _Mapping]] = ..., description: _Optional[str] = ...) -> None: ...
    class AlertInfo(_message.Message):
        __slots__ = ("type", "title", "description", "link")
        TYPE_FIELD_NUMBER: _ClassVar[int]
        TITLE_FIELD_NUMBER: _ClassVar[int]
        DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
        LINK_FIELD_NUMBER: _ClassVar[int]
        type: DisclaimerWidget.AlertType
        title: DisclaimerWidget.Title
        description: str
        link: _link_pb2.Link
        def __init__(self, type: _Optional[_Union[DisclaimerWidget.AlertType, str]] = ..., title: _Optional[_Union[DisclaimerWidget.Title, _Mapping]] = ..., description: _Optional[str] = ..., link: _Optional[_Union[_link_pb2.Link, _Mapping]] = ...) -> None: ...
    class Title(_message.Message):
        __slots__ = ("icon_name", "text")
        ICON_NAME_FIELD_NUMBER: _ClassVar[int]
        TEXT_FIELD_NUMBER: _ClassVar[int]
        icon_name: str
        text: str
        def __init__(self, icon_name: _Optional[str] = ..., text: _Optional[str] = ...) -> None: ...
    class Button(_message.Message):
        __slots__ = ("icon", "text", "actions")
        ICON_FIELD_NUMBER: _ClassVar[int]
        TEXT_FIELD_NUMBER: _ClassVar[int]
        ACTIONS_FIELD_NUMBER: _ClassVar[int]
        icon: str
        text: str
        actions: _actions_pb2.Actions
        def __init__(self, icon: _Optional[str] = ..., text: _Optional[str] = ..., actions: _Optional[_Union[_actions_pb2.Actions, _Mapping]] = ...) -> None: ...
    class Footer(_message.Message):
        __slots__ = ("primary_btn", "secondary_btn")
        PRIMARY_BTN_FIELD_NUMBER: _ClassVar[int]
        SECONDARY_BTN_FIELD_NUMBER: _ClassVar[int]
        primary_btn: DisclaimerWidget.Button
        secondary_btn: DisclaimerWidget.Button
        def __init__(self, primary_btn: _Optional[_Union[DisclaimerWidget.Button, _Mapping]] = ..., secondary_btn: _Optional[_Union[DisclaimerWidget.Button, _Mapping]] = ...) -> None: ...
    class ListItem(_message.Message):
        __slots__ = ("title", "description", "icon_name")
        TITLE_FIELD_NUMBER: _ClassVar[int]
        DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
        ICON_NAME_FIELD_NUMBER: _ClassVar[int]
        title: str
        description: _containers.RepeatedScalarFieldContainer[str]
        icon_name: str
        def __init__(self, title: _Optional[str] = ..., description: _Optional[_Iterable[str]] = ..., icon_name: _Optional[str] = ...) -> None: ...
    WIDGET_COMMONS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    widget_commons: _widget_commons_pb2.WidgetCommons
    data: DisclaimerWidget.Data
    def __init__(self, widget_commons: _Optional[_Union[_widget_commons_pb2.WidgetCommons, _Mapping]] = ..., data: _Optional[_Union[DisclaimerWidget.Data, _Mapping]] = ...) -> None: ...
