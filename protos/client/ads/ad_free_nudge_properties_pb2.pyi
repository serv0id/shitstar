from client.ads import info_pb2 as _info_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AdFreeNudgeProperties(_message.Message):
    __slots__ = ("info", "watched_time_seconds", "button_text")
    INFO_FIELD_NUMBER: _ClassVar[int]
    WATCHED_TIME_SECONDS_FIELD_NUMBER: _ClassVar[int]
    BUTTON_TEXT_FIELD_NUMBER: _ClassVar[int]
    info: _info_pb2.Info
    watched_time_seconds: int
    button_text: str
    def __init__(self, info: _Optional[_Union[_info_pb2.Info, _Mapping]] = ..., watched_time_seconds: _Optional[int] = ..., button_text: _Optional[str] = ...) -> None: ...
