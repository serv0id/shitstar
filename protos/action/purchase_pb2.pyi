from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PurchaseType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    WEB: _ClassVar[PurchaseType]
    WEB_VIEW: _ClassVar[PurchaseType]
    IAP: _ClassVar[PurchaseType]
WEB: PurchaseType
WEB_VIEW: PurchaseType
IAP: PurchaseType

class PurchaseAction(_message.Message):
    __slots__ = ["purchase_type", "commercial_pack_id", "payment_url", "payment_success_widget_url", "replace_page"]
    PURCHASE_TYPE_FIELD_NUMBER: _ClassVar[int]
    COMMERCIAL_PACK_ID_FIELD_NUMBER: _ClassVar[int]
    PAYMENT_URL_FIELD_NUMBER: _ClassVar[int]
    PAYMENT_SUCCESS_WIDGET_URL_FIELD_NUMBER: _ClassVar[int]
    REPLACE_PAGE_FIELD_NUMBER: _ClassVar[int]
    purchase_type: PurchaseType
    commercial_pack_id: str
    payment_url: str
    payment_success_widget_url: str
    replace_page: bool
    def __init__(self, purchase_type: _Optional[_Union[PurchaseType, str]] = ..., commercial_pack_id: _Optional[str] = ..., payment_url: _Optional[str] = ..., payment_success_widget_url: _Optional[str] = ..., replace_page: bool = ...) -> None: ...
