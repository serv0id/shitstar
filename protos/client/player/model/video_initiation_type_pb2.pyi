from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class VideoInitiationSource(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    VIDEO_INITIATION_SOURCE_UNSPECIFIED: _ClassVar[VideoInitiationSource]
    VIDEO_INITIATION_SOURCE_END_CREDITS: _ClassVar[VideoInitiationSource]
    VIDEO_INITIATION_SOURCE_VIDEO_END: _ClassVar[VideoInitiationSource]
    VIDEO_INITIATION_SOURCE_ACTIVE_WATCH: _ClassVar[VideoInitiationSource]

class VideoInitiationType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    VIDEO_INITIATION_TYPE_UNSPECIFIED: _ClassVar[VideoInitiationType]
    VIDEO_INITIATION_TYPE_AUTO_COUNTDOWN: _ClassVar[VideoInitiationType]
    VIDEO_INITIATION_TYPE_MANUAL_CLICK: _ClassVar[VideoInitiationType]
VIDEO_INITIATION_SOURCE_UNSPECIFIED: VideoInitiationSource
VIDEO_INITIATION_SOURCE_END_CREDITS: VideoInitiationSource
VIDEO_INITIATION_SOURCE_VIDEO_END: VideoInitiationSource
VIDEO_INITIATION_SOURCE_ACTIVE_WATCH: VideoInitiationSource
VIDEO_INITIATION_TYPE_UNSPECIFIED: VideoInitiationType
VIDEO_INITIATION_TYPE_AUTO_COUNTDOWN: VideoInitiationType
VIDEO_INITIATION_TYPE_MANUAL_CLICK: VideoInitiationType
