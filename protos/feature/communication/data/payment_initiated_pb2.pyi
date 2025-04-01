from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class InitStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    UNSPECIFIED: _ClassVar[InitStatus]
    LOADING: _ClassVar[InitStatus]
    SUCCESS: _ClassVar[InitStatus]
    FAILURE: _ClassVar[InitStatus]
UNSPECIFIED: InitStatus
LOADING: InitStatus
SUCCESS: InitStatus
FAILURE: InitStatus

class PaymentInitiated(_message.Message):
    __slots__ = ("is_initiated", "init_status")
    IS_INITIATED_FIELD_NUMBER: _ClassVar[int]
    INIT_STATUS_FIELD_NUMBER: _ClassVar[int]
    is_initiated: bool
    init_status: InitStatus
    def __init__(self, is_initiated: bool = ..., init_status: _Optional[_Union[InitStatus, str]] = ...) -> None: ...
