from client.resilency import widget_load_failed_commons_pb2 as _widget_load_failed_commons_pb2
from google.protobuf import any_pb2 as _any_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class WidgetLoadFailedProperties(_message.Message):
    __slots__ = ("common_properties", "custom_failure_properties")
    COMMON_PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_FAILURE_PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    common_properties: _widget_load_failed_commons_pb2.WidgetLoadFailedCommons
    custom_failure_properties: _any_pb2.Any
    def __init__(self, common_properties: _Optional[_Union[_widget_load_failed_commons_pb2.WidgetLoadFailedCommons, _Mapping]] = ..., custom_failure_properties: _Optional[_Union[_any_pb2.Any, _Mapping]] = ...) -> None: ...
