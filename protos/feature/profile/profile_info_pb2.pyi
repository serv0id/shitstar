from feature.image import image_pb2 as _image_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ProfileInfo(_message.Message):
    __slots__ = ("profile_id", "avatar", "is_celebrity")
    PROFILE_ID_FIELD_NUMBER: _ClassVar[int]
    AVATAR_FIELD_NUMBER: _ClassVar[int]
    IS_CELEBRITY_FIELD_NUMBER: _ClassVar[int]
    profile_id: str
    avatar: _image_pb2.Image
    is_celebrity: bool
    def __init__(self, profile_id: _Optional[str] = ..., avatar: _Optional[_Union[_image_pb2.Image, _Mapping]] = ..., is_celebrity: bool = ...) -> None: ...
