from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ViewedVotingPageProperties(_message.Message):
    __slots__ = ("voting_status", "vote_status", "page_load_time_ms", "total_load_time_ms")
    class VotingStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        VOTING_STATUS_UNSPECIFIED: _ClassVar[ViewedVotingPageProperties.VotingStatus]
        VOTING_STATUS_ACTIVE: _ClassVar[ViewedVotingPageProperties.VotingStatus]
        VOTING_STATUS_CLOSED: _ClassVar[ViewedVotingPageProperties.VotingStatus]
        VOTING_STATUS_YET_TO_START: _ClassVar[ViewedVotingPageProperties.VotingStatus]
    VOTING_STATUS_UNSPECIFIED: ViewedVotingPageProperties.VotingStatus
    VOTING_STATUS_ACTIVE: ViewedVotingPageProperties.VotingStatus
    VOTING_STATUS_CLOSED: ViewedVotingPageProperties.VotingStatus
    VOTING_STATUS_YET_TO_START: ViewedVotingPageProperties.VotingStatus
    class VoteStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        VOTE_STATUS_UNSPECIFIED: _ClassVar[ViewedVotingPageProperties.VoteStatus]
        VOTE_STATUS_NOT_VOTED: _ClassVar[ViewedVotingPageProperties.VoteStatus]
        VOTE_STATUS_OPTIONS_SELECTED: _ClassVar[ViewedVotingPageProperties.VoteStatus]
        VOTE_STATUS_SUBMITTED: _ClassVar[ViewedVotingPageProperties.VoteStatus]
    VOTE_STATUS_UNSPECIFIED: ViewedVotingPageProperties.VoteStatus
    VOTE_STATUS_NOT_VOTED: ViewedVotingPageProperties.VoteStatus
    VOTE_STATUS_OPTIONS_SELECTED: ViewedVotingPageProperties.VoteStatus
    VOTE_STATUS_SUBMITTED: ViewedVotingPageProperties.VoteStatus
    VOTING_STATUS_FIELD_NUMBER: _ClassVar[int]
    VOTE_STATUS_FIELD_NUMBER: _ClassVar[int]
    PAGE_LOAD_TIME_MS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_LOAD_TIME_MS_FIELD_NUMBER: _ClassVar[int]
    voting_status: ViewedVotingPageProperties.VotingStatus
    vote_status: ViewedVotingPageProperties.VoteStatus
    page_load_time_ms: int
    total_load_time_ms: int
    def __init__(self, voting_status: _Optional[_Union[ViewedVotingPageProperties.VotingStatus, str]] = ..., vote_status: _Optional[_Union[ViewedVotingPageProperties.VoteStatus, str]] = ..., page_load_time_ms: _Optional[int] = ..., total_load_time_ms: _Optional[int] = ...) -> None: ...
