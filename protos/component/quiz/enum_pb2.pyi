from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class CurrentState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CURRENT_STATE_UNSPECIFIED: _ClassVar[CurrentState]
    CURRENT_STATE_TO_BE_STARTED: _ClassVar[CurrentState]
    CURRENT_STATE_RESUMED: _ClassVar[CurrentState]
    CURRENT_STATE_COMPLETED: _ClassVar[CurrentState]

class EventTrigger(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EVENT_TRIGGER_UNSPECIFIED: _ClassVar[EventTrigger]
    EVENT_TRIGGER_MANUAL: _ClassVar[EventTrigger]
    EVENT_TRIGGER_AUTO: _ClassVar[EventTrigger]

class Result(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    RESULT_UNSPECIFIED: _ClassVar[Result]
    RESULT_CORRECT: _ClassVar[Result]
    RESULT_WRONG: _ClassVar[Result]

class InfoType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    INFO_TYPE_UNSPECIFIED: _ClassVar[InfoType]
    INFO_TYPE_FAQ: _ClassVar[InfoType]
    INFO_TYPE_T_N_C: _ClassVar[InfoType]
    INFO_TYPE_CLAIM_NOW: _ClassVar[InfoType]
CURRENT_STATE_UNSPECIFIED: CurrentState
CURRENT_STATE_TO_BE_STARTED: CurrentState
CURRENT_STATE_RESUMED: CurrentState
CURRENT_STATE_COMPLETED: CurrentState
EVENT_TRIGGER_UNSPECIFIED: EventTrigger
EVENT_TRIGGER_MANUAL: EventTrigger
EVENT_TRIGGER_AUTO: EventTrigger
RESULT_UNSPECIFIED: Result
RESULT_CORRECT: Result
RESULT_WRONG: Result
INFO_TYPE_UNSPECIFIED: InfoType
INFO_TYPE_FAQ: InfoType
INFO_TYPE_T_N_C: InfoType
INFO_TYPE_CLAIM_NOW: InfoType
