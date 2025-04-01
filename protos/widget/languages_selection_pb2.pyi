from base import widget_commons_pb2 as _widget_commons_pb2
from base import actions_pb2 as _actions_pb2
from feature.image import image_pb2 as _image_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class LanguagesSelectionWidget(_message.Message):
    __slots__ = ("widget_commons", "meta", "icons", "languages", "submit", "page_header")
    class Meta(_message.Message):
        __slots__ = ("text", "title", "sub_title")
        TEXT_FIELD_NUMBER: _ClassVar[int]
        TITLE_FIELD_NUMBER: _ClassVar[int]
        SUB_TITLE_FIELD_NUMBER: _ClassVar[int]
        text: str
        title: str
        sub_title: str
        def __init__(self, text: _Optional[str] = ..., title: _Optional[str] = ..., sub_title: _Optional[str] = ...) -> None: ...
    class Icons(_message.Message):
        __slots__ = ("unselected", "selected")
        UNSELECTED_FIELD_NUMBER: _ClassVar[int]
        SELECTED_FIELD_NUMBER: _ClassVar[int]
        unselected: str
        selected: str
        def __init__(self, unselected: _Optional[str] = ..., selected: _Optional[str] = ...) -> None: ...
    class Language(_message.Message):
        __slots__ = ("language", "text", "is_selected", "thumbnail")
        LANGUAGE_FIELD_NUMBER: _ClassVar[int]
        TEXT_FIELD_NUMBER: _ClassVar[int]
        IS_SELECTED_FIELD_NUMBER: _ClassVar[int]
        THUMBNAIL_FIELD_NUMBER: _ClassVar[int]
        language: str
        text: str
        is_selected: bool
        thumbnail: _image_pb2.Image
        def __init__(self, language: _Optional[str] = ..., text: _Optional[str] = ..., is_selected: bool = ..., thumbnail: _Optional[_Union[_image_pb2.Image, _Mapping]] = ...) -> None: ...
    class Submit(_message.Message):
        __slots__ = ("label", "icon", "actions")
        LABEL_FIELD_NUMBER: _ClassVar[int]
        ICON_FIELD_NUMBER: _ClassVar[int]
        ACTIONS_FIELD_NUMBER: _ClassVar[int]
        label: str
        icon: str
        actions: _actions_pb2.Actions
        def __init__(self, label: _Optional[str] = ..., icon: _Optional[str] = ..., actions: _Optional[_Union[_actions_pb2.Actions, _Mapping]] = ...) -> None: ...
    class PageHeader(_message.Message):
        __slots__ = ("text", "title", "sub_title")
        TEXT_FIELD_NUMBER: _ClassVar[int]
        TITLE_FIELD_NUMBER: _ClassVar[int]
        SUB_TITLE_FIELD_NUMBER: _ClassVar[int]
        text: str
        title: str
        sub_title: str
        def __init__(self, text: _Optional[str] = ..., title: _Optional[str] = ..., sub_title: _Optional[str] = ...) -> None: ...
    WIDGET_COMMONS_FIELD_NUMBER: _ClassVar[int]
    META_FIELD_NUMBER: _ClassVar[int]
    ICONS_FIELD_NUMBER: _ClassVar[int]
    LANGUAGES_FIELD_NUMBER: _ClassVar[int]
    SUBMIT_FIELD_NUMBER: _ClassVar[int]
    PAGE_HEADER_FIELD_NUMBER: _ClassVar[int]
    widget_commons: _widget_commons_pb2.WidgetCommons
    meta: LanguagesSelectionWidget.Meta
    icons: LanguagesSelectionWidget.Icons
    languages: _containers.RepeatedCompositeFieldContainer[LanguagesSelectionWidget.Language]
    submit: LanguagesSelectionWidget.Submit
    page_header: LanguagesSelectionWidget.PageHeader
    def __init__(self, widget_commons: _Optional[_Union[_widget_commons_pb2.WidgetCommons, _Mapping]] = ..., meta: _Optional[_Union[LanguagesSelectionWidget.Meta, _Mapping]] = ..., icons: _Optional[_Union[LanguagesSelectionWidget.Icons, _Mapping]] = ..., languages: _Optional[_Iterable[_Union[LanguagesSelectionWidget.Language, _Mapping]]] = ..., submit: _Optional[_Union[LanguagesSelectionWidget.Submit, _Mapping]] = ..., page_header: _Optional[_Union[LanguagesSelectionWidget.PageHeader, _Mapping]] = ...) -> None: ...
