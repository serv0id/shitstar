from feature.image import image_pb2 as _image_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Player(_message.Message):
    __slots__ = ("name", "icon", "short_desc", "detail_desc")
    NAME_FIELD_NUMBER: _ClassVar[int]
    ICON_FIELD_NUMBER: _ClassVar[int]
    SHORT_DESC_FIELD_NUMBER: _ClassVar[int]
    DETAIL_DESC_FIELD_NUMBER: _ClassVar[int]
    name: str
    icon: _image_pb2.Image
    short_desc: str
    detail_desc: str
    def __init__(self, name: _Optional[str] = ..., icon: _Optional[_Union[_image_pb2.Image, _Mapping]] = ..., short_desc: _Optional[str] = ..., detail_desc: _Optional[str] = ...) -> None: ...
