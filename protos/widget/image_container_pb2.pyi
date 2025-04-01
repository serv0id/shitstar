from base import template_pb2 as _template_pb2
from base import widget_commons_pb2 as _widget_commons_pb2
from feature.image import image_pb2 as _image_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ImageContainerWidget(_message.Message):
    __slots__ = ("template", "widget_commons", "data")
    class Shape(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        RECTANGULAR: _ClassVar[ImageContainerWidget.Shape]
        CIRCULAR: _ClassVar[ImageContainerWidget.Shape]
    RECTANGULAR: ImageContainerWidget.Shape
    CIRCULAR: ImageContainerWidget.Shape
    class Data(_message.Message):
        __slots__ = ("thumbnail",)
        THUMBNAIL_FIELD_NUMBER: _ClassVar[int]
        thumbnail: ImageContainerWidget.Thumbnail
        def __init__(self, thumbnail: _Optional[_Union[ImageContainerWidget.Thumbnail, _Mapping]] = ...) -> None: ...
    class Thumbnail(_message.Message):
        __slots__ = ("image", "shape", "tablet_image")
        IMAGE_FIELD_NUMBER: _ClassVar[int]
        SHAPE_FIELD_NUMBER: _ClassVar[int]
        TABLET_IMAGE_FIELD_NUMBER: _ClassVar[int]
        image: _image_pb2.Image
        shape: ImageContainerWidget.Shape
        tablet_image: _image_pb2.Image
        def __init__(self, image: _Optional[_Union[_image_pb2.Image, _Mapping]] = ..., shape: _Optional[_Union[ImageContainerWidget.Shape, str]] = ..., tablet_image: _Optional[_Union[_image_pb2.Image, _Mapping]] = ...) -> None: ...
    TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    WIDGET_COMMONS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    template: _template_pb2.Template
    widget_commons: _widget_commons_pb2.WidgetCommons
    data: ImageContainerWidget.Data
    def __init__(self, template: _Optional[_Union[_template_pb2.Template, _Mapping]] = ..., widget_commons: _Optional[_Union[_widget_commons_pb2.WidgetCommons, _Mapping]] = ..., data: _Optional[_Union[ImageContainerWidget.Data, _Mapping]] = ...) -> None: ...
