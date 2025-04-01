from feature.sports import player_pb2 as _player_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CricketPlayer(_message.Message):
    __slots__ = ("basic_player", "play_state", "play_state_desc")
    class PlayState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNKNOWN: _ClassVar[CricketPlayer.PlayState]
        YET_TO_BAT: _ClassVar[CricketPlayer.PlayState]
        NOT_OUT: _ClassVar[CricketPlayer.PlayState]
        OUT: _ClassVar[CricketPlayer.PlayState]
    UNKNOWN: CricketPlayer.PlayState
    YET_TO_BAT: CricketPlayer.PlayState
    NOT_OUT: CricketPlayer.PlayState
    OUT: CricketPlayer.PlayState
    BASIC_PLAYER_FIELD_NUMBER: _ClassVar[int]
    PLAY_STATE_FIELD_NUMBER: _ClassVar[int]
    PLAY_STATE_DESC_FIELD_NUMBER: _ClassVar[int]
    basic_player: _player_pb2.Player
    play_state: CricketPlayer.PlayState
    play_state_desc: str
    def __init__(self, basic_player: _Optional[_Union[_player_pb2.Player, _Mapping]] = ..., play_state: _Optional[_Union[CricketPlayer.PlayState, str]] = ..., play_state_desc: _Optional[str] = ...) -> None: ...
