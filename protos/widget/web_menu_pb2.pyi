from base import template_pb2 as _template_pb2
from base import widget_commons_pb2 as _widget_commons_pb2
from base import actions_pb2 as _actions_pb2
from feature.image import image_pb2 as _image_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class WebMenuWidget(_message.Message):
    __slots__ = ("widget_commons", "side_nav", "footer_nav")
    class SideNavItem(_message.Message):
        __slots__ = ("default_icon", "active_icon", "image_url", "title", "is_active", "actions")
        DEFAULT_ICON_FIELD_NUMBER: _ClassVar[int]
        ACTIVE_ICON_FIELD_NUMBER: _ClassVar[int]
        IMAGE_URL_FIELD_NUMBER: _ClassVar[int]
        TITLE_FIELD_NUMBER: _ClassVar[int]
        IS_ACTIVE_FIELD_NUMBER: _ClassVar[int]
        ACTIONS_FIELD_NUMBER: _ClassVar[int]
        default_icon: str
        active_icon: str
        image_url: str
        title: str
        is_active: bool
        actions: _actions_pb2.Actions
        def __init__(self, default_icon: _Optional[str] = ..., active_icon: _Optional[str] = ..., image_url: _Optional[str] = ..., title: _Optional[str] = ..., is_active: bool = ..., actions: _Optional[_Union[_actions_pb2.Actions, _Mapping]] = ...) -> None: ...
    class FooterNav(_message.Message):
        __slots__ = ("paragraphs", "columns", "social_handles", "legal", "app_links")
        class Paragraph(_message.Message):
            __slots__ = ("title", "content")
            TITLE_FIELD_NUMBER: _ClassVar[int]
            CONTENT_FIELD_NUMBER: _ClassVar[int]
            title: str
            content: str
            def __init__(self, title: _Optional[str] = ..., content: _Optional[str] = ...) -> None: ...
        class Column(_message.Message):
            __slots__ = ("header", "links")
            HEADER_FIELD_NUMBER: _ClassVar[int]
            LINKS_FIELD_NUMBER: _ClassVar[int]
            header: str
            links: _containers.RepeatedCompositeFieldContainer[WebMenuWidget.FooterNav.Link]
            def __init__(self, header: _Optional[str] = ..., links: _Optional[_Iterable[_Union[WebMenuWidget.FooterNav.Link, _Mapping]]] = ...) -> None: ...
        class SocialHandles(_message.Message):
            __slots__ = ("header", "handles")
            class Handle(_message.Message):
                __slots__ = ("handle", "icon", "actions")
                HANDLE_FIELD_NUMBER: _ClassVar[int]
                ICON_FIELD_NUMBER: _ClassVar[int]
                ACTIONS_FIELD_NUMBER: _ClassVar[int]
                handle: str
                icon: str
                actions: _actions_pb2.Actions
                def __init__(self, handle: _Optional[str] = ..., icon: _Optional[str] = ..., actions: _Optional[_Union[_actions_pb2.Actions, _Mapping]] = ...) -> None: ...
            HEADER_FIELD_NUMBER: _ClassVar[int]
            HANDLES_FIELD_NUMBER: _ClassVar[int]
            header: str
            handles: _containers.RepeatedCompositeFieldContainer[WebMenuWidget.FooterNav.SocialHandles.Handle]
            def __init__(self, header: _Optional[str] = ..., handles: _Optional[_Iterable[_Union[WebMenuWidget.FooterNav.SocialHandles.Handle, _Mapping]]] = ...) -> None: ...
        class Legal(_message.Message):
            __slots__ = ("paragraph", "links")
            PARAGRAPH_FIELD_NUMBER: _ClassVar[int]
            LINKS_FIELD_NUMBER: _ClassVar[int]
            paragraph: str
            links: _containers.RepeatedCompositeFieldContainer[WebMenuWidget.FooterNav.Link]
            def __init__(self, paragraph: _Optional[str] = ..., links: _Optional[_Iterable[_Union[WebMenuWidget.FooterNav.Link, _Mapping]]] = ...) -> None: ...
        class AppLink(_message.Message):
            __slots__ = ("image", "actions")
            IMAGE_FIELD_NUMBER: _ClassVar[int]
            ACTIONS_FIELD_NUMBER: _ClassVar[int]
            image: _image_pb2.Image
            actions: _actions_pb2.Actions
            def __init__(self, image: _Optional[_Union[_image_pb2.Image, _Mapping]] = ..., actions: _Optional[_Union[_actions_pb2.Actions, _Mapping]] = ...) -> None: ...
        class Link(_message.Message):
            __slots__ = ("text", "actions")
            TEXT_FIELD_NUMBER: _ClassVar[int]
            ACTIONS_FIELD_NUMBER: _ClassVar[int]
            text: str
            actions: _actions_pb2.Actions
            def __init__(self, text: _Optional[str] = ..., actions: _Optional[_Union[_actions_pb2.Actions, _Mapping]] = ...) -> None: ...
        PARAGRAPHS_FIELD_NUMBER: _ClassVar[int]
        COLUMNS_FIELD_NUMBER: _ClassVar[int]
        SOCIAL_HANDLES_FIELD_NUMBER: _ClassVar[int]
        LEGAL_FIELD_NUMBER: _ClassVar[int]
        APP_LINKS_FIELD_NUMBER: _ClassVar[int]
        paragraphs: _containers.RepeatedCompositeFieldContainer[WebMenuWidget.FooterNav.Paragraph]
        columns: _containers.RepeatedCompositeFieldContainer[WebMenuWidget.FooterNav.Column]
        social_handles: WebMenuWidget.FooterNav.SocialHandles
        legal: WebMenuWidget.FooterNav.Legal
        app_links: _containers.RepeatedCompositeFieldContainer[WebMenuWidget.FooterNav.AppLink]
        def __init__(self, paragraphs: _Optional[_Iterable[_Union[WebMenuWidget.FooterNav.Paragraph, _Mapping]]] = ..., columns: _Optional[_Iterable[_Union[WebMenuWidget.FooterNav.Column, _Mapping]]] = ..., social_handles: _Optional[_Union[WebMenuWidget.FooterNav.SocialHandles, _Mapping]] = ..., legal: _Optional[_Union[WebMenuWidget.FooterNav.Legal, _Mapping]] = ..., app_links: _Optional[_Iterable[_Union[WebMenuWidget.FooterNav.AppLink, _Mapping]]] = ...) -> None: ...
    WIDGET_COMMONS_FIELD_NUMBER: _ClassVar[int]
    SIDE_NAV_FIELD_NUMBER: _ClassVar[int]
    FOOTER_NAV_FIELD_NUMBER: _ClassVar[int]
    widget_commons: _widget_commons_pb2.WidgetCommons
    side_nav: _containers.RepeatedCompositeFieldContainer[WebMenuWidget.SideNavItem]
    footer_nav: WebMenuWidget.FooterNav
    def __init__(self, widget_commons: _Optional[_Union[_widget_commons_pb2.WidgetCommons, _Mapping]] = ..., side_nav: _Optional[_Iterable[_Union[WebMenuWidget.SideNavItem, _Mapping]]] = ..., footer_nav: _Optional[_Union[WebMenuWidget.FooterNav, _Mapping]] = ...) -> None: ...
