from options import opts_pb2 as _opts_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class Info(_message.Message):
    __slots__ = ("campaign_id", "goal_id", "id", "ids")
    CAMPAIGN_ID_FIELD_NUMBER: _ClassVar[int]
    GOAL_ID_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    IDS_FIELD_NUMBER: _ClassVar[int]
    campaign_id: str
    goal_id: str
    id: str
    ids: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, campaign_id: _Optional[str] = ..., goal_id: _Optional[str] = ..., id: _Optional[str] = ..., ids: _Optional[_Iterable[str]] = ...) -> None: ...
