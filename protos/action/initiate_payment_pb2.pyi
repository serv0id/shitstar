from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class InitiatePaymentAction(_message.Message):
    __slots__ = ["base_init_payload", "url", "use_async"]
    BASE_INIT_PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    USE_ASYNC_FIELD_NUMBER: _ClassVar[int]
    base_init_payload: str
    url: str
    use_async: bool
    def __init__(self, base_init_payload: _Optional[str] = ..., url: _Optional[str] = ..., use_async: bool = ...) -> None: ...
