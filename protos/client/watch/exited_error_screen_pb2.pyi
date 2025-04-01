from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ExitAction(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EXIT_ACTION_UNSPECIFIED: _ClassVar[ExitAction]
    EXIT_ACTION_GO_BACK: _ClassVar[ExitAction]
    EXIT_ACTION_DEFAULT: _ClassVar[ExitAction]
EXIT_ACTION_UNSPECIFIED: ExitAction
EXIT_ACTION_GO_BACK: ExitAction
EXIT_ACTION_DEFAULT: ExitAction

class ExitedErrorScreen(_message.Message):
    __slots__ = ("exit_action", "error_code")
    EXIT_ACTION_FIELD_NUMBER: _ClassVar[int]
    ERROR_CODE_FIELD_NUMBER: _ClassVar[int]
    exit_action: ExitAction
    error_code: str
    def __init__(self, exit_action: _Optional[_Union[ExitAction, str]] = ..., error_code: _Optional[str] = ...) -> None: ...
