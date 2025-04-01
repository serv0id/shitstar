from base import actions_pb2 as _actions_pb2
from base import widget_commons_pb2 as _widget_commons_pb2
from feature.commons import widget_wrapper_pb2 as _widget_wrapper_pb2
from widget import sports_cricket_summary_card_pb2 as _sports_cricket_summary_card_pb2
from widget import voting_button_pb2 as _voting_button_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PlayerActionBarWidget(_message.Message):
    __slots__ = ("widget_commons", "data")
    class CollapseMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NONE: _ClassVar[PlayerActionBarWidget.CollapseMode]
        LANDSCAPE: _ClassVar[PlayerActionBarWidget.CollapseMode]
        PORTRAIT_LANDSCAPE: _ClassVar[PlayerActionBarWidget.CollapseMode]
    NONE: PlayerActionBarWidget.CollapseMode
    LANDSCAPE: PlayerActionBarWidget.CollapseMode
    PORTRAIT_LANDSCAPE: PlayerActionBarWidget.CollapseMode
    class WidgetComponent(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[PlayerActionBarWidget.WidgetComponent]
        TITLE: _ClassVar[PlayerActionBarWidget.WidgetComponent]
        SUB_TITLE: _ClassVar[PlayerActionBarWidget.WidgetComponent]
        AUXILIARY_ACTION: _ClassVar[PlayerActionBarWidget.WidgetComponent]
        AUXILIARY_WIDGET: _ClassVar[PlayerActionBarWidget.WidgetComponent]
    UNSPECIFIED: PlayerActionBarWidget.WidgetComponent
    TITLE: PlayerActionBarWidget.WidgetComponent
    SUB_TITLE: PlayerActionBarWidget.WidgetComponent
    AUXILIARY_ACTION: PlayerActionBarWidget.WidgetComponent
    AUXILIARY_WIDGET: PlayerActionBarWidget.WidgetComponent
    class Data(_message.Message):
        __slots__ = ("title", "subtitle", "auxiliary_action", "auxiliary_widget", "subtitle_tags", "show_cta_in_landscape", "collapseMode", "visible_on_collapse", "top_accessory_widget")
        TITLE_FIELD_NUMBER: _ClassVar[int]
        SUBTITLE_FIELD_NUMBER: _ClassVar[int]
        AUXILIARY_ACTION_FIELD_NUMBER: _ClassVar[int]
        AUXILIARY_WIDGET_FIELD_NUMBER: _ClassVar[int]
        SUBTITLE_TAGS_FIELD_NUMBER: _ClassVar[int]
        SHOW_CTA_IN_LANDSCAPE_FIELD_NUMBER: _ClassVar[int]
        COLLAPSEMODE_FIELD_NUMBER: _ClassVar[int]
        VISIBLE_ON_COLLAPSE_FIELD_NUMBER: _ClassVar[int]
        TOP_ACCESSORY_WIDGET_FIELD_NUMBER: _ClassVar[int]
        title: str
        subtitle: str
        auxiliary_action: PlayerActionBarWidget.AuxiliaryAction
        auxiliary_widget: PlayerActionBarWidget.AuxiliaryWidget
        subtitle_tags: _containers.RepeatedScalarFieldContainer[str]
        show_cta_in_landscape: bool
        collapseMode: PlayerActionBarWidget.CollapseMode
        visible_on_collapse: PlayerActionBarWidget.WidgetComponent
        top_accessory_widget: PlayerActionBarWidget.TopAccessoryWidget
        def __init__(self, title: _Optional[str] = ..., subtitle: _Optional[str] = ..., auxiliary_action: _Optional[_Union[PlayerActionBarWidget.AuxiliaryAction, _Mapping]] = ..., auxiliary_widget: _Optional[_Union[PlayerActionBarWidget.AuxiliaryWidget, _Mapping]] = ..., subtitle_tags: _Optional[_Iterable[str]] = ..., show_cta_in_landscape: bool = ..., collapseMode: _Optional[_Union[PlayerActionBarWidget.CollapseMode, str]] = ..., visible_on_collapse: _Optional[_Union[PlayerActionBarWidget.WidgetComponent, str]] = ..., top_accessory_widget: _Optional[_Union[PlayerActionBarWidget.TopAccessoryWidget, _Mapping]] = ...) -> None: ...
    class TopAccessoryWidget(_message.Message):
        __slots__ = ("widget_wrapper", "widget_url")
        WIDGET_WRAPPER_FIELD_NUMBER: _ClassVar[int]
        WIDGET_URL_FIELD_NUMBER: _ClassVar[int]
        widget_wrapper: _widget_wrapper_pb2.WidgetWrapper
        widget_url: str
        def __init__(self, widget_wrapper: _Optional[_Union[_widget_wrapper_pb2.WidgetWrapper, _Mapping]] = ..., widget_url: _Optional[str] = ...) -> None: ...
    class AuxiliaryAction(_message.Message):
        __slots__ = ("subscribe", "vote", "video_switch", "vlc_toggle")
        SUBSCRIBE_FIELD_NUMBER: _ClassVar[int]
        VOTE_FIELD_NUMBER: _ClassVar[int]
        VIDEO_SWITCH_FIELD_NUMBER: _ClassVar[int]
        VLC_TOGGLE_FIELD_NUMBER: _ClassVar[int]
        subscribe: PlayerActionBarWidget.ConfigurableAction
        vote: PlayerActionBarWidget.ConfigurableAction
        video_switch: PlayerActionBarWidget.VideoSwitchAction
        vlc_toggle: PlayerActionBarWidget.ConfigurableAction
        def __init__(self, subscribe: _Optional[_Union[PlayerActionBarWidget.ConfigurableAction, _Mapping]] = ..., vote: _Optional[_Union[PlayerActionBarWidget.ConfigurableAction, _Mapping]] = ..., video_switch: _Optional[_Union[PlayerActionBarWidget.VideoSwitchAction, _Mapping]] = ..., vlc_toggle: _Optional[_Union[PlayerActionBarWidget.ConfigurableAction, _Mapping]] = ...) -> None: ...
    class ConfigurableAction(_message.Message):
        __slots__ = ("icon", "cta", "actions")
        ICON_FIELD_NUMBER: _ClassVar[int]
        CTA_FIELD_NUMBER: _ClassVar[int]
        ACTIONS_FIELD_NUMBER: _ClassVar[int]
        icon: str
        cta: str
        actions: _actions_pb2.Actions
        def __init__(self, icon: _Optional[str] = ..., cta: _Optional[str] = ..., actions: _Optional[_Union[_actions_pb2.Actions, _Mapping]] = ...) -> None: ...
    class VideoSwitchAction(_message.Message):
        __slots__ = ("label", "is_on")
        LABEL_FIELD_NUMBER: _ClassVar[int]
        IS_ON_FIELD_NUMBER: _ClassVar[int]
        label: str
        is_on: bool
        def __init__(self, label: _Optional[str] = ..., is_on: bool = ...) -> None: ...
    class AuxiliaryWidget(_message.Message):
        __slots__ = ("summary_card", "voting_button")
        SUMMARY_CARD_FIELD_NUMBER: _ClassVar[int]
        VOTING_BUTTON_FIELD_NUMBER: _ClassVar[int]
        summary_card: _sports_cricket_summary_card_pb2.CricketPollingSummaryCardWidget
        voting_button: _voting_button_pb2.VotingButtonWidget
        def __init__(self, summary_card: _Optional[_Union[_sports_cricket_summary_card_pb2.CricketPollingSummaryCardWidget, _Mapping]] = ..., voting_button: _Optional[_Union[_voting_button_pb2.VotingButtonWidget, _Mapping]] = ...) -> None: ...
    WIDGET_COMMONS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    widget_commons: _widget_commons_pb2.WidgetCommons
    data: PlayerActionBarWidget.Data
    def __init__(self, widget_commons: _Optional[_Union[_widget_commons_pb2.WidgetCommons, _Mapping]] = ..., data: _Optional[_Union[PlayerActionBarWidget.Data, _Mapping]] = ...) -> None: ...
