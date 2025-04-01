from client.player.model import playback_mode_info_pb2 as _playback_mode_info_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ChangeCaptionSetting(_message.Message):
    __slots__ = ("previous_language", "new_language", "player_orientation", "is_casting", "player_version")
    PREVIOUS_LANGUAGE_FIELD_NUMBER: _ClassVar[int]
    NEW_LANGUAGE_FIELD_NUMBER: _ClassVar[int]
    PLAYER_ORIENTATION_FIELD_NUMBER: _ClassVar[int]
    IS_CASTING_FIELD_NUMBER: _ClassVar[int]
    PLAYER_VERSION_FIELD_NUMBER: _ClassVar[int]
    previous_language: str
    new_language: str
    player_orientation: _playback_mode_info_pb2.PlayerOrientation
    is_casting: bool
    player_version: str
    def __init__(self, previous_language: _Optional[str] = ..., new_language: _Optional[str] = ..., player_orientation: _Optional[_Union[_playback_mode_info_pb2.PlayerOrientation, str]] = ..., is_casting: bool = ..., player_version: _Optional[str] = ...) -> None: ...
