from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AdEventType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    AD_EVENT_TYPE_UNSPECIFIED: _ClassVar[AdEventType]
    AD_EVENT_TYPE_IMPRESSION: _ClassVar[AdEventType]
    AD_EVENT_TYPE_Q25: _ClassVar[AdEventType]
    AD_EVENT_TYPE_Q50: _ClassVar[AdEventType]
    AD_EVENT_TYPE_Q75: _ClassVar[AdEventType]
    AD_EVENT_TYPE_Q100: _ClassVar[AdEventType]
    AD_EVENT_TYPE_CLICK: _ClassVar[AdEventType]
AD_EVENT_TYPE_UNSPECIFIED: AdEventType
AD_EVENT_TYPE_IMPRESSION: AdEventType
AD_EVENT_TYPE_Q25: AdEventType
AD_EVENT_TYPE_Q50: AdEventType
AD_EVENT_TYPE_Q75: AdEventType
AD_EVENT_TYPE_Q100: AdEventType
AD_EVENT_TYPE_CLICK: AdEventType

class AdEvent(_message.Message):
    __slots__ = ("event_type", "ca_id", "ts_occurred_ms")
    EVENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    CA_ID_FIELD_NUMBER: _ClassVar[int]
    TS_OCCURRED_MS_FIELD_NUMBER: _ClassVar[int]
    event_type: AdEventType
    ca_id: str
    ts_occurred_ms: int
    def __init__(self, event_type: _Optional[_Union[AdEventType, str]] = ..., ca_id: _Optional[str] = ..., ts_occurred_ms: _Optional[int] = ...) -> None: ...
