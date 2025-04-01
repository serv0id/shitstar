from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class OnboardingLanguage(_message.Message):
    __slots__ = ("languages_count", "selected_languages")
    LANGUAGES_COUNT_FIELD_NUMBER: _ClassVar[int]
    SELECTED_LANGUAGES_FIELD_NUMBER: _ClassVar[int]
    languages_count: int
    selected_languages: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, languages_count: _Optional[int] = ..., selected_languages: _Optional[_Iterable[str]] = ...) -> None: ...
