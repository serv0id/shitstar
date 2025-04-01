from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TriggerSource(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TRIGGER_SOURCE_UNSPECIFIED: _ClassVar[TriggerSource]
    TRIGGER_SOURCE_END_OF_PLAYBACK: _ClassVar[TriggerSource]
    TRIGGER_SOURCE_BROWSE: _ClassVar[TriggerSource]
TRIGGER_SOURCE_UNSPECIFIED: TriggerSource
TRIGGER_SOURCE_END_OF_PLAYBACK: TriggerSource
TRIGGER_SOURCE_BROWSE: TriggerSource

class InappRatingTriggered(_message.Message):
    __slots__ = ("source", "session_time", "is_repeat", "app_session_time")
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    SESSION_TIME_FIELD_NUMBER: _ClassVar[int]
    IS_REPEAT_FIELD_NUMBER: _ClassVar[int]
    APP_SESSION_TIME_FIELD_NUMBER: _ClassVar[int]
    source: TriggerSource
    session_time: str
    is_repeat: bool
    app_session_time: int
    def __init__(self, source: _Optional[_Union[TriggerSource, str]] = ..., session_time: _Optional[str] = ..., is_repeat: bool = ..., app_session_time: _Optional[int] = ...) -> None: ...
