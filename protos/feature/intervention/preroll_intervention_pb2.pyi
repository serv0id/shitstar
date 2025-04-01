from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class PrerollIntervention(_message.Message):
    __slots__ = ("payload", "vast_payload", "has_third_party_wrapper", "vast", "url")
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    VAST_PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    HAS_THIRD_PARTY_WRAPPER_FIELD_NUMBER: _ClassVar[int]
    VAST_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    payload: bytes
    vast_payload: str
    has_third_party_wrapper: bool
    vast: str
    url: str
    def __init__(self, payload: _Optional[bytes] = ..., vast_payload: _Optional[str] = ..., has_third_party_wrapper: bool = ..., vast: _Optional[str] = ..., url: _Optional[str] = ...) -> None: ...
