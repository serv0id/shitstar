from component.identity import enum_pb2 as _enum_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class UtilityProperties(_message.Message):
    __slots__ = ("source", "response")
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_FIELD_NUMBER: _ClassVar[int]
    source: _enum_pb2.PageSource
    response: _enum_pb2.ResponseMessage
    def __init__(self, source: _Optional[_Union[_enum_pb2.PageSource, str]] = ..., response: _Optional[_Union[_enum_pb2.ResponseMessage, str]] = ...) -> None: ...
