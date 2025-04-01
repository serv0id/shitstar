from component.quiz import enum_pb2 as _enum_pb2
from component.quiz import quiz_base_info_pb2 as _quiz_base_info_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ViewedEngagementTabProperties(_message.Message):
    __slots__ = ("base_properties", "tab_name", "current_state")
    BASE_PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    TAB_NAME_FIELD_NUMBER: _ClassVar[int]
    CURRENT_STATE_FIELD_NUMBER: _ClassVar[int]
    base_properties: _quiz_base_info_pb2.QuizBaseInfo
    tab_name: str
    current_state: _enum_pb2.CurrentState
    def __init__(self, base_properties: _Optional[_Union[_quiz_base_info_pb2.QuizBaseInfo, _Mapping]] = ..., tab_name: _Optional[str] = ..., current_state: _Optional[_Union[_enum_pb2.CurrentState, str]] = ...) -> None: ...
