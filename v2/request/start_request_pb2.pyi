from google.protobuf import any_pb2 as _any_pb2
from v2.ctx import context_pb2 as _context_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class StartRequest(_message.Message):
    __slots__ = ["deeplink_url", "body", "mode", "is_upgrade_shown", "context", "app_launch_count", "device_info", "client_capabilities"]
    class StartMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
        HARD: _ClassVar[StartRequest.StartMode]
        SOFT: _ClassVar[StartRequest.StartMode]
    HARD: StartRequest.StartMode
    SOFT: StartRequest.StartMode
    class DeviceInfo(_message.Message):
        __slots__ = ["device_ids", "device_meta"]
        class DeviceIdType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = []
            AD_ID: _ClassVar[StartRequest.DeviceInfo.DeviceIdType]
            ANDROID_ID: _ClassVar[StartRequest.DeviceInfo.DeviceIdType]
            UUID: _ClassVar[StartRequest.DeviceInfo.DeviceIdType]
            DEVICE_ID: _ClassVar[StartRequest.DeviceInfo.DeviceIdType]
        AD_ID: StartRequest.DeviceInfo.DeviceIdType
        ANDROID_ID: StartRequest.DeviceInfo.DeviceIdType
        UUID: StartRequest.DeviceInfo.DeviceIdType
        DEVICE_ID: StartRequest.DeviceInfo.DeviceIdType
        class DeviceId(_message.Message):
            __slots__ = ["id", "type"]
            ID_FIELD_NUMBER: _ClassVar[int]
            TYPE_FIELD_NUMBER: _ClassVar[int]
            id: str
            type: StartRequest.DeviceInfo.DeviceIdType
            def __init__(self, id: _Optional[str] = ..., type: _Optional[_Union[StartRequest.DeviceInfo.DeviceIdType, str]] = ...) -> None: ...
        class DeviceMeta(_message.Message):
            __slots__ = ["network_operator", "os_name", "os_version"]
            NETWORK_OPERATOR_FIELD_NUMBER: _ClassVar[int]
            OS_NAME_FIELD_NUMBER: _ClassVar[int]
            OS_VERSION_FIELD_NUMBER: _ClassVar[int]
            network_operator: str
            os_name: str
            os_version: str
            def __init__(self, network_operator: _Optional[str] = ..., os_name: _Optional[str] = ..., os_version: _Optional[str] = ...) -> None: ...
        DEVICE_IDS_FIELD_NUMBER: _ClassVar[int]
        DEVICE_META_FIELD_NUMBER: _ClassVar[int]
        device_ids: _containers.RepeatedCompositeFieldContainer[StartRequest.DeviceInfo.DeviceId]
        device_meta: StartRequest.DeviceInfo.DeviceMeta
        def __init__(self, device_ids: _Optional[_Iterable[_Union[StartRequest.DeviceInfo.DeviceId, _Mapping]]] = ..., device_meta: _Optional[_Union[StartRequest.DeviceInfo.DeviceMeta, _Mapping]] = ...) -> None: ...
    DEEPLINK_URL_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    MODE_FIELD_NUMBER: _ClassVar[int]
    IS_UPGRADE_SHOWN_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    APP_LAUNCH_COUNT_FIELD_NUMBER: _ClassVar[int]
    DEVICE_INFO_FIELD_NUMBER: _ClassVar[int]
    CLIENT_CAPABILITIES_FIELD_NUMBER: _ClassVar[int]
    deeplink_url: str
    body: _any_pb2.Any
    mode: StartRequest.StartMode
    is_upgrade_shown: bool
    context: _context_pb2.Context
    app_launch_count: int
    device_info: StartRequest.DeviceInfo
    client_capabilities: str
    def __init__(self, deeplink_url: _Optional[str] = ..., body: _Optional[_Union[_any_pb2.Any, _Mapping]] = ..., mode: _Optional[_Union[StartRequest.StartMode, str]] = ..., is_upgrade_shown: bool = ..., context: _Optional[_Union[_context_pb2.Context, _Mapping]] = ..., app_launch_count: _Optional[int] = ..., device_info: _Optional[_Union[StartRequest.DeviceInfo, _Mapping]] = ..., client_capabilities: _Optional[str] = ...) -> None: ...
