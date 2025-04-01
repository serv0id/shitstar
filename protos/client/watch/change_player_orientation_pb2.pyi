from client import orientation_pb2 as _orientation_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ChangePlayerOrientationProperties(_message.Message):
    __slots__ = ("previous_orientation", "new_orientation", "change_source")
    class OrientationSource(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ORIENTATION_SOURCE_UNSPECIFIED: _ClassVar[ChangePlayerOrientationProperties.OrientationSource]
        ORIENTATION_SOURCE_BUTTON: _ClassVar[ChangePlayerOrientationProperties.OrientationSource]
        ORIENTATION_SOURCE_PHONE_TILT: _ClassVar[ChangePlayerOrientationProperties.OrientationSource]
    ORIENTATION_SOURCE_UNSPECIFIED: ChangePlayerOrientationProperties.OrientationSource
    ORIENTATION_SOURCE_BUTTON: ChangePlayerOrientationProperties.OrientationSource
    ORIENTATION_SOURCE_PHONE_TILT: ChangePlayerOrientationProperties.OrientationSource
    PREVIOUS_ORIENTATION_FIELD_NUMBER: _ClassVar[int]
    NEW_ORIENTATION_FIELD_NUMBER: _ClassVar[int]
    CHANGE_SOURCE_FIELD_NUMBER: _ClassVar[int]
    previous_orientation: _orientation_pb2.Orientation
    new_orientation: _orientation_pb2.Orientation
    change_source: ChangePlayerOrientationProperties.OrientationSource
    def __init__(self, previous_orientation: _Optional[_Union[_orientation_pb2.Orientation, str]] = ..., new_orientation: _Optional[_Union[_orientation_pb2.Orientation, str]] = ..., change_source: _Optional[_Union[ChangePlayerOrientationProperties.OrientationSource, str]] = ...) -> None: ...
