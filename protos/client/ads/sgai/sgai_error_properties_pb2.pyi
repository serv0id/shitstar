from client.ads.sgai import content_meta_pb2 as _content_meta_pb2
from client.ads.sgai import error_pb2 as _error_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SgaiErrorProperties(_message.Message):
    __slots__ = ("content_meta", "error", "break_id")
    CONTENT_META_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    BREAK_ID_FIELD_NUMBER: _ClassVar[int]
    content_meta: _content_meta_pb2.ContentMeta
    error: _error_pb2.Error
    break_id: str
    def __init__(self, content_meta: _Optional[_Union[_content_meta_pb2.ContentMeta, _Mapping]] = ..., error: _Optional[_Union[_error_pb2.Error, _Mapping]] = ..., break_id: _Optional[str] = ...) -> None: ...
