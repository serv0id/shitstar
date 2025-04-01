from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class PlayerManagerProperties(_message.Message):
    __slots__ = ("create_player_time_ms", "get_player_time_ms", "destroy_player_time_ms", "wait_destroy_player_time_ms", "wait_destroy_time_ms")
    CREATE_PLAYER_TIME_MS_FIELD_NUMBER: _ClassVar[int]
    GET_PLAYER_TIME_MS_FIELD_NUMBER: _ClassVar[int]
    DESTROY_PLAYER_TIME_MS_FIELD_NUMBER: _ClassVar[int]
    WAIT_DESTROY_PLAYER_TIME_MS_FIELD_NUMBER: _ClassVar[int]
    WAIT_DESTROY_TIME_MS_FIELD_NUMBER: _ClassVar[int]
    create_player_time_ms: int
    get_player_time_ms: int
    destroy_player_time_ms: int
    wait_destroy_player_time_ms: bool
    wait_destroy_time_ms: int
    def __init__(self, create_player_time_ms: _Optional[int] = ..., get_player_time_ms: _Optional[int] = ..., destroy_player_time_ms: _Optional[int] = ..., wait_destroy_player_time_ms: bool = ..., wait_destroy_time_ms: _Optional[int] = ...) -> None: ...
