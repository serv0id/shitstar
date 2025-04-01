from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PreloadModels(_message.Message):
    __slots__ = ()
    class BffApi(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        BFF_API_UNSPECIFIED: _ClassVar[PreloadModels.BffApi]
        BFF_API_PAGE_BFF: _ClassVar[PreloadModels.BffApi]
        BFF_API_WIDGET_BFF: _ClassVar[PreloadModels.BffApi]
    BFF_API_UNSPECIFIED: PreloadModels.BffApi
    BFF_API_PAGE_BFF: PreloadModels.BffApi
    BFF_API_WIDGET_BFF: PreloadModels.BffApi
    class DataSourceType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        DATA_SOURCE_TYPE_UNSPECIFIED: _ClassVar[PreloadModels.DataSourceType]
        DATA_SOURCE_TYPE_NETWORK: _ClassVar[PreloadModels.DataSourceType]
        DATA_SOURCE_TYPE_CACHE: _ClassVar[PreloadModels.DataSourceType]
    DATA_SOURCE_TYPE_UNSPECIFIED: PreloadModels.DataSourceType
    DATA_SOURCE_TYPE_NETWORK: PreloadModels.DataSourceType
    DATA_SOURCE_TYPE_CACHE: PreloadModels.DataSourceType
    class DataType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        DATA_TYPE_UNSPECIFIED: _ClassVar[PreloadModels.DataType]
        DATA_TYPE_ADS: _ClassVar[PreloadModels.DataType]
        DATA_TYPE_CONTENT: _ClassVar[PreloadModels.DataType]
        DATA_TYPE_NO_PRELOAD: _ClassVar[PreloadModels.DataType]
        DATA_TYPE_FALL_BACK_TO_CONTENT: _ClassVar[PreloadModels.DataType]
    DATA_TYPE_UNSPECIFIED: PreloadModels.DataType
    DATA_TYPE_ADS: PreloadModels.DataType
    DATA_TYPE_CONTENT: PreloadModels.DataType
    DATA_TYPE_NO_PRELOAD: PreloadModels.DataType
    DATA_TYPE_FALL_BACK_TO_CONTENT: PreloadModels.DataType
    class VideoSegmentApiDetail(_message.Message):
        __slots__ = ("api_url", "response_time_ms", "video_segment_api_source_type")
        API_URL_FIELD_NUMBER: _ClassVar[int]
        RESPONSE_TIME_MS_FIELD_NUMBER: _ClassVar[int]
        VIDEO_SEGMENT_API_SOURCE_TYPE_FIELD_NUMBER: _ClassVar[int]
        api_url: str
        response_time_ms: int
        video_segment_api_source_type: PreloadModels.DataSourceType
        def __init__(self, api_url: _Optional[str] = ..., response_time_ms: _Optional[int] = ..., video_segment_api_source_type: _Optional[_Union[PreloadModels.DataSourceType, str]] = ...) -> None: ...
    class DataSourceTypeDetail(_message.Message):
        __slots__ = ("network", "cache")
        NETWORK_FIELD_NUMBER: _ClassVar[int]
        CACHE_FIELD_NUMBER: _ClassVar[int]
        network: PreloadModels.DataSourceTypeDetailNetwork
        cache: PreloadModels.DataSourceTypeDetailCache
        def __init__(self, network: _Optional[_Union[PreloadModels.DataSourceTypeDetailNetwork, _Mapping]] = ..., cache: _Optional[_Union[PreloadModels.DataSourceTypeDetailCache, _Mapping]] = ...) -> None: ...
    class DataSourceTypeDetailNetwork(_message.Message):
        __slots__ = ("network",)
        NETWORK_FIELD_NUMBER: _ClassVar[int]
        network: bool
        def __init__(self, network: bool = ...) -> None: ...
    class DataSourceTypeDetailCache(_message.Message):
        __slots__ = ("cache_identifier",)
        CACHE_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
        cache_identifier: str
        def __init__(self, cache_identifier: _Optional[str] = ...) -> None: ...
    def __init__(self) -> None: ...

class PlaybackMetricsPreloadInfo(_message.Message):
    __slots__ = ("bff_preload_source_type", "player_data_source_type", "player_data_api_details", "preload_player_data_type")
    BFF_PRELOAD_SOURCE_TYPE_FIELD_NUMBER: _ClassVar[int]
    PLAYER_DATA_SOURCE_TYPE_FIELD_NUMBER: _ClassVar[int]
    PLAYER_DATA_API_DETAILS_FIELD_NUMBER: _ClassVar[int]
    PRELOAD_PLAYER_DATA_TYPE_FIELD_NUMBER: _ClassVar[int]
    bff_preload_source_type: PreloadModels.DataSourceType
    player_data_source_type: PreloadModels.DataSourceType
    player_data_api_details: _containers.RepeatedCompositeFieldContainer[PreloadModels.VideoSegmentApiDetail]
    preload_player_data_type: PreloadModels.DataType
    def __init__(self, bff_preload_source_type: _Optional[_Union[PreloadModels.DataSourceType, str]] = ..., player_data_source_type: _Optional[_Union[PreloadModels.DataSourceType, str]] = ..., player_data_api_details: _Optional[_Iterable[_Union[PreloadModels.VideoSegmentApiDetail, _Mapping]]] = ..., preload_player_data_type: _Optional[_Union[PreloadModels.DataType, str]] = ...) -> None: ...
