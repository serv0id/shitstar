from component.quiz import question_section_properties_pb2 as _question_section_properties_pb2
from component.quiz import quiz_base_info_pb2 as _quiz_base_info_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ClickedHintProperties(_message.Message):
    __slots__ = ("base_properties", "engagement_id", "section_properties", "hint_meta", "hint_type")
    BASE_PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    ENGAGEMENT_ID_FIELD_NUMBER: _ClassVar[int]
    SECTION_PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    HINT_META_FIELD_NUMBER: _ClassVar[int]
    HINT_TYPE_FIELD_NUMBER: _ClassVar[int]
    base_properties: _quiz_base_info_pb2.QuizBaseInfo
    engagement_id: str
    section_properties: _question_section_properties_pb2.QuestionSectionProperties
    hint_meta: str
    hint_type: str
    def __init__(self, base_properties: _Optional[_Union[_quiz_base_info_pb2.QuizBaseInfo, _Mapping]] = ..., engagement_id: _Optional[str] = ..., section_properties: _Optional[_Union[_question_section_properties_pb2.QuestionSectionProperties, _Mapping]] = ..., hint_meta: _Optional[str] = ..., hint_type: _Optional[str] = ...) -> None: ...
