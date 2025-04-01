from base import template_pb2 as _template_pb2
from base import widget_commons_pb2 as _widget_commons_pb2
from base import actions_pb2 as _actions_pb2
from feature.image import illustration_pb2 as _illustration_pb2
from feature.image import image_pb2 as _image_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TabWidget(_message.Message):
    __slots__ = ("template", "widget_commons", "data")
    class ScreenSize(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNKNOWN: _ClassVar[TabWidget.ScreenSize]
        SMALL: _ClassVar[TabWidget.ScreenSize]
        MEDIUM: _ClassVar[TabWidget.ScreenSize]
        LARGE: _ClassVar[TabWidget.ScreenSize]
    UNKNOWN: TabWidget.ScreenSize
    SMALL: TabWidget.ScreenSize
    MEDIUM: TabWidget.ScreenSize
    LARGE: TabWidget.ScreenSize
    class Data(_message.Message):
        __slots__ = ("title", "is_selected", "selected_title", "tray_widget_url", "sub_title", "url", "icon", "disabled_screen_size_list", "actions", "instant_load", "illustration")
        TITLE_FIELD_NUMBER: _ClassVar[int]
        IS_SELECTED_FIELD_NUMBER: _ClassVar[int]
        SELECTED_TITLE_FIELD_NUMBER: _ClassVar[int]
        TRAY_WIDGET_URL_FIELD_NUMBER: _ClassVar[int]
        SUB_TITLE_FIELD_NUMBER: _ClassVar[int]
        URL_FIELD_NUMBER: _ClassVar[int]
        ICON_FIELD_NUMBER: _ClassVar[int]
        DISABLED_SCREEN_SIZE_LIST_FIELD_NUMBER: _ClassVar[int]
        ACTIONS_FIELD_NUMBER: _ClassVar[int]
        INSTANT_LOAD_FIELD_NUMBER: _ClassVar[int]
        ILLUSTRATION_FIELD_NUMBER: _ClassVar[int]
        title: str
        is_selected: bool
        selected_title: str
        tray_widget_url: str
        sub_title: str
        url: TabWidget.Url
        icon: _image_pb2.Image
        disabled_screen_size_list: _containers.RepeatedScalarFieldContainer[TabWidget.ScreenSize]
        actions: _actions_pb2.Actions
        instant_load: bool
        illustration: _illustration_pb2.Illustration
        def __init__(self, title: _Optional[str] = ..., is_selected: bool = ..., selected_title: _Optional[str] = ..., tray_widget_url: _Optional[str] = ..., sub_title: _Optional[str] = ..., url: _Optional[_Union[TabWidget.Url, _Mapping]] = ..., icon: _Optional[_Union[_image_pb2.Image, _Mapping]] = ..., disabled_screen_size_list: _Optional[_Iterable[_Union[TabWidget.ScreenSize, str]]] = ..., actions: _Optional[_Union[_actions_pb2.Actions, _Mapping]] = ..., instant_load: bool = ..., illustration: _Optional[_Union[_illustration_pb2.Illustration, _Mapping]] = ...) -> None: ...
    class Url(_message.Message):
        __slots__ = ("widget_url", "space_url")
        WIDGET_URL_FIELD_NUMBER: _ClassVar[int]
        SPACE_URL_FIELD_NUMBER: _ClassVar[int]
        widget_url: str
        space_url: str
        def __init__(self, widget_url: _Optional[str] = ..., space_url: _Optional[str] = ...) -> None: ...
    TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    WIDGET_COMMONS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    template: _template_pb2.Template
    widget_commons: _widget_commons_pb2.WidgetCommons
    data: TabWidget.Data
    def __init__(self, template: _Optional[_Union[_template_pb2.Template, _Mapping]] = ..., widget_commons: _Optional[_Union[_widget_commons_pb2.WidgetCommons, _Mapping]] = ..., data: _Optional[_Union[TabWidget.Data, _Mapping]] = ...) -> None: ...
