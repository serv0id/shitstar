from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class UserProperties(_message.Message):
    __slots__ = ("ssai_tag",)
    SSAI_TAG_FIELD_NUMBER: _ClassVar[int]
    ssai_tag: str
    def __init__(self, ssai_tag: _Optional[str] = ...) -> None: ...
