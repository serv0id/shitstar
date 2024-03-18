from base import analytics_pb2 as _analytics_pb2
from base import actions_pb2 as _actions_pb2
from feature.app_event import app_event_pb2 as _app_event_pb2
from feature.refresh import refresh_info_pb2 as _refresh_info_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PageDataCommons(_message.Message):
    __slots__ = ["instrumentation", "url", "invalidate_on", "refresh_api_url", "actions", "refresh_info"]
    INSTRUMENTATION_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    INVALIDATE_ON_FIELD_NUMBER: _ClassVar[int]
    REFRESH_API_URL_FIELD_NUMBER: _ClassVar[int]
    ACTIONS_FIELD_NUMBER: _ClassVar[int]
    REFRESH_INFO_FIELD_NUMBER: _ClassVar[int]
    instrumentation: _analytics_pb2.Instrumentation
    url: str
    invalidate_on: _containers.RepeatedScalarFieldContainer[_app_event_pb2.AppEvent]
    refresh_api_url: str
    actions: _actions_pb2.Actions
    refresh_info: _refresh_info_pb2.RefreshInfo
    def __init__(self, instrumentation: _Optional[_Union[_analytics_pb2.Instrumentation, _Mapping]] = ..., url: _Optional[str] = ..., invalidate_on: _Optional[_Iterable[_Union[_app_event_pb2.AppEvent, str]]] = ..., refresh_api_url: _Optional[str] = ..., actions: _Optional[_Union[_actions_pb2.Actions, _Mapping]] = ..., refresh_info: _Optional[_Union[_refresh_info_pb2.RefreshInfo, _Mapping]] = ...) -> None: ...
