from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class PreloadWebviewAction(_message.Message):
    __slots__ = ("page_url", "headers", "cookies", "preload_delay_ms")
    class HeadersEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    class CookiesEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    PAGE_URL_FIELD_NUMBER: _ClassVar[int]
    HEADERS_FIELD_NUMBER: _ClassVar[int]
    COOKIES_FIELD_NUMBER: _ClassVar[int]
    PRELOAD_DELAY_MS_FIELD_NUMBER: _ClassVar[int]
    page_url: str
    headers: _containers.ScalarMap[str, str]
    cookies: _containers.ScalarMap[str, str]
    preload_delay_ms: int
    def __init__(self, page_url: _Optional[str] = ..., headers: _Optional[_Mapping[str, str]] = ..., cookies: _Optional[_Mapping[str, str]] = ..., preload_delay_ms: _Optional[int] = ...) -> None: ...
