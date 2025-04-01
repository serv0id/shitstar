from base import widget_commons_pb2 as _widget_commons_pb2
from base import actions_pb2 as _actions_pb2
from widget import hero_pb2 as _hero_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class QuizWelcomeWidget(_message.Message):
    __slots__ = ("widget_commons", "data")
    class Data(_message.Message):
        __slots__ = ("quiz_info", "state", "first_launch")
        QUIZ_INFO_FIELD_NUMBER: _ClassVar[int]
        STATE_FIELD_NUMBER: _ClassVar[int]
        FIRST_LAUNCH_FIELD_NUMBER: _ClassVar[int]
        quiz_info: _hero_pb2.HeroWidget
        state: QuizWelcomeWidget.QuizWelcomeState
        first_launch: bool
        def __init__(self, quiz_info: _Optional[_Union[_hero_pb2.HeroWidget, _Mapping]] = ..., state: _Optional[_Union[QuizWelcomeWidget.QuizWelcomeState, _Mapping]] = ..., first_launch: bool = ...) -> None: ...
    class QuizWelcomeState(_message.Message):
        __slots__ = ("play_now", "end")
        PLAY_NOW_FIELD_NUMBER: _ClassVar[int]
        END_FIELD_NUMBER: _ClassVar[int]
        play_now: QuizWelcomeWidget.QuizPlayNowWidget
        end: QuizWelcomeWidget.QuizEndWidget
        def __init__(self, play_now: _Optional[_Union[QuizWelcomeWidget.QuizPlayNowWidget, _Mapping]] = ..., end: _Optional[_Union[QuizWelcomeWidget.QuizEndWidget, _Mapping]] = ...) -> None: ...
    class QuizPlayNowWidget(_message.Message):
        __slots__ = ("widget_commons", "data")
        class Data(_message.Message):
            __slots__ = ("cta", "disclaimer_rich_text")
            class AutoPlayingCTA(_message.Message):
                __slots__ = ("title", "auto_playing_duration_in_seconds", "action")
                TITLE_FIELD_NUMBER: _ClassVar[int]
                AUTO_PLAYING_DURATION_IN_SECONDS_FIELD_NUMBER: _ClassVar[int]
                ACTION_FIELD_NUMBER: _ClassVar[int]
                title: str
                auto_playing_duration_in_seconds: int
                action: _actions_pb2.Actions
                def __init__(self, title: _Optional[str] = ..., auto_playing_duration_in_seconds: _Optional[int] = ..., action: _Optional[_Union[_actions_pb2.Actions, _Mapping]] = ...) -> None: ...
            CTA_FIELD_NUMBER: _ClassVar[int]
            DISCLAIMER_RICH_TEXT_FIELD_NUMBER: _ClassVar[int]
            cta: QuizWelcomeWidget.QuizPlayNowWidget.Data.AutoPlayingCTA
            disclaimer_rich_text: str
            def __init__(self, cta: _Optional[_Union[QuizWelcomeWidget.QuizPlayNowWidget.Data.AutoPlayingCTA, _Mapping]] = ..., disclaimer_rich_text: _Optional[str] = ...) -> None: ...
        WIDGET_COMMONS_FIELD_NUMBER: _ClassVar[int]
        DATA_FIELD_NUMBER: _ClassVar[int]
        widget_commons: _widget_commons_pb2.WidgetCommons
        data: QuizWelcomeWidget.QuizPlayNowWidget.Data
        def __init__(self, widget_commons: _Optional[_Union[_widget_commons_pb2.WidgetCommons, _Mapping]] = ..., data: _Optional[_Union[QuizWelcomeWidget.QuizPlayNowWidget.Data, _Mapping]] = ...) -> None: ...
    class QuizEndWidget(_message.Message):
        __slots__ = ("widget_commons", "data")
        class Data(_message.Message):
            __slots__ = ("reminder",)
            REMINDER_FIELD_NUMBER: _ClassVar[int]
            reminder: str
            def __init__(self, reminder: _Optional[str] = ...) -> None: ...
        WIDGET_COMMONS_FIELD_NUMBER: _ClassVar[int]
        DATA_FIELD_NUMBER: _ClassVar[int]
        widget_commons: _widget_commons_pb2.WidgetCommons
        data: QuizWelcomeWidget.QuizEndWidget.Data
        def __init__(self, widget_commons: _Optional[_Union[_widget_commons_pb2.WidgetCommons, _Mapping]] = ..., data: _Optional[_Union[QuizWelcomeWidget.QuizEndWidget.Data, _Mapping]] = ...) -> None: ...
    WIDGET_COMMONS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    widget_commons: _widget_commons_pb2.WidgetCommons
    data: QuizWelcomeWidget.Data
    def __init__(self, widget_commons: _Optional[_Union[_widget_commons_pb2.WidgetCommons, _Mapping]] = ..., data: _Optional[_Union[QuizWelcomeWidget.Data, _Mapping]] = ...) -> None: ...
