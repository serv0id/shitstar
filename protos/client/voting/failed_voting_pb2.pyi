from client.voting import viewed_voting_page_pb2 as _viewed_voting_page_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FailedVotingProperties(_message.Message):
    __slots__ = ("voting_status", "vote_status", "failure_reason_code", "failure_source", "failure_stage")
    class FailureSource(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        FAILURE_SOURCE_UNSPECIFIED: _ClassVar[FailedVotingProperties.FailureSource]
        FAILURE_SOURCE_BFF: _ClassVar[FailedVotingProperties.FailureSource]
        FAILURE_SOURCE_DOMAIN: _ClassVar[FailedVotingProperties.FailureSource]
        FAILURE_SOURCE_CLIENT: _ClassVar[FailedVotingProperties.FailureSource]
    FAILURE_SOURCE_UNSPECIFIED: FailedVotingProperties.FailureSource
    FAILURE_SOURCE_BFF: FailedVotingProperties.FailureSource
    FAILURE_SOURCE_DOMAIN: FailedVotingProperties.FailureSource
    FAILURE_SOURCE_CLIENT: FailedVotingProperties.FailureSource
    class FailureStage(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        FAILURE_STAGE_UNSPECIFIED: _ClassVar[FailedVotingProperties.FailureStage]
        FAILURE_STAGE_PAGE_LOAD: _ClassVar[FailedVotingProperties.FailureStage]
        FAILURE_STAGE_OPTION_SELECT: _ClassVar[FailedVotingProperties.FailureStage]
        FAILURE_STAGE_VOTE_SUBMISSION: _ClassVar[FailedVotingProperties.FailureStage]
    FAILURE_STAGE_UNSPECIFIED: FailedVotingProperties.FailureStage
    FAILURE_STAGE_PAGE_LOAD: FailedVotingProperties.FailureStage
    FAILURE_STAGE_OPTION_SELECT: FailedVotingProperties.FailureStage
    FAILURE_STAGE_VOTE_SUBMISSION: FailedVotingProperties.FailureStage
    VOTING_STATUS_FIELD_NUMBER: _ClassVar[int]
    VOTE_STATUS_FIELD_NUMBER: _ClassVar[int]
    FAILURE_REASON_CODE_FIELD_NUMBER: _ClassVar[int]
    FAILURE_SOURCE_FIELD_NUMBER: _ClassVar[int]
    FAILURE_STAGE_FIELD_NUMBER: _ClassVar[int]
    voting_status: _viewed_voting_page_pb2.ViewedVotingPageProperties.VotingStatus
    vote_status: _viewed_voting_page_pb2.ViewedVotingPageProperties.VoteStatus
    failure_reason_code: str
    failure_source: FailedVotingProperties.FailureSource
    failure_stage: FailedVotingProperties.FailureStage
    def __init__(self, voting_status: _Optional[_Union[_viewed_voting_page_pb2.ViewedVotingPageProperties.VotingStatus, str]] = ..., vote_status: _Optional[_Union[_viewed_voting_page_pb2.ViewedVotingPageProperties.VoteStatus, str]] = ..., failure_reason_code: _Optional[str] = ..., failure_source: _Optional[_Union[FailedVotingProperties.FailureSource, str]] = ..., failure_stage: _Optional[_Union[FailedVotingProperties.FailureStage, str]] = ...) -> None: ...
