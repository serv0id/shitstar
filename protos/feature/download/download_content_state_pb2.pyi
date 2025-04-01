from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DownloadContentState(_message.Message):
    __slots__ = ("status", "stateMeta", "accessibilityTime", "subStateMeta")
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ALLOW: _ClassVar[DownloadContentState.Status]
        DELETE: _ClassVar[DownloadContentState.Status]
        RESTRICT_WATCH: _ClassVar[DownloadContentState.Status]
    ALLOW: DownloadContentState.Status
    DELETE: DownloadContentState.Status
    RESTRICT_WATCH: DownloadContentState.Status
    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SUBS_EXPIRY: _ClassVar[DownloadContentState.State]
        TIME_BASED_EXPIRY: _ClassVar[DownloadContentState.State]
        CONTENT_UNPUBLISHED: _ClassVar[DownloadContentState.State]
        CONTENT_DELETED: _ClassVar[DownloadContentState.State]
        TRAVELLING_USER: _ClassVar[DownloadContentState.State]
    SUBS_EXPIRY: DownloadContentState.State
    TIME_BASED_EXPIRY: DownloadContentState.State
    CONTENT_UNPUBLISHED: DownloadContentState.State
    CONTENT_DELETED: DownloadContentState.State
    TRAVELLING_USER: DownloadContentState.State
    class SubStateMeta(_message.Message):
        __slots__ = ("subState", "accessibilityTime")
        class SubState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            WATCH_BASED_EXPIRY: _ClassVar[DownloadContentState.SubStateMeta.SubState]
        WATCH_BASED_EXPIRY: DownloadContentState.SubStateMeta.SubState
        SUBSTATE_FIELD_NUMBER: _ClassVar[int]
        ACCESSIBILITYTIME_FIELD_NUMBER: _ClassVar[int]
        subState: DownloadContentState.SubStateMeta.SubState
        accessibilityTime: float
        def __init__(self, subState: _Optional[_Union[DownloadContentState.SubStateMeta.SubState, str]] = ..., accessibilityTime: _Optional[float] = ...) -> None: ...
    STATUS_FIELD_NUMBER: _ClassVar[int]
    STATEMETA_FIELD_NUMBER: _ClassVar[int]
    ACCESSIBILITYTIME_FIELD_NUMBER: _ClassVar[int]
    SUBSTATEMETA_FIELD_NUMBER: _ClassVar[int]
    status: DownloadContentState.Status
    stateMeta: DownloadContentState.State
    accessibilityTime: float
    subStateMeta: DownloadContentState.SubStateMeta
    def __init__(self, status: _Optional[_Union[DownloadContentState.Status, str]] = ..., stateMeta: _Optional[_Union[DownloadContentState.State, str]] = ..., accessibilityTime: _Optional[float] = ..., subStateMeta: _Optional[_Union[DownloadContentState.SubStateMeta, _Mapping]] = ...) -> None: ...
