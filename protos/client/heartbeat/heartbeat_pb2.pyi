from client.heartbeat.model import payload_pb2 as _payload_pb2
from client.player.model import client_capabilities_pb2 as _client_capabilities_pb2
from client.player.model import player_and_device_info_pb2 as _player_and_device_info_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class HeartbeatProperties(_message.Message):
    __slots__ = ("payloads", "player_name", "player_version", "client_capabilities", "ssai_cohort")
    PAYLOADS_FIELD_NUMBER: _ClassVar[int]
    PLAYER_NAME_FIELD_NUMBER: _ClassVar[int]
    PLAYER_VERSION_FIELD_NUMBER: _ClassVar[int]
    CLIENT_CAPABILITIES_FIELD_NUMBER: _ClassVar[int]
    SSAI_COHORT_FIELD_NUMBER: _ClassVar[int]
    payloads: _containers.RepeatedCompositeFieldContainer[_payload_pb2.Payload]
    player_name: _player_and_device_info_pb2.PlayerAndDeviceInfo.PlayerName
    player_version: str
    client_capabilities: _client_capabilities_pb2.ClientCapabilities
    ssai_cohort: str
    def __init__(self, payloads: _Optional[_Iterable[_Union[_payload_pb2.Payload, _Mapping]]] = ..., player_name: _Optional[_Union[_player_and_device_info_pb2.PlayerAndDeviceInfo.PlayerName, str]] = ..., player_version: _Optional[str] = ..., client_capabilities: _Optional[_Union[_client_capabilities_pb2.ClientCapabilities, _Mapping]] = ..., ssai_cohort: _Optional[str] = ...) -> None: ...
