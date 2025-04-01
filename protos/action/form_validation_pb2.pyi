from context import form_context_pb2 as _form_context_pb2
from feature.form import form_input_pb2 as _form_input_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FormValidationAction(_message.Message):
    __slots__ = ("form_context", "form_inputs")
    FORM_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    FORM_INPUTS_FIELD_NUMBER: _ClassVar[int]
    form_context: _form_context_pb2.FormContext
    form_inputs: _containers.RepeatedCompositeFieldContainer[_form_input_pb2.FormInput]
    def __init__(self, form_context: _Optional[_Union[_form_context_pb2.FormContext, _Mapping]] = ..., form_inputs: _Optional[_Iterable[_Union[_form_input_pb2.FormInput, _Mapping]]] = ...) -> None: ...
