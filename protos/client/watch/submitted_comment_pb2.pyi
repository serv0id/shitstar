from client.player.model import playback_mode_info_pb2 as _playback_mode_info_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SubmittedCommentProperties(_message.Message):
    __slots__ = ("event_name", "comment_id", "comment_type", "comment_text", "comment_length", "comment_lines", "comment_lang", "player_orientation")
    EVENT_NAME_FIELD_NUMBER: _ClassVar[int]
    COMMENT_ID_FIELD_NUMBER: _ClassVar[int]
    COMMENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    COMMENT_TEXT_FIELD_NUMBER: _ClassVar[int]
    COMMENT_LENGTH_FIELD_NUMBER: _ClassVar[int]
    COMMENT_LINES_FIELD_NUMBER: _ClassVar[int]
    COMMENT_LANG_FIELD_NUMBER: _ClassVar[int]
    PLAYER_ORIENTATION_FIELD_NUMBER: _ClassVar[int]
    event_name: str
    comment_id: str
    comment_type: str
    comment_text: str
    comment_length: int
    comment_lines: int
    comment_lang: str
    player_orientation: _playback_mode_info_pb2.PlayerOrientation
    def __init__(self, event_name: _Optional[str] = ..., comment_id: _Optional[str] = ..., comment_type: _Optional[str] = ..., comment_text: _Optional[str] = ..., comment_length: _Optional[int] = ..., comment_lines: _Optional[int] = ..., comment_lang: _Optional[str] = ..., player_orientation: _Optional[_Union[_playback_mode_info_pb2.PlayerOrientation, str]] = ...) -> None: ...
