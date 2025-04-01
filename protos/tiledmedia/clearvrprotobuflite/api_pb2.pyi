from google.protobuf import source_context_pb2 as _source_context_pb2
from google.protobuf import type_pb2 as _type_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Api(_message.Message):
    __slots__ = ("name", "methods", "options", "version", "source_context", "mixins", "syntax")
    NAME_FIELD_NUMBER: _ClassVar[int]
    METHODS_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    SOURCE_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    MIXINS_FIELD_NUMBER: _ClassVar[int]
    SYNTAX_FIELD_NUMBER: _ClassVar[int]
    name: str
    methods: _containers.RepeatedCompositeFieldContainer[Method]
    options: _containers.RepeatedCompositeFieldContainer[_type_pb2.Option]
    version: str
    source_context: _source_context_pb2.SourceContext
    mixins: _containers.RepeatedCompositeFieldContainer[Mixin]
    syntax: _type_pb2.Syntax
    def __init__(self, name: _Optional[str] = ..., methods: _Optional[_Iterable[_Union[Method, _Mapping]]] = ..., options: _Optional[_Iterable[_Union[_type_pb2.Option, _Mapping]]] = ..., version: _Optional[str] = ..., source_context: _Optional[_Union[_source_context_pb2.SourceContext, _Mapping]] = ..., mixins: _Optional[_Iterable[_Union[Mixin, _Mapping]]] = ..., syntax: _Optional[_Union[_type_pb2.Syntax, str]] = ...) -> None: ...

class Method(_message.Message):
    __slots__ = ("name", "request_type_url", "request_streaming", "response_type_url", "response_streaming", "options", "syntax")
    NAME_FIELD_NUMBER: _ClassVar[int]
    REQUEST_TYPE_URL_FIELD_NUMBER: _ClassVar[int]
    REQUEST_STREAMING_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_TYPE_URL_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_STREAMING_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    SYNTAX_FIELD_NUMBER: _ClassVar[int]
    name: str
    request_type_url: str
    request_streaming: bool
    response_type_url: str
    response_streaming: bool
    options: _containers.RepeatedCompositeFieldContainer[_type_pb2.Option]
    syntax: _type_pb2.Syntax
    def __init__(self, name: _Optional[str] = ..., request_type_url: _Optional[str] = ..., request_streaming: bool = ..., response_type_url: _Optional[str] = ..., response_streaming: bool = ..., options: _Optional[_Iterable[_Union[_type_pb2.Option, _Mapping]]] = ..., syntax: _Optional[_Union[_type_pb2.Syntax, str]] = ...) -> None: ...

class Mixin(_message.Message):
    __slots__ = ("name", "root")
    NAME_FIELD_NUMBER: _ClassVar[int]
    ROOT_FIELD_NUMBER: _ClassVar[int]
    name: str
    root: str
    def __init__(self, name: _Optional[str] = ..., root: _Optional[str] = ...) -> None: ...
