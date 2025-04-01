from composable.base import reference_pb2 as _reference_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ComposableCommons(_message.Message):
    __slots__ = ("bffId", "styleId")
    BFFID_FIELD_NUMBER: _ClassVar[int]
    STYLEID_FIELD_NUMBER: _ClassVar[int]
    bffId: _reference_pb2.Reference
    styleId: _reference_pb2.Reference
    def __init__(self, bffId: _Optional[_Union[_reference_pb2.Reference, _Mapping]] = ..., styleId: _Optional[_Union[_reference_pb2.Reference, _Mapping]] = ...) -> None: ...

class ComponentCommons(_message.Message):
    __slots__ = ("bffId", "parentStyleId")
    BFFID_FIELD_NUMBER: _ClassVar[int]
    PARENTSTYLEID_FIELD_NUMBER: _ClassVar[int]
    bffId: _reference_pb2.Reference
    parentStyleId: _reference_pb2.Reference
    def __init__(self, bffId: _Optional[_Union[_reference_pb2.Reference, _Mapping]] = ..., parentStyleId: _Optional[_Union[_reference_pb2.Reference, _Mapping]] = ...) -> None: ...
