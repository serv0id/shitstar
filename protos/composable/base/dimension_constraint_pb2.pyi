from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DimensionConstraint(_message.Message):
    __slots__ = ("min", "max")
    class Dimension(_message.Message):
        __slots__ = ("fixed",)
        FIXED_FIELD_NUMBER: _ClassVar[int]
        fixed: int
        def __init__(self, fixed: _Optional[int] = ...) -> None: ...
    MIN_FIELD_NUMBER: _ClassVar[int]
    MAX_FIELD_NUMBER: _ClassVar[int]
    min: DimensionConstraint.Dimension
    max: DimensionConstraint.Dimension
    def __init__(self, min: _Optional[_Union[DimensionConstraint.Dimension, _Mapping]] = ..., max: _Optional[_Union[DimensionConstraint.Dimension, _Mapping]] = ...) -> None: ...
