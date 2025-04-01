from base import widget_commons_pb2 as _widget_commons_pb2
from base import actions_pb2 as _actions_pb2
from feature.quiz import title_icon_combo_pb2 as _title_icon_combo_pb2
from widget import no_results_pb2 as _no_results_pb2
from widget import lottie_banner_pb2 as _lottie_banner_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class QuizLeaderBoardWidget(_message.Message):
    __slots__ = ("widget_commons", "data")
    class Data(_message.Message):
        __slots__ = ("boards", "hide_single_board_tab")
        BOARDS_FIELD_NUMBER: _ClassVar[int]
        HIDE_SINGLE_BOARD_TAB_FIELD_NUMBER: _ClassVar[int]
        boards: _containers.RepeatedCompositeFieldContainer[QuizLeaderBoardWidget.LeaderBoard]
        hide_single_board_tab: bool
        def __init__(self, boards: _Optional[_Iterable[_Union[QuizLeaderBoardWidget.LeaderBoard, _Mapping]]] = ..., hide_single_board_tab: bool = ...) -> None: ...
    class LeaderBoard(_message.Message):
        __slots__ = ("title", "state")
        TITLE_FIELD_NUMBER: _ClassVar[int]
        STATE_FIELD_NUMBER: _ClassVar[int]
        title: str
        state: QuizLeaderBoardWidget.LeaderBoardState
        def __init__(self, title: _Optional[str] = ..., state: _Optional[_Union[QuizLeaderBoardWidget.LeaderBoardState, _Mapping]] = ...) -> None: ...
    class LeaderBoardState(_message.Message):
        __slots__ = ("no_results", "leader_board")
        NO_RESULTS_FIELD_NUMBER: _ClassVar[int]
        LEADER_BOARD_FIELD_NUMBER: _ClassVar[int]
        no_results: _no_results_pb2.NoResultsWidget
        leader_board: QuizLeaderBoardWidget.LeaderBoardWidget
        def __init__(self, no_results: _Optional[_Union[_no_results_pb2.NoResultsWidget, _Mapping]] = ..., leader_board: _Optional[_Union[QuizLeaderBoardWidget.LeaderBoardWidget, _Mapping]] = ...) -> None: ...
    class LeaderBoardWidget(_message.Message):
        __slots__ = ("widget_commons", "data")
        class Data(_message.Message):
            __slots__ = ("top_reminder", "header", "rows", "prize_reminder")
            TOP_REMINDER_FIELD_NUMBER: _ClassVar[int]
            HEADER_FIELD_NUMBER: _ClassVar[int]
            ROWS_FIELD_NUMBER: _ClassVar[int]
            PRIZE_REMINDER_FIELD_NUMBER: _ClassVar[int]
            top_reminder: QuizLeaderBoardWidget.LeaderBoardReminder
            header: QuizLeaderBoardWidget.LeaderBoardHeader
            rows: _containers.RepeatedCompositeFieldContainer[QuizLeaderBoardWidget.LeaderBoardRow]
            prize_reminder: QuizLeaderBoardWidget.LeaderBoardPrizeReminder
            def __init__(self, top_reminder: _Optional[_Union[QuizLeaderBoardWidget.LeaderBoardReminder, _Mapping]] = ..., header: _Optional[_Union[QuizLeaderBoardWidget.LeaderBoardHeader, _Mapping]] = ..., rows: _Optional[_Iterable[_Union[QuizLeaderBoardWidget.LeaderBoardRow, _Mapping]]] = ..., prize_reminder: _Optional[_Union[QuizLeaderBoardWidget.LeaderBoardPrizeReminder, _Mapping]] = ...) -> None: ...
        WIDGET_COMMONS_FIELD_NUMBER: _ClassVar[int]
        DATA_FIELD_NUMBER: _ClassVar[int]
        widget_commons: _widget_commons_pb2.WidgetCommons
        data: QuizLeaderBoardWidget.LeaderBoardWidget.Data
        def __init__(self, widget_commons: _Optional[_Union[_widget_commons_pb2.WidgetCommons, _Mapping]] = ..., data: _Optional[_Union[QuizLeaderBoardWidget.LeaderBoardWidget.Data, _Mapping]] = ...) -> None: ...
    class LeaderBoardReminder(_message.Message):
        __slots__ = ("nudge_reminder", "prize_reminder")
        NUDGE_REMINDER_FIELD_NUMBER: _ClassVar[int]
        PRIZE_REMINDER_FIELD_NUMBER: _ClassVar[int]
        nudge_reminder: QuizLeaderBoardWidget.LeaderBoardNudge
        prize_reminder: _title_icon_combo_pb2.TitleIconCombo
        def __init__(self, nudge_reminder: _Optional[_Union[QuizLeaderBoardWidget.LeaderBoardNudge, _Mapping]] = ..., prize_reminder: _Optional[_Union[_title_icon_combo_pb2.TitleIconCombo, _Mapping]] = ...) -> None: ...
    class LeaderBoardPrizeReminder(_message.Message):
        __slots__ = ("normal_banner", "clicked_banner", "claim_domain_url")
        NORMAL_BANNER_FIELD_NUMBER: _ClassVar[int]
        CLICKED_BANNER_FIELD_NUMBER: _ClassVar[int]
        CLAIM_DOMAIN_URL_FIELD_NUMBER: _ClassVar[int]
        normal_banner: _lottie_banner_pb2.LottieBannerWidget
        clicked_banner: _lottie_banner_pb2.LottieBannerWidget
        claim_domain_url: str
        def __init__(self, normal_banner: _Optional[_Union[_lottie_banner_pb2.LottieBannerWidget, _Mapping]] = ..., clicked_banner: _Optional[_Union[_lottie_banner_pb2.LottieBannerWidget, _Mapping]] = ..., claim_domain_url: _Optional[str] = ...) -> None: ...
    class LeaderBoardNudge(_message.Message):
        __slots__ = ("title", "subtitle", "nudge")
        TITLE_FIELD_NUMBER: _ClassVar[int]
        SUBTITLE_FIELD_NUMBER: _ClassVar[int]
        NUDGE_FIELD_NUMBER: _ClassVar[int]
        title: str
        subtitle: str
        nudge: QuizLeaderBoardWidget.NudgeCTA
        def __init__(self, title: _Optional[str] = ..., subtitle: _Optional[str] = ..., nudge: _Optional[_Union[QuizLeaderBoardWidget.NudgeCTA, _Mapping]] = ...) -> None: ...
    class NudgeCTA(_message.Message):
        __slots__ = ("title", "action")
        TITLE_FIELD_NUMBER: _ClassVar[int]
        ACTION_FIELD_NUMBER: _ClassVar[int]
        title: str
        action: _actions_pb2.Actions
        def __init__(self, title: _Optional[str] = ..., action: _Optional[_Union[_actions_pb2.Actions, _Mapping]] = ...) -> None: ...
    class LeaderBoardHeader(_message.Message):
        __slots__ = ("rank_title", "prize_title", "points")
        RANK_TITLE_FIELD_NUMBER: _ClassVar[int]
        PRIZE_TITLE_FIELD_NUMBER: _ClassVar[int]
        POINTS_FIELD_NUMBER: _ClassVar[int]
        rank_title: str
        prize_title: str
        points: QuizLeaderBoardWidget.LeaderBoardPointsColumn
        def __init__(self, rank_title: _Optional[str] = ..., prize_title: _Optional[str] = ..., points: _Optional[_Union[QuizLeaderBoardWidget.LeaderBoardPointsColumn, _Mapping]] = ...) -> None: ...
    class LeaderBoardPointsColumn(_message.Message):
        __slots__ = ("points_title", "points_bonus")
        POINTS_TITLE_FIELD_NUMBER: _ClassVar[int]
        POINTS_BONUS_FIELD_NUMBER: _ClassVar[int]
        points_title: str
        points_bonus: _title_icon_combo_pb2.TitleIconCombo
        def __init__(self, points_title: _Optional[str] = ..., points_bonus: _Optional[_Union[_title_icon_combo_pb2.TitleIconCombo, _Mapping]] = ...) -> None: ...
    class LeaderBoardRow(_message.Message):
        __slots__ = ("rank", "prize", "points", "is_current_user", "actions")
        RANK_FIELD_NUMBER: _ClassVar[int]
        PRIZE_FIELD_NUMBER: _ClassVar[int]
        POINTS_FIELD_NUMBER: _ClassVar[int]
        IS_CURRENT_USER_FIELD_NUMBER: _ClassVar[int]
        ACTIONS_FIELD_NUMBER: _ClassVar[int]
        rank: str
        prize: _title_icon_combo_pb2.TitleIconCombo
        points: str
        is_current_user: bool
        actions: _actions_pb2.Actions
        def __init__(self, rank: _Optional[str] = ..., prize: _Optional[_Union[_title_icon_combo_pb2.TitleIconCombo, _Mapping]] = ..., points: _Optional[str] = ..., is_current_user: bool = ..., actions: _Optional[_Union[_actions_pb2.Actions, _Mapping]] = ...) -> None: ...
    WIDGET_COMMONS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    widget_commons: _widget_commons_pb2.WidgetCommons
    data: QuizLeaderBoardWidget.Data
    def __init__(self, widget_commons: _Optional[_Union[_widget_commons_pb2.WidgetCommons, _Mapping]] = ..., data: _Optional[_Union[QuizLeaderBoardWidget.Data, _Mapping]] = ...) -> None: ...
