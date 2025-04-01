from base import template_pb2 as _template_pb2
from base import widget_commons_pb2 as _widget_commons_pb2
from base import actions_pb2 as _actions_pb2
from feature.app_event import app_event_pb2 as _app_event_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MenuWidget(_message.Message):
    __slots__ = ("template", "widget_commons", "data")
    class ItemTheme(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        DEFAULT: _ClassVar[MenuWidget.ItemTheme]
        SUBS_DEFAULT: _ClassVar[MenuWidget.ItemTheme]
    DEFAULT: MenuWidget.ItemTheme
    SUBS_DEFAULT: MenuWidget.ItemTheme
    class Data(_message.Message):
        __slots__ = ("items", "refresh_url", "invalidate_on", "on_expand", "on_collapse")
        ITEMS_FIELD_NUMBER: _ClassVar[int]
        REFRESH_URL_FIELD_NUMBER: _ClassVar[int]
        INVALIDATE_ON_FIELD_NUMBER: _ClassVar[int]
        ON_EXPAND_FIELD_NUMBER: _ClassVar[int]
        ON_COLLAPSE_FIELD_NUMBER: _ClassVar[int]
        items: _containers.RepeatedCompositeFieldContainer[MenuWidget.Item]
        refresh_url: str
        invalidate_on: _containers.RepeatedScalarFieldContainer[_app_event_pb2.AppEvent]
        on_expand: _containers.RepeatedCompositeFieldContainer[_actions_pb2.Actions.Action]
        on_collapse: _containers.RepeatedCompositeFieldContainer[_actions_pb2.Actions.Action]
        def __init__(self, items: _Optional[_Iterable[_Union[MenuWidget.Item, _Mapping]]] = ..., refresh_url: _Optional[str] = ..., invalidate_on: _Optional[_Iterable[_Union[_app_event_pb2.AppEvent, str]]] = ..., on_expand: _Optional[_Iterable[_Union[_actions_pb2.Actions.Action, _Mapping]]] = ..., on_collapse: _Optional[_Iterable[_Union[_actions_pb2.Actions.Action, _Mapping]]] = ...) -> None: ...
    class Item(_message.Message):
        __slots__ = ("default_icon", "active_icon", "image_url", "title", "is_active", "actions", "theme")
        DEFAULT_ICON_FIELD_NUMBER: _ClassVar[int]
        ACTIVE_ICON_FIELD_NUMBER: _ClassVar[int]
        IMAGE_URL_FIELD_NUMBER: _ClassVar[int]
        TITLE_FIELD_NUMBER: _ClassVar[int]
        IS_ACTIVE_FIELD_NUMBER: _ClassVar[int]
        ACTIONS_FIELD_NUMBER: _ClassVar[int]
        THEME_FIELD_NUMBER: _ClassVar[int]
        default_icon: str
        active_icon: str
        image_url: str
        title: str
        is_active: bool
        actions: _actions_pb2.Actions
        theme: MenuWidget.ItemTheme
        def __init__(self, default_icon: _Optional[str] = ..., active_icon: _Optional[str] = ..., image_url: _Optional[str] = ..., title: _Optional[str] = ..., is_active: bool = ..., actions: _Optional[_Union[_actions_pb2.Actions, _Mapping]] = ..., theme: _Optional[_Union[MenuWidget.ItemTheme, str]] = ...) -> None: ...
    TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    WIDGET_COMMONS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    template: _template_pb2.Template
    widget_commons: _widget_commons_pb2.WidgetCommons
    data: MenuWidget.Data
    def __init__(self, template: _Optional[_Union[_template_pb2.Template, _Mapping]] = ..., widget_commons: _Optional[_Union[_widget_commons_pb2.WidgetCommons, _Mapping]] = ..., data: _Optional[_Union[MenuWidget.Data, _Mapping]] = ...) -> None: ...
