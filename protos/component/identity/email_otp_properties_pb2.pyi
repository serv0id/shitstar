from component.identity import enum_pb2 as _enum_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class EmailOtpProperties(_message.Message):
    __slots__ = ("country_prefix", "mode", "response", "source", "source_page_content_type", "is_previous_login_enabled", "login_mode", "login_method")
    COUNTRY_PREFIX_FIELD_NUMBER: _ClassVar[int]
    MODE_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    SOURCE_PAGE_CONTENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    IS_PREVIOUS_LOGIN_ENABLED_FIELD_NUMBER: _ClassVar[int]
    LOGIN_MODE_FIELD_NUMBER: _ClassVar[int]
    LOGIN_METHOD_FIELD_NUMBER: _ClassVar[int]
    country_prefix: str
    mode: _enum_pb2.InputEnterMode
    response: str
    source: _enum_pb2.PageSource
    source_page_content_type: str
    is_previous_login_enabled: bool
    login_mode: _enum_pb2.LoginMode
    login_method: _enum_pb2.InitiateBy
    def __init__(self, country_prefix: _Optional[str] = ..., mode: _Optional[_Union[_enum_pb2.InputEnterMode, str]] = ..., response: _Optional[str] = ..., source: _Optional[_Union[_enum_pb2.PageSource, str]] = ..., source_page_content_type: _Optional[str] = ..., is_previous_login_enabled: bool = ..., login_mode: _Optional[_Union[_enum_pb2.LoginMode, str]] = ..., login_method: _Optional[_Union[_enum_pb2.InitiateBy, str]] = ...) -> None: ...
