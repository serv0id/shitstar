from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class MemoryInfo(_message.Message):
    __slots__ = ("available_ram_mb", "is_memory_warning_raised", "available_disk_space_gb")
    AVAILABLE_RAM_MB_FIELD_NUMBER: _ClassVar[int]
    IS_MEMORY_WARNING_RAISED_FIELD_NUMBER: _ClassVar[int]
    AVAILABLE_DISK_SPACE_GB_FIELD_NUMBER: _ClassVar[int]
    available_ram_mb: int
    is_memory_warning_raised: bool
    available_disk_space_gb: float
    def __init__(self, available_ram_mb: _Optional[int] = ..., is_memory_warning_raised: bool = ..., available_disk_space_gb: _Optional[float] = ...) -> None: ...
