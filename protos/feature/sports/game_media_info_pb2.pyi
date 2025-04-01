from feature.image import image_pb2 as _image_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GameMediaInfo(_message.Message):
    __slots__ = ("thumbnail_image", "clip_duration", "is_playable_video")
    THUMBNAIL_IMAGE_FIELD_NUMBER: _ClassVar[int]
    CLIP_DURATION_FIELD_NUMBER: _ClassVar[int]
    IS_PLAYABLE_VIDEO_FIELD_NUMBER: _ClassVar[int]
    thumbnail_image: _image_pb2.Image
    clip_duration: str
    is_playable_video: bool
    def __init__(self, thumbnail_image: _Optional[_Union[_image_pb2.Image, _Mapping]] = ..., clip_duration: _Optional[str] = ..., is_playable_video: bool = ...) -> None: ...
