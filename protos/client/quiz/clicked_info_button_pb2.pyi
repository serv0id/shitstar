from component.quiz import enum_pb2 as _enum_pb2
from component.quiz import quiz_base_info_pb2 as _quiz_base_info_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ClickedInfoButtonProperties(_message.Message):
    __slots__ = ("base_properties", "info_type", "engagement_id")
    BASE_PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    INFO_TYPE_FIELD_NUMBER: _ClassVar[int]
    ENGAGEMENT_ID_FIELD_NUMBER: _ClassVar[int]
    base_properties: _quiz_base_info_pb2.QuizBaseInfo
    info_type: _enum_pb2.InfoType
    engagement_id: str
    def __init__(self, base_properties: _Optional[_Union[_quiz_base_info_pb2.QuizBaseInfo, _Mapping]] = ..., info_type: _Optional[_Union[_enum_pb2.InfoType, str]] = ..., engagement_id: _Optional[str] = ...) -> None: ...
