from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class SearchChromeCastDeviceAction(_message.Message):
    __slots__ = ("refresh_interval_in_millis",)
    REFRESH_INTERVAL_IN_MILLIS_FIELD_NUMBER: _ClassVar[int]
    refresh_interval_in_millis: int
    def __init__(self, refresh_interval_in_millis: _Optional[int] = ...) -> None: ...
