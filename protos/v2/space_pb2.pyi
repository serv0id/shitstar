from protos.v2 import widget_pb2 as _widget_pb2
from protos.v2 import refresh_space_pb2 as _refresh_space_pb2
from google.protobuf import any_pb2 as _any_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Space(_message.Message):
    __slots__ = ["id", "template", "version", "widget_wrappers", "data", "delivery_type", "dynamic_space_request", "deferred_space_request"]
    class SpaceDeliveryType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
        STATIC: _ClassVar[Space.SpaceDeliveryType]
        DYNAMIC: _ClassVar[Space.SpaceDeliveryType]
    STATIC: Space.SpaceDeliveryType
    DYNAMIC: Space.SpaceDeliveryType
    ID_FIELD_NUMBER: _ClassVar[int]
    TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    WIDGET_WRAPPERS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    DELIVERY_TYPE_FIELD_NUMBER: _ClassVar[int]
    DYNAMIC_SPACE_REQUEST_FIELD_NUMBER: _ClassVar[int]
    DEFERRED_SPACE_REQUEST_FIELD_NUMBER: _ClassVar[int]
    id: str
    template: str
    version: str
    widget_wrappers: _containers.RepeatedCompositeFieldContainer[_widget_pb2.WidgetWrapper]
    data: _any_pb2.Any
    delivery_type: Space.SpaceDeliveryType
    dynamic_space_request: _refresh_space_pb2.RefreshSpaceRequest
    deferred_space_request: _refresh_space_pb2.DeferredSpaceRequest
    def __init__(self, id: _Optional[str] = ..., template: _Optional[str] = ..., version: _Optional[str] = ..., widget_wrappers: _Optional[_Iterable[_Union[_widget_pb2.WidgetWrapper, _Mapping]]] = ..., data: _Optional[_Union[_any_pb2.Any, _Mapping]] = ..., delivery_type: _Optional[_Union[Space.SpaceDeliveryType, str]] = ..., dynamic_space_request: _Optional[_Union[_refresh_space_pb2.RefreshSpaceRequest, _Mapping]] = ..., deferred_space_request: _Optional[_Union[_refresh_space_pb2.DeferredSpaceRequest, _Mapping]] = ...) -> None: ...
