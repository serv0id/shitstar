from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class RatingNudgeProperties(_message.Message):
    __slots__ = ("current_rating", "is_user_triggered", "rating_nudge_ingress_type")
    CURRENT_RATING_FIELD_NUMBER: _ClassVar[int]
    IS_USER_TRIGGERED_FIELD_NUMBER: _ClassVar[int]
    RATING_NUDGE_INGRESS_TYPE_FIELD_NUMBER: _ClassVar[int]
    current_rating: str
    is_user_triggered: bool
    rating_nudge_ingress_type: str
    def __init__(self, current_rating: _Optional[str] = ..., is_user_triggered: bool = ..., rating_nudge_ingress_type: _Optional[str] = ...) -> None: ...
