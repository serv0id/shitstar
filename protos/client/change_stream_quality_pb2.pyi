from client.player.model import playback_mode_info_pb2 as _playback_mode_info_pb2
from client.player.model import playback_state_info_pb2 as _playback_state_info_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ChangeStreamQuality(_message.Message):
    __slots__ = ("previous_stream_quality", "new_stream_quality", "player_orientation", "player_version")
    PREVIOUS_STREAM_QUALITY_FIELD_NUMBER: _ClassVar[int]
    NEW_STREAM_QUALITY_FIELD_NUMBER: _ClassVar[int]
    PLAYER_ORIENTATION_FIELD_NUMBER: _ClassVar[int]
    PLAYER_VERSION_FIELD_NUMBER: _ClassVar[int]
    previous_stream_quality: _playback_state_info_pb2.VideoQuality
    new_stream_quality: _playback_state_info_pb2.VideoQuality
    player_orientation: _playback_mode_info_pb2.PlayerOrientation
    player_version: str
    def __init__(self, previous_stream_quality: _Optional[_Union[_playback_state_info_pb2.VideoQuality, str]] = ..., new_stream_quality: _Optional[_Union[_playback_state_info_pb2.VideoQuality, str]] = ..., player_orientation: _Optional[_Union[_playback_mode_info_pb2.PlayerOrientation, str]] = ..., player_version: _Optional[str] = ...) -> None: ...
