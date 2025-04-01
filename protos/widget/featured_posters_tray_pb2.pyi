from base import widget_commons_pb2 as _widget_commons_pb2
from feature.image import image_pb2 as _image_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FeaturedPostersTrayWidget(_message.Message):
    __slots__ = ("widget_commons", "data")
    class ListView(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        DEFAULT: _ClassVar[FeaturedPostersTrayWidget.ListView]
        HIGHLIGHT: _ClassVar[FeaturedPostersTrayWidget.ListView]
    DEFAULT: FeaturedPostersTrayWidget.ListView
    HIGHLIGHT: FeaturedPostersTrayWidget.ListView
    class Data(_message.Message):
        __slots__ = ("image_list", "list_view")
        IMAGE_LIST_FIELD_NUMBER: _ClassVar[int]
        LIST_VIEW_FIELD_NUMBER: _ClassVar[int]
        image_list: _containers.RepeatedCompositeFieldContainer[_image_pb2.Image]
        list_view: FeaturedPostersTrayWidget.ListView
        def __init__(self, image_list: _Optional[_Iterable[_Union[_image_pb2.Image, _Mapping]]] = ..., list_view: _Optional[_Union[FeaturedPostersTrayWidget.ListView, str]] = ...) -> None: ...
    WIDGET_COMMONS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    widget_commons: _widget_commons_pb2.WidgetCommons
    data: FeaturedPostersTrayWidget.Data
    def __init__(self, widget_commons: _Optional[_Union[_widget_commons_pb2.WidgetCommons, _Mapping]] = ..., data: _Optional[_Union[FeaturedPostersTrayWidget.Data, _Mapping]] = ...) -> None: ...
