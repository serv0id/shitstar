from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ViewedCastingDeviceListProperties(_message.Message):
    __slots__ = ("device_count", "device_list")
    DEVICE_COUNT_FIELD_NUMBER: _ClassVar[int]
    DEVICE_LIST_FIELD_NUMBER: _ClassVar[int]
    device_count: int
    device_list: str
    def __init__(self, device_count: _Optional[int] = ..., device_list: _Optional[str] = ...) -> None: ...
