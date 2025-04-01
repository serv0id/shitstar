from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class Midroll(_message.Message):
    __slots__ = ("server_url", "ssai_tag", "cue_points_url", "cue_points")
    SERVER_URL_FIELD_NUMBER: _ClassVar[int]
    SSAI_TAG_FIELD_NUMBER: _ClassVar[int]
    CUE_POINTS_URL_FIELD_NUMBER: _ClassVar[int]
    CUE_POINTS_FIELD_NUMBER: _ClassVar[int]
    server_url: str
    ssai_tag: str
    cue_points_url: str
    cue_points: str
    def __init__(self, server_url: _Optional[str] = ..., ssai_tag: _Optional[str] = ..., cue_points_url: _Optional[str] = ..., cue_points: _Optional[str] = ...) -> None: ...
