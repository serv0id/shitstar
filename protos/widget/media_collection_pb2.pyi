from base import widget_commons_pb2 as _widget_commons_pb2
from widget import media_container_pb2 as _media_container_pb2
from widget import auto_scroll_gallery_pb2 as _auto_scroll_gallery_pb2
from widget import hero_gec_pb2 as _hero_gec_pb2
from widget import hero_pb2 as _hero_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MediaCollectionWidget(_message.Message):
    __slots__ = ("widget_commons", "data")
    class Data(_message.Message):
        __slots__ = ("titles", "collection_type", "tray_items", "texts")
        class CollectionType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            UNSPECIFIED: _ClassVar[MediaCollectionWidget.Data.CollectionType]
            CAROUSEL: _ClassVar[MediaCollectionWidget.Data.CollectionType]
            HORIZONTAL_CARD: _ClassVar[MediaCollectionWidget.Data.CollectionType]
            VERTICAL_CARD: _ClassVar[MediaCollectionWidget.Data.CollectionType]
        UNSPECIFIED: MediaCollectionWidget.Data.CollectionType
        CAROUSEL: MediaCollectionWidget.Data.CollectionType
        HORIZONTAL_CARD: MediaCollectionWidget.Data.CollectionType
        VERTICAL_CARD: MediaCollectionWidget.Data.CollectionType
        TITLES_FIELD_NUMBER: _ClassVar[int]
        COLLECTION_TYPE_FIELD_NUMBER: _ClassVar[int]
        TRAY_ITEMS_FIELD_NUMBER: _ClassVar[int]
        TEXTS_FIELD_NUMBER: _ClassVar[int]
        titles: _hero_gec_pb2.HeroGECWidget
        collection_type: MediaCollectionWidget.Data.CollectionType
        tray_items: _containers.RepeatedCompositeFieldContainer[_auto_scroll_gallery_pb2.AutoScrollGalleryWidget]
        texts: _hero_pb2.HeroWidget
        def __init__(self, titles: _Optional[_Union[_hero_gec_pb2.HeroGECWidget, _Mapping]] = ..., collection_type: _Optional[_Union[MediaCollectionWidget.Data.CollectionType, str]] = ..., tray_items: _Optional[_Iterable[_Union[_auto_scroll_gallery_pb2.AutoScrollGalleryWidget, _Mapping]]] = ..., texts: _Optional[_Union[_hero_pb2.HeroWidget, _Mapping]] = ...) -> None: ...
    WIDGET_COMMONS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    widget_commons: _widget_commons_pb2.WidgetCommons
    data: MediaCollectionWidget.Data
    def __init__(self, widget_commons: _Optional[_Union[_widget_commons_pb2.WidgetCommons, _Mapping]] = ..., data: _Optional[_Union[MediaCollectionWidget.Data, _Mapping]] = ...) -> None: ...
