from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class PageContentLoadedCommons(_message.Message):
    __slots__ = ("total_image_loads", "slow_image_loads")
    TOTAL_IMAGE_LOADS_FIELD_NUMBER: _ClassVar[int]
    SLOW_IMAGE_LOADS_FIELD_NUMBER: _ClassVar[int]
    total_image_loads: int
    slow_image_loads: int
    def __init__(self, total_image_loads: _Optional[int] = ..., slow_image_loads: _Optional[int] = ...) -> None: ...
