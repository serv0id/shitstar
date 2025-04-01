from client.player.model import video_initiation_type_pb2 as _video_initiation_type_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class WatchNextVideoSegment(_message.Message):
    __slots__ = ("initiation_source",)
    INITIATION_SOURCE_FIELD_NUMBER: _ClassVar[int]
    initiation_source: _video_initiation_type_pb2.VideoInitiationSource
    def __init__(self, initiation_source: _Optional[_Union[_video_initiation_type_pb2.VideoInitiationSource, str]] = ...) -> None: ...
