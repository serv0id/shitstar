from component.identity import enum_pb2 as _enum_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SnaEventProps(_message.Message):
    __slots__ = ("vendor", "response", "response_time", "country_prefix", "force_mobile_data_usage")
    VENDOR_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_TIME_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_PREFIX_FIELD_NUMBER: _ClassVar[int]
    FORCE_MOBILE_DATA_USAGE_FIELD_NUMBER: _ClassVar[int]
    vendor: _enum_pb2.SnaVendorType
    response: str
    response_time: float
    country_prefix: str
    force_mobile_data_usage: bool
    def __init__(self, vendor: _Optional[_Union[_enum_pb2.SnaVendorType, str]] = ..., response: _Optional[str] = ..., response_time: _Optional[float] = ..., country_prefix: _Optional[str] = ..., force_mobile_data_usage: bool = ...) -> None: ...
