from google.protobuf import any_pb2 as _any_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class UserInfo(_message.Message):
    __slots__ = ("hid", "pid", "login_status", "highest_active_plan", "old_hid", "old_pid")
    class LoginStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNKNOWN: _ClassVar[UserInfo.LoginStatus]
        LOGGED_IN: _ClassVar[UserInfo.LoginStatus]
        GUEST: _ClassVar[UserInfo.LoginStatus]
        LOGGEDIN: _ClassVar[UserInfo.LoginStatus]
    UNKNOWN: UserInfo.LoginStatus
    LOGGED_IN: UserInfo.LoginStatus
    GUEST: UserInfo.LoginStatus
    LOGGEDIN: UserInfo.LoginStatus
    HID_FIELD_NUMBER: _ClassVar[int]
    PID_FIELD_NUMBER: _ClassVar[int]
    LOGIN_STATUS_FIELD_NUMBER: _ClassVar[int]
    HIGHEST_ACTIVE_PLAN_FIELD_NUMBER: _ClassVar[int]
    OLD_HID_FIELD_NUMBER: _ClassVar[int]
    OLD_PID_FIELD_NUMBER: _ClassVar[int]
    hid: str
    pid: str
    login_status: UserInfo.LoginStatus
    highest_active_plan: Plan
    old_hid: str
    old_pid: str
    def __init__(self, hid: _Optional[str] = ..., pid: _Optional[str] = ..., login_status: _Optional[_Union[UserInfo.LoginStatus, str]] = ..., highest_active_plan: _Optional[_Union[Plan, _Mapping]] = ..., old_hid: _Optional[str] = ..., old_pid: _Optional[str] = ...) -> None: ...

class Plan(_message.Message):
    __slots__ = ("family",)
    FAMILY_FIELD_NUMBER: _ClassVar[int]
    family: str
    def __init__(self, family: _Optional[str] = ...) -> None: ...
