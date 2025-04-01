from base import template_pb2 as _template_pb2
from base import widget_commons_pb2 as _widget_commons_pb2
from action import web_view_navigation_pb2 as _web_view_navigation_pb2
from action import page_navigation_pb2 as _page_navigation_pb2
from action import external_navigation_pb2 as _external_navigation_pb2
from action import mail_to_pb2 as _mail_to_pb2
from feature.accessibility import accessibility_pb2 as _accessibility_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PaywallFooterWidget(_message.Message):
    __slots__ = ("template", "widget_commons", "data")
    class Data(_message.Message):
        __slots__ = ("links", "help_info")
        LINKS_FIELD_NUMBER: _ClassVar[int]
        HELP_INFO_FIELD_NUMBER: _ClassVar[int]
        links: _containers.RepeatedCompositeFieldContainer[PaywallFooterWidget.Link]
        help_info: PaywallFooterWidget.HelpInfo
        def __init__(self, links: _Optional[_Iterable[_Union[PaywallFooterWidget.Link, _Mapping]]] = ..., help_info: _Optional[_Union[PaywallFooterWidget.HelpInfo, _Mapping]] = ...) -> None: ...
    class Link(_message.Message):
        __slots__ = ("label", "alt", "external_url", "mail_to", "web_view_navigation", "page_navigation")
        LABEL_FIELD_NUMBER: _ClassVar[int]
        ALT_FIELD_NUMBER: _ClassVar[int]
        EXTERNAL_URL_FIELD_NUMBER: _ClassVar[int]
        MAIL_TO_FIELD_NUMBER: _ClassVar[int]
        WEB_VIEW_NAVIGATION_FIELD_NUMBER: _ClassVar[int]
        PAGE_NAVIGATION_FIELD_NUMBER: _ClassVar[int]
        label: str
        alt: _accessibility_pb2.Accessibility
        external_url: _external_navigation_pb2.ExternalNavigationAction
        mail_to: _mail_to_pb2.MailtoAction
        web_view_navigation: _web_view_navigation_pb2.WebViewNavigationAction
        page_navigation: _page_navigation_pb2.PageNavigationAction
        def __init__(self, label: _Optional[str] = ..., alt: _Optional[_Union[_accessibility_pb2.Accessibility, _Mapping]] = ..., external_url: _Optional[_Union[_external_navigation_pb2.ExternalNavigationAction, _Mapping]] = ..., mail_to: _Optional[_Union[_mail_to_pb2.MailtoAction, _Mapping]] = ..., web_view_navigation: _Optional[_Union[_web_view_navigation_pb2.WebViewNavigationAction, _Mapping]] = ..., page_navigation: _Optional[_Union[_page_navigation_pb2.PageNavigationAction, _Mapping]] = ...) -> None: ...
    class HelpInfo(_message.Message):
        __slots__ = ("help_text", "help_link")
        HELP_TEXT_FIELD_NUMBER: _ClassVar[int]
        HELP_LINK_FIELD_NUMBER: _ClassVar[int]
        help_text: str
        help_link: PaywallFooterWidget.Link
        def __init__(self, help_text: _Optional[str] = ..., help_link: _Optional[_Union[PaywallFooterWidget.Link, _Mapping]] = ...) -> None: ...
    TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    WIDGET_COMMONS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    template: _template_pb2.Template
    widget_commons: _widget_commons_pb2.WidgetCommons
    data: PaywallFooterWidget.Data
    def __init__(self, template: _Optional[_Union[_template_pb2.Template, _Mapping]] = ..., widget_commons: _Optional[_Union[_widget_commons_pb2.WidgetCommons, _Mapping]] = ..., data: _Optional[_Union[PaywallFooterWidget.Data, _Mapping]] = ...) -> None: ...
