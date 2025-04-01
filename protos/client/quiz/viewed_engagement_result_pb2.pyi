from component.quiz import quiz_base_info_pb2 as _quiz_base_info_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ViewedEngagementResultProperties(_message.Message):
    __slots__ = ("base_properties", "engagement_id", "engagement_feature_score", "engagement_feature_bonus_score", "bonus_multiplier")
    BASE_PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    ENGAGEMENT_ID_FIELD_NUMBER: _ClassVar[int]
    ENGAGEMENT_FEATURE_SCORE_FIELD_NUMBER: _ClassVar[int]
    ENGAGEMENT_FEATURE_BONUS_SCORE_FIELD_NUMBER: _ClassVar[int]
    BONUS_MULTIPLIER_FIELD_NUMBER: _ClassVar[int]
    base_properties: _quiz_base_info_pb2.QuizBaseInfo
    engagement_id: str
    engagement_feature_score: int
    engagement_feature_bonus_score: int
    bonus_multiplier: int
    def __init__(self, base_properties: _Optional[_Union[_quiz_base_info_pb2.QuizBaseInfo, _Mapping]] = ..., engagement_id: _Optional[str] = ..., engagement_feature_score: _Optional[int] = ..., engagement_feature_bonus_score: _Optional[int] = ..., bonus_multiplier: _Optional[int] = ...) -> None: ...
