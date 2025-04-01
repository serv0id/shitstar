from base import template_pb2 as _template_pb2
from base import widget_commons_pb2 as _widget_commons_pb2
from base import actions_pb2 as _actions_pb2
from feature.image import image_pb2 as _image_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class WebFooterWidget(_message.Message):
    __slots__ = ("widget_commons", "data")
    class Data(_message.Message):
        __slots__ = ("paragraphs", "columns", "social_handles", "legal", "app_links")
        class ColumnType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            DEFAULT: _ClassVar[WebFooterWidget.Data.ColumnType]
            LINK: _ClassVar[WebFooterWidget.Data.ColumnType]
            LANGUAGE_SELECTOR: _ClassVar[WebFooterWidget.Data.ColumnType]
        DEFAULT: WebFooterWidget.Data.ColumnType
        LINK: WebFooterWidget.Data.ColumnType
        LANGUAGE_SELECTOR: WebFooterWidget.Data.ColumnType
        class Paragraph(_message.Message):
            __slots__ = ("title", "content")
            TITLE_FIELD_NUMBER: _ClassVar[int]
            CONTENT_FIELD_NUMBER: _ClassVar[int]
            title: str
            content: str
            def __init__(self, title: _Optional[str] = ..., content: _Optional[str] = ...) -> None: ...
        class Column(_message.Message):
            __slots__ = ("header", "links", "column_type", "column_type_v2")
            HEADER_FIELD_NUMBER: _ClassVar[int]
            LINKS_FIELD_NUMBER: _ClassVar[int]
            COLUMN_TYPE_FIELD_NUMBER: _ClassVar[int]
            COLUMN_TYPE_V2_FIELD_NUMBER: _ClassVar[int]
            header: str
            links: _containers.RepeatedCompositeFieldContainer[WebFooterWidget.Data.Link]
            column_type: str
            column_type_v2: WebFooterWidget.Data.ColumnType
            def __init__(self, header: _Optional[str] = ..., links: _Optional[_Iterable[_Union[WebFooterWidget.Data.Link, _Mapping]]] = ..., column_type: _Optional[str] = ..., column_type_v2: _Optional[_Union[WebFooterWidget.Data.ColumnType, str]] = ...) -> None: ...
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
            handles: _containers.RepeatedCompositeFieldContainer[WebFooterWidget.Data.SocialHandles.Handle]
            def __init__(self, header: _Optional[str] = ..., handles: _Optional[_Iterable[_Union[WebFooterWidget.Data.SocialHandles.Handle, _Mapping]]] = ...) -> None: ...
        class Legal(_message.Message):
            __slots__ = ("paragraph", "links")
            PARAGRAPH_FIELD_NUMBER: _ClassVar[int]
            LINKS_FIELD_NUMBER: _ClassVar[int]
            paragraph: str
            links: _containers.RepeatedCompositeFieldContainer[WebFooterWidget.Data.Link]
            def __init__(self, paragraph: _Optional[str] = ..., links: _Optional[_Iterable[_Union[WebFooterWidget.Data.Link, _Mapping]]] = ...) -> None: ...
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
        paragraphs: _containers.RepeatedCompositeFieldContainer[WebFooterWidget.Data.Paragraph]
        columns: _containers.RepeatedCompositeFieldContainer[WebFooterWidget.Data.Column]
        social_handles: WebFooterWidget.Data.SocialHandles
        legal: WebFooterWidget.Data.Legal
        app_links: _containers.RepeatedCompositeFieldContainer[WebFooterWidget.Data.AppLink]
        def __init__(self, paragraphs: _Optional[_Iterable[_Union[WebFooterWidget.Data.Paragraph, _Mapping]]] = ..., columns: _Optional[_Iterable[_Union[WebFooterWidget.Data.Column, _Mapping]]] = ..., social_handles: _Optional[_Union[WebFooterWidget.Data.SocialHandles, _Mapping]] = ..., legal: _Optional[_Union[WebFooterWidget.Data.Legal, _Mapping]] = ..., app_links: _Optional[_Iterable[_Union[WebFooterWidget.Data.AppLink, _Mapping]]] = ...) -> None: ...
    WIDGET_COMMONS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    widget_commons: _widget_commons_pb2.WidgetCommons
    data: WebFooterWidget.Data
    def __init__(self, widget_commons: _Optional[_Union[_widget_commons_pb2.WidgetCommons, _Mapping]] = ..., data: _Optional[_Union[WebFooterWidget.Data, _Mapping]] = ...) -> None: ...
