from base import analytics_pb2 as _analytics_pb2
from base import actions_pb2 as _actions_pb2
from base import data_bind_mechanism_pb2 as _data_bind_mechanism_pb2
from feature.motion_system import dynamic_visual_asset_config_pb2 as _dynamic_visual_asset_config_pb2
from feature.refresh import refresh_info_pb2 as _refresh_info_pb2
from feature.enhancements import collection_transformer_pb2 as _collection_transformer_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class WidgetCommons(_message.Message):
    __slots__ = ("id", "version", "instrumentation", "name", "actions", "data_bind_mechanism", "vda_configs", "cache_config", "unique_identifier", "refresh_info", "collection_transformer")
    ID_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    INSTRUMENTATION_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ACTIONS_FIELD_NUMBER: _ClassVar[int]
    DATA_BIND_MECHANISM_FIELD_NUMBER: _ClassVar[int]
    VDA_CONFIGS_FIELD_NUMBER: _ClassVar[int]
    CACHE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    UNIQUE_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    REFRESH_INFO_FIELD_NUMBER: _ClassVar[int]
    COLLECTION_TRANSFORMER_FIELD_NUMBER: _ClassVar[int]
    id: str
    version: str
    instrumentation: _analytics_pb2.Instrumentation
    name: str
    actions: _actions_pb2.Actions
    data_bind_mechanism: _data_bind_mechanism_pb2.DataBindMechanism
    vda_configs: _containers.RepeatedCompositeFieldContainer[_dynamic_visual_asset_config_pb2.DynamicVisualAssetConfig]
    cache_config: CacheConfig
    unique_identifier: int
    refresh_info: _refresh_info_pb2.RefreshInfo
    collection_transformer: _collection_transformer_pb2.CollectionTransformer
    def __init__(self, id: _Optional[str] = ..., version: _Optional[str] = ..., instrumentation: _Optional[_Union[_analytics_pb2.Instrumentation, _Mapping]] = ..., name: _Optional[str] = ..., actions: _Optional[_Union[_actions_pb2.Actions, _Mapping]] = ..., data_bind_mechanism: _Optional[_Union[_data_bind_mechanism_pb2.DataBindMechanism, _Mapping]] = ..., vda_configs: _Optional[_Iterable[_Union[_dynamic_visual_asset_config_pb2.DynamicVisualAssetConfig, _Mapping]]] = ..., cache_config: _Optional[_Union[CacheConfig, _Mapping]] = ..., unique_identifier: _Optional[int] = ..., refresh_info: _Optional[_Union[_refresh_info_pb2.RefreshInfo, _Mapping]] = ..., collection_transformer: _Optional[_Union[_collection_transformer_pb2.CollectionTransformer, _Mapping]] = ...) -> None: ...

class CacheConfig(_message.Message):
    __slots__ = ("isShortCircuitEligible", "is_cacheable")
    ISSHORTCIRCUITELIGIBLE_FIELD_NUMBER: _ClassVar[int]
    IS_CACHEABLE_FIELD_NUMBER: _ClassVar[int]
    isShortCircuitEligible: bool
    is_cacheable: bool
    def __init__(self, isShortCircuitEligible: bool = ..., is_cacheable: bool = ...) -> None: ...
