from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ChangeFillStatusProperties(_message.Message):
    __slots__ = ("previous_fill_type", "new_fill_type")
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATUS_UNSPECIFIED: _ClassVar[ChangeFillStatusProperties.Status]
        STATUS_FILL: _ClassVar[ChangeFillStatusProperties.Status]
        STATUS_FIT: _ClassVar[ChangeFillStatusProperties.Status]
    STATUS_UNSPECIFIED: ChangeFillStatusProperties.Status
    STATUS_FILL: ChangeFillStatusProperties.Status
    STATUS_FIT: ChangeFillStatusProperties.Status
    PREVIOUS_FILL_TYPE_FIELD_NUMBER: _ClassVar[int]
    NEW_FILL_TYPE_FIELD_NUMBER: _ClassVar[int]
    previous_fill_type: ChangeFillStatusProperties.Status
    new_fill_type: ChangeFillStatusProperties.Status
    def __init__(self, previous_fill_type: _Optional[_Union[ChangeFillStatusProperties.Status, str]] = ..., new_fill_type: _Optional[_Union[ChangeFillStatusProperties.Status, str]] = ...) -> None: ...
