from base import widget_commons_pb2 as _widget_commons_pb2
from widget import polling_pb2 as _polling_pb2
from feature.image import image_pb2 as _image_pb2
from widget import sports_cricket_team_pb2 as _sports_cricket_team_pb2
from feature.sports import game_pb2 as _game_pb2
from feature.sports import cricket_team_pb2 as _cricket_team_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CricketPollingSummaryCardWidget(_message.Message):
    __slots__ = ("widget_commons", "data")
    class Data(_message.Message):
        __slots__ = ("card", "polling")
        CARD_FIELD_NUMBER: _ClassVar[int]
        POLLING_FIELD_NUMBER: _ClassVar[int]
        card: CricketSummaryCardWidget
        polling: _polling_pb2.PollingData
        def __init__(self, card: _Optional[_Union[CricketSummaryCardWidget, _Mapping]] = ..., polling: _Optional[_Union[_polling_pb2.PollingData, _Mapping]] = ...) -> None: ...
    WIDGET_COMMONS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    widget_commons: _widget_commons_pb2.WidgetCommons
    data: CricketPollingSummaryCardWidget.Data
    def __init__(self, widget_commons: _Optional[_Union[_widget_commons_pb2.WidgetCommons, _Mapping]] = ..., data: _Optional[_Union[CricketPollingSummaryCardWidget.Data, _Mapping]] = ...) -> None: ...

class CricketSummaryCardWidget(_message.Message):
    __slots__ = ("widget_commons", "data")
    class Data(_message.Message):
        __slots__ = ("game_info", "first_team_v2", "second_team_v2", "latest_summary", "is_test_cricket", "last_few_balls", "innings", "current_batting_team_name", "name", "state", "meta_desc", "media_info", "first_team", "second_team")
        class GameState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            UNKNOWN: _ClassVar[CricketSummaryCardWidget.Data.GameState]
            NOT_START: _ClassVar[CricketSummaryCardWidget.Data.GameState]
            LIVE: _ClassVar[CricketSummaryCardWidget.Data.GameState]
            FINISHED: _ClassVar[CricketSummaryCardWidget.Data.GameState]
        UNKNOWN: CricketSummaryCardWidget.Data.GameState
        NOT_START: CricketSummaryCardWidget.Data.GameState
        LIVE: CricketSummaryCardWidget.Data.GameState
        FINISHED: CricketSummaryCardWidget.Data.GameState
        GAME_INFO_FIELD_NUMBER: _ClassVar[int]
        FIRST_TEAM_V2_FIELD_NUMBER: _ClassVar[int]
        SECOND_TEAM_V2_FIELD_NUMBER: _ClassVar[int]
        LATEST_SUMMARY_FIELD_NUMBER: _ClassVar[int]
        IS_TEST_CRICKET_FIELD_NUMBER: _ClassVar[int]
        LAST_FEW_BALLS_FIELD_NUMBER: _ClassVar[int]
        INNINGS_FIELD_NUMBER: _ClassVar[int]
        CURRENT_BATTING_TEAM_NAME_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        STATE_FIELD_NUMBER: _ClassVar[int]
        META_DESC_FIELD_NUMBER: _ClassVar[int]
        MEDIA_INFO_FIELD_NUMBER: _ClassVar[int]
        FIRST_TEAM_FIELD_NUMBER: _ClassVar[int]
        SECOND_TEAM_FIELD_NUMBER: _ClassVar[int]
        game_info: _game_pb2.Game
        first_team_v2: _cricket_team_pb2.CricketTeam
        second_team_v2: _cricket_team_pb2.CricketTeam
        latest_summary: str
        is_test_cricket: bool
        last_few_balls: _containers.RepeatedCompositeFieldContainer[CricketSummaryCardWidget.LastFewBallItem]
        innings: _containers.RepeatedScalarFieldContainer[str]
        current_batting_team_name: str
        name: str
        state: CricketSummaryCardWidget.Data.GameState
        meta_desc: str
        media_info: CricketSummaryCardWidget.MediaInfo
        first_team: _sports_cricket_team_pb2.CricketTeam
        second_team: _sports_cricket_team_pb2.CricketTeam
        def __init__(self, game_info: _Optional[_Union[_game_pb2.Game, _Mapping]] = ..., first_team_v2: _Optional[_Union[_cricket_team_pb2.CricketTeam, _Mapping]] = ..., second_team_v2: _Optional[_Union[_cricket_team_pb2.CricketTeam, _Mapping]] = ..., latest_summary: _Optional[str] = ..., is_test_cricket: bool = ..., last_few_balls: _Optional[_Iterable[_Union[CricketSummaryCardWidget.LastFewBallItem, _Mapping]]] = ..., innings: _Optional[_Iterable[str]] = ..., current_batting_team_name: _Optional[str] = ..., name: _Optional[str] = ..., state: _Optional[_Union[CricketSummaryCardWidget.Data.GameState, str]] = ..., meta_desc: _Optional[str] = ..., media_info: _Optional[_Union[CricketSummaryCardWidget.MediaInfo, _Mapping]] = ..., first_team: _Optional[_Union[_sports_cricket_team_pb2.CricketTeam, _Mapping]] = ..., second_team: _Optional[_Union[_sports_cricket_team_pb2.CricketTeam, _Mapping]] = ...) -> None: ...
    class MediaInfo(_message.Message):
        __slots__ = ("thumb_image", "clip_duration")
        THUMB_IMAGE_FIELD_NUMBER: _ClassVar[int]
        CLIP_DURATION_FIELD_NUMBER: _ClassVar[int]
        thumb_image: _image_pb2.Image
        clip_duration: str
        def __init__(self, thumb_image: _Optional[_Union[_image_pb2.Image, _Mapping]] = ..., clip_duration: _Optional[str] = ...) -> None: ...
    class LastFewBallItem(_message.Message):
        __slots__ = ("ball_type", "ball_score")
        class BallType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            UNKNOWN: _ClassVar[CricketSummaryCardWidget.LastFewBallItem.BallType]
            OVER_NUM: _ClassVar[CricketSummaryCardWidget.LastFewBallItem.BallType]
            NORMAL_SCORE: _ClassVar[CricketSummaryCardWidget.LastFewBallItem.BallType]
            FOUR: _ClassVar[CricketSummaryCardWidget.LastFewBallItem.BallType]
            SIX: _ClassVar[CricketSummaryCardWidget.LastFewBallItem.BallType]
            WICKET: _ClassVar[CricketSummaryCardWidget.LastFewBallItem.BallType]
        UNKNOWN: CricketSummaryCardWidget.LastFewBallItem.BallType
        OVER_NUM: CricketSummaryCardWidget.LastFewBallItem.BallType
        NORMAL_SCORE: CricketSummaryCardWidget.LastFewBallItem.BallType
        FOUR: CricketSummaryCardWidget.LastFewBallItem.BallType
        SIX: CricketSummaryCardWidget.LastFewBallItem.BallType
        WICKET: CricketSummaryCardWidget.LastFewBallItem.BallType
        BALL_TYPE_FIELD_NUMBER: _ClassVar[int]
        BALL_SCORE_FIELD_NUMBER: _ClassVar[int]
        ball_type: CricketSummaryCardWidget.LastFewBallItem.BallType
        ball_score: str
        def __init__(self, ball_type: _Optional[_Union[CricketSummaryCardWidget.LastFewBallItem.BallType, str]] = ..., ball_score: _Optional[str] = ...) -> None: ...
    WIDGET_COMMONS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    widget_commons: _widget_commons_pb2.WidgetCommons
    data: CricketSummaryCardWidget.Data
    def __init__(self, widget_commons: _Optional[_Union[_widget_commons_pb2.WidgetCommons, _Mapping]] = ..., data: _Optional[_Union[CricketSummaryCardWidget.Data, _Mapping]] = ...) -> None: ...
