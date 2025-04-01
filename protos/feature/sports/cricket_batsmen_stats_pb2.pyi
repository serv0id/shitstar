from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class CricketBatsmenStats(_message.Message):
    __slots__ = ("runs", "balls", "fours", "sixes", "strike_rates")
    RUNS_FIELD_NUMBER: _ClassVar[int]
    BALLS_FIELD_NUMBER: _ClassVar[int]
    FOURS_FIELD_NUMBER: _ClassVar[int]
    SIXES_FIELD_NUMBER: _ClassVar[int]
    STRIKE_RATES_FIELD_NUMBER: _ClassVar[int]
    runs: str
    balls: str
    fours: str
    sixes: str
    strike_rates: str
    def __init__(self, runs: _Optional[str] = ..., balls: _Optional[str] = ..., fours: _Optional[str] = ..., sixes: _Optional[str] = ..., strike_rates: _Optional[str] = ...) -> None: ...
