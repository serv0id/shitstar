from google.protobuf import any_pb2 as _any_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CustomProperty(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CUSTOM_PROPERTY_UNSPECIFIED: _ClassVar[CustomProperty]
    CUSTOM_PROPERTY_WIDGET_POSITION: _ClassVar[CustomProperty]
    CUSTOM_PROPERTY_WATCH_NEXT_SEGMENT: _ClassVar[CustomProperty]
    CUSTOM_PROPERTY_CACHED_RESPONSE: _ClassVar[CustomProperty]
CUSTOM_PROPERTY_UNSPECIFIED: CustomProperty
CUSTOM_PROPERTY_WIDGET_POSITION: CustomProperty
CUSTOM_PROPERTY_WATCH_NEXT_SEGMENT: CustomProperty
CUSTOM_PROPERTY_CACHED_RESPONSE: CustomProperty

class Context(_message.Message):
    __slots__ = ("page", "space", "widget", "page_context", "space_context", "widget_context", "position", "custom_properties")
    PAGE_FIELD_NUMBER: _ClassVar[int]
    SPACE_FIELD_NUMBER: _ClassVar[int]
    WIDGET_FIELD_NUMBER: _ClassVar[int]
    PAGE_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    SPACE_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    WIDGET_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    POSITION_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    page: _any_pb2.Any
    space: _any_pb2.Any
    widget: _any_pb2.Any
    page_context: InstrumentationContext
    space_context: InstrumentationContext
    widget_context: InstrumentationContext
    position: Position
    custom_properties: _containers.RepeatedCompositeFieldContainer[MetaInfo]
    def __init__(self, page: _Optional[_Union[_any_pb2.Any, _Mapping]] = ..., space: _Optional[_Union[_any_pb2.Any, _Mapping]] = ..., widget: _Optional[_Union[_any_pb2.Any, _Mapping]] = ..., page_context: _Optional[_Union[InstrumentationContext, _Mapping]] = ..., space_context: _Optional[_Union[InstrumentationContext, _Mapping]] = ..., widget_context: _Optional[_Union[InstrumentationContext, _Mapping]] = ..., position: _Optional[_Union[Position, _Mapping]] = ..., custom_properties: _Optional[_Iterable[_Union[MetaInfo, _Mapping]]] = ...) -> None: ...

class InstrumentationContext(_message.Message):
    __slots__ = ("url", "value")
    URL_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    url: str
    value: bytes
    def __init__(self, url: _Optional[str] = ..., value: _Optional[bytes] = ...) -> None: ...

class Position(_message.Message):
    __slots__ = ("template_name", "position", "entity_type", "parent_position")
    class EntityType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ENTITY_TYPE_UNSPECIFIED: _ClassVar[Position.EntityType]
        ENTITY_TYPE_PAGE: _ClassVar[Position.EntityType]
        ENTITY_TYPE_SPACE: _ClassVar[Position.EntityType]
        ENTITY_TYPE_WIDGET: _ClassVar[Position.EntityType]
    ENTITY_TYPE_UNSPECIFIED: Position.EntityType
    ENTITY_TYPE_PAGE: Position.EntityType
    ENTITY_TYPE_SPACE: Position.EntityType
    ENTITY_TYPE_WIDGET: Position.EntityType
    TEMPLATE_NAME_FIELD_NUMBER: _ClassVar[int]
    POSITION_FIELD_NUMBER: _ClassVar[int]
    ENTITY_TYPE_FIELD_NUMBER: _ClassVar[int]
    PARENT_POSITION_FIELD_NUMBER: _ClassVar[int]
    template_name: str
    position: int
    entity_type: Position.EntityType
    parent_position: Position
    def __init__(self, template_name: _Optional[str] = ..., position: _Optional[int] = ..., entity_type: _Optional[_Union[Position.EntityType, str]] = ..., parent_position: _Optional[_Union[Position, _Mapping]] = ...) -> None: ...

class MetaInfo(_message.Message):
    __slots__ = ("key", "value")
    KEY_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    key: CustomProperty
    value: _any_pb2.Any
    def __init__(self, key: _Optional[_Union[CustomProperty, str]] = ..., value: _Optional[_Union[_any_pb2.Any, _Mapping]] = ...) -> None: ...
