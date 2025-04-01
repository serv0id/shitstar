from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TerminateSessionRequest(_message.Message):
    __slots__ = ("session_ids", "session_details")
    class SessionDetail(_message.Message):
        __slots__ = ("session_id", "device_id")
        SESSION_ID_FIELD_NUMBER: _ClassVar[int]
        DEVICE_ID_FIELD_NUMBER: _ClassVar[int]
        session_id: str
        device_id: str
        def __init__(self, session_id: _Optional[str] = ..., device_id: _Optional[str] = ...) -> None: ...
    SESSION_IDS_FIELD_NUMBER: _ClassVar[int]
    SESSION_DETAILS_FIELD_NUMBER: _ClassVar[int]
    session_ids: _containers.RepeatedScalarFieldContainer[str]
    session_details: _containers.RepeatedCompositeFieldContainer[TerminateSessionRequest.SessionDetail]
    def __init__(self, session_ids: _Optional[_Iterable[str]] = ..., session_details: _Optional[_Iterable[_Union[TerminateSessionRequest.SessionDetail, _Mapping]]] = ...) -> None: ...
