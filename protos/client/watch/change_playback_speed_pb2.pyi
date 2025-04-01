from client import orientation_pb2 as _orientation_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ChangePlaybackSpeedProperties(_message.Message):
    __slots__ = ("previous_speed", "new_speed", "player_orientation", "player_version")
    PREVIOUS_SPEED_FIELD_NUMBER: _ClassVar[int]
    NEW_SPEED_FIELD_NUMBER: _ClassVar[int]
    PLAYER_ORIENTATION_FIELD_NUMBER: _ClassVar[int]
    PLAYER_VERSION_FIELD_NUMBER: _ClassVar[int]
    previous_speed: float
    new_speed: float
    player_orientation: _orientation_pb2.Orientation
    player_version: str
    def __init__(self, previous_speed: _Optional[float] = ..., new_speed: _Optional[float] = ..., player_orientation: _Optional[_Union[_orientation_pb2.Orientation, str]] = ..., player_version: _Optional[str] = ...) -> None: ...
