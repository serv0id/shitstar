from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PreloadConfig(_message.Message):
    __slots__ = ("trigger_position_ms", "preload_items", "milisecs_remaining", "wifi_only", "expiration_duration_ms")
    class ConfigItem(_message.Message):
        __slots__ = ("multiplayer_preload_enabled", "manifest_preload_enabled", "proxy_server_enabled", "api_params", "multiplayer_params", "manifest_params", "proxy_server_config")
        MULTIPLAYER_PRELOAD_ENABLED_FIELD_NUMBER: _ClassVar[int]
        MANIFEST_PRELOAD_ENABLED_FIELD_NUMBER: _ClassVar[int]
        PROXY_SERVER_ENABLED_FIELD_NUMBER: _ClassVar[int]
        API_PARAMS_FIELD_NUMBER: _ClassVar[int]
        MULTIPLAYER_PARAMS_FIELD_NUMBER: _ClassVar[int]
        MANIFEST_PARAMS_FIELD_NUMBER: _ClassVar[int]
        PROXY_SERVER_CONFIG_FIELD_NUMBER: _ClassVar[int]
        multiplayer_preload_enabled: bool
        manifest_preload_enabled: bool
        proxy_server_enabled: bool
        api_params: PreloadApiParams
        multiplayer_params: PreloadMultiPlayerParams
        manifest_params: PreloadManifestParams
        proxy_server_config: ProxyServerConfig
        def __init__(self, multiplayer_preload_enabled: bool = ..., manifest_preload_enabled: bool = ..., proxy_server_enabled: bool = ..., api_params: _Optional[_Union[PreloadApiParams, _Mapping]] = ..., multiplayer_params: _Optional[_Union[PreloadMultiPlayerParams, _Mapping]] = ..., manifest_params: _Optional[_Union[PreloadManifestParams, _Mapping]] = ..., proxy_server_config: _Optional[_Union[ProxyServerConfig, _Mapping]] = ...) -> None: ...
    TRIGGER_POSITION_MS_FIELD_NUMBER: _ClassVar[int]
    PRELOAD_ITEMS_FIELD_NUMBER: _ClassVar[int]
    MILISECS_REMAINING_FIELD_NUMBER: _ClassVar[int]
    WIFI_ONLY_FIELD_NUMBER: _ClassVar[int]
    EXPIRATION_DURATION_MS_FIELD_NUMBER: _ClassVar[int]
    trigger_position_ms: int
    preload_items: _containers.RepeatedCompositeFieldContainer[PreloadConfig.ConfigItem]
    milisecs_remaining: int
    wifi_only: bool
    expiration_duration_ms: int
    def __init__(self, trigger_position_ms: _Optional[int] = ..., preload_items: _Optional[_Iterable[_Union[PreloadConfig.ConfigItem, _Mapping]]] = ..., milisecs_remaining: _Optional[int] = ..., wifi_only: bool = ..., expiration_duration_ms: _Optional[int] = ...) -> None: ...

class PreloadApiParams(_message.Message):
    __slots__ = ("endpoint", "type")
    class ApiType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        page_bff: _ClassVar[PreloadApiParams.ApiType]
        PC: _ClassVar[PreloadApiParams.ApiType]
    page_bff: PreloadApiParams.ApiType
    PC: PreloadApiParams.ApiType
    ENDPOINT_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    endpoint: str
    type: PreloadApiParams.ApiType
    def __init__(self, endpoint: _Optional[str] = ..., type: _Optional[_Union[PreloadApiParams.ApiType, str]] = ...) -> None: ...

class PreloadMultiPlayerParams(_message.Message):
    __slots__ = ("preload_duration_ms",)
    PRELOAD_DURATION_MS_FIELD_NUMBER: _ClassVar[int]
    preload_duration_ms: int
    def __init__(self, preload_duration_ms: _Optional[int] = ...) -> None: ...

class PreloadManifestParams(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ProxyServerConfig(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...
