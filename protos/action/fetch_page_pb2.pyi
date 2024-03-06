from google.protobuf import any_pb2 as _any_pb2
from context import form_context_pb2 as _form_context_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FetchPageAction(_message.Message):
    __slots__ = ["url", "action_type", "page_data"]
    class FetchActionType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
        DEFAULT: _ClassVar[FetchPageAction.FetchActionType]
        FORM_SUBMIT: _ClassVar[FetchPageAction.FetchActionType]
    DEFAULT: FetchPageAction.FetchActionType
    FORM_SUBMIT: FetchPageAction.FetchActionType
    class PageData(_message.Message):
        __slots__ = ["body", "form_input"]
        BODY_FIELD_NUMBER: _ClassVar[int]
        FORM_INPUT_FIELD_NUMBER: _ClassVar[int]
        body: _any_pb2.Any
        form_input: FetchPageAction.FormInput
        def __init__(self, body: _Optional[_Union[_any_pb2.Any, _Mapping]] = ..., form_input: _Optional[_Union[FetchPageAction.FormInput, _Mapping]] = ...) -> None: ...
    class FormInput(_message.Message):
        __slots__ = ["form_context"]
        FORM_CONTEXT_FIELD_NUMBER: _ClassVar[int]
        form_context: _form_context_pb2.FormContext
        def __init__(self, form_context: _Optional[_Union[_form_context_pb2.FormContext, _Mapping]] = ...) -> None: ...
    URL_FIELD_NUMBER: _ClassVar[int]
    ACTION_TYPE_FIELD_NUMBER: _ClassVar[int]
    PAGE_DATA_FIELD_NUMBER: _ClassVar[int]
    url: str
    action_type: FetchPageAction.FetchActionType
    page_data: FetchPageAction.PageData
    def __init__(self, url: _Optional[str] = ..., action_type: _Optional[_Union[FetchPageAction.FetchActionType, str]] = ..., page_data: _Optional[_Union[FetchPageAction.PageData, _Mapping]] = ...) -> None: ...
