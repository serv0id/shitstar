from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class EcommerceEventsTrackMeta(_message.Message):
    __slots__ = ("ecommerce",)
    ECOMMERCE_FIELD_NUMBER: _ClassVar[int]
    ecommerce: Ecommerce
    def __init__(self, ecommerce: _Optional[_Union[Ecommerce, _Mapping]] = ...) -> None: ...

class Ecommerce(_message.Message):
    __slots__ = ("transaction_id", "pack_id", "value", "currency", "items")
    TRANSACTION_ID_FIELD_NUMBER: _ClassVar[int]
    PACK_ID_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    CURRENCY_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    transaction_id: str
    pack_id: str
    value: str
    currency: str
    items: _containers.RepeatedCompositeFieldContainer[Items]
    def __init__(self, transaction_id: _Optional[str] = ..., pack_id: _Optional[str] = ..., value: _Optional[str] = ..., currency: _Optional[str] = ..., items: _Optional[_Iterable[_Union[Items, _Mapping]]] = ...) -> None: ...

class Items(_message.Message):
    __slots__ = ("item_name", "price")
    ITEM_NAME_FIELD_NUMBER: _ClassVar[int]
    PRICE_FIELD_NUMBER: _ClassVar[int]
    item_name: str
    price: str
    def __init__(self, item_name: _Optional[str] = ..., price: _Optional[str] = ...) -> None: ...
