from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class UpsertRoutingTableQueryParamAction(_message.Message):
    __slots__ = ["routing_key", "query_params"]
    class QueryParam(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    ROUTING_KEY_FIELD_NUMBER: _ClassVar[int]
    QUERY_PARAMS_FIELD_NUMBER: _ClassVar[int]
    routing_key: str
    query_params: _containers.RepeatedCompositeFieldContainer[UpsertRoutingTableQueryParamAction.QueryParam]
    def __init__(self, routing_key: _Optional[str] = ..., query_params: _Optional[_Iterable[_Union[UpsertRoutingTableQueryParamAction.QueryParam, _Mapping]]] = ...) -> None: ...
