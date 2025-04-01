from base import widget_commons_pb2 as _widget_commons_pb2
from base import actions_pb2 as _actions_pb2
from feature.voting import voting_button_config_pb2 as _voting_button_config_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class VotingButtonWidget(_message.Message):
    __slots__ = ("widget_commons", "voting_button_config", "actions")
    WIDGET_COMMONS_FIELD_NUMBER: _ClassVar[int]
    VOTING_BUTTON_CONFIG_FIELD_NUMBER: _ClassVar[int]
    ACTIONS_FIELD_NUMBER: _ClassVar[int]
    widget_commons: _widget_commons_pb2.WidgetCommons
    voting_button_config: _voting_button_config_pb2.VotingButtonConfig
    actions: _actions_pb2.Actions
    def __init__(self, widget_commons: _Optional[_Union[_widget_commons_pb2.WidgetCommons, _Mapping]] = ..., voting_button_config: _Optional[_Union[_voting_button_config_pb2.VotingButtonConfig, _Mapping]] = ..., actions: _Optional[_Union[_actions_pb2.Actions, _Mapping]] = ...) -> None: ...
