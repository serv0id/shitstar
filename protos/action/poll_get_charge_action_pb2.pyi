from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class PollGetChargeAction(_message.Message):
    __slots__ = ("url", "polling_interval_in_MS", "timeoutInMS", "noOfFailureRetries")
    URL_FIELD_NUMBER: _ClassVar[int]
    POLLING_INTERVAL_IN_MS_FIELD_NUMBER: _ClassVar[int]
    TIMEOUTINMS_FIELD_NUMBER: _ClassVar[int]
    NOOFFAILURERETRIES_FIELD_NUMBER: _ClassVar[int]
    url: str
    polling_interval_in_MS: int
    timeoutInMS: int
    noOfFailureRetries: int
    def __init__(self, url: _Optional[str] = ..., polling_interval_in_MS: _Optional[int] = ..., timeoutInMS: _Optional[int] = ..., noOfFailureRetries: _Optional[int] = ...) -> None: ...
