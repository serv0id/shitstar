from component.identity import enum_pb2 as _enum_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class LoginItem(_message.Message):
    __slots__ = ("selector", "mode", "is_otp_filled")
    SELECTOR_FIELD_NUMBER: _ClassVar[int]
    MODE_FIELD_NUMBER: _ClassVar[int]
    IS_OTP_FILLED_FIELD_NUMBER: _ClassVar[int]
    selector: _enum_pb2.LoginItemType
    mode: _enum_pb2.InputEnterMode
    is_otp_filled: bool
    def __init__(self, selector: _Optional[_Union[_enum_pb2.LoginItemType, str]] = ..., mode: _Optional[_Union[_enum_pb2.InputEnterMode, str]] = ..., is_otp_filled: bool = ...) -> None: ...
