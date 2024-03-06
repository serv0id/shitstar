from base import analytics_pb2 as _analytics_pb2
from base import actions_pb2 as _actions_pb2
from base import data_bind_mechanism_pb2 as _data_bind_mechanism_pb2
from feature.motion_system import dynamic_visual_asset_config_pb2 as _dynamic_visual_asset_config_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class WidgetCommons(_message.Message):
    __slots__ = ["id", "version", "instrumentation", "name", "actions", "data_bind_mechanism", "vda_configs"]
    ID_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    INSTRUMENTATION_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ACTIONS_FIELD_NUMBER: _ClassVar[int]
    DATA_BIND_MECHANISM_FIELD_NUMBER: _ClassVar[int]
    VDA_CONFIGS_FIELD_NUMBER: _ClassVar[int]
    id: str
    version: str
    instrumentation: _analytics_pb2.Instrumentation
    name: str
    actions: _actions_pb2.Actions
    data_bind_mechanism: _data_bind_mechanism_pb2.DataBindMechanism
    vda_configs: _containers.RepeatedCompositeFieldContainer[_dynamic_visual_asset_config_pb2.DynamicVisualAssetConfig]
    def __init__(self, id: _Optional[str] = ..., version: _Optional[str] = ..., instrumentation: _Optional[_Union[_analytics_pb2.Instrumentation, _Mapping]] = ..., name: _Optional[str] = ..., actions: _Optional[_Union[_actions_pb2.Actions, _Mapping]] = ..., data_bind_mechanism: _Optional[_Union[_data_bind_mechanism_pb2.DataBindMechanism, _Mapping]] = ..., vda_configs: _Optional[_Iterable[_Union[_dynamic_visual_asset_config_pb2.DynamicVisualAssetConfig, _Mapping]]] = ...) -> None: ...
