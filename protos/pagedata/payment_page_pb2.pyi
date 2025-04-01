from base import page_data_commons_pb2 as _page_data_commons_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PaymentPageData(_message.Message):
    __slots__ = ("page_data_commons", "commercial_pack_id", "payment_success_widget_url")
    PAGE_DATA_COMMONS_FIELD_NUMBER: _ClassVar[int]
    COMMERCIAL_PACK_ID_FIELD_NUMBER: _ClassVar[int]
    PAYMENT_SUCCESS_WIDGET_URL_FIELD_NUMBER: _ClassVar[int]
    page_data_commons: _page_data_commons_pb2.PageDataCommons
    commercial_pack_id: str
    payment_success_widget_url: str
    def __init__(self, page_data_commons: _Optional[_Union[_page_data_commons_pb2.PageDataCommons, _Mapping]] = ..., commercial_pack_id: _Optional[str] = ..., payment_success_widget_url: _Optional[str] = ...) -> None: ...
