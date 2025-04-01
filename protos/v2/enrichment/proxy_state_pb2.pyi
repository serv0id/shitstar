from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ProxyState(_message.Message):
    __slots__ = ("ttl_sec", "issue_at", "entity_level", "num", "data")
    class EntityLevel(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[ProxyState.EntityLevel]
        HID_LEVEL: _ClassVar[ProxyState.EntityLevel]
        PID_LEVEL: _ClassVar[ProxyState.EntityLevel]
        DEVICE_LEVEL: _ClassVar[ProxyState.EntityLevel]
    UNSPECIFIED: ProxyState.EntityLevel
    HID_LEVEL: ProxyState.EntityLevel
    PID_LEVEL: ProxyState.EntityLevel
    DEVICE_LEVEL: ProxyState.EntityLevel
    TTL_SEC_FIELD_NUMBER: _ClassVar[int]
    ISSUE_AT_FIELD_NUMBER: _ClassVar[int]
    ENTITY_LEVEL_FIELD_NUMBER: _ClassVar[int]
    NUM_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    ttl_sec: int
    issue_at: int
    entity_level: ProxyState.EntityLevel
    num: int
    data: bytes
    def __init__(self, ttl_sec: _Optional[int] = ..., issue_at: _Optional[int] = ..., entity_level: _Optional[_Union[ProxyState.EntityLevel, str]] = ..., num: _Optional[int] = ..., data: _Optional[bytes] = ...) -> None: ...
