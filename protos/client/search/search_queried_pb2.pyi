from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class QueryInput(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    QUERY_INPUT_UNSPECIFIED: _ClassVar[QueryInput]
    QUERY_INPUT_TYPE: _ClassVar[QueryInput]
    QUERY_INPUT_VOICE: _ClassVar[QueryInput]
    QUERY_INPUT_FILTER: _ClassVar[QueryInput]
    QUERY_INPUT_TEXT: _ClassVar[QueryInput]
    QUERY_INPUT_TAB_CHANGE: _ClassVar[QueryInput]
    QUERY_INPUT_GLOBAL: _ClassVar[QueryInput]
    QUERY_INPUT_VOICE_REMOTE: _ClassVar[QueryInput]

class ReferrerInterface(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    REFERRER_INTERFACE_UNSPECIFIED: _ClassVar[ReferrerInterface]
    REFERRER_INTERFACE_HISTORY: _ClassVar[ReferrerInterface]
    REFERRER_INTERFACE_TRENDING: _ClassVar[ReferrerInterface]
    REFERRER_INTERFACE_USER_INPUT: _ClassVar[ReferrerInterface]
    REFERRER_INTERFACE_TV_SHOWS: _ClassVar[ReferrerInterface]
    REFERRER_INTERFACE_MOVIES: _ClassVar[ReferrerInterface]
    REFERRER_INTERFACE_RELATED_SEARCH: _ClassVar[ReferrerInterface]
    REFERRER_INTERFACE_TYPEAHEAD: _ClassVar[ReferrerInterface]
    REFERRER_INTERFACE_FILTER: _ClassVar[ReferrerInterface]
    REFERRER_INTERFACE_USER_INPUT_GLOBAL: _ClassVar[ReferrerInterface]
    REFERRER_INTERFACE_AUTO_SUGGEST: _ClassVar[ReferrerInterface]
    REFERRER_INTERFACE_HINT_TEXT: _ClassVar[ReferrerInterface]
QUERY_INPUT_UNSPECIFIED: QueryInput
QUERY_INPUT_TYPE: QueryInput
QUERY_INPUT_VOICE: QueryInput
QUERY_INPUT_FILTER: QueryInput
QUERY_INPUT_TEXT: QueryInput
QUERY_INPUT_TAB_CHANGE: QueryInput
QUERY_INPUT_GLOBAL: QueryInput
QUERY_INPUT_VOICE_REMOTE: QueryInput
REFERRER_INTERFACE_UNSPECIFIED: ReferrerInterface
REFERRER_INTERFACE_HISTORY: ReferrerInterface
REFERRER_INTERFACE_TRENDING: ReferrerInterface
REFERRER_INTERFACE_USER_INPUT: ReferrerInterface
REFERRER_INTERFACE_TV_SHOWS: ReferrerInterface
REFERRER_INTERFACE_MOVIES: ReferrerInterface
REFERRER_INTERFACE_RELATED_SEARCH: ReferrerInterface
REFERRER_INTERFACE_TYPEAHEAD: ReferrerInterface
REFERRER_INTERFACE_FILTER: ReferrerInterface
REFERRER_INTERFACE_USER_INPUT_GLOBAL: ReferrerInterface
REFERRER_INTERFACE_AUTO_SUGGEST: ReferrerInterface
REFERRER_INTERFACE_HINT_TEXT: ReferrerInterface

class SearchQueriedProperties(_message.Message):
    __slots__ = ("search_session_id", "search_id", "query_input", "query_text", "referrer_interface")
    SEARCH_SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    SEARCH_ID_FIELD_NUMBER: _ClassVar[int]
    QUERY_INPUT_FIELD_NUMBER: _ClassVar[int]
    QUERY_TEXT_FIELD_NUMBER: _ClassVar[int]
    REFERRER_INTERFACE_FIELD_NUMBER: _ClassVar[int]
    search_session_id: str
    search_id: str
    query_input: QueryInput
    query_text: str
    referrer_interface: ReferrerInterface
    def __init__(self, search_session_id: _Optional[str] = ..., search_id: _Optional[str] = ..., query_input: _Optional[_Union[QueryInput, str]] = ..., query_text: _Optional[str] = ..., referrer_interface: _Optional[_Union[ReferrerInterface, str]] = ...) -> None: ...
