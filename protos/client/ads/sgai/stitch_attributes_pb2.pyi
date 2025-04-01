from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class StitchAttributes(_message.Message):
    __slots__ = ("total_ad_breaks", "sgai_ad_breaks", "stitched_ad_breaks", "period_cache_hits", "fuse_cache_hits", "total_latency")
    TOTAL_AD_BREAKS_FIELD_NUMBER: _ClassVar[int]
    SGAI_AD_BREAKS_FIELD_NUMBER: _ClassVar[int]
    STITCHED_AD_BREAKS_FIELD_NUMBER: _ClassVar[int]
    PERIOD_CACHE_HITS_FIELD_NUMBER: _ClassVar[int]
    FUSE_CACHE_HITS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_LATENCY_FIELD_NUMBER: _ClassVar[int]
    total_ad_breaks: int
    sgai_ad_breaks: int
    stitched_ad_breaks: int
    period_cache_hits: int
    fuse_cache_hits: int
    total_latency: int
    def __init__(self, total_ad_breaks: _Optional[int] = ..., sgai_ad_breaks: _Optional[int] = ..., stitched_ad_breaks: _Optional[int] = ..., period_cache_hits: _Optional[int] = ..., fuse_cache_hits: _Optional[int] = ..., total_latency: _Optional[int] = ...) -> None: ...
