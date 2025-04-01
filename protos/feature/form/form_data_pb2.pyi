from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FormData(_message.Message):
    __slots__ = ("is_valid", "form_value")
    class FormValue(_message.Message):
        __slots__ = ("text_value", "option_value")
        TEXT_VALUE_FIELD_NUMBER: _ClassVar[int]
        OPTION_VALUE_FIELD_NUMBER: _ClassVar[int]
        text_value: FormData.TextValue
        option_value: FormData.OptionValue
        def __init__(self, text_value: _Optional[_Union[FormData.TextValue, _Mapping]] = ..., option_value: _Optional[_Union[FormData.OptionValue, _Mapping]] = ...) -> None: ...
    class TextValue(_message.Message):
        __slots__ = ("value",)
        VALUE_FIELD_NUMBER: _ClassVar[int]
        value: str
        def __init__(self, value: _Optional[str] = ...) -> None: ...
    class OptionValue(_message.Message):
        __slots__ = ("options",)
        OPTIONS_FIELD_NUMBER: _ClassVar[int]
        options: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, options: _Optional[_Iterable[str]] = ...) -> None: ...
    IS_VALID_FIELD_NUMBER: _ClassVar[int]
    FORM_VALUE_FIELD_NUMBER: _ClassVar[int]
    is_valid: bool
    form_value: FormData.FormValue
    def __init__(self, is_valid: bool = ..., form_value: _Optional[_Union[FormData.FormValue, _Mapping]] = ...) -> None: ...
