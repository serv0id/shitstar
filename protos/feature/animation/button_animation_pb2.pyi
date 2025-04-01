from feature.image import image_pb2 as _image_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ButtonAnimation(_message.Message):
    __slots__ = ("type", "animation_data")
    class ButtonAnimationType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ANIMATION_NONE: _ClassVar[ButtonAnimation.ButtonAnimationType]
        ANIMATION_WATCH_FREE: _ClassVar[ButtonAnimation.ButtonAnimationType]
    ANIMATION_NONE: ButtonAnimation.ButtonAnimationType
    ANIMATION_WATCH_FREE: ButtonAnimation.ButtonAnimationType
    class AnimationData(_message.Message):
        __slots__ = ("animation_watch_free_data",)
        ANIMATION_WATCH_FREE_DATA_FIELD_NUMBER: _ClassVar[int]
        animation_watch_free_data: ButtonAnimation.AnimationWatchFreeData
        def __init__(self, animation_watch_free_data: _Optional[_Union[ButtonAnimation.AnimationWatchFreeData, _Mapping]] = ...) -> None: ...
    class AnimationWatchFreeData(_message.Message):
        __slots__ = ("free_text_image",)
        FREE_TEXT_IMAGE_FIELD_NUMBER: _ClassVar[int]
        free_text_image: _image_pb2.Image
        def __init__(self, free_text_image: _Optional[_Union[_image_pb2.Image, _Mapping]] = ...) -> None: ...
    TYPE_FIELD_NUMBER: _ClassVar[int]
    ANIMATION_DATA_FIELD_NUMBER: _ClassVar[int]
    type: ButtonAnimation.ButtonAnimationType
    animation_data: ButtonAnimation.AnimationData
    def __init__(self, type: _Optional[_Union[ButtonAnimation.ButtonAnimationType, str]] = ..., animation_data: _Optional[_Union[ButtonAnimation.AnimationData, _Mapping]] = ...) -> None: ...
