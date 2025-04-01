from base import actions_pb2 as _actions_pb2
from base import widget_commons_pb2 as _widget_commons_pb2
from widget import polling_pb2 as _polling_pb2
from widget import button_stack_pb2 as _button_stack_pb2
from feature.sports import game_pb2 as _game_pb2
from feature.refresh import refresh_info_pb2 as _refresh_info_pb2
from feature.sports import cricket_team_pb2 as _cricket_team_pb2
from feature.remind_me import remind_me_info_pb2 as _remind_me_info_pb2
from feature.accessibility import accessibility_pb2 as _accessibility_pb2
from feature.live import live_info_pb2 as _live_info_pb2
from feature.atom import button_pb2 as _button_pb2
from feature.image import image_pb2 as _image_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MatchCardWidget(_message.Message):
    __slots__ = ("widget_commons", "data")
    class ScoreCardType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNKNOWN: _ClassVar[MatchCardWidget.ScoreCardType]
        SCORES: _ClassVar[MatchCardWidget.ScoreCardType]
        DATE_TIME: _ClassVar[MatchCardWidget.ScoreCardType]
    UNKNOWN: MatchCardWidget.ScoreCardType
    SCORES: MatchCardWidget.ScoreCardType
    DATE_TIME: MatchCardWidget.ScoreCardType
    class Data(_message.Message):
        __slots__ = ("live_info", "team_1", "team_2", "leading_info", "trailing_info", "match_summary", "start_time", "card_type", "is_focused", "ctas", "actions", "alt", "live_score_timestamp")
        LIVE_INFO_FIELD_NUMBER: _ClassVar[int]
        TEAM_1_FIELD_NUMBER: _ClassVar[int]
        TEAM_2_FIELD_NUMBER: _ClassVar[int]
        LEADING_INFO_FIELD_NUMBER: _ClassVar[int]
        TRAILING_INFO_FIELD_NUMBER: _ClassVar[int]
        MATCH_SUMMARY_FIELD_NUMBER: _ClassVar[int]
        START_TIME_FIELD_NUMBER: _ClassVar[int]
        CARD_TYPE_FIELD_NUMBER: _ClassVar[int]
        IS_FOCUSED_FIELD_NUMBER: _ClassVar[int]
        CTAS_FIELD_NUMBER: _ClassVar[int]
        ACTIONS_FIELD_NUMBER: _ClassVar[int]
        ALT_FIELD_NUMBER: _ClassVar[int]
        LIVE_SCORE_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
        live_info: _live_info_pb2.LiveInfo
        team_1: MatchCardWidget.Team
        team_2: MatchCardWidget.Team
        leading_info: str
        trailing_info: str
        match_summary: MatchCardWidget.Callout
        start_time: int
        card_type: MatchCardWidget.ScoreCardType
        is_focused: bool
        ctas: _button_stack_pb2.ButtonStackWidget
        actions: _actions_pb2.Actions
        alt: _accessibility_pb2.Accessibility
        live_score_timestamp: int
        def __init__(self, live_info: _Optional[_Union[_live_info_pb2.LiveInfo, _Mapping]] = ..., team_1: _Optional[_Union[MatchCardWidget.Team, _Mapping]] = ..., team_2: _Optional[_Union[MatchCardWidget.Team, _Mapping]] = ..., leading_info: _Optional[str] = ..., trailing_info: _Optional[str] = ..., match_summary: _Optional[_Union[MatchCardWidget.Callout, _Mapping]] = ..., start_time: _Optional[int] = ..., card_type: _Optional[_Union[MatchCardWidget.ScoreCardType, str]] = ..., is_focused: bool = ..., ctas: _Optional[_Union[_button_stack_pb2.ButtonStackWidget, _Mapping]] = ..., actions: _Optional[_Union[_actions_pb2.Actions, _Mapping]] = ..., alt: _Optional[_Union[_accessibility_pb2.Accessibility, _Mapping]] = ..., live_score_timestamp: _Optional[int] = ...) -> None: ...
    class Team(_message.Message):
        __slots__ = ("image", "name", "score_label", "is_inactive", "id")
        IMAGE_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        SCORE_LABEL_FIELD_NUMBER: _ClassVar[int]
        IS_INACTIVE_FIELD_NUMBER: _ClassVar[int]
        ID_FIELD_NUMBER: _ClassVar[int]
        image: _image_pb2.Image
        name: str
        score_label: str
        is_inactive: bool
        id: str
        def __init__(self, image: _Optional[_Union[_image_pb2.Image, _Mapping]] = ..., name: _Optional[str] = ..., score_label: _Optional[str] = ..., is_inactive: bool = ..., id: _Optional[str] = ...) -> None: ...
    class Callout(_message.Message):
        __slots__ = ("title", "is_highlighted")
        TITLE_FIELD_NUMBER: _ClassVar[int]
        IS_HIGHLIGHTED_FIELD_NUMBER: _ClassVar[int]
        title: str
        is_highlighted: bool
        def __init__(self, title: _Optional[str] = ..., is_highlighted: bool = ...) -> None: ...
    WIDGET_COMMONS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    widget_commons: _widget_commons_pb2.WidgetCommons
    data: MatchCardWidget.Data
    def __init__(self, widget_commons: _Optional[_Union[_widget_commons_pb2.WidgetCommons, _Mapping]] = ..., data: _Optional[_Union[MatchCardWidget.Data, _Mapping]] = ...) -> None: ...
