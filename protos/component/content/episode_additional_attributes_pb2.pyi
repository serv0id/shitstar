from component.content import show_additional_attributes_pb2 as _show_additional_attributes_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class EpisodeAdditionalAttributes(_message.Message):
    __slots__ = ("season_number", "season_name", "show_attributes")
    SEASON_NUMBER_FIELD_NUMBER: _ClassVar[int]
    SEASON_NAME_FIELD_NUMBER: _ClassVar[int]
    SHOW_ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    season_number: int
    season_name: str
    show_attributes: _show_additional_attributes_pb2.ShowAdditionalAttributes
    def __init__(self, season_number: _Optional[int] = ..., season_name: _Optional[str] = ..., show_attributes: _Optional[_Union[_show_additional_attributes_pb2.ShowAdditionalAttributes, _Mapping]] = ...) -> None: ...
