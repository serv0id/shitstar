from client.context.base import page_pb2 as _page_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class WatchPage(_message.Message):
    __slots__ = ("base", "content_id")
    BASE_FIELD_NUMBER: _ClassVar[int]
    CONTENT_ID_FIELD_NUMBER: _ClassVar[int]
    base: _page_pb2.Page
    content_id: str
    def __init__(self, base: _Optional[_Union[_page_pb2.Page, _Mapping]] = ..., content_id: _Optional[str] = ...) -> None: ...
