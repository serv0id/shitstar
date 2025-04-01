from client.ads import ad_slot_pb2 as _ad_slot_pb2
from options import opts_pb2 as _opts_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Received(_message.Message):
    __slots__ = ("response_time", "received_count", "received_type_list", "response_time_ms", "received_ad_slots")
    RESPONSE_TIME_FIELD_NUMBER: _ClassVar[int]
    RECEIVED_COUNT_FIELD_NUMBER: _ClassVar[int]
    RECEIVED_TYPE_LIST_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_TIME_MS_FIELD_NUMBER: _ClassVar[int]
    RECEIVED_AD_SLOTS_FIELD_NUMBER: _ClassVar[int]
    response_time: int
    received_count: int
    received_type_list: str
    response_time_ms: int
    received_ad_slots: _containers.RepeatedCompositeFieldContainer[_ad_slot_pb2.AdSlot]
    def __init__(self, response_time: _Optional[int] = ..., received_count: _Optional[int] = ..., received_type_list: _Optional[str] = ..., response_time_ms: _Optional[int] = ..., received_ad_slots: _Optional[_Iterable[_Union[_ad_slot_pb2.AdSlot, _Mapping]]] = ...) -> None: ...
