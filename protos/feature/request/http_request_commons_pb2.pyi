from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class HttpRequestCommons(_message.Message):
    __slots__ = ["url", "request_type", "headers", "body", "attach_default_headers"]
    class HttpRequestType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
        GET: _ClassVar[HttpRequestCommons.HttpRequestType]
        POST: _ClassVar[HttpRequestCommons.HttpRequestType]
        PUT: _ClassVar[HttpRequestCommons.HttpRequestType]
    GET: HttpRequestCommons.HttpRequestType
    POST: HttpRequestCommons.HttpRequestType
    PUT: HttpRequestCommons.HttpRequestType
    class HttpHeader(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    URL_FIELD_NUMBER: _ClassVar[int]
    REQUEST_TYPE_FIELD_NUMBER: _ClassVar[int]
    HEADERS_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    ATTACH_DEFAULT_HEADERS_FIELD_NUMBER: _ClassVar[int]
    url: str
    request_type: HttpRequestCommons.HttpRequestType
    headers: _containers.RepeatedCompositeFieldContainer[HttpRequestCommons.HttpHeader]
    body: bytes
    attach_default_headers: bool
    def __init__(self, url: _Optional[str] = ..., request_type: _Optional[_Union[HttpRequestCommons.HttpRequestType, str]] = ..., headers: _Optional[_Iterable[_Union[HttpRequestCommons.HttpHeader, _Mapping]]] = ..., body: _Optional[bytes] = ..., attach_default_headers: bool = ...) -> None: ...
