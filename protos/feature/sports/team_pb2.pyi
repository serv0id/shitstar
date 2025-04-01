from feature.image import image_pb2 as _image_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Team(_message.Message):
    __slots__ = ("name", "icon", "id")
    NAME_FIELD_NUMBER: _ClassVar[int]
    ICON_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    icon: _image_pb2.Image
    id: str
    def __init__(self, name: _Optional[str] = ..., icon: _Optional[_Union[_image_pb2.Image, _Mapping]] = ..., id: _Optional[str] = ...) -> None: ...
