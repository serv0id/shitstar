from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ReportedIssueProperties(_message.Message):
    __slots__ = ("issue_sub_type", "issue_status", "issue_sub_type_v2")
    class ReportedIssueStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        REPORTED_ISSUE_STATUS_UNSPECIFIED: _ClassVar[ReportedIssueProperties.ReportedIssueStatus]
        REPORTED_ISSUE_STATUS_STARTED: _ClassVar[ReportedIssueProperties.ReportedIssueStatus]
        REPORTED_ISSUE_STATUS_SENT: _ClassVar[ReportedIssueProperties.ReportedIssueStatus]
        REPORTED_ISSUE_STATUS_FAILED: _ClassVar[ReportedIssueProperties.ReportedIssueStatus]
        REPORTED_ISSUE_STATUS_CANCELLED: _ClassVar[ReportedIssueProperties.ReportedIssueStatus]
    REPORTED_ISSUE_STATUS_UNSPECIFIED: ReportedIssueProperties.ReportedIssueStatus
    REPORTED_ISSUE_STATUS_STARTED: ReportedIssueProperties.ReportedIssueStatus
    REPORTED_ISSUE_STATUS_SENT: ReportedIssueProperties.ReportedIssueStatus
    REPORTED_ISSUE_STATUS_FAILED: ReportedIssueProperties.ReportedIssueStatus
    REPORTED_ISSUE_STATUS_CANCELLED: ReportedIssueProperties.ReportedIssueStatus
    class ReportedIssueType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        REPORTED_ISSUE_TYPE_UNSPECIFIED: _ClassVar[ReportedIssueProperties.ReportedIssueType]
        REPORTED_ISSUE_TYPE_BUFFERING_CONNECTION: _ClassVar[ReportedIssueProperties.ReportedIssueType]
        REPORTED_ISSUE_TYPE_VIDEO_QUALITY: _ClassVar[ReportedIssueProperties.ReportedIssueType]
        REPORTED_ISSUE_TYPE_AUDIO_QUALITY: _ClassVar[ReportedIssueProperties.ReportedIssueType]
        REPORTED_ISSUE_TYPE_SUBTITLES_CAPTIONS: _ClassVar[ReportedIssueProperties.ReportedIssueType]
    REPORTED_ISSUE_TYPE_UNSPECIFIED: ReportedIssueProperties.ReportedIssueType
    REPORTED_ISSUE_TYPE_BUFFERING_CONNECTION: ReportedIssueProperties.ReportedIssueType
    REPORTED_ISSUE_TYPE_VIDEO_QUALITY: ReportedIssueProperties.ReportedIssueType
    REPORTED_ISSUE_TYPE_AUDIO_QUALITY: ReportedIssueProperties.ReportedIssueType
    REPORTED_ISSUE_TYPE_SUBTITLES_CAPTIONS: ReportedIssueProperties.ReportedIssueType
    ISSUE_SUB_TYPE_FIELD_NUMBER: _ClassVar[int]
    ISSUE_STATUS_FIELD_NUMBER: _ClassVar[int]
    ISSUE_SUB_TYPE_V2_FIELD_NUMBER: _ClassVar[int]
    issue_sub_type: str
    issue_status: ReportedIssueProperties.ReportedIssueStatus
    issue_sub_type_v2: ReportedIssueProperties.ReportedIssueType
    def __init__(self, issue_sub_type: _Optional[str] = ..., issue_status: _Optional[_Union[ReportedIssueProperties.ReportedIssueStatus, str]] = ..., issue_sub_type_v2: _Optional[_Union[ReportedIssueProperties.ReportedIssueType, str]] = ...) -> None: ...
