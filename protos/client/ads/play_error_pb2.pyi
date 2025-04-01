from options import opts_pb2 as _opts_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class PlayError(_message.Message):
    __slots__ = ("aspect_ratio", "segment_url", "url", "url_bitrate")
    ASPECT_RATIO_FIELD_NUMBER: _ClassVar[int]
    SEGMENT_URL_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    URL_BITRATE_FIELD_NUMBER: _ClassVar[int]
    aspect_ratio: str
    segment_url: str
    url: str
    url_bitrate: str
    def __init__(self, aspect_ratio: _Optional[str] = ..., segment_url: _Optional[str] = ..., url: _Optional[str] = ..., url_bitrate: _Optional[str] = ...) -> None: ...
