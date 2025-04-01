from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ClientCache(_message.Message):
    __slots__ = ("items",)
    class CacheItemType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[ClientCache.CacheItemType]
        WIDGET: _ClassVar[ClientCache.CacheItemType]
        PAGE: _ClassVar[ClientCache.CacheItemType]
        SPACE: _ClassVar[ClientCache.CacheItemType]
    UNSPECIFIED: ClientCache.CacheItemType
    WIDGET: ClientCache.CacheItemType
    PAGE: ClientCache.CacheItemType
    SPACE: ClientCache.CacheItemType
    class ClientCacheItem(_message.Message):
        __slots__ = ("item_type", "unique_identifier", "last_updated_at_in_epoch")
        ITEM_TYPE_FIELD_NUMBER: _ClassVar[int]
        UNIQUE_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
        LAST_UPDATED_AT_IN_EPOCH_FIELD_NUMBER: _ClassVar[int]
        item_type: ClientCache.CacheItemType
        unique_identifier: int
        last_updated_at_in_epoch: int
        def __init__(self, item_type: _Optional[_Union[ClientCache.CacheItemType, str]] = ..., unique_identifier: _Optional[int] = ..., last_updated_at_in_epoch: _Optional[int] = ...) -> None: ...
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[ClientCache.ClientCacheItem]
    def __init__(self, items: _Optional[_Iterable[_Union[ClientCache.ClientCacheItem, _Mapping]]] = ...) -> None: ...
