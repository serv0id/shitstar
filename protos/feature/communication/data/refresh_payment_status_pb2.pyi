from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class RefreshPaymentStatus(_message.Message):
    __slots__ = ("refresh_url", "refresh_interval")
    REFRESH_URL_FIELD_NUMBER: _ClassVar[int]
    REFRESH_INTERVAL_FIELD_NUMBER: _ClassVar[int]
    refresh_url: str
    refresh_interval: int
    def __init__(self, refresh_url: _Optional[str] = ..., refresh_interval: _Optional[int] = ...) -> None: ...
