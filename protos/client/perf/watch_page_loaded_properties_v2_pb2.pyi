from client.preload import preload_journey_pb2 as _preload_journey_pb2
from client.preload import preload_journey_v2_pb2 as _preload_journey_v2_pb2
from client.watch import player_manager_properties_pb2 as _player_manager_properties_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class WatchPageLoadedPropertiesV2(_message.Message):
    __slots__ = ("bff_preparation_time_v2_ms", "time_between_bff_and_player_v2_ms", "watch_session_id_v2", "preload_info_v2", "watch_player_client_capability_time_v2_ms")
    BFF_PREPARATION_TIME_V2_MS_FIELD_NUMBER: _ClassVar[int]
    TIME_BETWEEN_BFF_AND_PLAYER_V2_MS_FIELD_NUMBER: _ClassVar[int]
    WATCH_SESSION_ID_V2_FIELD_NUMBER: _ClassVar[int]
    PRELOAD_INFO_V2_FIELD_NUMBER: _ClassVar[int]
    WATCH_PLAYER_CLIENT_CAPABILITY_TIME_V2_MS_FIELD_NUMBER: _ClassVar[int]
    bff_preparation_time_v2_ms: int
    time_between_bff_and_player_v2_ms: int
    watch_session_id_v2: str
    preload_info_v2: _preload_journey_v2_pb2.PreloadAdditionV2
    watch_player_client_capability_time_v2_ms: int
    def __init__(self, bff_preparation_time_v2_ms: _Optional[int] = ..., time_between_bff_and_player_v2_ms: _Optional[int] = ..., watch_session_id_v2: _Optional[str] = ..., preload_info_v2: _Optional[_Union[_preload_journey_v2_pb2.PreloadAdditionV2, _Mapping]] = ..., watch_player_client_capability_time_v2_ms: _Optional[int] = ...) -> None: ...
