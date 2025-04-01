from feature.sports import team_pb2 as _team_pb2
from feature.sports import player_one_line_stats_pb2 as _player_one_line_stats_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CricketTeam(_message.Message):
    __slots__ = ("basic_team", "score_title", "score_subtitle", "key_player_stats", "latest_desc", "is_batting")
    BASIC_TEAM_FIELD_NUMBER: _ClassVar[int]
    SCORE_TITLE_FIELD_NUMBER: _ClassVar[int]
    SCORE_SUBTITLE_FIELD_NUMBER: _ClassVar[int]
    KEY_PLAYER_STATS_FIELD_NUMBER: _ClassVar[int]
    LATEST_DESC_FIELD_NUMBER: _ClassVar[int]
    IS_BATTING_FIELD_NUMBER: _ClassVar[int]
    basic_team: _team_pb2.Team
    score_title: str
    score_subtitle: str
    key_player_stats: _containers.RepeatedCompositeFieldContainer[_player_one_line_stats_pb2.PlayerOneLineStats]
    latest_desc: str
    is_batting: bool
    def __init__(self, basic_team: _Optional[_Union[_team_pb2.Team, _Mapping]] = ..., score_title: _Optional[str] = ..., score_subtitle: _Optional[str] = ..., key_player_stats: _Optional[_Iterable[_Union[_player_one_line_stats_pb2.PlayerOneLineStats, _Mapping]]] = ..., latest_desc: _Optional[str] = ..., is_batting: bool = ...) -> None: ...
