from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class Viewport(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    VIEWPORT_UNSPECIFIED: _ClassVar[Viewport]
    VIEWPORT_PORTRAIT: _ClassVar[Viewport]
    VIEWPORT_LANDSCAPE: _ClassVar[Viewport]
    VIEWPORT_PIP: _ClassVar[Viewport]
VIEWPORT_UNSPECIFIED: Viewport
VIEWPORT_PORTRAIT: Viewport
VIEWPORT_LANDSCAPE: Viewport
VIEWPORT_PIP: Viewport
