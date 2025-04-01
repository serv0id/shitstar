from feature.request import http_request_commons_pb2 as _http_request_commons_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TokenIdentifier(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    UNKNOWN: _ClassVar[TokenIdentifier]
    JIT: _ClassVar[TokenIdentifier]
UNKNOWN: TokenIdentifier
JIT: TokenIdentifier

class HttpTokenRequest(_message.Message):
    __slots__ = ("identifier", "request")
    IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    REQUEST_FIELD_NUMBER: _ClassVar[int]
    identifier: TokenIdentifier
    request: _http_request_commons_pb2.HttpRequestCommons
    def __init__(self, identifier: _Optional[_Union[TokenIdentifier, str]] = ..., request: _Optional[_Union[_http_request_commons_pb2.HttpRequestCommons, _Mapping]] = ...) -> None: ...
