from google.protobuf import any_pb2 as _any_pb2
from context import context_pb2 as _context_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FetchStartAction(_message.Message):
    __slots__ = ("url", "deeplink_url", "body", "context", "replace_page", "render_mode")
    class RenderMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        DEFAULT: _ClassVar[FetchStartAction.RenderMode]
        MODAL: _ClassVar[FetchStartAction.RenderMode]
    DEFAULT: FetchStartAction.RenderMode
    MODAL: FetchStartAction.RenderMode
    URL_FIELD_NUMBER: _ClassVar[int]
    DEEPLINK_URL_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    REPLACE_PAGE_FIELD_NUMBER: _ClassVar[int]
    RENDER_MODE_FIELD_NUMBER: _ClassVar[int]
    url: str
    deeplink_url: str
    body: _any_pb2.Any
    context: _context_pb2.Context
    replace_page: bool
    render_mode: FetchStartAction.RenderMode
    def __init__(self, url: _Optional[str] = ..., deeplink_url: _Optional[str] = ..., body: _Optional[_Union[_any_pb2.Any, _Mapping]] = ..., context: _Optional[_Union[_context_pb2.Context, _Mapping]] = ..., replace_page: bool = ..., render_mode: _Optional[_Union[FetchStartAction.RenderMode, str]] = ...) -> None: ...
