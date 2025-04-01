from client.perf import page_content_loaded_commons_pb2 as _page_content_loaded_commons_pb2
from google.protobuf import any_pb2 as _any_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PageContentLoadedProperties(_message.Message):
    __slots__ = ("common_properties",)
    COMMON_PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    common_properties: _page_content_loaded_commons_pb2.PageContentLoadedCommons
    def __init__(self, common_properties: _Optional[_Union[_page_content_loaded_commons_pb2.PageContentLoadedCommons, _Mapping]] = ...) -> None: ...
