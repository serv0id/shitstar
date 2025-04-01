from google.protobuf import any_pb2 as _any_pb2
from google.protobuf import source_context_pb2 as _source_context_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Syntax(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SYNTAX_PROTO2: _ClassVar[Syntax]
    SYNTAX_PROTO3: _ClassVar[Syntax]
SYNTAX_PROTO2: Syntax
SYNTAX_PROTO3: Syntax

class Type(_message.Message):
    __slots__ = ("name", "fields", "oneofs", "options", "source_context", "syntax")
    NAME_FIELD_NUMBER: _ClassVar[int]
    FIELDS_FIELD_NUMBER: _ClassVar[int]
    ONEOFS_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    SOURCE_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    SYNTAX_FIELD_NUMBER: _ClassVar[int]
    name: str
    fields: _containers.RepeatedCompositeFieldContainer[Field]
    oneofs: _containers.RepeatedScalarFieldContainer[str]
    options: _containers.RepeatedCompositeFieldContainer[Option]
    source_context: _source_context_pb2.SourceContext
    syntax: Syntax
    def __init__(self, name: _Optional[str] = ..., fields: _Optional[_Iterable[_Union[Field, _Mapping]]] = ..., oneofs: _Optional[_Iterable[str]] = ..., options: _Optional[_Iterable[_Union[Option, _Mapping]]] = ..., source_context: _Optional[_Union[_source_context_pb2.SourceContext, _Mapping]] = ..., syntax: _Optional[_Union[Syntax, str]] = ...) -> None: ...

class Field(_message.Message):
    __slots__ = ("kind", "cardinality", "number", "name", "type_url", "oneof_index", "packed", "options", "json_name", "default_value")
    class Kind(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        TYPE_UNKNOWN: _ClassVar[Field.Kind]
        TYPE_DOUBLE: _ClassVar[Field.Kind]
        TYPE_FLOAT: _ClassVar[Field.Kind]
        TYPE_INT64: _ClassVar[Field.Kind]
        TYPE_UINT64: _ClassVar[Field.Kind]
        TYPE_INT32: _ClassVar[Field.Kind]
        TYPE_FIXED64: _ClassVar[Field.Kind]
        TYPE_FIXED32: _ClassVar[Field.Kind]
        TYPE_BOOL: _ClassVar[Field.Kind]
        TYPE_STRING: _ClassVar[Field.Kind]
        TYPE_GROUP: _ClassVar[Field.Kind]
        TYPE_MESSAGE: _ClassVar[Field.Kind]
        TYPE_BYTES: _ClassVar[Field.Kind]
        TYPE_UINT32: _ClassVar[Field.Kind]
        TYPE_ENUM: _ClassVar[Field.Kind]
        TYPE_SFIXED32: _ClassVar[Field.Kind]
        TYPE_SFIXED64: _ClassVar[Field.Kind]
        TYPE_SINT32: _ClassVar[Field.Kind]
        TYPE_SINT64: _ClassVar[Field.Kind]
    TYPE_UNKNOWN: Field.Kind
    TYPE_DOUBLE: Field.Kind
    TYPE_FLOAT: Field.Kind
    TYPE_INT64: Field.Kind
    TYPE_UINT64: Field.Kind
    TYPE_INT32: Field.Kind
    TYPE_FIXED64: Field.Kind
    TYPE_FIXED32: Field.Kind
    TYPE_BOOL: Field.Kind
    TYPE_STRING: Field.Kind
    TYPE_GROUP: Field.Kind
    TYPE_MESSAGE: Field.Kind
    TYPE_BYTES: Field.Kind
    TYPE_UINT32: Field.Kind
    TYPE_ENUM: Field.Kind
    TYPE_SFIXED32: Field.Kind
    TYPE_SFIXED64: Field.Kind
    TYPE_SINT32: Field.Kind
    TYPE_SINT64: Field.Kind
    class Cardinality(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        CARDINALITY_UNKNOWN: _ClassVar[Field.Cardinality]
        CARDINALITY_OPTIONAL: _ClassVar[Field.Cardinality]
        CARDINALITY_REQUIRED: _ClassVar[Field.Cardinality]
        CARDINALITY_REPEATED: _ClassVar[Field.Cardinality]
    CARDINALITY_UNKNOWN: Field.Cardinality
    CARDINALITY_OPTIONAL: Field.Cardinality
    CARDINALITY_REQUIRED: Field.Cardinality
    CARDINALITY_REPEATED: Field.Cardinality
    KIND_FIELD_NUMBER: _ClassVar[int]
    CARDINALITY_FIELD_NUMBER: _ClassVar[int]
    NUMBER_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    TYPE_URL_FIELD_NUMBER: _ClassVar[int]
    ONEOF_INDEX_FIELD_NUMBER: _ClassVar[int]
    PACKED_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    JSON_NAME_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_VALUE_FIELD_NUMBER: _ClassVar[int]
    kind: Field.Kind
    cardinality: Field.Cardinality
    number: int
    name: str
    type_url: str
    oneof_index: int
    packed: bool
    options: _containers.RepeatedCompositeFieldContainer[Option]
    json_name: str
    default_value: str
    def __init__(self, kind: _Optional[_Union[Field.Kind, str]] = ..., cardinality: _Optional[_Union[Field.Cardinality, str]] = ..., number: _Optional[int] = ..., name: _Optional[str] = ..., type_url: _Optional[str] = ..., oneof_index: _Optional[int] = ..., packed: bool = ..., options: _Optional[_Iterable[_Union[Option, _Mapping]]] = ..., json_name: _Optional[str] = ..., default_value: _Optional[str] = ...) -> None: ...

class Enum(_message.Message):
    __slots__ = ("name", "enumvalue", "options", "source_context", "syntax")
    NAME_FIELD_NUMBER: _ClassVar[int]
    ENUMVALUE_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    SOURCE_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    SYNTAX_FIELD_NUMBER: _ClassVar[int]
    name: str
    enumvalue: _containers.RepeatedCompositeFieldContainer[EnumValue]
    options: _containers.RepeatedCompositeFieldContainer[Option]
    source_context: _source_context_pb2.SourceContext
    syntax: Syntax
    def __init__(self, name: _Optional[str] = ..., enumvalue: _Optional[_Iterable[_Union[EnumValue, _Mapping]]] = ..., options: _Optional[_Iterable[_Union[Option, _Mapping]]] = ..., source_context: _Optional[_Union[_source_context_pb2.SourceContext, _Mapping]] = ..., syntax: _Optional[_Union[Syntax, str]] = ...) -> None: ...

class EnumValue(_message.Message):
    __slots__ = ("name", "number", "options")
    NAME_FIELD_NUMBER: _ClassVar[int]
    NUMBER_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    name: str
    number: int
    options: _containers.RepeatedCompositeFieldContainer[Option]
    def __init__(self, name: _Optional[str] = ..., number: _Optional[int] = ..., options: _Optional[_Iterable[_Union[Option, _Mapping]]] = ...) -> None: ...

class Option(_message.Message):
    __slots__ = ("name", "value")
    NAME_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    name: str
    value: _any_pb2.Any
    def __init__(self, name: _Optional[str] = ..., value: _Optional[_Union[_any_pb2.Any, _Mapping]] = ...) -> None: ...
