from client.identity.properties import video_bg_info_pb2 as _video_bg_info_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class StartedOnboardingVideo(_message.Message):
    __slots__ = ("start_lag_in_sec", "network_type", "network_speed", "screen_size", "network_speed_in_mb")
    START_LAG_IN_SEC_FIELD_NUMBER: _ClassVar[int]
    NETWORK_TYPE_FIELD_NUMBER: _ClassVar[int]
    NETWORK_SPEED_FIELD_NUMBER: _ClassVar[int]
    SCREEN_SIZE_FIELD_NUMBER: _ClassVar[int]
    NETWORK_SPEED_IN_MB_FIELD_NUMBER: _ClassVar[int]
    start_lag_in_sec: float
    network_type: _video_bg_info_pb2.NetworkType
    network_speed: int
    screen_size: _video_bg_info_pb2.ScreenSize
    network_speed_in_mb: float
    def __init__(self, start_lag_in_sec: _Optional[float] = ..., network_type: _Optional[_Union[_video_bg_info_pb2.NetworkType, str]] = ..., network_speed: _Optional[int] = ..., screen_size: _Optional[_Union[_video_bg_info_pb2.ScreenSize, _Mapping]] = ..., network_speed_in_mb: _Optional[float] = ...) -> None: ...
