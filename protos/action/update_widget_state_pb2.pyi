from feature.commons import widget_wrapper_pb2 as _widget_wrapper_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class UpdateWidgetStateAction(_message.Message):
    __slots__ = ("operation", "payload", "unique_identifier")
    class Operation(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[UpdateWidgetStateAction.Operation]
        ADD: _ClassVar[UpdateWidgetStateAction.Operation]
        REMOVE: _ClassVar[UpdateWidgetStateAction.Operation]
        RESET: _ClassVar[UpdateWidgetStateAction.Operation]
        UPDATE: _ClassVar[UpdateWidgetStateAction.Operation]
    UNSPECIFIED: UpdateWidgetStateAction.Operation
    ADD: UpdateWidgetStateAction.Operation
    REMOVE: UpdateWidgetStateAction.Operation
    RESET: UpdateWidgetStateAction.Operation
    UPDATE: UpdateWidgetStateAction.Operation
    class Payload(_message.Message):
        __slots__ = ("widget_wrapper",)
        WIDGET_WRAPPER_FIELD_NUMBER: _ClassVar[int]
        widget_wrapper: _widget_wrapper_pb2.WidgetWrapper
        def __init__(self, widget_wrapper: _Optional[_Union[_widget_wrapper_pb2.WidgetWrapper, _Mapping]] = ...) -> None: ...
    OPERATION_FIELD_NUMBER: _ClassVar[int]
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    UNIQUE_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    operation: UpdateWidgetStateAction.Operation
    payload: UpdateWidgetStateAction.Payload
    unique_identifier: int
    def __init__(self, operation: _Optional[_Union[UpdateWidgetStateAction.Operation, str]] = ..., payload: _Optional[_Union[UpdateWidgetStateAction.Payload, _Mapping]] = ..., unique_identifier: _Optional[int] = ...) -> None: ...
