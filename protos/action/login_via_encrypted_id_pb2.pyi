from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class LoginViaEncryptedIdAction(_message.Message):
    __slots__ = ("url", "encrypted_id")
    URL_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTED_ID_FIELD_NUMBER: _ClassVar[int]
    url: str
    encrypted_id: str
    def __init__(self, url: _Optional[str] = ..., encrypted_id: _Optional[str] = ...) -> None: ...
