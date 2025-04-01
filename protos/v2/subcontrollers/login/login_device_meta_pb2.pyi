from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class LoginDeviceMeta(_message.Message):
    __slots__ = ("device_name",)
    DEVICE_NAME_FIELD_NUMBER: _ClassVar[int]
    device_name: str
    def __init__(self, device_name: _Optional[str] = ...) -> None: ...
