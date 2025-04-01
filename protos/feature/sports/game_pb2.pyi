from feature.image import image_pb2 as _image_pb2
from feature.sports import game_media_info_pb2 as _game_media_info_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GameState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    UNKNOWN: _ClassVar[GameState]
    NOT_START: _ClassVar[GameState]
    LIVE: _ClassVar[GameState]
    FINISHED: _ClassVar[GameState]
UNKNOWN: GameState
NOT_START: GameState
LIVE: GameState
FINISHED: GameState

class Game(_message.Message):
    __slots__ = ("name", "state", "meta_desc", "media_info")
    NAME_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    META_DESC_FIELD_NUMBER: _ClassVar[int]
    MEDIA_INFO_FIELD_NUMBER: _ClassVar[int]
    name: str
    state: GameState
    meta_desc: str
    media_info: _game_media_info_pb2.GameMediaInfo
    def __init__(self, name: _Optional[str] = ..., state: _Optional[_Union[GameState, str]] = ..., meta_desc: _Optional[str] = ..., media_info: _Optional[_Union[_game_media_info_pb2.GameMediaInfo, _Mapping]] = ...) -> None: ...
