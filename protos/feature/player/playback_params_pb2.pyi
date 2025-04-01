from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class PlaybackParams(_message.Message):
    __slots__ = ("content_url", "license_url", "certificate_url", "playback_tags")
    CONTENT_URL_FIELD_NUMBER: _ClassVar[int]
    LICENSE_URL_FIELD_NUMBER: _ClassVar[int]
    CERTIFICATE_URL_FIELD_NUMBER: _ClassVar[int]
    PLAYBACK_TAGS_FIELD_NUMBER: _ClassVar[int]
    content_url: str
    license_url: str
    certificate_url: str
    playback_tags: str
    def __init__(self, content_url: _Optional[str] = ..., license_url: _Optional[str] = ..., certificate_url: _Optional[str] = ..., playback_tags: _Optional[str] = ...) -> None: ...
