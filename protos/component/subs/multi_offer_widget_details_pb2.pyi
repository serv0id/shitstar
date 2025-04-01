from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class MultiOfferWidgetDetails(_message.Message):
    __slots__ = ("offer_types", "offer_titles")
    OFFER_TYPES_FIELD_NUMBER: _ClassVar[int]
    OFFER_TITLES_FIELD_NUMBER: _ClassVar[int]
    offer_types: _containers.RepeatedScalarFieldContainer[str]
    offer_titles: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, offer_types: _Optional[_Iterable[str]] = ..., offer_titles: _Optional[_Iterable[str]] = ...) -> None: ...
