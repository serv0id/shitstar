from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class WatchlistState(_message.Message):
    __slots__ = ("is_watchlisted",)
    IS_WATCHLISTED_FIELD_NUMBER: _ClassVar[int]
    is_watchlisted: bool
    def __init__(self, is_watchlisted: bool = ...) -> None: ...
