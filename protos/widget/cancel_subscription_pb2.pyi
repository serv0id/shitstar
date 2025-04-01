from base import widget_commons_pb2 as _widget_commons_pb2
from base import actions_pb2 as _actions_pb2
from feature.branding import brand_pb2 as _brand_pb2
from feature.image import image_pb2 as _image_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CancelSubscriptionWidget(_message.Message):
    __slots__ = ("widget_commons", "data")
    class Data(_message.Message):
        __slots__ = ("logo", "dismiss", "title", "sub_title", "cta", "sub_title_info", "cancel_image", "help_section", "sub_titles")
        LOGO_FIELD_NUMBER: _ClassVar[int]
        DISMISS_FIELD_NUMBER: _ClassVar[int]
        TITLE_FIELD_NUMBER: _ClassVar[int]
        SUB_TITLE_FIELD_NUMBER: _ClassVar[int]
        CTA_FIELD_NUMBER: _ClassVar[int]
        SUB_TITLE_INFO_FIELD_NUMBER: _ClassVar[int]
        CANCEL_IMAGE_FIELD_NUMBER: _ClassVar[int]
        HELP_SECTION_FIELD_NUMBER: _ClassVar[int]
        SUB_TITLES_FIELD_NUMBER: _ClassVar[int]
        logo: _brand_pb2.Brand
        dismiss: CancelSubscriptionWidget.DismissOperation
        title: str
        sub_title: str
        cta: CancelSubscriptionWidget.Cta
        sub_title_info: CancelSubscriptionWidget.SubTitle
        cancel_image: _image_pb2.Image
        help_section: CancelSubscriptionWidget.HelpSection
        sub_titles: _containers.RepeatedCompositeFieldContainer[CancelSubscriptionWidget.SubTitle]
        def __init__(self, logo: _Optional[_Union[_brand_pb2.Brand, str]] = ..., dismiss: _Optional[_Union[CancelSubscriptionWidget.DismissOperation, _Mapping]] = ..., title: _Optional[str] = ..., sub_title: _Optional[str] = ..., cta: _Optional[_Union[CancelSubscriptionWidget.Cta, _Mapping]] = ..., sub_title_info: _Optional[_Union[CancelSubscriptionWidget.SubTitle, _Mapping]] = ..., cancel_image: _Optional[_Union[_image_pb2.Image, _Mapping]] = ..., help_section: _Optional[_Union[CancelSubscriptionWidget.HelpSection, _Mapping]] = ..., sub_titles: _Optional[_Iterable[_Union[CancelSubscriptionWidget.SubTitle, _Mapping]]] = ...) -> None: ...
    class HelpSection(_message.Message):
        __slots__ = ("label", "actions", "help_icon")
        LABEL_FIELD_NUMBER: _ClassVar[int]
        ACTIONS_FIELD_NUMBER: _ClassVar[int]
        HELP_ICON_FIELD_NUMBER: _ClassVar[int]
        label: str
        actions: _actions_pb2.Actions
        help_icon: str
        def __init__(self, label: _Optional[str] = ..., actions: _Optional[_Union[_actions_pb2.Actions, _Mapping]] = ..., help_icon: _Optional[str] = ...) -> None: ...
    class SubTitle(_message.Message):
        __slots__ = ("title", "link")
        TITLE_FIELD_NUMBER: _ClassVar[int]
        LINK_FIELD_NUMBER: _ClassVar[int]
        title: str
        link: CancelSubscriptionWidget.Link
        def __init__(self, title: _Optional[str] = ..., link: _Optional[_Union[CancelSubscriptionWidget.Link, _Mapping]] = ...) -> None: ...
    class Link(_message.Message):
        __slots__ = ("text", "action")
        TEXT_FIELD_NUMBER: _ClassVar[int]
        ACTION_FIELD_NUMBER: _ClassVar[int]
        text: str
        action: _actions_pb2.Actions
        def __init__(self, text: _Optional[str] = ..., action: _Optional[_Union[_actions_pb2.Actions, _Mapping]] = ...) -> None: ...
    class DismissOperation(_message.Message):
        __slots__ = ("icon_name", "action")
        ICON_NAME_FIELD_NUMBER: _ClassVar[int]
        ACTION_FIELD_NUMBER: _ClassVar[int]
        icon_name: str
        action: _actions_pb2.Actions
        def __init__(self, icon_name: _Optional[str] = ..., action: _Optional[_Union[_actions_pb2.Actions, _Mapping]] = ...) -> None: ...
    class Cta(_message.Message):
        __slots__ = ("text", "action")
        TEXT_FIELD_NUMBER: _ClassVar[int]
        ACTION_FIELD_NUMBER: _ClassVar[int]
        text: str
        action: _actions_pb2.Actions
        def __init__(self, text: _Optional[str] = ..., action: _Optional[_Union[_actions_pb2.Actions, _Mapping]] = ...) -> None: ...
    WIDGET_COMMONS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    widget_commons: _widget_commons_pb2.WidgetCommons
    data: CancelSubscriptionWidget.Data
    def __init__(self, widget_commons: _Optional[_Union[_widget_commons_pb2.WidgetCommons, _Mapping]] = ..., data: _Optional[_Union[CancelSubscriptionWidget.Data, _Mapping]] = ...) -> None: ...
