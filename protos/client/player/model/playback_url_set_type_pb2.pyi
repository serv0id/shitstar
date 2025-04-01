from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class PlaybackUrlSetType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PLAYBACK_URL_SET_TYPE_UNSPECIFIED: _ClassVar[PlaybackUrlSetType]
    PLAYBACK_URL_SET_TYPE_PRIMARY: _ClassVar[PlaybackUrlSetType]
    PLAYBACK_URL_SET_TYPE_FALLBACK: _ClassVar[PlaybackUrlSetType]
PLAYBACK_URL_SET_TYPE_UNSPECIFIED: PlaybackUrlSetType
PLAYBACK_URL_SET_TYPE_PRIMARY: PlaybackUrlSetType
PLAYBACK_URL_SET_TYPE_FALLBACK: PlaybackUrlSetType
