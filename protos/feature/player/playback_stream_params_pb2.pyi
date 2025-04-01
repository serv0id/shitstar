from feature.player import playback_params_pb2 as _playback_params_pb2
from feature.player import channel_params_pb2 as _channel_params_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PlaybackStreamParams(_message.Message):
    __slots__ = ("url_params", "channel_params")
    URL_PARAMS_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_PARAMS_FIELD_NUMBER: _ClassVar[int]
    url_params: _playback_params_pb2.PlaybackParams
    channel_params: _channel_params_pb2.ChannelParams
    def __init__(self, url_params: _Optional[_Union[_playback_params_pb2.PlaybackParams, _Mapping]] = ..., channel_params: _Optional[_Union[_channel_params_pb2.ChannelParams, _Mapping]] = ...) -> None: ...
