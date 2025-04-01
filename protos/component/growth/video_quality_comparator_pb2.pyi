from component.playback import video_quality_pb2 as _video_quality_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class VideoQualityComparatorProperties(_message.Message):
    __slots__ = ("lower_video_quality", "higher_video_quality")
    LOWER_VIDEO_QUALITY_FIELD_NUMBER: _ClassVar[int]
    HIGHER_VIDEO_QUALITY_FIELD_NUMBER: _ClassVar[int]
    lower_video_quality: _video_quality_pb2.VideoQuality
    higher_video_quality: _video_quality_pb2.VideoQuality
    def __init__(self, lower_video_quality: _Optional[_Union[_video_quality_pb2.VideoQuality, str]] = ..., higher_video_quality: _Optional[_Union[_video_quality_pb2.VideoQuality, str]] = ...) -> None: ...
