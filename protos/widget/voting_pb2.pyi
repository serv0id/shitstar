from base import widget_commons_pb2 as _widget_commons_pb2
from base import actions_pb2 as _actions_pb2
from feature.image import image_pb2 as _image_pb2
from feature.voting import voting_button_config_pb2 as _voting_button_config_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class VotingWidget(_message.Message):
    __slots__ = ("widget_commons", "data")
    class Data(_message.Message):
        __slots__ = ("banner_title", "pre_state_title", "active_state_title", "post_state_title", "event_time_elapsed_title", "submit_screen_title", "submit_button_title", "voting_lines", "sponsor_title", "sponsor_litems", "voting_button_config")
        BANNER_TITLE_FIELD_NUMBER: _ClassVar[int]
        PRE_STATE_TITLE_FIELD_NUMBER: _ClassVar[int]
        ACTIVE_STATE_TITLE_FIELD_NUMBER: _ClassVar[int]
        POST_STATE_TITLE_FIELD_NUMBER: _ClassVar[int]
        EVENT_TIME_ELAPSED_TITLE_FIELD_NUMBER: _ClassVar[int]
        SUBMIT_SCREEN_TITLE_FIELD_NUMBER: _ClassVar[int]
        SUBMIT_BUTTON_TITLE_FIELD_NUMBER: _ClassVar[int]
        VOTING_LINES_FIELD_NUMBER: _ClassVar[int]
        SPONSOR_TITLE_FIELD_NUMBER: _ClassVar[int]
        SPONSOR_LITEMS_FIELD_NUMBER: _ClassVar[int]
        VOTING_BUTTON_CONFIG_FIELD_NUMBER: _ClassVar[int]
        banner_title: VotingWidget.Title
        pre_state_title: VotingWidget.Title
        active_state_title: VotingWidget.Title
        post_state_title: VotingWidget.Title
        event_time_elapsed_title: VotingWidget.Title
        submit_screen_title: VotingWidget.Title
        submit_button_title: str
        voting_lines: _containers.RepeatedCompositeFieldContainer[VotingWidget.VotingLine]
        sponsor_title: str
        sponsor_litems: _containers.RepeatedCompositeFieldContainer[VotingWidget.SponsorItem]
        voting_button_config: _voting_button_config_pb2.VotingButtonConfig
        def __init__(self, banner_title: _Optional[_Union[VotingWidget.Title, _Mapping]] = ..., pre_state_title: _Optional[_Union[VotingWidget.Title, _Mapping]] = ..., active_state_title: _Optional[_Union[VotingWidget.Title, _Mapping]] = ..., post_state_title: _Optional[_Union[VotingWidget.Title, _Mapping]] = ..., event_time_elapsed_title: _Optional[_Union[VotingWidget.Title, _Mapping]] = ..., submit_screen_title: _Optional[_Union[VotingWidget.Title, _Mapping]] = ..., submit_button_title: _Optional[str] = ..., voting_lines: _Optional[_Iterable[_Union[VotingWidget.VotingLine, _Mapping]]] = ..., sponsor_title: _Optional[str] = ..., sponsor_litems: _Optional[_Iterable[_Union[VotingWidget.SponsorItem, _Mapping]]] = ..., voting_button_config: _Optional[_Union[_voting_button_config_pb2.VotingButtonConfig, _Mapping]] = ...) -> None: ...
    class VotingLine(_message.Message):
        __slots__ = ("voting_id", "voting_options", "voting_submit_url", "max_selectable_option", "max_vote_per_option")
        VOTING_ID_FIELD_NUMBER: _ClassVar[int]
        VOTING_OPTIONS_FIELD_NUMBER: _ClassVar[int]
        VOTING_SUBMIT_URL_FIELD_NUMBER: _ClassVar[int]
        MAX_SELECTABLE_OPTION_FIELD_NUMBER: _ClassVar[int]
        MAX_VOTE_PER_OPTION_FIELD_NUMBER: _ClassVar[int]
        voting_id: str
        voting_options: _containers.RepeatedCompositeFieldContainer[VotingWidget.VotingOption]
        voting_submit_url: str
        max_selectable_option: int
        max_vote_per_option: int
        def __init__(self, voting_id: _Optional[str] = ..., voting_options: _Optional[_Iterable[_Union[VotingWidget.VotingOption, _Mapping]]] = ..., voting_submit_url: _Optional[str] = ..., max_selectable_option: _Optional[int] = ..., max_vote_per_option: _Optional[int] = ...) -> None: ...
    class VotingOption(_message.Message):
        __slots__ = ("profile_photo", "name", "id")
        PROFILE_PHOTO_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        ID_FIELD_NUMBER: _ClassVar[int]
        profile_photo: _image_pb2.Image
        name: str
        id: str
        def __init__(self, profile_photo: _Optional[_Union[_image_pb2.Image, _Mapping]] = ..., name: _Optional[str] = ..., id: _Optional[str] = ...) -> None: ...
    class SponsorItem(_message.Message):
        __slots__ = ("sponsor_logo", "sponsor_link", "actions")
        SPONSOR_LOGO_FIELD_NUMBER: _ClassVar[int]
        SPONSOR_LINK_FIELD_NUMBER: _ClassVar[int]
        ACTIONS_FIELD_NUMBER: _ClassVar[int]
        sponsor_logo: _image_pb2.Image
        sponsor_link: str
        actions: _actions_pb2.Actions
        def __init__(self, sponsor_logo: _Optional[_Union[_image_pb2.Image, _Mapping]] = ..., sponsor_link: _Optional[str] = ..., actions: _Optional[_Union[_actions_pb2.Actions, _Mapping]] = ...) -> None: ...
    class Title(_message.Message):
        __slots__ = ("title", "sub_title", "plural_title")
        TITLE_FIELD_NUMBER: _ClassVar[int]
        SUB_TITLE_FIELD_NUMBER: _ClassVar[int]
        PLURAL_TITLE_FIELD_NUMBER: _ClassVar[int]
        title: str
        sub_title: str
        plural_title: str
        def __init__(self, title: _Optional[str] = ..., sub_title: _Optional[str] = ..., plural_title: _Optional[str] = ...) -> None: ...
    WIDGET_COMMONS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    widget_commons: _widget_commons_pb2.WidgetCommons
    data: VotingWidget.Data
    def __init__(self, widget_commons: _Optional[_Union[_widget_commons_pb2.WidgetCommons, _Mapping]] = ..., data: _Optional[_Union[VotingWidget.Data, _Mapping]] = ...) -> None: ...
