from google.protobuf import descriptor_pb2 as _descriptor_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor
PROPERTY_FIELD_NUMBER: _ClassVar[int]
property: _descriptor.FieldDescriptor
CHILD_FIELDS_PREFIX_FIELD_NUMBER: _ClassVar[int]
child_fields_prefix: _descriptor.FieldDescriptor
DATA_LAKE_COLUMN_NAME_FIELD_NUMBER: _ClassVar[int]
data_lake_column_name: _descriptor.FieldDescriptor
EVENT_FIELD_NUMBER: _ClassVar[int]
event: _descriptor.FieldDescriptor
JSON_FIELD_PREFIX_FIELD_NUMBER: _ClassVar[int]
json_field_prefix: _descriptor.FieldDescriptor

class PropertyOptions(_message.Message):
    __slots__ = ("is_pii", "description", "is_traits", "json_path")
    IS_PII_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    IS_TRAITS_FIELD_NUMBER: _ClassVar[int]
    JSON_PATH_FIELD_NUMBER: _ClassVar[int]
    is_pii: bool
    description: str
    is_traits: bool
    json_path: str
    def __init__(self, is_pii: bool = ..., description: _Optional[str] = ..., is_traits: bool = ..., json_path: _Optional[str] = ...) -> None: ...

class EventOptions(_message.Message):
    __slots__ = ("is_native", "description")
    IS_NATIVE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    is_native: bool
    description: str
    def __init__(self, is_native: bool = ..., description: _Optional[str] = ...) -> None: ...
