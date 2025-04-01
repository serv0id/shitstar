from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class StoryWidgetProperties(_message.Message):
    __slots__ = ("total_cards_available", "story_id")
    TOTAL_CARDS_AVAILABLE_FIELD_NUMBER: _ClassVar[int]
    STORY_ID_FIELD_NUMBER: _ClassVar[int]
    total_cards_available: int
    story_id: int
    def __init__(self, total_cards_available: _Optional[int] = ..., story_id: _Optional[int] = ...) -> None: ...
