from context import form_context_pb2 as _form_context_pb2
from feature.form import form_input_pb2 as _form_input_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FormInputResetAction(_message.Message):
    __slots__ = ["form_context", "form_input"]
    FORM_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    FORM_INPUT_FIELD_NUMBER: _ClassVar[int]
    form_context: _form_context_pb2.FormContext
    form_input: _form_input_pb2.FormInput
    def __init__(self, form_context: _Optional[_Union[_form_context_pb2.FormContext, _Mapping]] = ..., form_input: _Optional[_Union[_form_input_pb2.FormInput, _Mapping]] = ...) -> None: ...
