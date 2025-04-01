from base import page_data_commons_pb2 as _page_data_commons_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class LandingPageData(_message.Message):
    __slots__ = ("page_data_commons", "IsCompactMasthead")
    PAGE_DATA_COMMONS_FIELD_NUMBER: _ClassVar[int]
    ISCOMPACTMASTHEAD_FIELD_NUMBER: _ClassVar[int]
    page_data_commons: _page_data_commons_pb2.PageDataCommons
    IsCompactMasthead: bool
    def __init__(self, page_data_commons: _Optional[_Union[_page_data_commons_pb2.PageDataCommons, _Mapping]] = ..., IsCompactMasthead: bool = ...) -> None: ...
