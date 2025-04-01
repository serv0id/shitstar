from base import widget_commons_pb2 as _widget_commons_pb2
from feature.image import image_pb2 as _image_pb2
from widget import sports_cricket_player_pb2 as _sports_cricket_player_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CricketTeam(_message.Message):
    __slots__ = ("name", "icon", "score_title", "score_subtitle", "key_player_stats", "latest_desc", "is_batting")
    class KeyPlayerStats(_message.Message):
        __slots__ = ("player", "stats")
        PLAYER_FIELD_NUMBER: _ClassVar[int]
        STATS_FIELD_NUMBER: _ClassVar[int]
        player: _sports_cricket_player_pb2.CricketPlayer
        stats: str
        def __init__(self, player: _Optional[_Union[_sports_cricket_player_pb2.CricketPlayer, _Mapping]] = ..., stats: _Optional[str] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    ICON_FIELD_NUMBER: _ClassVar[int]
    SCORE_TITLE_FIELD_NUMBER: _ClassVar[int]
    SCORE_SUBTITLE_FIELD_NUMBER: _ClassVar[int]
    KEY_PLAYER_STATS_FIELD_NUMBER: _ClassVar[int]
    LATEST_DESC_FIELD_NUMBER: _ClassVar[int]
    IS_BATTING_FIELD_NUMBER: _ClassVar[int]
    name: str
    icon: _image_pb2.Image
    score_title: str
    score_subtitle: str
    key_player_stats: _containers.RepeatedCompositeFieldContainer[CricketTeam.KeyPlayerStats]
    latest_desc: str
    is_batting: bool
    def __init__(self, name: _Optional[str] = ..., icon: _Optional[_Union[_image_pb2.Image, _Mapping]] = ..., score_title: _Optional[str] = ..., score_subtitle: _Optional[str] = ..., key_player_stats: _Optional[_Iterable[_Union[CricketTeam.KeyPlayerStats, _Mapping]]] = ..., latest_desc: _Optional[str] = ..., is_batting: bool = ...) -> None: ...
