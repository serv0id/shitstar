from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class PlayerLayer(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    INVALID: _ClassVar[PlayerLayer]
    CONTENT_HEADER: _ClassVar[PlayerLayer]
    STICKY_HEADER: _ClassVar[PlayerLayer]
    OVERLAY: _ClassVar[PlayerLayer]
    SETTINGS: _ClassVar[PlayerLayer]
INVALID: PlayerLayer
CONTENT_HEADER: PlayerLayer
STICKY_HEADER: PlayerLayer
OVERLAY: PlayerLayer
SETTINGS: PlayerLayer
