from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PreloadedArtwork(_message.Message):
    __slots__ = ("artwork_status", "artwork_source", "display_lag_ms", "video_failure_reason", "artwork_failure_reason")
    class PreloadedArtworkStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        PRELOADED_ARTWORK_STATUS_UNSPECIFIED: _ClassVar[PreloadedArtwork.PreloadedArtworkStatus]
        PRELOADED_ARTWORK_STATUS_SUCCESS: _ClassVar[PreloadedArtwork.PreloadedArtworkStatus]
        PRELOADED_ARTWORK_STATUS_FAILED: _ClassVar[PreloadedArtwork.PreloadedArtworkStatus]
        PRELOADED_ARTWORK_STATUS_SKIPPED: _ClassVar[PreloadedArtwork.PreloadedArtworkStatus]
        PRELOADED_ARTWORK_STATUS_VIDEO_FAILED: _ClassVar[PreloadedArtwork.PreloadedArtworkStatus]
    PRELOADED_ARTWORK_STATUS_UNSPECIFIED: PreloadedArtwork.PreloadedArtworkStatus
    PRELOADED_ARTWORK_STATUS_SUCCESS: PreloadedArtwork.PreloadedArtworkStatus
    PRELOADED_ARTWORK_STATUS_FAILED: PreloadedArtwork.PreloadedArtworkStatus
    PRELOADED_ARTWORK_STATUS_SKIPPED: PreloadedArtwork.PreloadedArtworkStatus
    PRELOADED_ARTWORK_STATUS_VIDEO_FAILED: PreloadedArtwork.PreloadedArtworkStatus
    class PreloadedArtworkSource(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        PRELOADED_ARTWORK_SOURCE_UNSPECIFIED: _ClassVar[PreloadedArtwork.PreloadedArtworkSource]
        PRELOADED_ARTWORK_SOURCE_PRELOADED: _ClassVar[PreloadedArtwork.PreloadedArtworkSource]
        PRELOADED_ARTWORK_SOURCE_DOWNLOADED: _ClassVar[PreloadedArtwork.PreloadedArtworkSource]
    PRELOADED_ARTWORK_SOURCE_UNSPECIFIED: PreloadedArtwork.PreloadedArtworkSource
    PRELOADED_ARTWORK_SOURCE_PRELOADED: PreloadedArtwork.PreloadedArtworkSource
    PRELOADED_ARTWORK_SOURCE_DOWNLOADED: PreloadedArtwork.PreloadedArtworkSource
    ARTWORK_STATUS_FIELD_NUMBER: _ClassVar[int]
    ARTWORK_SOURCE_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_LAG_MS_FIELD_NUMBER: _ClassVar[int]
    VIDEO_FAILURE_REASON_FIELD_NUMBER: _ClassVar[int]
    ARTWORK_FAILURE_REASON_FIELD_NUMBER: _ClassVar[int]
    artwork_status: PreloadedArtwork.PreloadedArtworkStatus
    artwork_source: PreloadedArtwork.PreloadedArtworkSource
    display_lag_ms: float
    video_failure_reason: str
    artwork_failure_reason: str
    def __init__(self, artwork_status: _Optional[_Union[PreloadedArtwork.PreloadedArtworkStatus, str]] = ..., artwork_source: _Optional[_Union[PreloadedArtwork.PreloadedArtworkSource, str]] = ..., display_lag_ms: _Optional[float] = ..., video_failure_reason: _Optional[str] = ..., artwork_failure_reason: _Optional[str] = ...) -> None: ...
