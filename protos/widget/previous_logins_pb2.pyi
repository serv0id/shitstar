from base import template_pb2 as _template_pb2
from base import widget_commons_pb2 as _widget_commons_pb2
from feature.branding import brand_pb2 as _brand_pb2
from base import actions_pb2 as _actions_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PreviousLoginsWidget(_message.Message):
    __slots__ = ("template", "widget_commons", "data")
    class SubscriptionBadge(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NONE: _ClassVar[PreviousLoginsWidget.SubscriptionBadge]
        SUBSCRIBER: _ClassVar[PreviousLoginsWidget.SubscriptionBadge]
    NONE: PreviousLoginsWidget.SubscriptionBadge
    SUBSCRIBER: PreviousLoginsWidget.SubscriptionBadge
    class Data(_message.Message):
        __slots__ = ("logo", "title", "manage_text", "login_with_another_account", "previous_login_items", "help_rich_text")
        LOGO_FIELD_NUMBER: _ClassVar[int]
        TITLE_FIELD_NUMBER: _ClassVar[int]
        MANAGE_TEXT_FIELD_NUMBER: _ClassVar[int]
        LOGIN_WITH_ANOTHER_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
        PREVIOUS_LOGIN_ITEMS_FIELD_NUMBER: _ClassVar[int]
        HELP_RICH_TEXT_FIELD_NUMBER: _ClassVar[int]
        logo: _brand_pb2.Brand
        title: str
        manage_text: str
        login_with_another_account: PreviousLoginsWidget.LoginWithAnotherAccount
        previous_login_items: _containers.RepeatedCompositeFieldContainer[PreviousLoginsWidget.PreviousLoginItems]
        help_rich_text: str
        def __init__(self, logo: _Optional[_Union[_brand_pb2.Brand, str]] = ..., title: _Optional[str] = ..., manage_text: _Optional[str] = ..., login_with_another_account: _Optional[_Union[PreviousLoginsWidget.LoginWithAnotherAccount, _Mapping]] = ..., previous_login_items: _Optional[_Iterable[_Union[PreviousLoginsWidget.PreviousLoginItems, _Mapping]]] = ..., help_rich_text: _Optional[str] = ...) -> None: ...
    class LoginWithAnotherAccount(_message.Message):
        __slots__ = ("text", "actions")
        TEXT_FIELD_NUMBER: _ClassVar[int]
        ACTIONS_FIELD_NUMBER: _ClassVar[int]
        text: str
        actions: _actions_pb2.Actions
        def __init__(self, text: _Optional[str] = ..., actions: _Optional[_Union[_actions_pb2.Actions, _Mapping]] = ...) -> None: ...
    class PreviousLoginItems(_message.Message):
        __slots__ = ("title", "description", "encrypted_identifier", "subscription_badge", "forget_login", "actions")
        class ForgetLogin(_message.Message):
            __slots__ = ("title", "forget_login_url")
            TITLE_FIELD_NUMBER: _ClassVar[int]
            FORGET_LOGIN_URL_FIELD_NUMBER: _ClassVar[int]
            title: str
            forget_login_url: str
            def __init__(self, title: _Optional[str] = ..., forget_login_url: _Optional[str] = ...) -> None: ...
        TITLE_FIELD_NUMBER: _ClassVar[int]
        DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
        ENCRYPTED_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
        SUBSCRIPTION_BADGE_FIELD_NUMBER: _ClassVar[int]
        FORGET_LOGIN_FIELD_NUMBER: _ClassVar[int]
        ACTIONS_FIELD_NUMBER: _ClassVar[int]
        title: str
        description: str
        encrypted_identifier: str
        subscription_badge: PreviousLoginsWidget.SubscriptionBadge
        forget_login: PreviousLoginsWidget.PreviousLoginItems.ForgetLogin
        actions: _actions_pb2.Actions
        def __init__(self, title: _Optional[str] = ..., description: _Optional[str] = ..., encrypted_identifier: _Optional[str] = ..., subscription_badge: _Optional[_Union[PreviousLoginsWidget.SubscriptionBadge, str]] = ..., forget_login: _Optional[_Union[PreviousLoginsWidget.PreviousLoginItems.ForgetLogin, _Mapping]] = ..., actions: _Optional[_Union[_actions_pb2.Actions, _Mapping]] = ...) -> None: ...
    TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    WIDGET_COMMONS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    template: _template_pb2.Template
    widget_commons: _widget_commons_pb2.WidgetCommons
    data: PreviousLoginsWidget.Data
    def __init__(self, template: _Optional[_Union[_template_pb2.Template, _Mapping]] = ..., widget_commons: _Optional[_Union[_widget_commons_pb2.WidgetCommons, _Mapping]] = ..., data: _Optional[_Union[PreviousLoginsWidget.Data, _Mapping]] = ...) -> None: ...
