from component.quiz import enum_pb2 as _enum_pb2
from component.quiz import quiz_base_info_pb2 as _quiz_base_info_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ClickedShareEngagementProperties(_message.Message):
    __slots__ = ("base_properties", "button_cta", "bonus_score", "engagement_id")
    BASE_PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    BUTTON_CTA_FIELD_NUMBER: _ClassVar[int]
    BONUS_SCORE_FIELD_NUMBER: _ClassVar[int]
    ENGAGEMENT_ID_FIELD_NUMBER: _ClassVar[int]
    base_properties: _quiz_base_info_pb2.QuizBaseInfo
    button_cta: str
    bonus_score: int
    engagement_id: str
    def __init__(self, base_properties: _Optional[_Union[_quiz_base_info_pb2.QuizBaseInfo, _Mapping]] = ..., button_cta: _Optional[str] = ..., bonus_score: _Optional[int] = ..., engagement_id: _Optional[str] = ...) -> None: ...
