from component.identity import enum_pb2 as _enum_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PreRegProperties(_message.Message):
    __slots__ = ("page_title", "response", "mode", "source")
    PAGE_TITLE_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_FIELD_NUMBER: _ClassVar[int]
    MODE_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    page_title: str
    response: str
    mode: _enum_pb2.InputEnterMode
    source: _enum_pb2.PreReg
    def __init__(self, page_title: _Optional[str] = ..., response: _Optional[str] = ..., mode: _Optional[_Union[_enum_pb2.InputEnterMode, str]] = ..., source: _Optional[_Union[_enum_pb2.PreReg, str]] = ...) -> None: ...
