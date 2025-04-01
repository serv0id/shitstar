from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class Source(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    LOGIN: _ClassVar[Source]
    PRE_LAUNCH: _ClassVar[Source]
    SKIPPABLE_LOGIN: _ClassVar[Source]
LOGIN: Source
PRE_LAUNCH: Source
SKIPPABLE_LOGIN: Source
