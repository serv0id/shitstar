from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class EvictionReason(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EVICTION_REASON_UNSPECIFIED: _ClassVar[EvictionReason]
    EVICTION_REASON_THRESHOLD_CROSSED: _ClassVar[EvictionReason]
    EVICTION_REASON_ALREADY_RATED: _ClassVar[EvictionReason]
EVICTION_REASON_UNSPECIFIED: EvictionReason
EVICTION_REASON_THRESHOLD_CROSSED: EvictionReason
EVICTION_REASON_ALREADY_RATED: EvictionReason

class EvictingContentRatingCardProperties(_message.Message):
    __slots__ = ("threshold", "reason")
    THRESHOLD_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    threshold: int
    reason: EvictionReason
    def __init__(self, threshold: _Optional[int] = ..., reason: _Optional[_Union[EvictionReason, str]] = ...) -> None: ...
