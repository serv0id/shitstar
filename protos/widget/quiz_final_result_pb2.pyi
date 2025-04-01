from base import widget_commons_pb2 as _widget_commons_pb2
from base import actions_pb2 as _actions_pb2
from feature.image import lottie_pb2 as _lottie_pb2
from feature.quiz import title_icon_combo_pb2 as _title_icon_combo_pb2
from feature.quiz import title_pb2 as _title_pb2
from feature.quiz import streak_vector_pb2 as _streak_vector_pb2
from widget import hero_pb2 as _hero_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class QuizFinalResultWidget(_message.Message):
    __slots__ = ("widget_commons", "data")
    class Data(_message.Message):
        __slots__ = ("score", "win_title", "win_points", "bonus", "streak", "share_cta", "view_prizes_winners", "background_color_hex", "share_brand_date", "share_bonus_request_url", "show_happy_lottie", "weekly_points", "season_points", "streak_vector", "show_season_points", "transition_season_duration_in_ms", "enable_streak_layout")
        SCORE_FIELD_NUMBER: _ClassVar[int]
        WIN_TITLE_FIELD_NUMBER: _ClassVar[int]
        WIN_POINTS_FIELD_NUMBER: _ClassVar[int]
        BONUS_FIELD_NUMBER: _ClassVar[int]
        STREAK_FIELD_NUMBER: _ClassVar[int]
        SHARE_CTA_FIELD_NUMBER: _ClassVar[int]
        VIEW_PRIZES_WINNERS_FIELD_NUMBER: _ClassVar[int]
        BACKGROUND_COLOR_HEX_FIELD_NUMBER: _ClassVar[int]
        SHARE_BRAND_DATE_FIELD_NUMBER: _ClassVar[int]
        SHARE_BONUS_REQUEST_URL_FIELD_NUMBER: _ClassVar[int]
        SHOW_HAPPY_LOTTIE_FIELD_NUMBER: _ClassVar[int]
        WEEKLY_POINTS_FIELD_NUMBER: _ClassVar[int]
        SEASON_POINTS_FIELD_NUMBER: _ClassVar[int]
        STREAK_VECTOR_FIELD_NUMBER: _ClassVar[int]
        SHOW_SEASON_POINTS_FIELD_NUMBER: _ClassVar[int]
        TRANSITION_SEASON_DURATION_IN_MS_FIELD_NUMBER: _ClassVar[int]
        ENABLE_STREAK_LAYOUT_FIELD_NUMBER: _ClassVar[int]
        score: _hero_pb2.HeroWidget
        win_title: str
        win_points: _title_pb2.Title
        bonus: _title_icon_combo_pb2.TitleIconCombo
        streak: _title_icon_combo_pb2.TitleIconCombo
        share_cta: QuizFinalResultWidget.ShareCTA
        view_prizes_winners: QuizFinalResultWidget.TextCtaWidget
        background_color_hex: str
        share_brand_date: _title_icon_combo_pb2.TitleIconCombo
        share_bonus_request_url: str
        show_happy_lottie: bool
        weekly_points: QuizFinalResultWidget.Points
        season_points: QuizFinalResultWidget.Points
        streak_vector: _streak_vector_pb2.StreakVector
        show_season_points: bool
        transition_season_duration_in_ms: int
        enable_streak_layout: bool
        def __init__(self, score: _Optional[_Union[_hero_pb2.HeroWidget, _Mapping]] = ..., win_title: _Optional[str] = ..., win_points: _Optional[_Union[_title_pb2.Title, _Mapping]] = ..., bonus: _Optional[_Union[_title_icon_combo_pb2.TitleIconCombo, _Mapping]] = ..., streak: _Optional[_Union[_title_icon_combo_pb2.TitleIconCombo, _Mapping]] = ..., share_cta: _Optional[_Union[QuizFinalResultWidget.ShareCTA, _Mapping]] = ..., view_prizes_winners: _Optional[_Union[QuizFinalResultWidget.TextCtaWidget, _Mapping]] = ..., background_color_hex: _Optional[str] = ..., share_brand_date: _Optional[_Union[_title_icon_combo_pb2.TitleIconCombo, _Mapping]] = ..., share_bonus_request_url: _Optional[str] = ..., show_happy_lottie: bool = ..., weekly_points: _Optional[_Union[QuizFinalResultWidget.Points, _Mapping]] = ..., season_points: _Optional[_Union[QuizFinalResultWidget.Points, _Mapping]] = ..., streak_vector: _Optional[_Union[_streak_vector_pb2.StreakVector, _Mapping]] = ..., show_season_points: bool = ..., transition_season_duration_in_ms: _Optional[int] = ..., enable_streak_layout: bool = ...) -> None: ...
    class ShareCTA(_message.Message):
        __slots__ = ("title", "subtitle", "action")
        TITLE_FIELD_NUMBER: _ClassVar[int]
        SUBTITLE_FIELD_NUMBER: _ClassVar[int]
        ACTION_FIELD_NUMBER: _ClassVar[int]
        title: str
        subtitle: str
        action: _actions_pb2.Actions
        def __init__(self, title: _Optional[str] = ..., subtitle: _Optional[str] = ..., action: _Optional[_Union[_actions_pb2.Actions, _Mapping]] = ...) -> None: ...
    class TextCtaWidget(_message.Message):
        __slots__ = ("title", "action")
        TITLE_FIELD_NUMBER: _ClassVar[int]
        ACTION_FIELD_NUMBER: _ClassVar[int]
        title: str
        action: _actions_pb2.Actions
        def __init__(self, title: _Optional[str] = ..., action: _Optional[_Union[_actions_pb2.Actions, _Mapping]] = ...) -> None: ...
    class Points(_message.Message):
        __slots__ = ("detail", "points")
        DETAIL_FIELD_NUMBER: _ClassVar[int]
        POINTS_FIELD_NUMBER: _ClassVar[int]
        detail: _hero_pb2.HeroWidget
        points: _title_pb2.Title
        def __init__(self, detail: _Optional[_Union[_hero_pb2.HeroWidget, _Mapping]] = ..., points: _Optional[_Union[_title_pb2.Title, _Mapping]] = ...) -> None: ...
    WIDGET_COMMONS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    widget_commons: _widget_commons_pb2.WidgetCommons
    data: QuizFinalResultWidget.Data
    def __init__(self, widget_commons: _Optional[_Union[_widget_commons_pb2.WidgetCommons, _Mapping]] = ..., data: _Optional[_Union[QuizFinalResultWidget.Data, _Mapping]] = ...) -> None: ...
