from client.voting import viewed_voting_page_pb2 as _viewed_voting_page_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class QuitVotingPageProperties(_message.Message):
    __slots__ = ("voting_status", "voting_action", "selected_options", "event_trigger", "vote_status")
    class VotingAction(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        VOTING_ACTION_UNSPECIFIED: _ClassVar[QuitVotingPageProperties.VotingAction]
        VOTING_ACTION_SELECTED_OPTIONS: _ClassVar[QuitVotingPageProperties.VotingAction]
        VOTING_ACTION_MODIFIED_OPTIONS: _ClassVar[QuitVotingPageProperties.VotingAction]
        VOTING_ACTION_SUBMITTED: _ClassVar[QuitVotingPageProperties.VotingAction]
        VOTING_ACTION_NO_ACTION: _ClassVar[QuitVotingPageProperties.VotingAction]
        VOTING_ACTION_VIEWED_CAST_VOTES: _ClassVar[QuitVotingPageProperties.VotingAction]
    VOTING_ACTION_UNSPECIFIED: QuitVotingPageProperties.VotingAction
    VOTING_ACTION_SELECTED_OPTIONS: QuitVotingPageProperties.VotingAction
    VOTING_ACTION_MODIFIED_OPTIONS: QuitVotingPageProperties.VotingAction
    VOTING_ACTION_SUBMITTED: QuitVotingPageProperties.VotingAction
    VOTING_ACTION_NO_ACTION: QuitVotingPageProperties.VotingAction
    VOTING_ACTION_VIEWED_CAST_VOTES: QuitVotingPageProperties.VotingAction
    class EventTrigger(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        EVENT_TRIGGER_UNSPECIFIED: _ClassVar[QuitVotingPageProperties.EventTrigger]
        EVENT_TRIGGER_VOTES_SUBMITTED: _ClassVar[QuitVotingPageProperties.EventTrigger]
        EVENT_TRIGGER_BACK_NAVIGATION: _ClassVar[QuitVotingPageProperties.EventTrigger]
        EVENT_TRIGGER_CLICKED_CLOSE_BUTTON: _ClassVar[QuitVotingPageProperties.EventTrigger]
    EVENT_TRIGGER_UNSPECIFIED: QuitVotingPageProperties.EventTrigger
    EVENT_TRIGGER_VOTES_SUBMITTED: QuitVotingPageProperties.EventTrigger
    EVENT_TRIGGER_BACK_NAVIGATION: QuitVotingPageProperties.EventTrigger
    EVENT_TRIGGER_CLICKED_CLOSE_BUTTON: QuitVotingPageProperties.EventTrigger
    VOTING_STATUS_FIELD_NUMBER: _ClassVar[int]
    VOTING_ACTION_FIELD_NUMBER: _ClassVar[int]
    SELECTED_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    EVENT_TRIGGER_FIELD_NUMBER: _ClassVar[int]
    VOTE_STATUS_FIELD_NUMBER: _ClassVar[int]
    voting_status: _viewed_voting_page_pb2.ViewedVotingPageProperties.VotingStatus
    voting_action: QuitVotingPageProperties.VotingAction
    selected_options: _containers.RepeatedScalarFieldContainer[str]
    event_trigger: QuitVotingPageProperties.EventTrigger
    vote_status: _viewed_voting_page_pb2.ViewedVotingPageProperties.VoteStatus
    def __init__(self, voting_status: _Optional[_Union[_viewed_voting_page_pb2.ViewedVotingPageProperties.VotingStatus, str]] = ..., voting_action: _Optional[_Union[QuitVotingPageProperties.VotingAction, str]] = ..., selected_options: _Optional[_Iterable[str]] = ..., event_trigger: _Optional[_Union[QuitVotingPageProperties.EventTrigger, str]] = ..., vote_status: _Optional[_Union[_viewed_voting_page_pb2.ViewedVotingPageProperties.VoteStatus, str]] = ...) -> None: ...
