from client.ads.sgai import creative_pb2 as _creative_pb2
from client.heartbeat.model import http_connection_stats_pb2 as _http_connection_stats_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AdBreak(_message.Message):
    __slots__ = ("break_id", "api_latency", "stitch_latency", "is_ad_crashed", "api_metrics", "break_duration_ms", "creatives")
    BREAK_ID_FIELD_NUMBER: _ClassVar[int]
    API_LATENCY_FIELD_NUMBER: _ClassVar[int]
    STITCH_LATENCY_FIELD_NUMBER: _ClassVar[int]
    IS_AD_CRASHED_FIELD_NUMBER: _ClassVar[int]
    API_METRICS_FIELD_NUMBER: _ClassVar[int]
    BREAK_DURATION_MS_FIELD_NUMBER: _ClassVar[int]
    CREATIVES_FIELD_NUMBER: _ClassVar[int]
    break_id: str
    api_latency: int
    stitch_latency: int
    is_ad_crashed: bool
    api_metrics: _http_connection_stats_pb2.HttpConnectionStats
    break_duration_ms: int
    creatives: _containers.RepeatedCompositeFieldContainer[_creative_pb2.Creative]
    def __init__(self, break_id: _Optional[str] = ..., api_latency: _Optional[int] = ..., stitch_latency: _Optional[int] = ..., is_ad_crashed: bool = ..., api_metrics: _Optional[_Union[_http_connection_stats_pb2.HttpConnectionStats, _Mapping]] = ..., break_duration_ms: _Optional[int] = ..., creatives: _Optional[_Iterable[_Union[_creative_pb2.Creative, _Mapping]]] = ...) -> None: ...
