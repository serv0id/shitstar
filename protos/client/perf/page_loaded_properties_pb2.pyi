from client.perf import page_loaded_commons_pb2 as _page_loaded_commons_pb2
from client.perf import watch_page_loaded_properties_v2_pb2 as _watch_page_loaded_properties_v2_pb2
from client.preload import preload_journey_pb2 as _preload_journey_pb2
from google.protobuf import any_pb2 as _any_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PageLoadedProperties(_message.Message):
    __slots__ = ("common_properties", "custom_page_properties", "preload_source", "watch_page_loaded_properties")
    COMMON_PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_PAGE_PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    PRELOAD_SOURCE_FIELD_NUMBER: _ClassVar[int]
    WATCH_PAGE_LOADED_PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    common_properties: _page_loaded_commons_pb2.PageLoadedCommons
    custom_page_properties: _any_pb2.Any
    preload_source: _preload_journey_pb2.PreloadSource
    watch_page_loaded_properties: _watch_page_loaded_properties_v2_pb2.WatchPageLoadedPropertiesV2
    def __init__(self, common_properties: _Optional[_Union[_page_loaded_commons_pb2.PageLoadedCommons, _Mapping]] = ..., custom_page_properties: _Optional[_Union[_any_pb2.Any, _Mapping]] = ..., preload_source: _Optional[_Union[_preload_journey_pb2.PreloadSource, _Mapping]] = ..., watch_page_loaded_properties: _Optional[_Union[_watch_page_loaded_properties_v2_pb2.WatchPageLoadedPropertiesV2, _Mapping]] = ...) -> None: ...
