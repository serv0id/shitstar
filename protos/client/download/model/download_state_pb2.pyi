from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class DownloadState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    DOWNLOAD_STATE_UNSPECIFIED: _ClassVar[DownloadState]
    DOWNLOAD_STATE_NONE: _ClassVar[DownloadState]
    DOWNLOAD_STATE_INITIATED: _ClassVar[DownloadState]
    DOWNLOAD_STATE_STARTED: _ClassVar[DownloadState]
    DOWNLOAD_STATE_PAUSED: _ClassVar[DownloadState]
    DOWNLOAD_STATE_COMPLETED: _ClassVar[DownloadState]
    DOWNLOAD_STATE_FAILED: _ClassVar[DownloadState]
    DOWNLOAD_STATE_CANCELLED: _ClassVar[DownloadState]
    DOWNLOAD_STATE_TERMINATED: _ClassVar[DownloadState]
    DOWNLOAD_STATE_IN_PROGRESS: _ClassVar[DownloadState]
    DOWNLOAD_STATE_RESUMED: _ClassVar[DownloadState]
    DOWNLOAD_STATE_DELETED: _ClassVar[DownloadState]
    DOWNLOAD_STATE_MARKED_AS_DELETED: _ClassVar[DownloadState]
    DOWNLOAD_STATE_QUEUED: _ClassVar[DownloadState]
    DOWNLOAD_STATE_EXPIRED: _ClassVar[DownloadState]
    DOWNLOAD_STATE_FAILED_DUE_TO_APP_TERMINATION: _ClassVar[DownloadState]
    DOWNLOAD_STATE_LICENSE_FETCHING_IN_PROGRESS: _ClassVar[DownloadState]
    DOWNLOAD_STATE_LICENSE_FETCHING_FAILED: _ClassVar[DownloadState]
    DOWNLOAD_STATE_DOWNLOAD_PAUSED_OVER_CELLULAR: _ClassVar[DownloadState]
    DOWNLOAD_STATE_PREPROCESSING: _ClassVar[DownloadState]
    DOWNLOAD_STATE_CHECK_DOWNLOAD: _ClassVar[DownloadState]
    DOWNLOAD_STATE_START_DOWNLOAD: _ClassVar[DownloadState]
    DOWNLOAD_STATE_SIZE_MODULE: _ClassVar[DownloadState]
    DOWNLOAD_STATE_DRM_MODULE: _ClassVar[DownloadState]
    DOWNLOAD_STATE_FAILED_AT_CHECK_DOWNLOAD: _ClassVar[DownloadState]
    DOWNLOAD_STATE_FAILED_AT_START_DOWNLOAD: _ClassVar[DownloadState]
    DOWNLOAD_STATE_FAILED_AT_SIZE_MODULE: _ClassVar[DownloadState]
    DOWNLOAD_STATE_FAILED_AT_DRM_MODULE: _ClassVar[DownloadState]
DOWNLOAD_STATE_UNSPECIFIED: DownloadState
DOWNLOAD_STATE_NONE: DownloadState
DOWNLOAD_STATE_INITIATED: DownloadState
DOWNLOAD_STATE_STARTED: DownloadState
DOWNLOAD_STATE_PAUSED: DownloadState
DOWNLOAD_STATE_COMPLETED: DownloadState
DOWNLOAD_STATE_FAILED: DownloadState
DOWNLOAD_STATE_CANCELLED: DownloadState
DOWNLOAD_STATE_TERMINATED: DownloadState
DOWNLOAD_STATE_IN_PROGRESS: DownloadState
DOWNLOAD_STATE_RESUMED: DownloadState
DOWNLOAD_STATE_DELETED: DownloadState
DOWNLOAD_STATE_MARKED_AS_DELETED: DownloadState
DOWNLOAD_STATE_QUEUED: DownloadState
DOWNLOAD_STATE_EXPIRED: DownloadState
DOWNLOAD_STATE_FAILED_DUE_TO_APP_TERMINATION: DownloadState
DOWNLOAD_STATE_LICENSE_FETCHING_IN_PROGRESS: DownloadState
DOWNLOAD_STATE_LICENSE_FETCHING_FAILED: DownloadState
DOWNLOAD_STATE_DOWNLOAD_PAUSED_OVER_CELLULAR: DownloadState
DOWNLOAD_STATE_PREPROCESSING: DownloadState
DOWNLOAD_STATE_CHECK_DOWNLOAD: DownloadState
DOWNLOAD_STATE_START_DOWNLOAD: DownloadState
DOWNLOAD_STATE_SIZE_MODULE: DownloadState
DOWNLOAD_STATE_DRM_MODULE: DownloadState
DOWNLOAD_STATE_FAILED_AT_CHECK_DOWNLOAD: DownloadState
DOWNLOAD_STATE_FAILED_AT_START_DOWNLOAD: DownloadState
DOWNLOAD_STATE_FAILED_AT_SIZE_MODULE: DownloadState
DOWNLOAD_STATE_FAILED_AT_DRM_MODULE: DownloadState
