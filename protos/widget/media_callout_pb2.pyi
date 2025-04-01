from base import widget_commons_pb2 as _widget_commons_pb2
from widget import media_container_pb2 as _media_container_pb2
from widget import text_prompt_pb2 as _text_prompt_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MediaCalloutWidget(_message.Message):
    __slots__ = ("widget_commons", "data")
    class Data(_message.Message):
        __slots__ = ("primary_texts", "media", "secondary_texts", "image_orientation")
        class ImageOrientation(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            UNSPECIFIED: _ClassVar[MediaCalloutWidget.Data.ImageOrientation]
            VERTICAL: _ClassVar[MediaCalloutWidget.Data.ImageOrientation]
            HORIZONTAL: _ClassVar[MediaCalloutWidget.Data.ImageOrientation]
        UNSPECIFIED: MediaCalloutWidget.Data.ImageOrientation
        VERTICAL: MediaCalloutWidget.Data.ImageOrientation
        HORIZONTAL: MediaCalloutWidget.Data.ImageOrientation
        PRIMARY_TEXTS_FIELD_NUMBER: _ClassVar[int]
        MEDIA_FIELD_NUMBER: _ClassVar[int]
        SECONDARY_TEXTS_FIELD_NUMBER: _ClassVar[int]
        IMAGE_ORIENTATION_FIELD_NUMBER: _ClassVar[int]
        primary_texts: _text_prompt_pb2.TextPromptWidget
        media: _media_container_pb2.MediaContainerWidget
        secondary_texts: _text_prompt_pb2.TextPromptWidget
        image_orientation: MediaCalloutWidget.Data.ImageOrientation
        def __init__(self, primary_texts: _Optional[_Union[_text_prompt_pb2.TextPromptWidget, _Mapping]] = ..., media: _Optional[_Union[_media_container_pb2.MediaContainerWidget, _Mapping]] = ..., secondary_texts: _Optional[_Union[_text_prompt_pb2.TextPromptWidget, _Mapping]] = ..., image_orientation: _Optional[_Union[MediaCalloutWidget.Data.ImageOrientation, str]] = ...) -> None: ...
    WIDGET_COMMONS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    widget_commons: _widget_commons_pb2.WidgetCommons
    data: MediaCalloutWidget.Data
    def __init__(self, widget_commons: _Optional[_Union[_widget_commons_pb2.WidgetCommons, _Mapping]] = ..., data: _Optional[_Union[MediaCalloutWidget.Data, _Mapping]] = ...) -> None: ...
