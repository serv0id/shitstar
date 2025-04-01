from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FreeTimerSource(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    FREE_TIMER_SOURCE_UNSPECIFIED: _ClassVar[FreeTimerSource]
    FREE_TIMER_SOURCE_SELF: _ClassVar[FreeTimerSource]
    FREE_TIMER_SOURCE_EXTERNAL: _ClassVar[FreeTimerSource]
    FREE_TIMER_SOURCE_PREF_EXTERNAL: _ClassVar[FreeTimerSource]

class FreeTimerRealSource(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    FREE_TIMER_REAL_SOURCE_UNSPECIFIED: _ClassVar[FreeTimerRealSource]
    FREE_TIMER_REAL_SOURCE_BFF: _ClassVar[FreeTimerRealSource]
    FREE_TIMER_REAL_SOURCE_REFRESH: _ClassVar[FreeTimerRealSource]
    FREE_TIMER_REAL_SOURCE_MASTER_MANIFEST: _ClassVar[FreeTimerRealSource]
FREE_TIMER_SOURCE_UNSPECIFIED: FreeTimerSource
FREE_TIMER_SOURCE_SELF: FreeTimerSource
FREE_TIMER_SOURCE_EXTERNAL: FreeTimerSource
FREE_TIMER_SOURCE_PREF_EXTERNAL: FreeTimerSource
FREE_TIMER_REAL_SOURCE_UNSPECIFIED: FreeTimerRealSource
FREE_TIMER_REAL_SOURCE_BFF: FreeTimerRealSource
FREE_TIMER_REAL_SOURCE_REFRESH: FreeTimerRealSource
FREE_TIMER_REAL_SOURCE_MASTER_MANIFEST: FreeTimerRealSource

class FreeTimer(_message.Message):
    __slots__ = ("free_timer_source",)
    FREE_TIMER_SOURCE_FIELD_NUMBER: _ClassVar[int]
    free_timer_source: FreeTimerSource
    def __init__(self, free_timer_source: _Optional[_Union[FreeTimerSource, str]] = ...) -> None: ...
