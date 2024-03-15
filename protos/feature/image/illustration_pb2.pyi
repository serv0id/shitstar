from feature.image import image_pb2 as _image_pb2
from feature.image import lottie_pb2 as _lottie_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Illustration(_message.Message):
    __slots__ = ["image", "icon", "lottie"]
    IMAGE_FIELD_NUMBER: _ClassVar[int]
    ICON_FIELD_NUMBER: _ClassVar[int]
    LOTTIE_FIELD_NUMBER: _ClassVar[int]
    image: _image_pb2.Image
    icon: str
    lottie: _lottie_pb2.Lottie
    def __init__(self, image: _Optional[_Union[_image_pb2.Image, _Mapping]] = ..., icon: _Optional[str] = ..., lottie: _Optional[_Union[_lottie_pb2.Lottie, _Mapping]] = ...) -> None: ...
