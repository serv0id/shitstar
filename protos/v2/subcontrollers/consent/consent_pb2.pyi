from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ConsentInfo(_message.Message):
    __slots__ = ("consent_id", "identifier_type", "consent_type", "consent_version", "status", "identifier", "consent_for")
    CONSENT_ID_FIELD_NUMBER: _ClassVar[int]
    IDENTIFIER_TYPE_FIELD_NUMBER: _ClassVar[int]
    CONSENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    CONSENT_VERSION_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    CONSENT_FOR_FIELD_NUMBER: _ClassVar[int]
    consent_id: str
    identifier_type: str
    consent_type: str
    consent_version: int
    status: str
    identifier: str
    consent_for: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, consent_id: _Optional[str] = ..., identifier_type: _Optional[str] = ..., consent_type: _Optional[str] = ..., consent_version: _Optional[int] = ..., status: _Optional[str] = ..., identifier: _Optional[str] = ..., consent_for: _Optional[_Iterable[str]] = ...) -> None: ...
