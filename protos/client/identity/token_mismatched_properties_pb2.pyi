from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class TokenMismatchedProperties(_message.Message):
    __slots__ = ("is_app_id_present", "token_app_id", "local_app_id", "request_url")
    IS_APP_ID_PRESENT_FIELD_NUMBER: _ClassVar[int]
    TOKEN_APP_ID_FIELD_NUMBER: _ClassVar[int]
    LOCAL_APP_ID_FIELD_NUMBER: _ClassVar[int]
    REQUEST_URL_FIELD_NUMBER: _ClassVar[int]
    is_app_id_present: bool
    token_app_id: str
    local_app_id: str
    request_url: str
    def __init__(self, is_app_id_present: bool = ..., token_app_id: _Optional[str] = ..., local_app_id: _Optional[str] = ..., request_url: _Optional[str] = ...) -> None: ...
