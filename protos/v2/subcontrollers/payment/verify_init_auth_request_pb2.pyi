from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class VerifyInitAuthRequest(_message.Message):
    __slots__ = ("post_url", "communication_type", "request_id")
    POST_URL_FIELD_NUMBER: _ClassVar[int]
    COMMUNICATION_TYPE_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    post_url: str
    communication_type: str
    request_id: str
    def __init__(self, post_url: _Optional[str] = ..., communication_type: _Optional[str] = ..., request_id: _Optional[str] = ...) -> None: ...
