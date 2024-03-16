from protos.v2 import refresh_space_pb2 as _refresh_space_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class RefreshPageRequest(_message.Message):
    __slots__ = ["page_url", "space_requests"]
    PAGE_URL_FIELD_NUMBER: _ClassVar[int]
    SPACE_REQUESTS_FIELD_NUMBER: _ClassVar[int]
    page_url: str
    space_requests: _containers.RepeatedCompositeFieldContainer[_refresh_space_pb2.RefreshSpaceRequest]
    def __init__(self, page_url: _Optional[str] = ..., space_requests: _Optional[_Iterable[_Union[_refresh_space_pb2.RefreshSpaceRequest, _Mapping]]] = ...) -> None: ...

class DeferredPageRequest(_message.Message):
    __slots__ = ["page_url", "page_slug", "space_requests"]
    PAGE_URL_FIELD_NUMBER: _ClassVar[int]
    PAGE_SLUG_FIELD_NUMBER: _ClassVar[int]
    SPACE_REQUESTS_FIELD_NUMBER: _ClassVar[int]
    page_url: str
    page_slug: str
    space_requests: _containers.RepeatedCompositeFieldContainer[_refresh_space_pb2.DeferredSpaceRequest]
    def __init__(self, page_url: _Optional[str] = ..., page_slug: _Optional[str] = ..., space_requests: _Optional[_Iterable[_Union[_refresh_space_pb2.DeferredSpaceRequest, _Mapping]]] = ...) -> None: ...
