from v2 import refresh_widget_pb2 as _refresh_widget_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class RefreshSpaceRequest(_message.Message):
    __slots__ = ("space_id", "space_url", "widget_requests")
    SPACE_ID_FIELD_NUMBER: _ClassVar[int]
    SPACE_URL_FIELD_NUMBER: _ClassVar[int]
    WIDGET_REQUESTS_FIELD_NUMBER: _ClassVar[int]
    space_id: str
    space_url: str
    widget_requests: _containers.RepeatedCompositeFieldContainer[_refresh_widget_pb2.RefreshWidgetRequest]
    def __init__(self, space_id: _Optional[str] = ..., space_url: _Optional[str] = ..., widget_requests: _Optional[_Iterable[_Union[_refresh_widget_pb2.RefreshWidgetRequest, _Mapping]]] = ...) -> None: ...

class DeferredSpaceRequest(_message.Message):
    __slots__ = ("space_url", "widget_requests")
    SPACE_URL_FIELD_NUMBER: _ClassVar[int]
    WIDGET_REQUESTS_FIELD_NUMBER: _ClassVar[int]
    space_url: str
    widget_requests: _containers.RepeatedCompositeFieldContainer[_refresh_widget_pb2.DeferredWidgetRequest]
    def __init__(self, space_url: _Optional[str] = ..., widget_requests: _Optional[_Iterable[_Union[_refresh_widget_pb2.DeferredWidgetRequest, _Mapping]]] = ...) -> None: ...
