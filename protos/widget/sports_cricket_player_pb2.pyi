from base import widget_commons_pb2 as _widget_commons_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CricketPlayer(_message.Message):
    __slots__ = ("name", "short_desc", "detail_desc", "play_state", "play_state_desc")
    class PlayState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNKNOWN: _ClassVar[CricketPlayer.PlayState]
        YET_TO_BAT: _ClassVar[CricketPlayer.PlayState]
        NOT_OUT: _ClassVar[CricketPlayer.PlayState]
        OUT: _ClassVar[CricketPlayer.PlayState]
    UNKNOWN: CricketPlayer.PlayState
    YET_TO_BAT: CricketPlayer.PlayState
    NOT_OUT: CricketPlayer.PlayState
    OUT: CricketPlayer.PlayState
    NAME_FIELD_NUMBER: _ClassVar[int]
    SHORT_DESC_FIELD_NUMBER: _ClassVar[int]
    DETAIL_DESC_FIELD_NUMBER: _ClassVar[int]
    PLAY_STATE_FIELD_NUMBER: _ClassVar[int]
    PLAY_STATE_DESC_FIELD_NUMBER: _ClassVar[int]
    name: str
    short_desc: str
    detail_desc: str
    play_state: CricketPlayer.PlayState
    play_state_desc: str
    def __init__(self, name: _Optional[str] = ..., short_desc: _Optional[str] = ..., detail_desc: _Optional[str] = ..., play_state: _Optional[_Union[CricketPlayer.PlayState, str]] = ..., play_state_desc: _Optional[str] = ...) -> None: ...
