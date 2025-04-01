from component.quiz import quiz_base_info_pb2 as _quiz_base_info_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ViewedClaimRewardProperties(_message.Message):
    __slots__ = ("base_properties", "engagement_id", "button_cta")
    BASE_PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    ENGAGEMENT_ID_FIELD_NUMBER: _ClassVar[int]
    BUTTON_CTA_FIELD_NUMBER: _ClassVar[int]
    base_properties: _quiz_base_info_pb2.QuizBaseInfo
    engagement_id: str
    button_cta: str
    def __init__(self, base_properties: _Optional[_Union[_quiz_base_info_pb2.QuizBaseInfo, _Mapping]] = ..., engagement_id: _Optional[str] = ..., button_cta: _Optional[str] = ...) -> None: ...
