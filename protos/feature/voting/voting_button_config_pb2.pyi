from base import actions_pb2 as _actions_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class VotingButtonConfig(_message.Message):
    __slots__ = ("icon", "title", "start_time", "end_time", "server_return_time", "voting_widget_url", "voting_domain_query_url", "voting_id", "error_handle_action", "content_title")
    ICON_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    SERVER_RETURN_TIME_FIELD_NUMBER: _ClassVar[int]
    VOTING_WIDGET_URL_FIELD_NUMBER: _ClassVar[int]
    VOTING_DOMAIN_QUERY_URL_FIELD_NUMBER: _ClassVar[int]
    VOTING_ID_FIELD_NUMBER: _ClassVar[int]
    ERROR_HANDLE_ACTION_FIELD_NUMBER: _ClassVar[int]
    CONTENT_TITLE_FIELD_NUMBER: _ClassVar[int]
    icon: str
    title: str
    start_time: int
    end_time: int
    server_return_time: int
    voting_widget_url: str
    voting_domain_query_url: str
    voting_id: str
    error_handle_action: _actions_pb2.Actions
    content_title: str
    def __init__(self, icon: _Optional[str] = ..., title: _Optional[str] = ..., start_time: _Optional[int] = ..., end_time: _Optional[int] = ..., server_return_time: _Optional[int] = ..., voting_widget_url: _Optional[str] = ..., voting_domain_query_url: _Optional[str] = ..., voting_id: _Optional[str] = ..., error_handle_action: _Optional[_Union[_actions_pb2.Actions, _Mapping]] = ..., content_title: _Optional[str] = ...) -> None: ...
