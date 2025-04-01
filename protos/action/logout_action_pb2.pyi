from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class LogoutAction(_message.Message):
    __slots__ = ("user_token", "hid", "pid", "login_status", "highest_active_plan")
    class LoginStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNKNOWN: _ClassVar[LogoutAction.LoginStatus]
        LOGGED_IN: _ClassVar[LogoutAction.LoginStatus]
        GUEST: _ClassVar[LogoutAction.LoginStatus]
        LOGGEDIN: _ClassVar[LogoutAction.LoginStatus]
    UNKNOWN: LogoutAction.LoginStatus
    LOGGED_IN: LogoutAction.LoginStatus
    GUEST: LogoutAction.LoginStatus
    LOGGEDIN: LogoutAction.LoginStatus
    USER_TOKEN_FIELD_NUMBER: _ClassVar[int]
    HID_FIELD_NUMBER: _ClassVar[int]
    PID_FIELD_NUMBER: _ClassVar[int]
    LOGIN_STATUS_FIELD_NUMBER: _ClassVar[int]
    HIGHEST_ACTIVE_PLAN_FIELD_NUMBER: _ClassVar[int]
    user_token: str
    hid: str
    pid: str
    login_status: LogoutAction.LoginStatus
    highest_active_plan: Plan
    def __init__(self, user_token: _Optional[str] = ..., hid: _Optional[str] = ..., pid: _Optional[str] = ..., login_status: _Optional[_Union[LogoutAction.LoginStatus, str]] = ..., highest_active_plan: _Optional[_Union[Plan, _Mapping]] = ...) -> None: ...

class Plan(_message.Message):
    __slots__ = ("family",)
    FAMILY_FIELD_NUMBER: _ClassVar[int]
    family: str
    def __init__(self, family: _Optional[str] = ...) -> None: ...
