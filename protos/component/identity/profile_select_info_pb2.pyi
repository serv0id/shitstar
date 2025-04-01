from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ProfileSelectionInfo(_message.Message):
    __slots__ = ("page", "actioned_pid")
    PAGE_FIELD_NUMBER: _ClassVar[int]
    ACTIONED_PID_FIELD_NUMBER: _ClassVar[int]
    page: str
    actioned_pid: str
    def __init__(self, page: _Optional[str] = ..., actioned_pid: _Optional[str] = ...) -> None: ...
