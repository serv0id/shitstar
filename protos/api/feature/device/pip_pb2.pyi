from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PlayerType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PLAYER_TYPE_UNSPECIFIED: _ClassVar[PlayerType]
    PLAYER_TYPE_IN_APP_PIP: _ClassVar[PlayerType]
    PLAYER_TYPE_NORMAL: _ClassVar[PlayerType]
    PLAYER_TYPE_NOT_ACTIVE: _ClassVar[PlayerType]

class PlayerStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PLAYER_STATUS_UNSPECIFIED: _ClassVar[PlayerStatus]
    PLAYER_STATUS_STREAMING: _ClassVar[PlayerStatus]
    PLAYER_STATUS_PAUSED: _ClassVar[PlayerStatus]
    PLAYER_STATUS_LOADING: _ClassVar[PlayerStatus]
PLAYER_TYPE_UNSPECIFIED: PlayerType
PLAYER_TYPE_IN_APP_PIP: PlayerType
PLAYER_TYPE_NORMAL: PlayerType
PLAYER_TYPE_NOT_ACTIVE: PlayerType
PLAYER_STATUS_UNSPECIFIED: PlayerStatus
PLAYER_STATUS_STREAMING: PlayerStatus
PLAYER_STATUS_PAUSED: PlayerStatus
PLAYER_STATUS_LOADING: PlayerStatus

class PipInfo(_message.Message):
    __slots__ = ("player_type", "player_status")
    PLAYER_TYPE_FIELD_NUMBER: _ClassVar[int]
    PLAYER_STATUS_FIELD_NUMBER: _ClassVar[int]
    player_type: PlayerType
    player_status: PlayerStatus
    def __init__(self, player_type: _Optional[_Union[PlayerType, str]] = ..., player_status: _Optional[_Union[PlayerStatus, str]] = ...) -> None: ...

class PipInfoV2(_message.Message):
    __slots__ = ("player_type_v2", "player_status_v2")
    PLAYER_TYPE_V2_FIELD_NUMBER: _ClassVar[int]
    PLAYER_STATUS_V2_FIELD_NUMBER: _ClassVar[int]
    player_type_v2: PlayerType
    player_status_v2: PlayerStatus
    def __init__(self, player_type_v2: _Optional[_Union[PlayerType, str]] = ..., player_status_v2: _Optional[_Union[PlayerStatus, str]] = ...) -> None: ...
