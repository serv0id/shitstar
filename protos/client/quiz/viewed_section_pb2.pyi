from component.quiz import enum_pb2 as _enum_pb2
from component.quiz import question_section_properties_pb2 as _question_section_properties_pb2
from component.quiz import quiz_base_info_pb2 as _quiz_base_info_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ViewedSectionProperties(_message.Message):
    __slots__ = ("base_properties", "event_trigger", "engagement_id", "section_properties", "hint_meta")
    BASE_PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    EVENT_TRIGGER_FIELD_NUMBER: _ClassVar[int]
    ENGAGEMENT_ID_FIELD_NUMBER: _ClassVar[int]
    SECTION_PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    HINT_META_FIELD_NUMBER: _ClassVar[int]
    base_properties: _quiz_base_info_pb2.QuizBaseInfo
    event_trigger: _enum_pb2.EventTrigger
    engagement_id: str
    section_properties: _question_section_properties_pb2.QuestionSectionProperties
    hint_meta: str
    def __init__(self, base_properties: _Optional[_Union[_quiz_base_info_pb2.QuizBaseInfo, _Mapping]] = ..., event_trigger: _Optional[_Union[_enum_pb2.EventTrigger, str]] = ..., engagement_id: _Optional[str] = ..., section_properties: _Optional[_Union[_question_section_properties_pb2.QuestionSectionProperties, _Mapping]] = ..., hint_meta: _Optional[str] = ...) -> None: ...
