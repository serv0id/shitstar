from client.player.model import playback_mode_info_pb2 as _playback_mode_info_pb2
from client.player.model import stream_mode_pb2 as _stream_mode_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MaxviewModeSwitcherTrigger(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    MAXVIEW_MODE_SWITCHER_TRIGGER_UNSPECIFIED: _ClassVar[MaxviewModeSwitcherTrigger]
    MAXVIEW_MODE_SWITCHER_TRIGGER_TOGGLE_CTA: _ClassVar[MaxviewModeSwitcherTrigger]
    MAXVIEW_MODE_SWITCHER_TRIGGER_HORIZONTAL_EXPAND: _ClassVar[MaxviewModeSwitcherTrigger]
MAXVIEW_MODE_SWITCHER_TRIGGER_UNSPECIFIED: MaxviewModeSwitcherTrigger
MAXVIEW_MODE_SWITCHER_TRIGGER_TOGGLE_CTA: MaxviewModeSwitcherTrigger
MAXVIEW_MODE_SWITCHER_TRIGGER_HORIZONTAL_EXPAND: MaxviewModeSwitcherTrigger

class ClickedMaxviewModeSwitcherProperties(_message.Message):
    __slots__ = ("mode", "player_orientation", "stream_state", "trigger")
    MODE_FIELD_NUMBER: _ClassVar[int]
    PLAYER_ORIENTATION_FIELD_NUMBER: _ClassVar[int]
    STREAM_STATE_FIELD_NUMBER: _ClassVar[int]
    TRIGGER_FIELD_NUMBER: _ClassVar[int]
    mode: _stream_mode_pb2.StreamMode
    player_orientation: _playback_mode_info_pb2.PlayerOrientation
    stream_state: str
    trigger: MaxviewModeSwitcherTrigger
    def __init__(self, mode: _Optional[_Union[_stream_mode_pb2.StreamMode, str]] = ..., player_orientation: _Optional[_Union[_playback_mode_info_pb2.PlayerOrientation, str]] = ..., stream_state: _Optional[str] = ..., trigger: _Optional[_Union[MaxviewModeSwitcherTrigger, str]] = ...) -> None: ...
