from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class NetworkType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    NETWORK_TYPE_UNSPECIFIED: _ClassVar[NetworkType]
    NETWORK_TYPE_OFFLINE: _ClassVar[NetworkType]
    NETWORK_TYPE_2G: _ClassVar[NetworkType]
    NETWORK_TYPE_3G: _ClassVar[NetworkType]
    NETWORK_TYPE_4G: _ClassVar[NetworkType]
    NETWORK_TYPE_5G: _ClassVar[NetworkType]
    NETWORK_TYPE_WIFI: _ClassVar[NetworkType]
NETWORK_TYPE_UNSPECIFIED: NetworkType
NETWORK_TYPE_OFFLINE: NetworkType
NETWORK_TYPE_2G: NetworkType
NETWORK_TYPE_3G: NetworkType
NETWORK_TYPE_4G: NetworkType
NETWORK_TYPE_5G: NetworkType
NETWORK_TYPE_WIFI: NetworkType

class NetworkInfo(_message.Message):
    __slots__ = ("is_wifi_on", "wifi_ssid", "is_cellular_on", "cellular_mcc_mnc", "asn", "network_type", "is_bluetooth_on", "network_speed_kbps", "carrier")
    IS_WIFI_ON_FIELD_NUMBER: _ClassVar[int]
    WIFI_SSID_FIELD_NUMBER: _ClassVar[int]
    IS_CELLULAR_ON_FIELD_NUMBER: _ClassVar[int]
    CELLULAR_MCC_MNC_FIELD_NUMBER: _ClassVar[int]
    ASN_FIELD_NUMBER: _ClassVar[int]
    NETWORK_TYPE_FIELD_NUMBER: _ClassVar[int]
    IS_BLUETOOTH_ON_FIELD_NUMBER: _ClassVar[int]
    NETWORK_SPEED_KBPS_FIELD_NUMBER: _ClassVar[int]
    CARRIER_FIELD_NUMBER: _ClassVar[int]
    is_wifi_on: bool
    wifi_ssid: str
    is_cellular_on: bool
    cellular_mcc_mnc: str
    asn: int
    network_type: NetworkType
    is_bluetooth_on: bool
    network_speed_kbps: int
    carrier: str
    def __init__(self, is_wifi_on: bool = ..., wifi_ssid: _Optional[str] = ..., is_cellular_on: bool = ..., cellular_mcc_mnc: _Optional[str] = ..., asn: _Optional[int] = ..., network_type: _Optional[_Union[NetworkType, str]] = ..., is_bluetooth_on: bool = ..., network_speed_kbps: _Optional[int] = ..., carrier: _Optional[str] = ...) -> None: ...
