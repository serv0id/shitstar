from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class VideoPlaybackType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    VIDEO_PLAYBACK_UNSPECIFIED: _ClassVar[VideoPlaybackType]
    VIDEO_PLAYBACK_AUTOPLAY: _ClassVar[VideoPlaybackType]
    VIDEO_PLAYBACK_NORMAL: _ClassVar[VideoPlaybackType]
VIDEO_PLAYBACK_UNSPECIFIED: VideoPlaybackType
VIDEO_PLAYBACK_AUTOPLAY: VideoPlaybackType
VIDEO_PLAYBACK_NORMAL: VideoPlaybackType

class DisplayVideo(_message.Message):
    __slots__ = ("playback_type", "payload")
    PLAYBACK_TYPE_FIELD_NUMBER: _ClassVar[int]
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    playback_type: VideoPlaybackType
    payload: str
    def __init__(self, playback_type: _Optional[_Union[VideoPlaybackType, str]] = ..., payload: _Optional[str] = ...) -> None: ...
