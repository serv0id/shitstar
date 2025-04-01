from base import widget_commons_pb2 as _widget_commons_pb2
from feature.image import image_pb2 as _image_pb2
from widget import vertical_large_content_poster_pb2 as _vertical_large_content_poster_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ImageOverlayVerticalLargeContentPosterWidget(_message.Message):
    __slots__ = ("widget_commons", "data")
    class Pivot(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNKNOWN: _ClassVar[ImageOverlayVerticalLargeContentPosterWidget.Pivot]
        LEFT: _ClassVar[ImageOverlayVerticalLargeContentPosterWidget.Pivot]
        RIGHT: _ClassVar[ImageOverlayVerticalLargeContentPosterWidget.Pivot]
    UNKNOWN: ImageOverlayVerticalLargeContentPosterWidget.Pivot
    LEFT: ImageOverlayVerticalLargeContentPosterWidget.Pivot
    RIGHT: ImageOverlayVerticalLargeContentPosterWidget.Pivot
    class Data(_message.Message):
        __slots__ = ("overlay_image", "pivot", "vertical_large_content_poster")
        OVERLAY_IMAGE_FIELD_NUMBER: _ClassVar[int]
        PIVOT_FIELD_NUMBER: _ClassVar[int]
        VERTICAL_LARGE_CONTENT_POSTER_FIELD_NUMBER: _ClassVar[int]
        overlay_image: _image_pb2.Image
        pivot: ImageOverlayVerticalLargeContentPosterWidget.Pivot
        vertical_large_content_poster: _vertical_large_content_poster_pb2.VerticalLargeContentPosterWidget
        def __init__(self, overlay_image: _Optional[_Union[_image_pb2.Image, _Mapping]] = ..., pivot: _Optional[_Union[ImageOverlayVerticalLargeContentPosterWidget.Pivot, str]] = ..., vertical_large_content_poster: _Optional[_Union[_vertical_large_content_poster_pb2.VerticalLargeContentPosterWidget, _Mapping]] = ...) -> None: ...
    WIDGET_COMMONS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    widget_commons: _widget_commons_pb2.WidgetCommons
    data: ImageOverlayVerticalLargeContentPosterWidget.Data
    def __init__(self, widget_commons: _Optional[_Union[_widget_commons_pb2.WidgetCommons, _Mapping]] = ..., data: _Optional[_Union[ImageOverlayVerticalLargeContentPosterWidget.Data, _Mapping]] = ...) -> None: ...
