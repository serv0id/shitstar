from base import template_pb2 as _template_pb2
from base import widget_commons_pb2 as _widget_commons_pb2
from base import actions_pb2 as _actions_pb2
from feature.image import image_pb2 as _image_pb2
from feature.animation import video_animation_pb2 as _video_animation_pb2
from feature.image import lottie_pb2 as _lottie_pb2
from widget import info_pill_pb2 as _info_pill_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SubNavigationWidget(_message.Message):
    __slots__ = ("widget_commons", "data")
    class Data(_message.Message):
        __slots__ = ("items", "close_navigation_actions", "close_navigation_icon", "sub_menu_items", "animatation_meta", "animation_meta")
        ITEMS_FIELD_NUMBER: _ClassVar[int]
        CLOSE_NAVIGATION_ACTIONS_FIELD_NUMBER: _ClassVar[int]
        CLOSE_NAVIGATION_ICON_FIELD_NUMBER: _ClassVar[int]
        SUB_MENU_ITEMS_FIELD_NUMBER: _ClassVar[int]
        ANIMATATION_META_FIELD_NUMBER: _ClassVar[int]
        ANIMATION_META_FIELD_NUMBER: _ClassVar[int]
        items: _containers.RepeatedCompositeFieldContainer[SubNavigationWidget.Item]
        close_navigation_actions: _actions_pb2.Actions
        close_navigation_icon: str
        sub_menu_items: _containers.RepeatedCompositeFieldContainer[SubNavigationWidget.SubMenuItem]
        animatation_meta: _containers.RepeatedCompositeFieldContainer[_video_animation_pb2.VideoAnimation]
        animation_meta: _containers.RepeatedCompositeFieldContainer[_lottie_pb2.Lottie]
        def __init__(self, items: _Optional[_Iterable[_Union[SubNavigationWidget.Item, _Mapping]]] = ..., close_navigation_actions: _Optional[_Union[_actions_pb2.Actions, _Mapping]] = ..., close_navigation_icon: _Optional[str] = ..., sub_menu_items: _Optional[_Iterable[_Union[SubNavigationWidget.SubMenuItem, _Mapping]]] = ..., animatation_meta: _Optional[_Iterable[_Union[_video_animation_pb2.VideoAnimation, _Mapping]]] = ..., animation_meta: _Optional[_Iterable[_Union[_lottie_pb2.Lottie, _Mapping]]] = ...) -> None: ...
    class SubMenuItem(_message.Message):
        __slots__ = ("item", "info_pill")
        ITEM_FIELD_NUMBER: _ClassVar[int]
        INFO_PILL_FIELD_NUMBER: _ClassVar[int]
        item: SubNavigationWidget.Item
        info_pill: _info_pill_pb2.InfoPillWidget
        def __init__(self, item: _Optional[_Union[SubNavigationWidget.Item, _Mapping]] = ..., info_pill: _Optional[_Union[_info_pill_pb2.InfoPillWidget, _Mapping]] = ...) -> None: ...
    class Item(_message.Message):
        __slots__ = ("title", "is_active", "actions", "id", "icon", "is_collapsible", "animation")
        TITLE_FIELD_NUMBER: _ClassVar[int]
        IS_ACTIVE_FIELD_NUMBER: _ClassVar[int]
        ACTIONS_FIELD_NUMBER: _ClassVar[int]
        ID_FIELD_NUMBER: _ClassVar[int]
        ICON_FIELD_NUMBER: _ClassVar[int]
        IS_COLLAPSIBLE_FIELD_NUMBER: _ClassVar[int]
        ANIMATION_FIELD_NUMBER: _ClassVar[int]
        title: str
        is_active: bool
        actions: _actions_pb2.Actions
        id: str
        icon: str
        is_collapsible: bool
        animation: SubNavigationWidget.Animation
        def __init__(self, title: _Optional[str] = ..., is_active: bool = ..., actions: _Optional[_Union[_actions_pb2.Actions, _Mapping]] = ..., id: _Optional[str] = ..., icon: _Optional[str] = ..., is_collapsible: bool = ..., animation: _Optional[_Union[SubNavigationWidget.Animation, _Mapping]] = ...) -> None: ...
    class Animation(_message.Message):
        __slots__ = ("animating_images",)
        ANIMATING_IMAGES_FIELD_NUMBER: _ClassVar[int]
        animating_images: SubNavigationWidget.AnimatingImages
        def __init__(self, animating_images: _Optional[_Union[SubNavigationWidget.AnimatingImages, _Mapping]] = ...) -> None: ...
    class AnimatingImages(_message.Message):
        __slots__ = ("images",)
        IMAGES_FIELD_NUMBER: _ClassVar[int]
        images: _containers.RepeatedCompositeFieldContainer[_image_pb2.Image]
        def __init__(self, images: _Optional[_Iterable[_Union[_image_pb2.Image, _Mapping]]] = ...) -> None: ...
    WIDGET_COMMONS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    widget_commons: _widget_commons_pb2.WidgetCommons
    data: SubNavigationWidget.Data
    def __init__(self, widget_commons: _Optional[_Union[_widget_commons_pb2.WidgetCommons, _Mapping]] = ..., data: _Optional[_Union[SubNavigationWidget.Data, _Mapping]] = ...) -> None: ...
