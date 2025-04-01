from base import actions_pb2 as _actions_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class LanguageSelector(_message.Message):
    __slots__ = ("languages",)
    class Language(_message.Message):
        __slots__ = ("id", "name", "display_name", "description", "is_selected", "iso2code", "iso3code", "is_default", "actions")
        ID_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
        DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
        IS_SELECTED_FIELD_NUMBER: _ClassVar[int]
        ISO2CODE_FIELD_NUMBER: _ClassVar[int]
        ISO3CODE_FIELD_NUMBER: _ClassVar[int]
        IS_DEFAULT_FIELD_NUMBER: _ClassVar[int]
        ACTIONS_FIELD_NUMBER: _ClassVar[int]
        id: str
        name: str
        display_name: str
        description: str
        is_selected: bool
        iso2code: str
        iso3code: str
        is_default: bool
        actions: _actions_pb2.Actions
        def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., display_name: _Optional[str] = ..., description: _Optional[str] = ..., is_selected: bool = ..., iso2code: _Optional[str] = ..., iso3code: _Optional[str] = ..., is_default: bool = ..., actions: _Optional[_Union[_actions_pb2.Actions, _Mapping]] = ...) -> None: ...
    LANGUAGES_FIELD_NUMBER: _ClassVar[int]
    languages: _containers.RepeatedCompositeFieldContainer[LanguageSelector.Language]
    def __init__(self, languages: _Optional[_Iterable[_Union[LanguageSelector.Language, _Mapping]]] = ...) -> None: ...
