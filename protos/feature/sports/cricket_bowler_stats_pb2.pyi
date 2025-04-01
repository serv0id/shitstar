from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class CricketBowlerStats(_message.Message):
    __slots__ = ("overs", "maidens", "runs", "wickets", "economy")
    OVERS_FIELD_NUMBER: _ClassVar[int]
    MAIDENS_FIELD_NUMBER: _ClassVar[int]
    RUNS_FIELD_NUMBER: _ClassVar[int]
    WICKETS_FIELD_NUMBER: _ClassVar[int]
    ECONOMY_FIELD_NUMBER: _ClassVar[int]
    overs: str
    maidens: str
    runs: str
    wickets: str
    economy: str
    def __init__(self, overs: _Optional[str] = ..., maidens: _Optional[str] = ..., runs: _Optional[str] = ..., wickets: _Optional[str] = ..., economy: _Optional[str] = ...) -> None: ...
