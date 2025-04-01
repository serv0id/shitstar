from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ExitAction(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EXIT_ACTION_UNSPECIFIED: _ClassVar[ExitAction]
    EXIT_ACTION_CLICKED_RESULT: _ClassVar[ExitAction]
    EXIT_ACTION_CLICKED_BACK_BUTTON: _ClassVar[ExitAction]
    EXIT_ACTION_MINIMIZED_APP: _ClassVar[ExitAction]
    EXIT_ACTION_CLICKED_HOME_ICON: _ClassVar[ExitAction]
    EXIT_ACTION_CLICKED_SPORTS_ICON: _ClassVar[ExitAction]
    EXIT_ACTION_CLICKED_MY_SPACE_ICON: _ClassVar[ExitAction]
EXIT_ACTION_UNSPECIFIED: ExitAction
EXIT_ACTION_CLICKED_RESULT: ExitAction
EXIT_ACTION_CLICKED_BACK_BUTTON: ExitAction
EXIT_ACTION_MINIMIZED_APP: ExitAction
EXIT_ACTION_CLICKED_HOME_ICON: ExitAction
EXIT_ACTION_CLICKED_SPORTS_ICON: ExitAction
EXIT_ACTION_CLICKED_MY_SPACE_ICON: ExitAction

class SearchExitProperties(_message.Message):
    __slots__ = ("search_session_id", "last_search_id", "exit_action")
    SEARCH_SESSION_ID_FIELD_NUMBER: _ClassVar[int]
    LAST_SEARCH_ID_FIELD_NUMBER: _ClassVar[int]
    EXIT_ACTION_FIELD_NUMBER: _ClassVar[int]
    search_session_id: str
    last_search_id: str
    exit_action: ExitAction
    def __init__(self, search_session_id: _Optional[str] = ..., last_search_id: _Optional[str] = ..., exit_action: _Optional[_Union[ExitAction, str]] = ...) -> None: ...
