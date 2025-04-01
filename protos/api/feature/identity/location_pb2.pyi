from options import opts_pb2 as _opts_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Location(_message.Message):
    __slots__ = ("country", "region_code", "city", "lat", "long", "ip_address", "asn_number", "pincode", "location_source")
    class LocationSource(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        LOCATION_SOURCE_UNSPECIFIED: _ClassVar[Location.LocationSource]
        LOCATION_SOURCE_NETACUITY: _ClassVar[Location.LocationSource]
        LOCATION_SOURCE_AKAMAI: _ClassVar[Location.LocationSource]
    LOCATION_SOURCE_UNSPECIFIED: Location.LocationSource
    LOCATION_SOURCE_NETACUITY: Location.LocationSource
    LOCATION_SOURCE_AKAMAI: Location.LocationSource
    COUNTRY_FIELD_NUMBER: _ClassVar[int]
    REGION_CODE_FIELD_NUMBER: _ClassVar[int]
    CITY_FIELD_NUMBER: _ClassVar[int]
    LAT_FIELD_NUMBER: _ClassVar[int]
    LONG_FIELD_NUMBER: _ClassVar[int]
    IP_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    ASN_NUMBER_FIELD_NUMBER: _ClassVar[int]
    PINCODE_FIELD_NUMBER: _ClassVar[int]
    LOCATION_SOURCE_FIELD_NUMBER: _ClassVar[int]
    country: str
    region_code: str
    city: str
    lat: float
    long: float
    ip_address: str
    asn_number: int
    pincode: str
    location_source: Location.LocationSource
    def __init__(self, country: _Optional[str] = ..., region_code: _Optional[str] = ..., city: _Optional[str] = ..., lat: _Optional[float] = ..., long: _Optional[float] = ..., ip_address: _Optional[str] = ..., asn_number: _Optional[int] = ..., pincode: _Optional[str] = ..., location_source: _Optional[_Union[Location.LocationSource, str]] = ...) -> None: ...
