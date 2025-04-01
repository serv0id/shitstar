from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class AppEvent(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    UNKNOWN: _ClassVar[AppEvent]
    TOKEN_CHANGED: _ClassVar[AppEvent]
    PROFILE_UPDATED: _ClassVar[AppEvent]
    USER_SESSIONS_UPDATED: _ClassVar[AppEvent]
    FREE_WATCH_TIMER_EXPIRED: _ClassVar[AppEvent]
UNKNOWN: AppEvent
TOKEN_CHANGED: AppEvent
PROFILE_UPDATED: AppEvent
USER_SESSIONS_UPDATED: AppEvent
FREE_WATCH_TIMER_EXPIRED: AppEvent
