from google.protobuf import any_pb2 as _any_pb2
from v2 import refresh_widget_pb2 as _refresh_widget_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class WidgetDeliveryType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    STATIC: _ClassVar[WidgetDeliveryType]
    DYNAMIC: _ClassVar[WidgetDeliveryType]
    DEFERRED: _ClassVar[WidgetDeliveryType]
    SHORT_CIRCUITED: _ClassVar[WidgetDeliveryType]
STATIC: WidgetDeliveryType
DYNAMIC: WidgetDeliveryType
DEFERRED: WidgetDeliveryType
SHORT_CIRCUITED: WidgetDeliveryType

class WidgetWrapper(_message.Message):
    __slots__ = ("template", "widget", "id", "delivery_type", "dynamic_widget_request", "deferred_widget_request", "defer_id", "unique_identifier")
    TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    WIDGET_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    DELIVERY_TYPE_FIELD_NUMBER: _ClassVar[int]
    DYNAMIC_WIDGET_REQUEST_FIELD_NUMBER: _ClassVar[int]
    DEFERRED_WIDGET_REQUEST_FIELD_NUMBER: _ClassVar[int]
    DEFER_ID_FIELD_NUMBER: _ClassVar[int]
    UNIQUE_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    template: str
    widget: _any_pb2.Any
    id: str
    delivery_type: WidgetDeliveryType
    dynamic_widget_request: _refresh_widget_pb2.RefreshWidgetRequest
    deferred_widget_request: _refresh_widget_pb2.DeferredWidgetRequest
    defer_id: str
    unique_identifier: int
    def __init__(self, template: _Optional[str] = ..., widget: _Optional[_Union[_any_pb2.Any, _Mapping]] = ..., id: _Optional[str] = ..., delivery_type: _Optional[_Union[WidgetDeliveryType, str]] = ..., dynamic_widget_request: _Optional[_Union[_refresh_widget_pb2.RefreshWidgetRequest, _Mapping]] = ..., deferred_widget_request: _Optional[_Union[_refresh_widget_pb2.DeferredWidgetRequest, _Mapping]] = ..., defer_id: _Optional[str] = ..., unique_identifier: _Optional[int] = ...) -> None: ...
