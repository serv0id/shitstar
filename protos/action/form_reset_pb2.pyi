from context import form_context_pb2 as _form_context_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FormResetAction(_message.Message):
    __slots__ = ["form_context"]
    FORM_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    form_context: _form_context_pb2.FormContext
    def __init__(self, form_context: _Optional[_Union[_form_context_pb2.FormContext, _Mapping]] = ...) -> None: ...
