from component.identity import enum_pb2 as _enum_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ForcedLoggedOutProperties(_message.Message):
    __slots__ = ("reason_for_logout", "trigger_url", "mode")
    REASON_FOR_LOGOUT_FIELD_NUMBER: _ClassVar[int]
    TRIGGER_URL_FIELD_NUMBER: _ClassVar[int]
    MODE_FIELD_NUMBER: _ClassVar[int]
    reason_for_logout: _enum_pb2.LogoutTrigger
    trigger_url: str
    mode: _enum_pb2.LogoutMode
    def __init__(self, reason_for_logout: _Optional[_Union[_enum_pb2.LogoutTrigger, str]] = ..., trigger_url: _Optional[str] = ..., mode: _Optional[_Union[_enum_pb2.LogoutMode, str]] = ...) -> None: ...
