from feature.image import aspect_ratio_pb2 as _aspect_ratio_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Lottie(_message.Message):
    __slots__ = ["aspect_ratio", "url", "name"]
    ASPECT_RATIO_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    aspect_ratio: _aspect_ratio_pb2.AspectRatio
    url: str
    name: str
    def __init__(self, aspect_ratio: _Optional[_Union[_aspect_ratio_pb2.AspectRatio, _Mapping]] = ..., url: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...
