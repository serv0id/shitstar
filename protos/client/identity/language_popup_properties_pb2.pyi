from component.identity import enum_pb2 as _enum_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ClickedLanguagePopupProperties(_message.Message):
    __slots__ = ("popup_action_type",)
    POPUP_ACTION_TYPE_FIELD_NUMBER: _ClassVar[int]
    popup_action_type: _enum_pb2.LanguagePopupActionType
    def __init__(self, popup_action_type: _Optional[_Union[_enum_pb2.LanguagePopupActionType, str]] = ...) -> None: ...

class ViewedLanguagePopupProperties(_message.Message):
    __slots__ = ("current_language", "preferred_languages")
    CURRENT_LANGUAGE_FIELD_NUMBER: _ClassVar[int]
    PREFERRED_LANGUAGES_FIELD_NUMBER: _ClassVar[int]
    current_language: str
    preferred_languages: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, current_language: _Optional[str] = ..., preferred_languages: _Optional[_Iterable[str]] = ...) -> None: ...
