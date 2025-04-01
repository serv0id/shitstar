from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class FormContext(_message.Message):
    __slots__ = ("form_id",)
    FORM_ID_FIELD_NUMBER: _ClassVar[int]
    form_id: str
    def __init__(self, form_id: _Optional[str] = ...) -> None: ...
