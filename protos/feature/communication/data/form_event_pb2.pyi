from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FormEvent(_message.Message):
    __slots__ = ["type"]
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
        RESET: _ClassVar[FormEvent.Type]
        SUBMIT: _ClassVar[FormEvent.Type]
    RESET: FormEvent.Type
    SUBMIT: FormEvent.Type
    TYPE_FIELD_NUMBER: _ClassVar[int]
    type: FormEvent.Type
    def __init__(self, type: _Optional[_Union[FormEvent.Type, str]] = ...) -> None: ...
