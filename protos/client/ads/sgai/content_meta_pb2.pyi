from client.player.model import client_capabilities_pb2 as _client_capabilities_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ContentMeta(_message.Message):
    __slots__ = ("content_id", "si_match_id", "audio_codec", "media_codec", "language_tag", "resolution", "bandwidth")
    CONTENT_ID_FIELD_NUMBER: _ClassVar[int]
    SI_MATCH_ID_FIELD_NUMBER: _ClassVar[int]
    AUDIO_CODEC_FIELD_NUMBER: _ClassVar[int]
    MEDIA_CODEC_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_TAG_FIELD_NUMBER: _ClassVar[int]
    RESOLUTION_FIELD_NUMBER: _ClassVar[int]
    BANDWIDTH_FIELD_NUMBER: _ClassVar[int]
    content_id: str
    si_match_id: str
    audio_codec: _client_capabilities_pb2.ClientCapabilities.AudioCodec
    media_codec: _client_capabilities_pb2.ClientCapabilities.VideoCodec
    language_tag: str
    resolution: str
    bandwidth: int
    def __init__(self, content_id: _Optional[str] = ..., si_match_id: _Optional[str] = ..., audio_codec: _Optional[_Union[_client_capabilities_pb2.ClientCapabilities.AudioCodec, str]] = ..., media_codec: _Optional[_Union[_client_capabilities_pb2.ClientCapabilities.VideoCodec, str]] = ..., language_tag: _Optional[str] = ..., resolution: _Optional[str] = ..., bandwidth: _Optional[int] = ...) -> None: ...
