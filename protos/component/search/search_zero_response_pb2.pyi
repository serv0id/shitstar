from component.search import search_response_pb2 as _search_response_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SearchZeroResponseProperties(_message.Message):
    __slots__ = ("response_type", "total_results_count")
    RESPONSE_TYPE_FIELD_NUMBER: _ClassVar[int]
    TOTAL_RESULTS_COUNT_FIELD_NUMBER: _ClassVar[int]
    response_type: _search_response_pb2.ResponseType
    total_results_count: int
    def __init__(self, response_type: _Optional[_Union[_search_response_pb2.ResponseType, str]] = ..., total_results_count: _Optional[int] = ...) -> None: ...
