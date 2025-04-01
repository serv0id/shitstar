from client.player.model import client_capabilities_pb2 as _client_capabilities_pb2
from client.player.model import drm_parameters_pb2 as _drm_parameters_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class WidevineLevel(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    WIDEVINE_LEVEL_UNSPECIFIED: _ClassVar[WidevineLevel]
    WIDEVINE_LEVEL_L1: _ClassVar[WidevineLevel]
    WIDEVINE_LEVEL_L2: _ClassVar[WidevineLevel]
    WIDEVINE_LEVEL_L3: _ClassVar[WidevineLevel]

class PlayreadyLevel(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PLAYREADY_LEVEL_UNSPECIFIED: _ClassVar[PlayreadyLevel]
    PLAYREADY_LEVEL_SL150: _ClassVar[PlayreadyLevel]
    PLAYREADY_LEVEL_SL2000: _ClassVar[PlayreadyLevel]
    PLAYREADY_LEVEL_SL3000: _ClassVar[PlayreadyLevel]
WIDEVINE_LEVEL_UNSPECIFIED: WidevineLevel
WIDEVINE_LEVEL_L1: WidevineLevel
WIDEVINE_LEVEL_L2: WidevineLevel
WIDEVINE_LEVEL_L3: WidevineLevel
PLAYREADY_LEVEL_UNSPECIFIED: PlayreadyLevel
PLAYREADY_LEVEL_SL150: PlayreadyLevel
PLAYREADY_LEVEL_SL2000: PlayreadyLevel
PLAYREADY_LEVEL_SL3000: PlayreadyLevel

class PlayerAndDeviceInfo(_message.Message):
    __slots__ = ("client_capabilities", "drm_parameters", "player_name", "player_version", "widevine_system_id", "widevine_security_level", "decoders", "playready_security_level")
    class PlayerName(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        PLAYER_NAME_UNSPECIFIED: _ClassVar[PlayerAndDeviceInfo.PlayerName]
        PLAYER_NAME_HSPLAYER_EXOPLAYER: _ClassVar[PlayerAndDeviceInfo.PlayerName]
        PLAYER_NAME_HSPLAYER_AVPLAYER: _ClassVar[PlayerAndDeviceInfo.PlayerName]
        PLAYER_NAME_HSPLAYER_SHAKA: _ClassVar[PlayerAndDeviceInfo.PlayerName]
        PLAYER_NAME_HSPLAYER_TILEDMEDIA: _ClassVar[PlayerAndDeviceInfo.PlayerName]
        PLAYER_NAME_MULTICAST_LIVE_TV: _ClassVar[PlayerAndDeviceInfo.PlayerName]
    PLAYER_NAME_UNSPECIFIED: PlayerAndDeviceInfo.PlayerName
    PLAYER_NAME_HSPLAYER_EXOPLAYER: PlayerAndDeviceInfo.PlayerName
    PLAYER_NAME_HSPLAYER_AVPLAYER: PlayerAndDeviceInfo.PlayerName
    PLAYER_NAME_HSPLAYER_SHAKA: PlayerAndDeviceInfo.PlayerName
    PLAYER_NAME_HSPLAYER_TILEDMEDIA: PlayerAndDeviceInfo.PlayerName
    PLAYER_NAME_MULTICAST_LIVE_TV: PlayerAndDeviceInfo.PlayerName
    CLIENT_CAPABILITIES_FIELD_NUMBER: _ClassVar[int]
    DRM_PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    PLAYER_NAME_FIELD_NUMBER: _ClassVar[int]
    PLAYER_VERSION_FIELD_NUMBER: _ClassVar[int]
    WIDEVINE_SYSTEM_ID_FIELD_NUMBER: _ClassVar[int]
    WIDEVINE_SECURITY_LEVEL_FIELD_NUMBER: _ClassVar[int]
    DECODERS_FIELD_NUMBER: _ClassVar[int]
    PLAYREADY_SECURITY_LEVEL_FIELD_NUMBER: _ClassVar[int]
    client_capabilities: _client_capabilities_pb2.ClientCapabilities
    drm_parameters: _drm_parameters_pb2.DrmParameters
    player_name: PlayerAndDeviceInfo.PlayerName
    player_version: str
    widevine_system_id: str
    widevine_security_level: WidevineLevel
    decoders: _containers.RepeatedScalarFieldContainer[str]
    playready_security_level: PlayreadyLevel
    def __init__(self, client_capabilities: _Optional[_Union[_client_capabilities_pb2.ClientCapabilities, _Mapping]] = ..., drm_parameters: _Optional[_Union[_drm_parameters_pb2.DrmParameters, _Mapping]] = ..., player_name: _Optional[_Union[PlayerAndDeviceInfo.PlayerName, str]] = ..., player_version: _Optional[str] = ..., widevine_system_id: _Optional[str] = ..., widevine_security_level: _Optional[_Union[WidevineLevel, str]] = ..., decoders: _Optional[_Iterable[str]] = ..., playready_security_level: _Optional[_Union[PlayreadyLevel, str]] = ...) -> None: ...
