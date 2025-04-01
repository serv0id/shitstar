from component.quiz import enum_pb2 as _enum_pb2
from component.quiz import quiz_base_info_pb2 as _quiz_base_info_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ClickedPlayNowProperties(_message.Message):
    __slots__ = ("base_properties", "button_cta", "event_trigger")
    BASE_PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    BUTTON_CTA_FIELD_NUMBER: _ClassVar[int]
    EVENT_TRIGGER_FIELD_NUMBER: _ClassVar[int]
    base_properties: _quiz_base_info_pb2.QuizBaseInfo
    button_cta: str
    event_trigger: _enum_pb2.EventTrigger
    def __init__(self, base_properties: _Optional[_Union[_quiz_base_info_pb2.QuizBaseInfo, _Mapping]] = ..., button_cta: _Optional[str] = ..., event_trigger: _Optional[_Union[_enum_pb2.EventTrigger, str]] = ...) -> None: ...
