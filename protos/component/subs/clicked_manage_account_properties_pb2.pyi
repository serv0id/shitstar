from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ClickedManageAccountProperties(_message.Message):
    __slots__ = ("link", "referrer")
    LINK_FIELD_NUMBER: _ClassVar[int]
    REFERRER_FIELD_NUMBER: _ClassVar[int]
    link: str
    referrer: str
    def __init__(self, link: _Optional[str] = ..., referrer: _Optional[str] = ...) -> None: ...
