from feature.request import http_token_request_pb2 as _http_token_request_pb2
from feature.color import color_pb2 as _color_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class WebViewNavigationAction(_message.Message):
    __slots__ = ("web_view_url", "replace", "jit", "background_color", "disable_zoom")
    WEB_VIEW_URL_FIELD_NUMBER: _ClassVar[int]
    REPLACE_FIELD_NUMBER: _ClassVar[int]
    JIT_FIELD_NUMBER: _ClassVar[int]
    BACKGROUND_COLOR_FIELD_NUMBER: _ClassVar[int]
    DISABLE_ZOOM_FIELD_NUMBER: _ClassVar[int]
    web_view_url: str
    replace: bool
    jit: _http_token_request_pb2.HttpTokenRequest
    background_color: _color_pb2.Color
    disable_zoom: bool
    def __init__(self, web_view_url: _Optional[str] = ..., replace: bool = ..., jit: _Optional[_Union[_http_token_request_pb2.HttpTokenRequest, _Mapping]] = ..., background_color: _Optional[_Union[_color_pb2.Color, _Mapping]] = ..., disable_zoom: bool = ...) -> None: ...
