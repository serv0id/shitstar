from feature.image import illustration_pb2 as _illustration_pb2
from feature.quiz import title_pb2 as _title_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TitleIconCombo(_message.Message):
    __slots__ = ("title", "illustration")
    TITLE_FIELD_NUMBER: _ClassVar[int]
    ILLUSTRATION_FIELD_NUMBER: _ClassVar[int]
    title: _title_pb2.Title
    illustration: _illustration_pb2.Illustration
    def __init__(self, title: _Optional[_Union[_title_pb2.Title, _Mapping]] = ..., illustration: _Optional[_Union[_illustration_pb2.Illustration, _Mapping]] = ...) -> None: ...
