from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class RecaptchaErrorProperties(_message.Message):
    __slots__ = ("error_source", "error_reason")
    class Source(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SOURCE_UNSPECIFIED: _ClassVar[RecaptchaErrorProperties.Source]
        SOURCE_SDK_INIT: _ClassVar[RecaptchaErrorProperties.Source]
        SOURCE_TOKEN_GENERATION: _ClassVar[RecaptchaErrorProperties.Source]
        SOURCE_TOKEN_RETRY: _ClassVar[RecaptchaErrorProperties.Source]
    SOURCE_UNSPECIFIED: RecaptchaErrorProperties.Source
    SOURCE_SDK_INIT: RecaptchaErrorProperties.Source
    SOURCE_TOKEN_GENERATION: RecaptchaErrorProperties.Source
    SOURCE_TOKEN_RETRY: RecaptchaErrorProperties.Source
    ERROR_SOURCE_FIELD_NUMBER: _ClassVar[int]
    ERROR_REASON_FIELD_NUMBER: _ClassVar[int]
    error_source: RecaptchaErrorProperties.Source
    error_reason: str
    def __init__(self, error_source: _Optional[_Union[RecaptchaErrorProperties.Source, str]] = ..., error_reason: _Optional[str] = ...) -> None: ...
