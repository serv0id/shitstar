from base import widget_commons_pb2 as _widget_commons_pb2
from base import actions_pb2 as _actions_pb2
from feature.image import image_pb2 as _image_pb2
from feature.atom import button_pb2 as _button_pb2
from feature.callout_tag import callout_tag_pb2 as _callout_tag_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MediaContentInfoSmallWidget(_message.Message):
    __slots__ = ("widget_commons", "data")
    class ImageType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        DEFAULT_TYPE: _ClassVar[MediaContentInfoSmallWidget.ImageType]
        CIRCLE: _ClassVar[MediaContentInfoSmallWidget.ImageType]
        RECTANGLE: _ClassVar[MediaContentInfoSmallWidget.ImageType]
    DEFAULT_TYPE: MediaContentInfoSmallWidget.ImageType
    CIRCLE: MediaContentInfoSmallWidget.ImageType
    RECTANGLE: MediaContentInfoSmallWidget.ImageType
    class Data(_message.Message):
        __slots__ = ("poster", "title", "sub_title", "tags", "kebab", "poster_image_type")
        POSTER_FIELD_NUMBER: _ClassVar[int]
        TITLE_FIELD_NUMBER: _ClassVar[int]
        SUB_TITLE_FIELD_NUMBER: _ClassVar[int]
        TAGS_FIELD_NUMBER: _ClassVar[int]
        KEBAB_FIELD_NUMBER: _ClassVar[int]
        POSTER_IMAGE_TYPE_FIELD_NUMBER: _ClassVar[int]
        poster: _image_pb2.Image
        title: str
        sub_title: str
        tags: _containers.RepeatedCompositeFieldContainer[_callout_tag_pb2.CalloutTag]
        kebab: _button_pb2.Button
        poster_image_type: MediaContentInfoSmallWidget.ImageType
        def __init__(self, poster: _Optional[_Union[_image_pb2.Image, _Mapping]] = ..., title: _Optional[str] = ..., sub_title: _Optional[str] = ..., tags: _Optional[_Iterable[_Union[_callout_tag_pb2.CalloutTag, _Mapping]]] = ..., kebab: _Optional[_Union[_button_pb2.Button, _Mapping]] = ..., poster_image_type: _Optional[_Union[MediaContentInfoSmallWidget.ImageType, str]] = ...) -> None: ...
    WIDGET_COMMONS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    widget_commons: _widget_commons_pb2.WidgetCommons
    data: MediaContentInfoSmallWidget.Data
    def __init__(self, widget_commons: _Optional[_Union[_widget_commons_pb2.WidgetCommons, _Mapping]] = ..., data: _Optional[_Union[MediaContentInfoSmallWidget.Data, _Mapping]] = ...) -> None: ...
