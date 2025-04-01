from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class AppStoryViewProperties(_message.Message):
    __slots__ = ("story_type", "stories_count")
    STORY_TYPE_FIELD_NUMBER: _ClassVar[int]
    STORIES_COUNT_FIELD_NUMBER: _ClassVar[int]
    story_type: str
    stories_count: int
    def __init__(self, story_type: _Optional[str] = ..., stories_count: _Optional[int] = ...) -> None: ...
