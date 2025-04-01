from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class QuizBaseInfo(_message.Message):
    __slots__ = ("engagement_type", "stream_state", "season_id")
    ENGAGEMENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    STREAM_STATE_FIELD_NUMBER: _ClassVar[int]
    SEASON_ID_FIELD_NUMBER: _ClassVar[int]
    engagement_type: str
    stream_state: str
    season_id: int
    def __init__(self, engagement_type: _Optional[str] = ..., stream_state: _Optional[str] = ..., season_id: _Optional[int] = ...) -> None: ...
