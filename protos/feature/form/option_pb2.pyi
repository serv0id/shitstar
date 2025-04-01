from feature.image import image_pb2 as _image_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Option(_message.Message):
    __slots__ = ("id", "title", "image", "is_selected", "percentage")
    ID_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    IMAGE_FIELD_NUMBER: _ClassVar[int]
    IS_SELECTED_FIELD_NUMBER: _ClassVar[int]
    PERCENTAGE_FIELD_NUMBER: _ClassVar[int]
    id: str
    title: str
    image: _image_pb2.Image
    is_selected: bool
    percentage: float
    def __init__(self, id: _Optional[str] = ..., title: _Optional[str] = ..., image: _Optional[_Union[_image_pb2.Image, _Mapping]] = ..., is_selected: bool = ..., percentage: _Optional[float] = ...) -> None: ...
