from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class HttpConnectionStats(_message.Message):
    __slots__ = ("call_start_time_ms", "dns_start_times_ms", "dns_end_times_ms", "connection_start_times_ms", "connection_end_times_ms", "secure_connection_start_times_ms", "secure_connection_end_times_ms", "connection_acquire_time_ms", "connection_release_time_ms", "request_header_start_times_ms", "request_header_end_times_ms", "request_body_start_times_ms", "request_body_end_times_ms", "response_header_start_times_ms", "response_header_end_times_ms", "response_body_start_times_ms", "response_body_end_times_ms", "call_end_time_ms")
    CALL_START_TIME_MS_FIELD_NUMBER: _ClassVar[int]
    DNS_START_TIMES_MS_FIELD_NUMBER: _ClassVar[int]
    DNS_END_TIMES_MS_FIELD_NUMBER: _ClassVar[int]
    CONNECTION_START_TIMES_MS_FIELD_NUMBER: _ClassVar[int]
    CONNECTION_END_TIMES_MS_FIELD_NUMBER: _ClassVar[int]
    SECURE_CONNECTION_START_TIMES_MS_FIELD_NUMBER: _ClassVar[int]
    SECURE_CONNECTION_END_TIMES_MS_FIELD_NUMBER: _ClassVar[int]
    CONNECTION_ACQUIRE_TIME_MS_FIELD_NUMBER: _ClassVar[int]
    CONNECTION_RELEASE_TIME_MS_FIELD_NUMBER: _ClassVar[int]
    REQUEST_HEADER_START_TIMES_MS_FIELD_NUMBER: _ClassVar[int]
    REQUEST_HEADER_END_TIMES_MS_FIELD_NUMBER: _ClassVar[int]
    REQUEST_BODY_START_TIMES_MS_FIELD_NUMBER: _ClassVar[int]
    REQUEST_BODY_END_TIMES_MS_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_HEADER_START_TIMES_MS_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_HEADER_END_TIMES_MS_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_BODY_START_TIMES_MS_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_BODY_END_TIMES_MS_FIELD_NUMBER: _ClassVar[int]
    CALL_END_TIME_MS_FIELD_NUMBER: _ClassVar[int]
    call_start_time_ms: int
    dns_start_times_ms: _containers.RepeatedScalarFieldContainer[int]
    dns_end_times_ms: _containers.RepeatedScalarFieldContainer[int]
    connection_start_times_ms: _containers.RepeatedScalarFieldContainer[int]
    connection_end_times_ms: _containers.RepeatedScalarFieldContainer[int]
    secure_connection_start_times_ms: _containers.RepeatedScalarFieldContainer[int]
    secure_connection_end_times_ms: _containers.RepeatedScalarFieldContainer[int]
    connection_acquire_time_ms: int
    connection_release_time_ms: int
    request_header_start_times_ms: _containers.RepeatedScalarFieldContainer[int]
    request_header_end_times_ms: _containers.RepeatedScalarFieldContainer[int]
    request_body_start_times_ms: _containers.RepeatedScalarFieldContainer[int]
    request_body_end_times_ms: _containers.RepeatedScalarFieldContainer[int]
    response_header_start_times_ms: _containers.RepeatedScalarFieldContainer[int]
    response_header_end_times_ms: _containers.RepeatedScalarFieldContainer[int]
    response_body_start_times_ms: _containers.RepeatedScalarFieldContainer[int]
    response_body_end_times_ms: _containers.RepeatedScalarFieldContainer[int]
    call_end_time_ms: int
    def __init__(self, call_start_time_ms: _Optional[int] = ..., dns_start_times_ms: _Optional[_Iterable[int]] = ..., dns_end_times_ms: _Optional[_Iterable[int]] = ..., connection_start_times_ms: _Optional[_Iterable[int]] = ..., connection_end_times_ms: _Optional[_Iterable[int]] = ..., secure_connection_start_times_ms: _Optional[_Iterable[int]] = ..., secure_connection_end_times_ms: _Optional[_Iterable[int]] = ..., connection_acquire_time_ms: _Optional[int] = ..., connection_release_time_ms: _Optional[int] = ..., request_header_start_times_ms: _Optional[_Iterable[int]] = ..., request_header_end_times_ms: _Optional[_Iterable[int]] = ..., request_body_start_times_ms: _Optional[_Iterable[int]] = ..., request_body_end_times_ms: _Optional[_Iterable[int]] = ..., response_header_start_times_ms: _Optional[_Iterable[int]] = ..., response_header_end_times_ms: _Optional[_Iterable[int]] = ..., response_body_start_times_ms: _Optional[_Iterable[int]] = ..., response_body_end_times_ms: _Optional[_Iterable[int]] = ..., call_end_time_ms: _Optional[int] = ...) -> None: ...
