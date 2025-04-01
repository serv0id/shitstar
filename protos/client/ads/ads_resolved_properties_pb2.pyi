from client.ads import ad_resolution_info_pb2 as _ad_resolution_info_pb2
from client.ads import common_pb2 as _common_pb2
from client.ads import type_pb2 as _type_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AdsResolvedProperties(_message.Message):
    __slots__ = ("common_properties", "resolution_time_ms", "resolution_infos")
    COMMON_PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    RESOLUTION_TIME_MS_FIELD_NUMBER: _ClassVar[int]
    RESOLUTION_INFOS_FIELD_NUMBER: _ClassVar[int]
    common_properties: _common_pb2.Common
    resolution_time_ms: int
    resolution_infos: _containers.RepeatedCompositeFieldContainer[_ad_resolution_info_pb2.AdResolutionInfo]
    def __init__(self, common_properties: _Optional[_Union[_common_pb2.Common, _Mapping]] = ..., resolution_time_ms: _Optional[int] = ..., resolution_infos: _Optional[_Iterable[_Union[_ad_resolution_info_pb2.AdResolutionInfo, _Mapping]]] = ...) -> None: ...
