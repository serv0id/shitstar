from base import widget_commons_pb2 as _widget_commons_pb2
from widget import sports_cricket_team_pb2 as _sports_cricket_team_pb2
from widget import sports_cricket_player_pb2 as _sports_cricket_player_pb2
from feature.sports import cricket_team_pb2 as _cricket_team_pb2
from feature.sports import cricket_player_pb2 as _cricket_player_pb2
from widget import sports_cricket_summary_card_pb2 as _sports_cricket_summary_card_pb2
from feature.sports import cricket_batsmen_stats_pb2 as _cricket_batsmen_stats_pb2
from feature.sports import cricket_bowler_stats_pb2 as _cricket_bowler_stats_pb2
from feature.sports import cricket_fall_of_wickets_stats_pb2 as _cricket_fall_of_wickets_stats_pb2
from widget import no_results_pb2 as _no_results_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CricketScorecardWidget(_message.Message):
    __slots__ = ("widget_commons", "data")
    class Data(_message.Message):
        __slots__ = ("summary_card", "boards", "is_test_cricket", "poling_data", "refresh_url", "no_score", "timestamp", "is_match_over")
        SUMMARY_CARD_FIELD_NUMBER: _ClassVar[int]
        BOARDS_FIELD_NUMBER: _ClassVar[int]
        IS_TEST_CRICKET_FIELD_NUMBER: _ClassVar[int]
        POLING_DATA_FIELD_NUMBER: _ClassVar[int]
        REFRESH_URL_FIELD_NUMBER: _ClassVar[int]
        NO_SCORE_FIELD_NUMBER: _ClassVar[int]
        TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
        IS_MATCH_OVER_FIELD_NUMBER: _ClassVar[int]
        summary_card: _sports_cricket_summary_card_pb2.CricketSummaryCardWidget
        boards: _containers.RepeatedCompositeFieldContainer[CricketScorecardWidget.ScoreBoard]
        is_test_cricket: bool
        poling_data: CricketScorecardWidget.ScoreCardPollingData
        refresh_url: str
        no_score: _no_results_pb2.NoResultsWidget
        timestamp: int
        is_match_over: bool
        def __init__(self, summary_card: _Optional[_Union[_sports_cricket_summary_card_pb2.CricketSummaryCardWidget, _Mapping]] = ..., boards: _Optional[_Iterable[_Union[CricketScorecardWidget.ScoreBoard, _Mapping]]] = ..., is_test_cricket: bool = ..., poling_data: _Optional[_Union[CricketScorecardWidget.ScoreCardPollingData, _Mapping]] = ..., refresh_url: _Optional[str] = ..., no_score: _Optional[_Union[_no_results_pb2.NoResultsWidget, _Mapping]] = ..., timestamp: _Optional[int] = ..., is_match_over: bool = ...) -> None: ...
    class ScoreCardPollingData(_message.Message):
        __slots__ = ("active", "frequency", "polling_url")
        ACTIVE_FIELD_NUMBER: _ClassVar[int]
        FREQUENCY_FIELD_NUMBER: _ClassVar[int]
        POLLING_URL_FIELD_NUMBER: _ClassVar[int]
        active: bool
        frequency: int
        polling_url: str
        def __init__(self, active: bool = ..., frequency: _Optional[int] = ..., polling_url: _Optional[str] = ...) -> None: ...
    class ScoreBoard(_message.Message):
        __slots__ = ("team_v2", "inning", "score_state", "is_selected", "team")
        TEAM_V2_FIELD_NUMBER: _ClassVar[int]
        INNING_FIELD_NUMBER: _ClassVar[int]
        SCORE_STATE_FIELD_NUMBER: _ClassVar[int]
        IS_SELECTED_FIELD_NUMBER: _ClassVar[int]
        TEAM_FIELD_NUMBER: _ClassVar[int]
        team_v2: _cricket_team_pb2.CricketTeam
        inning: str
        score_state: CricketScorecardWidget.ScoreBoardState
        is_selected: bool
        team: _sports_cricket_team_pb2.CricketTeam
        def __init__(self, team_v2: _Optional[_Union[_cricket_team_pb2.CricketTeam, _Mapping]] = ..., inning: _Optional[str] = ..., score_state: _Optional[_Union[CricketScorecardWidget.ScoreBoardState, _Mapping]] = ..., is_selected: bool = ..., team: _Optional[_Union[_sports_cricket_team_pb2.CricketTeam, _Mapping]] = ...) -> None: ...
    class ScoreBoardState(_message.Message):
        __slots__ = ("zero_state", "batting_stats")
        ZERO_STATE_FIELD_NUMBER: _ClassVar[int]
        BATTING_STATS_FIELD_NUMBER: _ClassVar[int]
        zero_state: CricketScorecardWidget.ScoreBoardZeroState
        batting_stats: CricketScorecardWidget.ScoreBoardBattingStats
        def __init__(self, zero_state: _Optional[_Union[CricketScorecardWidget.ScoreBoardZeroState, _Mapping]] = ..., batting_stats: _Optional[_Union[CricketScorecardWidget.ScoreBoardBattingStats, _Mapping]] = ...) -> None: ...
    class ScoreBoardZeroState(_message.Message):
        __slots__ = ("players_v2", "players")
        PLAYERS_V2_FIELD_NUMBER: _ClassVar[int]
        PLAYERS_FIELD_NUMBER: _ClassVar[int]
        players_v2: _containers.RepeatedCompositeFieldContainer[_cricket_player_pb2.CricketPlayer]
        players: _containers.RepeatedCompositeFieldContainer[_sports_cricket_player_pb2.CricketPlayer]
        def __init__(self, players_v2: _Optional[_Iterable[_Union[_cricket_player_pb2.CricketPlayer, _Mapping]]] = ..., players: _Optional[_Iterable[_Union[_sports_cricket_player_pb2.CricketPlayer, _Mapping]]] = ...) -> None: ...
    class ScoreBoardBattingStats(_message.Message):
        __slots__ = ("sections",)
        SECTIONS_FIELD_NUMBER: _ClassVar[int]
        sections: _containers.RepeatedCompositeFieldContainer[CricketScorecardWidget.ScoreBoardSection]
        def __init__(self, sections: _Optional[_Iterable[_Union[CricketScorecardWidget.ScoreBoardSection, _Mapping]]] = ...) -> None: ...
    class ScoreBoardSection(_message.Message):
        __slots__ = ("batting", "bowling", "fall_of_wickets")
        BATTING_FIELD_NUMBER: _ClassVar[int]
        BOWLING_FIELD_NUMBER: _ClassVar[int]
        FALL_OF_WICKETS_FIELD_NUMBER: _ClassVar[int]
        batting: CricketScorecardWidget.BattingSection
        bowling: CricketScorecardWidget.BowlingSection
        fall_of_wickets: CricketScorecardWidget.FallOfWicketsSection
        def __init__(self, batting: _Optional[_Union[CricketScorecardWidget.BattingSection, _Mapping]] = ..., bowling: _Optional[_Union[CricketScorecardWidget.BowlingSection, _Mapping]] = ..., fall_of_wickets: _Optional[_Union[CricketScorecardWidget.FallOfWicketsSection, _Mapping]] = ...) -> None: ...
    class BattingSection(_message.Message):
        __slots__ = ("header", "rows", "total_row", "yet_to_bat")
        HEADER_FIELD_NUMBER: _ClassVar[int]
        ROWS_FIELD_NUMBER: _ClassVar[int]
        TOTAL_ROW_FIELD_NUMBER: _ClassVar[int]
        YET_TO_BAT_FIELD_NUMBER: _ClassVar[int]
        header: CricketScorecardWidget.BatsmenHeader
        rows: _containers.RepeatedCompositeFieldContainer[CricketScorecardWidget.BatsmenRow]
        total_row: CricketScorecardWidget.BattingTotalRow
        yet_to_bat: CricketScorecardWidget.BatsmensYetToBat
        def __init__(self, header: _Optional[_Union[CricketScorecardWidget.BatsmenHeader, _Mapping]] = ..., rows: _Optional[_Iterable[_Union[CricketScorecardWidget.BatsmenRow, _Mapping]]] = ..., total_row: _Optional[_Union[CricketScorecardWidget.BattingTotalRow, _Mapping]] = ..., yet_to_bat: _Optional[_Union[CricketScorecardWidget.BatsmensYetToBat, _Mapping]] = ...) -> None: ...
    class BatsmenHeader(_message.Message):
        __slots__ = ("title", "stats_v2", "stats")
        TITLE_FIELD_NUMBER: _ClassVar[int]
        STATS_V2_FIELD_NUMBER: _ClassVar[int]
        STATS_FIELD_NUMBER: _ClassVar[int]
        title: str
        stats_v2: _cricket_batsmen_stats_pb2.CricketBatsmenStats
        stats: CricketScorecardWidget.BatsmenStats
        def __init__(self, title: _Optional[str] = ..., stats_v2: _Optional[_Union[_cricket_batsmen_stats_pb2.CricketBatsmenStats, _Mapping]] = ..., stats: _Optional[_Union[CricketScorecardWidget.BatsmenStats, _Mapping]] = ...) -> None: ...
    class BatsmenRow(_message.Message):
        __slots__ = ("player_v2", "stats_v2", "player", "stats")
        PLAYER_V2_FIELD_NUMBER: _ClassVar[int]
        STATS_V2_FIELD_NUMBER: _ClassVar[int]
        PLAYER_FIELD_NUMBER: _ClassVar[int]
        STATS_FIELD_NUMBER: _ClassVar[int]
        player_v2: _cricket_player_pb2.CricketPlayer
        stats_v2: _cricket_batsmen_stats_pb2.CricketBatsmenStats
        player: _sports_cricket_player_pb2.CricketPlayer
        stats: CricketScorecardWidget.BatsmenStats
        def __init__(self, player_v2: _Optional[_Union[_cricket_player_pb2.CricketPlayer, _Mapping]] = ..., stats_v2: _Optional[_Union[_cricket_batsmen_stats_pb2.CricketBatsmenStats, _Mapping]] = ..., player: _Optional[_Union[_sports_cricket_player_pb2.CricketPlayer, _Mapping]] = ..., stats: _Optional[_Union[CricketScorecardWidget.BatsmenStats, _Mapping]] = ...) -> None: ...
    class BatsmenStats(_message.Message):
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
    class BattingTotalRow(_message.Message):
        __slots__ = ("title", "score", "overs_and_run_rates")
        TITLE_FIELD_NUMBER: _ClassVar[int]
        SCORE_FIELD_NUMBER: _ClassVar[int]
        OVERS_AND_RUN_RATES_FIELD_NUMBER: _ClassVar[int]
        title: str
        score: str
        overs_and_run_rates: str
        def __init__(self, title: _Optional[str] = ..., score: _Optional[str] = ..., overs_and_run_rates: _Optional[str] = ...) -> None: ...
    class BatsmensYetToBat(_message.Message):
        __slots__ = ("title", "players_name_content")
        TITLE_FIELD_NUMBER: _ClassVar[int]
        PLAYERS_NAME_CONTENT_FIELD_NUMBER: _ClassVar[int]
        title: str
        players_name_content: str
        def __init__(self, title: _Optional[str] = ..., players_name_content: _Optional[str] = ...) -> None: ...
    class BowlingSection(_message.Message):
        __slots__ = ("header", "rows")
        HEADER_FIELD_NUMBER: _ClassVar[int]
        ROWS_FIELD_NUMBER: _ClassVar[int]
        header: CricketScorecardWidget.BowlerHeader
        rows: _containers.RepeatedCompositeFieldContainer[CricketScorecardWidget.BowlerRow]
        def __init__(self, header: _Optional[_Union[CricketScorecardWidget.BowlerHeader, _Mapping]] = ..., rows: _Optional[_Iterable[_Union[CricketScorecardWidget.BowlerRow, _Mapping]]] = ...) -> None: ...
    class BowlerHeader(_message.Message):
        __slots__ = ("title", "stats_v2", "stats")
        TITLE_FIELD_NUMBER: _ClassVar[int]
        STATS_V2_FIELD_NUMBER: _ClassVar[int]
        STATS_FIELD_NUMBER: _ClassVar[int]
        title: str
        stats_v2: _cricket_bowler_stats_pb2.CricketBowlerStats
        stats: CricketScorecardWidget.BowlerStats
        def __init__(self, title: _Optional[str] = ..., stats_v2: _Optional[_Union[_cricket_bowler_stats_pb2.CricketBowlerStats, _Mapping]] = ..., stats: _Optional[_Union[CricketScorecardWidget.BowlerStats, _Mapping]] = ...) -> None: ...
    class BowlerRow(_message.Message):
        __slots__ = ("player_v2", "stats_v2", "player", "stats")
        PLAYER_V2_FIELD_NUMBER: _ClassVar[int]
        STATS_V2_FIELD_NUMBER: _ClassVar[int]
        PLAYER_FIELD_NUMBER: _ClassVar[int]
        STATS_FIELD_NUMBER: _ClassVar[int]
        player_v2: _cricket_player_pb2.CricketPlayer
        stats_v2: _cricket_bowler_stats_pb2.CricketBowlerStats
        player: _sports_cricket_player_pb2.CricketPlayer
        stats: CricketScorecardWidget.BowlerStats
        def __init__(self, player_v2: _Optional[_Union[_cricket_player_pb2.CricketPlayer, _Mapping]] = ..., stats_v2: _Optional[_Union[_cricket_bowler_stats_pb2.CricketBowlerStats, _Mapping]] = ..., player: _Optional[_Union[_sports_cricket_player_pb2.CricketPlayer, _Mapping]] = ..., stats: _Optional[_Union[CricketScorecardWidget.BowlerStats, _Mapping]] = ...) -> None: ...
    class BowlerStats(_message.Message):
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
    class FallOfWicketsSection(_message.Message):
        __slots__ = ("header", "rows")
        HEADER_FIELD_NUMBER: _ClassVar[int]
        ROWS_FIELD_NUMBER: _ClassVar[int]
        header: CricketScorecardWidget.FallOfWicketsHeader
        rows: _containers.RepeatedCompositeFieldContainer[CricketScorecardWidget.FallOfWicketsRow]
        def __init__(self, header: _Optional[_Union[CricketScorecardWidget.FallOfWicketsHeader, _Mapping]] = ..., rows: _Optional[_Iterable[_Union[CricketScorecardWidget.FallOfWicketsRow, _Mapping]]] = ...) -> None: ...
    class FallOfWicketsHeader(_message.Message):
        __slots__ = ("title", "stats_v2", "stats")
        TITLE_FIELD_NUMBER: _ClassVar[int]
        STATS_V2_FIELD_NUMBER: _ClassVar[int]
        STATS_FIELD_NUMBER: _ClassVar[int]
        title: str
        stats_v2: _cricket_fall_of_wickets_stats_pb2.CricketFallOfWicketsStats
        stats: CricketScorecardWidget.FallOfWicketsStats
        def __init__(self, title: _Optional[str] = ..., stats_v2: _Optional[_Union[_cricket_fall_of_wickets_stats_pb2.CricketFallOfWicketsStats, _Mapping]] = ..., stats: _Optional[_Union[CricketScorecardWidget.FallOfWicketsStats, _Mapping]] = ...) -> None: ...
    class FallOfWicketsRow(_message.Message):
        __slots__ = ("player_v2", "stats_v2", "player", "stats")
        PLAYER_V2_FIELD_NUMBER: _ClassVar[int]
        STATS_V2_FIELD_NUMBER: _ClassVar[int]
        PLAYER_FIELD_NUMBER: _ClassVar[int]
        STATS_FIELD_NUMBER: _ClassVar[int]
        player_v2: _cricket_player_pb2.CricketPlayer
        stats_v2: _cricket_fall_of_wickets_stats_pb2.CricketFallOfWicketsStats
        player: _sports_cricket_player_pb2.CricketPlayer
        stats: CricketScorecardWidget.FallOfWicketsStats
        def __init__(self, player_v2: _Optional[_Union[_cricket_player_pb2.CricketPlayer, _Mapping]] = ..., stats_v2: _Optional[_Union[_cricket_fall_of_wickets_stats_pb2.CricketFallOfWicketsStats, _Mapping]] = ..., player: _Optional[_Union[_sports_cricket_player_pb2.CricketPlayer, _Mapping]] = ..., stats: _Optional[_Union[CricketScorecardWidget.FallOfWicketsStats, _Mapping]] = ...) -> None: ...
    class FallOfWicketsStats(_message.Message):
        __slots__ = ("score", "over")
        SCORE_FIELD_NUMBER: _ClassVar[int]
        OVER_FIELD_NUMBER: _ClassVar[int]
        score: str
        over: str
        def __init__(self, score: _Optional[str] = ..., over: _Optional[str] = ...) -> None: ...
    WIDGET_COMMONS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    widget_commons: _widget_commons_pb2.WidgetCommons
    data: CricketScorecardWidget.Data
    def __init__(self, widget_commons: _Optional[_Union[_widget_commons_pb2.WidgetCommons, _Mapping]] = ..., data: _Optional[_Union[CricketScorecardWidget.Data, _Mapping]] = ...) -> None: ...
