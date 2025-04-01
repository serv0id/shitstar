from feature.image import illustration_pb2 as _illustration_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class LiveInfo(_message.Message):
    __slots__ = ("live_display_text", "concurrency_display_text", "concurrency_refresh_info", "views_display_text", "concurrency_pattern", "views_pattern", "status_badge")
    class ConcurrencyRefreshInfo(_message.Message):
        __slots__ = ("ttl_in_seconds", "widget_url", "refresh_url")
        TTL_IN_SECONDS_FIELD_NUMBER: _ClassVar[int]
        WIDGET_URL_FIELD_NUMBER: _ClassVar[int]
        REFRESH_URL_FIELD_NUMBER: _ClassVar[int]
        ttl_in_seconds: int
        widget_url: str
        refresh_url: str
        def __init__(self, ttl_in_seconds: _Optional[int] = ..., widget_url: _Optional[str] = ..., refresh_url: _Optional[str] = ...) -> None: ...
    LIVE_DISPLAY_TEXT_FIELD_NUMBER: _ClassVar[int]
    CONCURRENCY_DISPLAY_TEXT_FIELD_NUMBER: _ClassVar[int]
    CONCURRENCY_REFRESH_INFO_FIELD_NUMBER: _ClassVar[int]
    VIEWS_DISPLAY_TEXT_FIELD_NUMBER: _ClassVar[int]
    CONCURRENCY_PATTERN_FIELD_NUMBER: _ClassVar[int]
    VIEWS_PATTERN_FIELD_NUMBER: _ClassVar[int]
    STATUS_BADGE_FIELD_NUMBER: _ClassVar[int]
    live_display_text: str
    concurrency_display_text: str
    concurrency_refresh_info: LiveInfo.ConcurrencyRefreshInfo
    views_display_text: str
    concurrency_pattern: str
    views_pattern: str
    status_badge: _illustration_pb2.Illustration
    def __init__(self, live_display_text: _Optional[str] = ..., concurrency_display_text: _Optional[str] = ..., concurrency_refresh_info: _Optional[_Union[LiveInfo.ConcurrencyRefreshInfo, _Mapping]] = ..., views_display_text: _Optional[str] = ..., concurrency_pattern: _Optional[str] = ..., views_pattern: _Optional[str] = ..., status_badge: _Optional[_Union[_illustration_pb2.Illustration, _Mapping]] = ...) -> None: ...
