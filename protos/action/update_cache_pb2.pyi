from feature.commons import widget_wrapper_pb2 as _widget_wrapper_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class UpdateCacheAction(_message.Message):
    __slots__ = ("operation", "payload", "cache_identifier", "cache_id")
    class Operation(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[UpdateCacheAction.Operation]
        ADD: _ClassVar[UpdateCacheAction.Operation]
        REMOVE: _ClassVar[UpdateCacheAction.Operation]
        RESET: _ClassVar[UpdateCacheAction.Operation]
    UNSPECIFIED: UpdateCacheAction.Operation
    ADD: UpdateCacheAction.Operation
    REMOVE: UpdateCacheAction.Operation
    RESET: UpdateCacheAction.Operation
    class Payload(_message.Message):
        __slots__ = ("widget_wrapper",)
        WIDGET_WRAPPER_FIELD_NUMBER: _ClassVar[int]
        widget_wrapper: _widget_wrapper_pb2.WidgetWrapper
        def __init__(self, widget_wrapper: _Optional[_Union[_widget_wrapper_pb2.WidgetWrapper, _Mapping]] = ...) -> None: ...
    OPERATION_FIELD_NUMBER: _ClassVar[int]
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    CACHE_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    CACHE_ID_FIELD_NUMBER: _ClassVar[int]
    operation: UpdateCacheAction.Operation
    payload: UpdateCacheAction.Payload
    cache_identifier: str
    cache_id: int
    def __init__(self, operation: _Optional[_Union[UpdateCacheAction.Operation, str]] = ..., payload: _Optional[_Union[UpdateCacheAction.Payload, _Mapping]] = ..., cache_identifier: _Optional[str] = ..., cache_id: _Optional[int] = ...) -> None: ...
