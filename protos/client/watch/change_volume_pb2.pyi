from client import orientation_pb2 as _orientation_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ChangeVolumeProperties(_message.Message):
    __slots__ = ("previous_volume_pct", "new_volume_pct", "change_source", "player_orientation")
    class VolumeSource(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        VOLUME_SOURCE_UNSPECIFIED: _ClassVar[ChangeVolumeProperties.VolumeSource]
        VOLUME_SOURCE_GESTURE: _ClassVar[ChangeVolumeProperties.VolumeSource]
        VOLUME_SOURCE_VOLUME_BAR: _ClassVar[ChangeVolumeProperties.VolumeSource]
        VOLUME_SOURCE_PHONE: _ClassVar[ChangeVolumeProperties.VolumeSource]
    VOLUME_SOURCE_UNSPECIFIED: ChangeVolumeProperties.VolumeSource
    VOLUME_SOURCE_GESTURE: ChangeVolumeProperties.VolumeSource
    VOLUME_SOURCE_VOLUME_BAR: ChangeVolumeProperties.VolumeSource
    VOLUME_SOURCE_PHONE: ChangeVolumeProperties.VolumeSource
    PREVIOUS_VOLUME_PCT_FIELD_NUMBER: _ClassVar[int]
    NEW_VOLUME_PCT_FIELD_NUMBER: _ClassVar[int]
    CHANGE_SOURCE_FIELD_NUMBER: _ClassVar[int]
    PLAYER_ORIENTATION_FIELD_NUMBER: _ClassVar[int]
    previous_volume_pct: int
    new_volume_pct: int
    change_source: ChangeVolumeProperties.VolumeSource
    player_orientation: _orientation_pb2.Orientation
    def __init__(self, previous_volume_pct: _Optional[int] = ..., new_volume_pct: _Optional[int] = ..., change_source: _Optional[_Union[ChangeVolumeProperties.VolumeSource, str]] = ..., player_orientation: _Optional[_Union[_orientation_pb2.Orientation, str]] = ...) -> None: ...
