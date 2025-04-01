from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class Accessibility(_message.Message):
    __slots__ = ("label", "action_label", "test_tag")
    LABEL_FIELD_NUMBER: _ClassVar[int]
    ACTION_LABEL_FIELD_NUMBER: _ClassVar[int]
    TEST_TAG_FIELD_NUMBER: _ClassVar[int]
    label: str
    action_label: str
    test_tag: str
    def __init__(self, label: _Optional[str] = ..., action_label: _Optional[str] = ..., test_tag: _Optional[str] = ...) -> None: ...
