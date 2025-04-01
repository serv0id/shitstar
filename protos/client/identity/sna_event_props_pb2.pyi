from component.identity import sna_event_props_pb2 as _sna_event_props_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SnaEventPropsWrapper(_message.Message):
    __slots__ = ("sna_event_properties",)
    SNA_EVENT_PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    sna_event_properties: _sna_event_props_pb2.SnaEventProps
    def __init__(self, sna_event_properties: _Optional[_Union[_sna_event_props_pb2.SnaEventProps, _Mapping]] = ...) -> None: ...
