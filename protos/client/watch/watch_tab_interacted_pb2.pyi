from client.player.model import playback_mode_info_pb2 as _playback_mode_info_pb2
from client.player.model import stream_mode_pb2 as _stream_mode_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class WatchTabInteracted(_message.Message):
    __slots__ = ("event_name", "event_type", "action_type", "previous_state", "current_state", "previous_title", "current_title", "stream_state", "player_orientation", "mode")
    class ActionType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ACTION_TYPE_UNSPECIFIED: _ClassVar[WatchTabInteracted.ActionType]
        ACTION_TYPE_CHANGED_INNINGS: _ClassVar[WatchTabInteracted.ActionType]
        ACTION_TYPE_SCROLL: _ClassVar[WatchTabInteracted.ActionType]
        ACTION_TYPE_UPDATE: _ClassVar[WatchTabInteracted.ActionType]
    ACTION_TYPE_UNSPECIFIED: WatchTabInteracted.ActionType
    ACTION_TYPE_CHANGED_INNINGS: WatchTabInteracted.ActionType
    ACTION_TYPE_SCROLL: WatchTabInteracted.ActionType
    ACTION_TYPE_UPDATE: WatchTabInteracted.ActionType
    EVENT_NAME_FIELD_NUMBER: _ClassVar[int]
    EVENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    ACTION_TYPE_FIELD_NUMBER: _ClassVar[int]
    PREVIOUS_STATE_FIELD_NUMBER: _ClassVar[int]
    CURRENT_STATE_FIELD_NUMBER: _ClassVar[int]
    PREVIOUS_TITLE_FIELD_NUMBER: _ClassVar[int]
    CURRENT_TITLE_FIELD_NUMBER: _ClassVar[int]
    STREAM_STATE_FIELD_NUMBER: _ClassVar[int]
    PLAYER_ORIENTATION_FIELD_NUMBER: _ClassVar[int]
    MODE_FIELD_NUMBER: _ClassVar[int]
    event_name: str
    event_type: str
    action_type: WatchTabInteracted.ActionType
    previous_state: str
    current_state: str
    previous_title: str
    current_title: str
    stream_state: str
    player_orientation: _playback_mode_info_pb2.PlayerOrientation
    mode: _stream_mode_pb2.StreamMode
    def __init__(self, event_name: _Optional[str] = ..., event_type: _Optional[str] = ..., action_type: _Optional[_Union[WatchTabInteracted.ActionType, str]] = ..., previous_state: _Optional[str] = ..., current_state: _Optional[str] = ..., previous_title: _Optional[str] = ..., current_title: _Optional[str] = ..., stream_state: _Optional[str] = ..., player_orientation: _Optional[_Union[_playback_mode_info_pb2.PlayerOrientation, str]] = ..., mode: _Optional[_Union[_stream_mode_pb2.StreamMode, str]] = ...) -> None: ...
