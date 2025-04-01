from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FailureProperties(_message.Message):
    __slots__ = ("failure_type", "failure_reason")
    class FailureType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        FAILURE_TYPE_UNSPECIFIED: _ClassVar[FailureProperties.FailureType]
        FAILURE_TYPE_SDK: _ClassVar[FailureProperties.FailureType]
        FAILURE_TYPE_INIT: _ClassVar[FailureProperties.FailureType]
        FAILURE_TYPE_NOTIFY: _ClassVar[FailureProperties.FailureType]
    FAILURE_TYPE_UNSPECIFIED: FailureProperties.FailureType
    FAILURE_TYPE_SDK: FailureProperties.FailureType
    FAILURE_TYPE_INIT: FailureProperties.FailureType
    FAILURE_TYPE_NOTIFY: FailureProperties.FailureType
    FAILURE_TYPE_FIELD_NUMBER: _ClassVar[int]
    FAILURE_REASON_FIELD_NUMBER: _ClassVar[int]
    failure_type: FailureProperties.FailureType
    failure_reason: str
    def __init__(self, failure_type: _Optional[_Union[FailureProperties.FailureType, str]] = ..., failure_reason: _Optional[str] = ...) -> None: ...
