from client.player.model import playback_mode_info_pb2 as _playback_mode_info_pb2
from client.player.model import stream_mode_pb2 as _stream_mode_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class WatchTabViewed(_message.Message):
    __slots__ = ("event_name", "event_type", "tab_name", "loaded_by_default", "previous_tab", "stream_state", "player_orientation", "mode")
    EVENT_NAME_FIELD_NUMBER: _ClassVar[int]
    EVENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    TAB_NAME_FIELD_NUMBER: _ClassVar[int]
    LOADED_BY_DEFAULT_FIELD_NUMBER: _ClassVar[int]
    PREVIOUS_TAB_FIELD_NUMBER: _ClassVar[int]
    STREAM_STATE_FIELD_NUMBER: _ClassVar[int]
    PLAYER_ORIENTATION_FIELD_NUMBER: _ClassVar[int]
    MODE_FIELD_NUMBER: _ClassVar[int]
    event_name: str
    event_type: str
    tab_name: str
    loaded_by_default: bool
    previous_tab: str
    stream_state: str
    player_orientation: _playback_mode_info_pb2.PlayerOrientation
    mode: _stream_mode_pb2.StreamMode
    def __init__(self, event_name: _Optional[str] = ..., event_type: _Optional[str] = ..., tab_name: _Optional[str] = ..., loaded_by_default: bool = ..., previous_tab: _Optional[str] = ..., stream_state: _Optional[str] = ..., player_orientation: _Optional[_Union[_playback_mode_info_pb2.PlayerOrientation, str]] = ..., mode: _Optional[_Union[_stream_mode_pb2.StreamMode, str]] = ...) -> None: ...
