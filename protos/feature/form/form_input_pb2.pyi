from feature.form import form_data_pb2 as _form_data_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FormInput(_message.Message):
    __slots__ = ("form_input_id", "form_data")
    FORM_INPUT_ID_FIELD_NUMBER: _ClassVar[int]
    FORM_DATA_FIELD_NUMBER: _ClassVar[int]
    form_input_id: str
    form_data: _form_data_pb2.FormData
    def __init__(self, form_input_id: _Optional[str] = ..., form_data: _Optional[_Union[_form_data_pb2.FormData, _Mapping]] = ...) -> None: ...
