from feature.image import image_pb2 as _image_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Heatmap(_message.Message):
    __slots__ = ("heatmap_image_url", "scene_items")
    HEATMAP_IMAGE_URL_FIELD_NUMBER: _ClassVar[int]
    SCENE_ITEMS_FIELD_NUMBER: _ClassVar[int]
    heatmap_image_url: str
    scene_items: _containers.RepeatedCompositeFieldContainer[SceneItem]
    def __init__(self, heatmap_image_url: _Optional[str] = ..., scene_items: _Optional[_Iterable[_Union[SceneItem, _Mapping]]] = ...) -> None: ...

class SceneItem(_message.Message):
    __slots__ = ("timestamp", "emoji", "image", "description")
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    EMOJI_FIELD_NUMBER: _ClassVar[int]
    IMAGE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    timestamp: str
    emoji: str
    image: _image_pb2.Image
    description: str
    def __init__(self, timestamp: _Optional[str] = ..., emoji: _Optional[str] = ..., image: _Optional[_Union[_image_pb2.Image, _Mapping]] = ..., description: _Optional[str] = ...) -> None: ...
