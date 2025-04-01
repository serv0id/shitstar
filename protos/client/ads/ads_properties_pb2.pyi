from client.ads import common_pb2 as _common_pb2
from client.ads import error_pb2 as _error_pb2
from client.ads import play_error_pb2 as _play_error_pb2
from client.ads import received_pb2 as _received_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AdsProperties(_message.Message):
    __slots__ = ("user_segments", "pid", "aaid", "aaid_lat", "idfa", "idfa_lat", "common_properties", "received_properties", "error_properties", "play_error_properties")
    USER_SEGMENTS_FIELD_NUMBER: _ClassVar[int]
    PID_FIELD_NUMBER: _ClassVar[int]
    AAID_FIELD_NUMBER: _ClassVar[int]
    AAID_LAT_FIELD_NUMBER: _ClassVar[int]
    IDFA_FIELD_NUMBER: _ClassVar[int]
    IDFA_LAT_FIELD_NUMBER: _ClassVar[int]
    COMMON_PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    RECEIVED_PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    ERROR_PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    PLAY_ERROR_PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    user_segments: _containers.RepeatedScalarFieldContainer[str]
    pid: str
    aaid: str
    aaid_lat: str
    idfa: str
    idfa_lat: str
    common_properties: _common_pb2.Common
    received_properties: _received_pb2.Received
    error_properties: _error_pb2.Error
    play_error_properties: _play_error_pb2.PlayError
    def __init__(self, user_segments: _Optional[_Iterable[str]] = ..., pid: _Optional[str] = ..., aaid: _Optional[str] = ..., aaid_lat: _Optional[str] = ..., idfa: _Optional[str] = ..., idfa_lat: _Optional[str] = ..., common_properties: _Optional[_Union[_common_pb2.Common, _Mapping]] = ..., received_properties: _Optional[_Union[_received_pb2.Received, _Mapping]] = ..., error_properties: _Optional[_Union[_error_pb2.Error, _Mapping]] = ..., play_error_properties: _Optional[_Union[_play_error_pb2.PlayError, _Mapping]] = ...) -> None: ...
