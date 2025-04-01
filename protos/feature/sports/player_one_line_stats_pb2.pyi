from feature.sports import player_pb2 as _player_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PlayerOneLineStats(_message.Message):
    __slots__ = ("player", "one_line_stats")
    PLAYER_FIELD_NUMBER: _ClassVar[int]
    ONE_LINE_STATS_FIELD_NUMBER: _ClassVar[int]
    player: _player_pb2.Player
    one_line_stats: str
    def __init__(self, player: _Optional[_Union[_player_pb2.Player, _Mapping]] = ..., one_line_stats: _Optional[str] = ...) -> None: ...
