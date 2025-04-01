from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ClickedOpenAppProperties(_message.Message):
    __slots__ = ("referrer",)
    REFERRER_FIELD_NUMBER: _ClassVar[int]
    referrer: str
    def __init__(self, referrer: _Optional[str] = ...) -> None: ...
