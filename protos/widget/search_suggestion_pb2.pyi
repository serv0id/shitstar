from base import template_pb2 as _template_pb2
from base import widget_commons_pb2 as _widget_commons_pb2
from base import actions_pb2 as _actions_pb2
from feature.image import image_pb2 as _image_pb2
from feature.search import badge_pb2 as _badge_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SearchSuggestionWidget(_message.Message):
    __slots__ = ("template", "widget_commons", "data")
    class SuggestionType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        TRENDING_QUERY: _ClassVar[SearchSuggestionWidget.SuggestionType]
        TRENDING_CONTENT: _ClassVar[SearchSuggestionWidget.SuggestionType]
        HISTORY_QUERY: _ClassVar[SearchSuggestionWidget.SuggestionType]
        HISTORY_CONTENT: _ClassVar[SearchSuggestionWidget.SuggestionType]
        RELATED_SEARCH: _ClassVar[SearchSuggestionWidget.SuggestionType]
    TRENDING_QUERY: SearchSuggestionWidget.SuggestionType
    TRENDING_CONTENT: SearchSuggestionWidget.SuggestionType
    HISTORY_QUERY: SearchSuggestionWidget.SuggestionType
    HISTORY_CONTENT: SearchSuggestionWidget.SuggestionType
    RELATED_SEARCH: SearchSuggestionWidget.SuggestionType
    class Data(_message.Message):
        __slots__ = ("header", "items", "widgets")
        HEADER_FIELD_NUMBER: _ClassVar[int]
        ITEMS_FIELD_NUMBER: _ClassVar[int]
        WIDGETS_FIELD_NUMBER: _ClassVar[int]
        header: str
        items: _containers.RepeatedCompositeFieldContainer[SearchSuggestionWidget.Item]
        widgets: _containers.RepeatedCompositeFieldContainer[SearchSuggestionItemWidget]
        def __init__(self, header: _Optional[str] = ..., items: _Optional[_Iterable[_Union[SearchSuggestionWidget.Item, _Mapping]]] = ..., widgets: _Optional[_Iterable[_Union[SearchSuggestionItemWidget, _Mapping]]] = ...) -> None: ...
    class Item(_message.Message):
        __slots__ = ("type", "title", "image", "actions", "duration", "playable", "badge")
        TYPE_FIELD_NUMBER: _ClassVar[int]
        TITLE_FIELD_NUMBER: _ClassVar[int]
        IMAGE_FIELD_NUMBER: _ClassVar[int]
        ACTIONS_FIELD_NUMBER: _ClassVar[int]
        DURATION_FIELD_NUMBER: _ClassVar[int]
        PLAYABLE_FIELD_NUMBER: _ClassVar[int]
        BADGE_FIELD_NUMBER: _ClassVar[int]
        type: SearchSuggestionWidget.SuggestionType
        title: str
        image: _image_pb2.Image
        actions: _actions_pb2.Actions
        duration: str
        playable: bool
        badge: _badge_pb2.Badge
        def __init__(self, type: _Optional[_Union[SearchSuggestionWidget.SuggestionType, str]] = ..., title: _Optional[str] = ..., image: _Optional[_Union[_image_pb2.Image, _Mapping]] = ..., actions: _Optional[_Union[_actions_pb2.Actions, _Mapping]] = ..., duration: _Optional[str] = ..., playable: bool = ..., badge: _Optional[_Union[_badge_pb2.Badge, _Mapping]] = ...) -> None: ...
    TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    WIDGET_COMMONS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    template: _template_pb2.Template
    widget_commons: _widget_commons_pb2.WidgetCommons
    data: SearchSuggestionWidget.Data
    def __init__(self, template: _Optional[_Union[_template_pb2.Template, _Mapping]] = ..., widget_commons: _Optional[_Union[_widget_commons_pb2.WidgetCommons, _Mapping]] = ..., data: _Optional[_Union[SearchSuggestionWidget.Data, _Mapping]] = ...) -> None: ...

class SearchSuggestionItemWidget(_message.Message):
    __slots__ = ("widget_commons", "data")
    class Data(_message.Message):
        __slots__ = ("type", "title", "image", "actions", "duration", "playable", "badge")
        TYPE_FIELD_NUMBER: _ClassVar[int]
        TITLE_FIELD_NUMBER: _ClassVar[int]
        IMAGE_FIELD_NUMBER: _ClassVar[int]
        ACTIONS_FIELD_NUMBER: _ClassVar[int]
        DURATION_FIELD_NUMBER: _ClassVar[int]
        PLAYABLE_FIELD_NUMBER: _ClassVar[int]
        BADGE_FIELD_NUMBER: _ClassVar[int]
        type: SearchSuggestionWidget.SuggestionType
        title: str
        image: _image_pb2.Image
        actions: _actions_pb2.Actions
        duration: str
        playable: bool
        badge: _badge_pb2.Badge
        def __init__(self, type: _Optional[_Union[SearchSuggestionWidget.SuggestionType, str]] = ..., title: _Optional[str] = ..., image: _Optional[_Union[_image_pb2.Image, _Mapping]] = ..., actions: _Optional[_Union[_actions_pb2.Actions, _Mapping]] = ..., duration: _Optional[str] = ..., playable: bool = ..., badge: _Optional[_Union[_badge_pb2.Badge, _Mapping]] = ...) -> None: ...
    WIDGET_COMMONS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    widget_commons: _widget_commons_pb2.WidgetCommons
    data: SearchSuggestionItemWidget.Data
    def __init__(self, widget_commons: _Optional[_Union[_widget_commons_pb2.WidgetCommons, _Mapping]] = ..., data: _Optional[_Union[SearchSuggestionItemWidget.Data, _Mapping]] = ...) -> None: ...
