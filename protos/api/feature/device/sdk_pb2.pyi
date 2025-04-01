from options import opts_pb2 as _opts_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Sdk(_message.Message):
    __slots__ = ("appsflyer",)
    class AppsFlyer(_message.Message):
        __slots__ = ("id", "conversion_type")
        class ConversionType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            CONVERSION_TYPE_UNSPECIFIED: _ClassVar[Sdk.AppsFlyer.ConversionType]
            CONVERSION_TYPE_ORGANIC: _ClassVar[Sdk.AppsFlyer.ConversionType]
            CONVERSION_TYPE_NON_ORGANIC: _ClassVar[Sdk.AppsFlyer.ConversionType]
        CONVERSION_TYPE_UNSPECIFIED: Sdk.AppsFlyer.ConversionType
        CONVERSION_TYPE_ORGANIC: Sdk.AppsFlyer.ConversionType
        CONVERSION_TYPE_NON_ORGANIC: Sdk.AppsFlyer.ConversionType
        ID_FIELD_NUMBER: _ClassVar[int]
        CONVERSION_TYPE_FIELD_NUMBER: _ClassVar[int]
        id: str
        conversion_type: Sdk.AppsFlyer.ConversionType
        def __init__(self, id: _Optional[str] = ..., conversion_type: _Optional[_Union[Sdk.AppsFlyer.ConversionType, str]] = ...) -> None: ...
    APPSFLYER_FIELD_NUMBER: _ClassVar[int]
    appsflyer: Sdk.AppsFlyer
    def __init__(self, appsflyer: _Optional[_Union[Sdk.AppsFlyer, _Mapping]] = ...) -> None: ...
