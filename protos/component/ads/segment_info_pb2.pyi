from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class SegmentInfo(_message.Message):
    __slots__ = ("user_segment",)
    USER_SEGMENT_FIELD_NUMBER: _ClassVar[int]
    user_segment: str
    def __init__(self, user_segment: _Optional[str] = ...) -> None: ...
