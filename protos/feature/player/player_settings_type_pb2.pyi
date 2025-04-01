from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class PlayerSettingsType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    NONE: _ClassVar[PlayerSettingsType]
    VIDEO_QUALITY: _ClassVar[PlayerSettingsType]
    AUDIO_LANGUAGE: _ClassVar[PlayerSettingsType]
    SUBTITLE: _ClassVar[PlayerSettingsType]
    PLAYBACK_SPEED: _ClassVar[PlayerSettingsType]
NONE: PlayerSettingsType
VIDEO_QUALITY: PlayerSettingsType
AUDIO_LANGUAGE: PlayerSettingsType
SUBTITLE: PlayerSettingsType
PLAYBACK_SPEED: PlayerSettingsType
