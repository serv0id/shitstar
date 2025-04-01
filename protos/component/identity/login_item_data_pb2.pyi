from component.identity import enum_pb2 as _enum_pb2
from component.identity import user_action_pb2 as _user_action_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class LoginItemData(_message.Message):
    __slots__ = ("user_action", "country_prefix", "is_previous_login_enabled", "login_mode", "page_referrer", "login_template", "resiliency_flag", "login_resiliency_mode")
    class ResiliencyFlag(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        RESILIENCY_FLAG_UNSPECIFIED: _ClassVar[LoginItemData.ResiliencyFlag]
        RESILIENCY_FLAG_ENABLED: _ClassVar[LoginItemData.ResiliencyFlag]
        RESILIENCY_FLAG_DISABLED: _ClassVar[LoginItemData.ResiliencyFlag]
    RESILIENCY_FLAG_UNSPECIFIED: LoginItemData.ResiliencyFlag
    RESILIENCY_FLAG_ENABLED: LoginItemData.ResiliencyFlag
    RESILIENCY_FLAG_DISABLED: LoginItemData.ResiliencyFlag
    USER_ACTION_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_PREFIX_FIELD_NUMBER: _ClassVar[int]
    IS_PREVIOUS_LOGIN_ENABLED_FIELD_NUMBER: _ClassVar[int]
    LOGIN_MODE_FIELD_NUMBER: _ClassVar[int]
    PAGE_REFERRER_FIELD_NUMBER: _ClassVar[int]
    LOGIN_TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    RESILIENCY_FLAG_FIELD_NUMBER: _ClassVar[int]
    LOGIN_RESILIENCY_MODE_FIELD_NUMBER: _ClassVar[int]
    user_action: _user_action_pb2.UserAction
    country_prefix: str
    is_previous_login_enabled: bool
    login_mode: _enum_pb2.LoginMode
    page_referrer: _enum_pb2.PageReferrer
    login_template: _enum_pb2.LoginTemplate
    resiliency_flag: LoginItemData.ResiliencyFlag
    login_resiliency_mode: _enum_pb2.LoginResiliencyMode
    def __init__(self, user_action: _Optional[_Union[_user_action_pb2.UserAction, _Mapping]] = ..., country_prefix: _Optional[str] = ..., is_previous_login_enabled: bool = ..., login_mode: _Optional[_Union[_enum_pb2.LoginMode, str]] = ..., page_referrer: _Optional[_Union[_enum_pb2.PageReferrer, str]] = ..., login_template: _Optional[_Union[_enum_pb2.LoginTemplate, str]] = ..., resiliency_flag: _Optional[_Union[LoginItemData.ResiliencyFlag, str]] = ..., login_resiliency_mode: _Optional[_Union[_enum_pb2.LoginResiliencyMode, str]] = ...) -> None: ...
