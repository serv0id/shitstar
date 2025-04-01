from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ChannelParams(_message.Message):
    __slots__ = ("channel_id", "playback_tags")
    CHANNEL_ID_FIELD_NUMBER: _ClassVar[int]
    PLAYBACK_TAGS_FIELD_NUMBER: _ClassVar[int]
    channel_id: str
    playback_tags: str
    def __init__(self, channel_id: _Optional[str] = ..., playback_tags: _Optional[str] = ...) -> None: ...
