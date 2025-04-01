from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Translation(_message.Message):
    __slots__ = ("string_identifier", "is_bundled", "string_store_api_call_status", "display_language")
    class ApiCallStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        API_CALL_STATUS_UNSPECIFIED: _ClassVar[Translation.ApiCallStatus]
        API_CALL_STATUS_STARTED: _ClassVar[Translation.ApiCallStatus]
        API_CALL_STATUS_COMPLETED: _ClassVar[Translation.ApiCallStatus]
        API_CALL_STATUS_FAILED: _ClassVar[Translation.ApiCallStatus]
    API_CALL_STATUS_UNSPECIFIED: Translation.ApiCallStatus
    API_CALL_STATUS_STARTED: Translation.ApiCallStatus
    API_CALL_STATUS_COMPLETED: Translation.ApiCallStatus
    API_CALL_STATUS_FAILED: Translation.ApiCallStatus
    STRING_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    IS_BUNDLED_FIELD_NUMBER: _ClassVar[int]
    STRING_STORE_API_CALL_STATUS_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_LANGUAGE_FIELD_NUMBER: _ClassVar[int]
    string_identifier: str
    is_bundled: bool
    string_store_api_call_status: Translation.ApiCallStatus
    display_language: str
    def __init__(self, string_identifier: _Optional[str] = ..., is_bundled: bool = ..., string_store_api_call_status: _Optional[_Union[Translation.ApiCallStatus, str]] = ..., display_language: _Optional[str] = ...) -> None: ...
