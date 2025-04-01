from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class OnboardingItemsInfo(_message.Message):
    __slots__ = ("selected_items_count", "selected_items")
    SELECTED_ITEMS_COUNT_FIELD_NUMBER: _ClassVar[int]
    SELECTED_ITEMS_FIELD_NUMBER: _ClassVar[int]
    selected_items_count: int
    selected_items: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, selected_items_count: _Optional[int] = ..., selected_items: _Optional[_Iterable[str]] = ...) -> None: ...
