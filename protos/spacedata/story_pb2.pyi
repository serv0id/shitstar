from base import space_data_commons_pb2 as _space_data_commons_pb2
from feature.header import story_header_pb2 as _story_header_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class StorySpaceData(_message.Message):
    __slots__ = ("space_data_commons", "header_type", "stories_config")
    class HeaderType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[StorySpaceData.HeaderType]
        SLIDER: _ClassVar[StorySpaceData.HeaderType]
    UNSPECIFIED: StorySpaceData.HeaderType
    SLIDER: StorySpaceData.HeaderType
    SPACE_DATA_COMMONS_FIELD_NUMBER: _ClassVar[int]
    HEADER_TYPE_FIELD_NUMBER: _ClassVar[int]
    STORIES_CONFIG_FIELD_NUMBER: _ClassVar[int]
    space_data_commons: _space_data_commons_pb2.SpaceDataCommons
    header_type: StorySpaceData.HeaderType
    stories_config: _story_header_pb2.StoryHeaderConfig
    def __init__(self, space_data_commons: _Optional[_Union[_space_data_commons_pb2.SpaceDataCommons, _Mapping]] = ..., header_type: _Optional[_Union[StorySpaceData.HeaderType, str]] = ..., stories_config: _Optional[_Union[_story_header_pb2.StoryHeaderConfig, _Mapping]] = ...) -> None: ...
