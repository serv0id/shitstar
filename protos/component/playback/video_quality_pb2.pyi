from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class VideoQuality(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    VIDEO_QUALITY_UNSPECIFIED: _ClassVar[VideoQuality]
    VIDEO_QUALITY_SD: _ClassVar[VideoQuality]
    VIDEO_QUALITY_HD: _ClassVar[VideoQuality]
    VIDEO_QUALITY_FHD: _ClassVar[VideoQuality]
    VIDEO_QUALITY_4K: _ClassVar[VideoQuality]
VIDEO_QUALITY_UNSPECIFIED: VideoQuality
VIDEO_QUALITY_SD: VideoQuality
VIDEO_QUALITY_HD: VideoQuality
VIDEO_QUALITY_FHD: VideoQuality
VIDEO_QUALITY_4K: VideoQuality
