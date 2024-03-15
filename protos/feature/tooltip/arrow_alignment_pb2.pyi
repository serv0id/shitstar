from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class ArrowAlignment(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    UNDEFINED: _ClassVar[ArrowAlignment]
    START: _ClassVar[ArrowAlignment]
    END: _ClassVar[ArrowAlignment]
    TOP: _ClassVar[ArrowAlignment]
    BOTTOM: _ClassVar[ArrowAlignment]
UNDEFINED: ArrowAlignment
START: ArrowAlignment
END: ArrowAlignment
TOP: ArrowAlignment
BOTTOM: ArrowAlignment
