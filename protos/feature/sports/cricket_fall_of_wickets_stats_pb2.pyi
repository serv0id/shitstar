from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class CricketFallOfWicketsStats(_message.Message):
    __slots__ = ("score", "over")
    SCORE_FIELD_NUMBER: _ClassVar[int]
    OVER_FIELD_NUMBER: _ClassVar[int]
    score: str
    over: str
    def __init__(self, score: _Optional[str] = ..., over: _Optional[str] = ...) -> None: ...
