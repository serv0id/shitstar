from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class LocationSource(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    UNKNOWN_SOURCE: _ClassVar[LocationSource]
    NETACUITY: _ClassVar[LocationSource]
    AKAMAI: _ClassVar[LocationSource]
    LOCATION_VIEW_CURRENT_LOC: _ClassVar[LocationSource]
    LOCATION_VIEW_EXTERNAL_TRACKER: _ClassVar[LocationSource]
UNKNOWN_SOURCE: LocationSource
NETACUITY: LocationSource
AKAMAI: LocationSource
LOCATION_VIEW_CURRENT_LOC: LocationSource
LOCATION_VIEW_EXTERNAL_TRACKER: LocationSource

class DeviceLocation(_message.Message):
    __slots__ = ("city", "pincode", "state", "country", "preferred_source", "data")
    class DataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: LocationData
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[LocationData, _Mapping]] = ...) -> None: ...
    CITY_FIELD_NUMBER: _ClassVar[int]
    PINCODE_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_FIELD_NUMBER: _ClassVar[int]
    PREFERRED_SOURCE_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    city: str
    pincode: str
    state: str
    country: str
    preferred_source: LocationSource
    data: _containers.MessageMap[int, LocationData]
    def __init__(self, city: _Optional[str] = ..., pincode: _Optional[str] = ..., state: _Optional[str] = ..., country: _Optional[str] = ..., preferred_source: _Optional[_Union[LocationSource, str]] = ..., data: _Optional[_Mapping[int, LocationData]] = ...) -> None: ...

class LocationData(_message.Message):
    __slots__ = ("city", "state", "country", "pincode", "country_code", "lat", "long", "city_std", "state_std")
    CITY_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_FIELD_NUMBER: _ClassVar[int]
    PINCODE_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_CODE_FIELD_NUMBER: _ClassVar[int]
    LAT_FIELD_NUMBER: _ClassVar[int]
    LONG_FIELD_NUMBER: _ClassVar[int]
    CITY_STD_FIELD_NUMBER: _ClassVar[int]
    STATE_STD_FIELD_NUMBER: _ClassVar[int]
    city: str
    state: str
    country: str
    pincode: str
    country_code: str
    lat: str
    long: str
    city_std: str
    state_std: str
    def __init__(self, city: _Optional[str] = ..., state: _Optional[str] = ..., country: _Optional[str] = ..., pincode: _Optional[str] = ..., country_code: _Optional[str] = ..., lat: _Optional[str] = ..., long: _Optional[str] = ..., city_std: _Optional[str] = ..., state_std: _Optional[str] = ...) -> None: ...
