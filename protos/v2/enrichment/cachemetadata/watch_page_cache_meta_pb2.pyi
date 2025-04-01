from v2.enrichment.cachemetadata import unified_cache_meta_pb2 as _unified_cache_meta_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class WatchPageCacheMeta(_message.Message):
    __slots__ = ("is_logged_in", "is_free", "client_capabilities", "ab_group_ids", "cdn_distribution_key", "max_resolution")
    IS_LOGGED_IN_FIELD_NUMBER: _ClassVar[int]
    IS_FREE_FIELD_NUMBER: _ClassVar[int]
    CLIENT_CAPABILITIES_FIELD_NUMBER: _ClassVar[int]
    AB_GROUP_IDS_FIELD_NUMBER: _ClassVar[int]
    CDN_DISTRIBUTION_KEY_FIELD_NUMBER: _ClassVar[int]
    MAX_RESOLUTION_FIELD_NUMBER: _ClassVar[int]
    is_logged_in: bool
    is_free: bool
    client_capabilities: _unified_cache_meta_pb2.ClientCapabilities
    ab_group_ids: _containers.RepeatedScalarFieldContainer[str]
    cdn_distribution_key: int
    max_resolution: str
    def __init__(self, is_logged_in: bool = ..., is_free: bool = ..., client_capabilities: _Optional[_Union[_unified_cache_meta_pb2.ClientCapabilities, _Mapping]] = ..., ab_group_ids: _Optional[_Iterable[str]] = ..., cdn_distribution_key: _Optional[int] = ..., max_resolution: _Optional[str] = ...) -> None: ...
