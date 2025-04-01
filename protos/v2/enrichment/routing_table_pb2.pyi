from google.protobuf import any_pb2 as _any_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class RoutingTable(_message.Message):
    __slots__ = ("routing_table", "cache_metadata")
    class RoutingTableEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: RoutingTable.Operations
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[RoutingTable.Operations, _Mapping]] = ...) -> None: ...
    class CacheMetadataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _any_pb2.Any
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[_any_pb2.Any, _Mapping]] = ...) -> None: ...
    class Operations(_message.Message):
        __slots__ = ("replace", "query_params", "domain")
        class Replace(_message.Message):
            __slots__ = ("to_replace", "replace_with")
            TO_REPLACE_FIELD_NUMBER: _ClassVar[int]
            REPLACE_WITH_FIELD_NUMBER: _ClassVar[int]
            to_replace: str
            replace_with: str
            def __init__(self, to_replace: _Optional[str] = ..., replace_with: _Optional[str] = ...) -> None: ...
        class QueryParam(_message.Message):
            __slots__ = ("key", "value")
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: str
            value: str
            def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
        REPLACE_FIELD_NUMBER: _ClassVar[int]
        QUERY_PARAMS_FIELD_NUMBER: _ClassVar[int]
        DOMAIN_FIELD_NUMBER: _ClassVar[int]
        replace: RoutingTable.Operations.Replace
        query_params: _containers.RepeatedCompositeFieldContainer[RoutingTable.Operations.QueryParam]
        domain: str
        def __init__(self, replace: _Optional[_Union[RoutingTable.Operations.Replace, _Mapping]] = ..., query_params: _Optional[_Iterable[_Union[RoutingTable.Operations.QueryParam, _Mapping]]] = ..., domain: _Optional[str] = ...) -> None: ...
    ROUTING_TABLE_FIELD_NUMBER: _ClassVar[int]
    CACHE_METADATA_FIELD_NUMBER: _ClassVar[int]
    routing_table: _containers.MessageMap[str, RoutingTable.Operations]
    cache_metadata: _containers.MessageMap[str, _any_pb2.Any]
    def __init__(self, routing_table: _Optional[_Mapping[str, RoutingTable.Operations]] = ..., cache_metadata: _Optional[_Mapping[str, _any_pb2.Any]] = ...) -> None: ...
