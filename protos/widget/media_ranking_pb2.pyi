from base import widget_commons_pb2 as _widget_commons_pb2
from widget import media_container_pb2 as _media_container_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MediaRankingWidget(_message.Message):
    __slots__ = ("widget_commons", "data")
    class Data(_message.Message):
        __slots__ = ("items",)
        ITEMS_FIELD_NUMBER: _ClassVar[int]
        items: _containers.RepeatedCompositeFieldContainer[MediaRankingWidget.Items]
        def __init__(self, items: _Optional[_Iterable[_Union[MediaRankingWidget.Items, _Mapping]]] = ...) -> None: ...
    class Items(_message.Message):
        __slots__ = ("media", "subtext", "fill_percentage", "image_orientation")
        class ImageOrientation(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            UNSPECIFIED: _ClassVar[MediaRankingWidget.Items.ImageOrientation]
            ELONGATED: _ClassVar[MediaRankingWidget.Items.ImageOrientation]
        UNSPECIFIED: MediaRankingWidget.Items.ImageOrientation
        ELONGATED: MediaRankingWidget.Items.ImageOrientation
        MEDIA_FIELD_NUMBER: _ClassVar[int]
        SUBTEXT_FIELD_NUMBER: _ClassVar[int]
        FILL_PERCENTAGE_FIELD_NUMBER: _ClassVar[int]
        IMAGE_ORIENTATION_FIELD_NUMBER: _ClassVar[int]
        media: _media_container_pb2.MediaContainerWidget
        subtext: str
        fill_percentage: int
        image_orientation: MediaRankingWidget.Items.ImageOrientation
        def __init__(self, media: _Optional[_Union[_media_container_pb2.MediaContainerWidget, _Mapping]] = ..., subtext: _Optional[str] = ..., fill_percentage: _Optional[int] = ..., image_orientation: _Optional[_Union[MediaRankingWidget.Items.ImageOrientation, str]] = ...) -> None: ...
    WIDGET_COMMONS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    widget_commons: _widget_commons_pb2.WidgetCommons
    data: MediaRankingWidget.Data
    def __init__(self, widget_commons: _Optional[_Union[_widget_commons_pb2.WidgetCommons, _Mapping]] = ..., data: _Optional[_Union[MediaRankingWidget.Data, _Mapping]] = ...) -> None: ...
