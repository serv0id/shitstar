from options import opts_pb2 as _opts_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class Resolution(_message.Message):
    __slots__ = ("width_px", "height_px")
    WIDTH_PX_FIELD_NUMBER: _ClassVar[int]
    HEIGHT_PX_FIELD_NUMBER: _ClassVar[int]
    width_px: int
    height_px: int
    def __init__(self, width_px: _Optional[int] = ..., height_px: _Optional[int] = ...) -> None: ...
