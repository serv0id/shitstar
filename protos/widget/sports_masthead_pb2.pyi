from base import template_pb2 as _template_pb2
from base import widget_commons_pb2 as _widget_commons_pb2
from base import actions_pb2 as _actions_pb2
from feature.image import image_pb2 as _image_pb2
from feature.live import live_info_pb2 as _live_info_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SportsMastheadWidget(_message.Message):
    __slots__ = ("widget_commons", "data")
    class Data(_message.Message):
        __slots__ = ("hero_img", "thumbnail", "content_info")
        HERO_IMG_FIELD_NUMBER: _ClassVar[int]
        THUMBNAIL_FIELD_NUMBER: _ClassVar[int]
        CONTENT_INFO_FIELD_NUMBER: _ClassVar[int]
        hero_img: _image_pb2.Image
        thumbnail: _image_pb2.Image
        content_info: SportsMastheadWidget.ContentInfo
        def __init__(self, hero_img: _Optional[_Union[_image_pb2.Image, _Mapping]] = ..., thumbnail: _Optional[_Union[_image_pb2.Image, _Mapping]] = ..., content_info: _Optional[_Union[SportsMastheadWidget.ContentInfo, _Mapping]] = ...) -> None: ...
    class ContentInfo(_message.Message):
        __slots__ = ("title", "description", "primary_cta", "actions", "core_meta_tags", "hero_image_type", "live_info")
        class HeroImageType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            UNKNOWN: _ClassVar[SportsMastheadWidget.ContentInfo.HeroImageType]
            STANDARD: _ClassVar[SportsMastheadWidget.ContentInfo.HeroImageType]
            FALLBACK: _ClassVar[SportsMastheadWidget.ContentInfo.HeroImageType]
        UNKNOWN: SportsMastheadWidget.ContentInfo.HeroImageType
        STANDARD: SportsMastheadWidget.ContentInfo.HeroImageType
        FALLBACK: SportsMastheadWidget.ContentInfo.HeroImageType
        TITLE_FIELD_NUMBER: _ClassVar[int]
        DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
        PRIMARY_CTA_FIELD_NUMBER: _ClassVar[int]
        ACTIONS_FIELD_NUMBER: _ClassVar[int]
        CORE_META_TAGS_FIELD_NUMBER: _ClassVar[int]
        HERO_IMAGE_TYPE_FIELD_NUMBER: _ClassVar[int]
        LIVE_INFO_FIELD_NUMBER: _ClassVar[int]
        title: str
        description: str
        primary_cta: SportsMastheadWidget.IconLabelButton
        actions: _actions_pb2.Actions
        core_meta_tags: _containers.RepeatedCompositeFieldContainer[SportsMastheadWidget.Tag]
        hero_image_type: SportsMastheadWidget.ContentInfo.HeroImageType
        live_info: _live_info_pb2.LiveInfo
        def __init__(self, title: _Optional[str] = ..., description: _Optional[str] = ..., primary_cta: _Optional[_Union[SportsMastheadWidget.IconLabelButton, _Mapping]] = ..., actions: _Optional[_Union[_actions_pb2.Actions, _Mapping]] = ..., core_meta_tags: _Optional[_Iterable[_Union[SportsMastheadWidget.Tag, _Mapping]]] = ..., hero_image_type: _Optional[_Union[SportsMastheadWidget.ContentInfo.HeroImageType, str]] = ..., live_info: _Optional[_Union[_live_info_pb2.LiveInfo, _Mapping]] = ...) -> None: ...
    class IconLabelButton(_message.Message):
        __slots__ = ("icon_name", "label", "actions")
        ICON_NAME_FIELD_NUMBER: _ClassVar[int]
        LABEL_FIELD_NUMBER: _ClassVar[int]
        ACTIONS_FIELD_NUMBER: _ClassVar[int]
        icon_name: str
        label: str
        actions: _actions_pb2.Actions
        def __init__(self, icon_name: _Optional[str] = ..., label: _Optional[str] = ..., actions: _Optional[_Union[_actions_pb2.Actions, _Mapping]] = ...) -> None: ...
    class Tag(_message.Message):
        __slots__ = ("value", "actions", "type")
        VALUE_FIELD_NUMBER: _ClassVar[int]
        ACTIONS_FIELD_NUMBER: _ClassVar[int]
        TYPE_FIELD_NUMBER: _ClassVar[int]
        value: str
        actions: _actions_pb2.Actions
        type: str
        def __init__(self, value: _Optional[str] = ..., actions: _Optional[_Union[_actions_pb2.Actions, _Mapping]] = ..., type: _Optional[str] = ...) -> None: ...
    WIDGET_COMMONS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    widget_commons: _widget_commons_pb2.WidgetCommons
    data: SportsMastheadWidget.Data
    def __init__(self, widget_commons: _Optional[_Union[_widget_commons_pb2.WidgetCommons, _Mapping]] = ..., data: _Optional[_Union[SportsMastheadWidget.Data, _Mapping]] = ...) -> None: ...
