from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class SelectedRatingProperties(_message.Message):
    __slots__ = ("prev_rating", "new_content_rating", "displayed_rating_options", "rating_nudge_ingress_type")
    PREV_RATING_FIELD_NUMBER: _ClassVar[int]
    NEW_CONTENT_RATING_FIELD_NUMBER: _ClassVar[int]
    DISPLAYED_RATING_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    RATING_NUDGE_INGRESS_TYPE_FIELD_NUMBER: _ClassVar[int]
    prev_rating: str
    new_content_rating: str
    displayed_rating_options: _containers.RepeatedScalarFieldContainer[str]
    rating_nudge_ingress_type: str
    def __init__(self, prev_rating: _Optional[str] = ..., new_content_rating: _Optional[str] = ..., displayed_rating_options: _Optional[_Iterable[str]] = ..., rating_nudge_ingress_type: _Optional[str] = ...) -> None: ...
