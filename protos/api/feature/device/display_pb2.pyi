from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class DisplayInfo(_message.Message):
    __slots__ = ("brightness_level_percent", "is_hdr_enabled")
    BRIGHTNESS_LEVEL_PERCENT_FIELD_NUMBER: _ClassVar[int]
    IS_HDR_ENABLED_FIELD_NUMBER: _ClassVar[int]
    brightness_level_percent: int
    is_hdr_enabled: bool
    def __init__(self, brightness_level_percent: _Optional[int] = ..., is_hdr_enabled: bool = ...) -> None: ...
