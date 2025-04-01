from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class Log(_message.Message):
    __slots__ = ("app_log", "system_log")
    APP_LOG_FIELD_NUMBER: _ClassVar[int]
    SYSTEM_LOG_FIELD_NUMBER: _ClassVar[int]
    app_log: str
    system_log: str
    def __init__(self, app_log: _Optional[str] = ..., system_log: _Optional[str] = ...) -> None: ...
