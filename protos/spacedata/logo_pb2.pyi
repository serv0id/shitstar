from base import space_data_commons_pb2 as _space_data_commons_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class LogoSpaceData(_message.Message):
    __slots__ = ("space_data_commons",)
    SPACE_DATA_COMMONS_FIELD_NUMBER: _ClassVar[int]
    space_data_commons: _space_data_commons_pb2.SpaceDataCommons
    def __init__(self, space_data_commons: _Optional[_Union[_space_data_commons_pb2.SpaceDataCommons, _Mapping]] = ...) -> None: ...
