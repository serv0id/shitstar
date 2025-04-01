from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CacheExpiryPolicy(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CACHE_EXPIRY_POLICY_UNSPECIFIED: _ClassVar[CacheExpiryPolicy]
    CACHE_EXPIRY_POLICY_ACCESS: _ClassVar[CacheExpiryPolicy]
    CACHE_EXPIRY_POLICY_SESSION: _ClassVar[CacheExpiryPolicy]
    CACHE_EXPIRY_POLICY_CROSS_SESSION: _ClassVar[CacheExpiryPolicy]

class CacheDeleteReason(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CACHE_DELETE_REASON_UNSPECIFIED: _ClassVar[CacheDeleteReason]
    CACHE_DELETE_REASON_EXPIRED: _ClassVar[CacheDeleteReason]
    CACHE_DELETE_REASON_VACATED: _ClassVar[CacheDeleteReason]
    CACHE_DELETE_REASON_INVALIDATED: _ClassVar[CacheDeleteReason]
CACHE_EXPIRY_POLICY_UNSPECIFIED: CacheExpiryPolicy
CACHE_EXPIRY_POLICY_ACCESS: CacheExpiryPolicy
CACHE_EXPIRY_POLICY_SESSION: CacheExpiryPolicy
CACHE_EXPIRY_POLICY_CROSS_SESSION: CacheExpiryPolicy
CACHE_DELETE_REASON_UNSPECIFIED: CacheDeleteReason
CACHE_DELETE_REASON_EXPIRED: CacheDeleteReason
CACHE_DELETE_REASON_VACATED: CacheDeleteReason
CACHE_DELETE_REASON_INVALIDATED: CacheDeleteReason

class CacheWriteProperties(_message.Message):
    __slots__ = ("common", "deleted_entries", "deleted_size_in_bytes", "is_discarded")
    COMMON_FIELD_NUMBER: _ClassVar[int]
    DELETED_ENTRIES_FIELD_NUMBER: _ClassVar[int]
    DELETED_SIZE_IN_BYTES_FIELD_NUMBER: _ClassVar[int]
    IS_DISCARDED_FIELD_NUMBER: _ClassVar[int]
    common: CacheCommonModel
    deleted_entries: int
    deleted_size_in_bytes: int
    is_discarded: bool
    def __init__(self, common: _Optional[_Union[CacheCommonModel, _Mapping]] = ..., deleted_entries: _Optional[int] = ..., deleted_size_in_bytes: _Optional[int] = ..., is_discarded: bool = ...) -> None: ...

class CacheHitProperties(_message.Message):
    __slots__ = ("common",)
    COMMON_FIELD_NUMBER: _ClassVar[int]
    common: CacheCommonModel
    def __init__(self, common: _Optional[_Union[CacheCommonModel, _Mapping]] = ...) -> None: ...

class CacheDeleteProperties(_message.Message):
    __slots__ = ("common", "reason")
    COMMON_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    common: CacheCommonModel
    reason: CacheDeleteReason
    def __init__(self, common: _Optional[_Union[CacheCommonModel, _Mapping]] = ..., reason: _Optional[_Union[CacheDeleteReason, str]] = ...) -> None: ...

class CacheClearProperties(_message.Message):
    __slots__ = ("items",)
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[CacheCommonModel]
    def __init__(self, items: _Optional[_Iterable[_Union[CacheCommonModel, _Mapping]]] = ...) -> None: ...

class CacheCommonModel(_message.Message):
    __slots__ = ("identifier", "expiry_policy", "max_age", "size_in_bytes", "cache_key")
    IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    EXPIRY_POLICY_FIELD_NUMBER: _ClassVar[int]
    MAX_AGE_FIELD_NUMBER: _ClassVar[int]
    SIZE_IN_BYTES_FIELD_NUMBER: _ClassVar[int]
    CACHE_KEY_FIELD_NUMBER: _ClassVar[int]
    identifier: str
    expiry_policy: CacheExpiryPolicy
    max_age: int
    size_in_bytes: int
    cache_key: str
    def __init__(self, identifier: _Optional[str] = ..., expiry_policy: _Optional[_Union[CacheExpiryPolicy, str]] = ..., max_age: _Optional[int] = ..., size_in_bytes: _Optional[int] = ..., cache_key: _Optional[str] = ...) -> None: ...
