from feature.image import image_pb2 as _image_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ScreenSizeImage(_message.Message):
    __slots__ = ("small_image", "medium_image", "large_image", "extra_large_image")
    SMALL_IMAGE_FIELD_NUMBER: _ClassVar[int]
    MEDIUM_IMAGE_FIELD_NUMBER: _ClassVar[int]
    LARGE_IMAGE_FIELD_NUMBER: _ClassVar[int]
    EXTRA_LARGE_IMAGE_FIELD_NUMBER: _ClassVar[int]
    small_image: _image_pb2.Image
    medium_image: _image_pb2.Image
    large_image: _image_pb2.Image
    extra_large_image: _image_pb2.Image
    def __init__(self, small_image: _Optional[_Union[_image_pb2.Image, _Mapping]] = ..., medium_image: _Optional[_Union[_image_pb2.Image, _Mapping]] = ..., large_image: _Optional[_Union[_image_pb2.Image, _Mapping]] = ..., extra_large_image: _Optional[_Union[_image_pb2.Image, _Mapping]] = ...) -> None: ...
