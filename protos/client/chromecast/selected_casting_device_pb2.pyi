from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class SelectedCastingDeviceProperties(_message.Message):
    __slots__ = ("selected_device_name", "selected_device_meta")
    SELECTED_DEVICE_NAME_FIELD_NUMBER: _ClassVar[int]
    SELECTED_DEVICE_META_FIELD_NUMBER: _ClassVar[int]
    selected_device_name: str
    selected_device_meta: str
    def __init__(self, selected_device_name: _Optional[str] = ..., selected_device_meta: _Optional[str] = ...) -> None: ...
