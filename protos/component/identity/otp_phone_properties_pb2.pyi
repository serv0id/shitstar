from component.identity import enum_pb2 as _enum_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class OtpPhoneProperties(_message.Message):
    __slots__ = ("response", "country_prefix", "source", "mode", "login_source", "level", "source_page_content_type", "initiate_by")
    RESPONSE_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_PREFIX_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    MODE_FIELD_NUMBER: _ClassVar[int]
    LOGIN_SOURCE_FIELD_NUMBER: _ClassVar[int]
    LEVEL_FIELD_NUMBER: _ClassVar[int]
    SOURCE_PAGE_CONTENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    INITIATE_BY_FIELD_NUMBER: _ClassVar[int]
    response: str
    country_prefix: str
    source: _enum_pb2.PageSource
    mode: _enum_pb2.InputEnterMode
    login_source: _enum_pb2.LoginSource
    level: float
    source_page_content_type: str
    initiate_by: _enum_pb2.InitiateBy
    def __init__(self, response: _Optional[str] = ..., country_prefix: _Optional[str] = ..., source: _Optional[_Union[_enum_pb2.PageSource, str]] = ..., mode: _Optional[_Union[_enum_pb2.InputEnterMode, str]] = ..., login_source: _Optional[_Union[_enum_pb2.LoginSource, str]] = ..., level: _Optional[float] = ..., source_page_content_type: _Optional[str] = ..., initiate_by: _Optional[_Union[_enum_pb2.InitiateBy, str]] = ...) -> None: ...
