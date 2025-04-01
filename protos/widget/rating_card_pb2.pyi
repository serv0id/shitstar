from base import actions_pb2 as _actions_pb2
from base import template_pb2 as _template_pb2
from base import widget_commons_pb2 as _widget_commons_pb2
from widget import media_container_pb2 as _media_container_pb2
from widget import tooltip_action_menu_pb2 as _tooltip_action_menu_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class RatingCardWidget(_message.Message):
    __slots__ = ("widget_commons", "data")
    class LayoutVariant(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        DEFAULT: _ClassVar[RatingCardWidget.LayoutVariant]
        REGULAR_HORIZONTAL: _ClassVar[RatingCardWidget.LayoutVariant]
        REGULAR_VERTICAL: _ClassVar[RatingCardWidget.LayoutVariant]
    DEFAULT: RatingCardWidget.LayoutVariant
    REGULAR_HORIZONTAL: RatingCardWidget.LayoutVariant
    REGULAR_VERTICAL: RatingCardWidget.LayoutVariant
    class Data(_message.Message):
        __slots__ = ("content_id", "label", "title", "media", "tooltip_action_menu_widget", "layout_variant")
        CONTENT_ID_FIELD_NUMBER: _ClassVar[int]
        LABEL_FIELD_NUMBER: _ClassVar[int]
        TITLE_FIELD_NUMBER: _ClassVar[int]
        MEDIA_FIELD_NUMBER: _ClassVar[int]
        TOOLTIP_ACTION_MENU_WIDGET_FIELD_NUMBER: _ClassVar[int]
        LAYOUT_VARIANT_FIELD_NUMBER: _ClassVar[int]
        content_id: str
        label: str
        title: str
        media: _media_container_pb2.MediaContainerWidget
        tooltip_action_menu_widget: _tooltip_action_menu_pb2.TooltipActionMenuWidget
        layout_variant: RatingCardWidget.LayoutVariant
        def __init__(self, content_id: _Optional[str] = ..., label: _Optional[str] = ..., title: _Optional[str] = ..., media: _Optional[_Union[_media_container_pb2.MediaContainerWidget, _Mapping]] = ..., tooltip_action_menu_widget: _Optional[_Union[_tooltip_action_menu_pb2.TooltipActionMenuWidget, _Mapping]] = ..., layout_variant: _Optional[_Union[RatingCardWidget.LayoutVariant, str]] = ...) -> None: ...
    WIDGET_COMMONS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    widget_commons: _widget_commons_pb2.WidgetCommons
    data: RatingCardWidget.Data
    def __init__(self, widget_commons: _Optional[_Union[_widget_commons_pb2.WidgetCommons, _Mapping]] = ..., data: _Optional[_Union[RatingCardWidget.Data, _Mapping]] = ...) -> None: ...
