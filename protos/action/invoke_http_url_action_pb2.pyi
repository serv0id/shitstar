from feature.request import http_request_commons_pb2 as _http_request_commons_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class InvokeHttpUrlAction(_message.Message):
    __slots__ = ("request_commons",)
    REQUEST_COMMONS_FIELD_NUMBER: _ClassVar[int]
    request_commons: _http_request_commons_pb2.HttpRequestCommons
    def __init__(self, request_commons: _Optional[_Union[_http_request_commons_pb2.HttpRequestCommons, _Mapping]] = ...) -> None: ...
