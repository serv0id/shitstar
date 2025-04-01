from base import page_data_commons_pb2 as _page_data_commons_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FeedPageData(_message.Message):
    __slots__ = ("page_data_commons", "hide_bottom_nav")
    PAGE_DATA_COMMONS_FIELD_NUMBER: _ClassVar[int]
    HIDE_BOTTOM_NAV_FIELD_NUMBER: _ClassVar[int]
    page_data_commons: _page_data_commons_pb2.PageDataCommons
    hide_bottom_nav: bool
    def __init__(self, page_data_commons: _Optional[_Union[_page_data_commons_pb2.PageDataCommons, _Mapping]] = ..., hide_bottom_nav: bool = ...) -> None: ...
