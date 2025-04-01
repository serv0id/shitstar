from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class InstalledApps(_message.Message):
    __slots__ = ("app_installs", "scan_timestamp", "scan_timestamp_ms", "app_details")
    class AppType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        APP_TYPE_UNSPECIFIED: _ClassVar[InstalledApps.AppType]
        APP_TYPE_SYSTEM_INSTALLED: _ClassVar[InstalledApps.AppType]
        APP_TYPE_USER_INSTALLED: _ClassVar[InstalledApps.AppType]
    APP_TYPE_UNSPECIFIED: InstalledApps.AppType
    APP_TYPE_SYSTEM_INSTALLED: InstalledApps.AppType
    APP_TYPE_USER_INSTALLED: InstalledApps.AppType
    class AppDetail(_message.Message):
        __slots__ = ("name", "package_name", "type")
        NAME_FIELD_NUMBER: _ClassVar[int]
        PACKAGE_NAME_FIELD_NUMBER: _ClassVar[int]
        TYPE_FIELD_NUMBER: _ClassVar[int]
        name: str
        package_name: str
        type: InstalledApps.AppType
        def __init__(self, name: _Optional[str] = ..., package_name: _Optional[str] = ..., type: _Optional[_Union[InstalledApps.AppType, str]] = ...) -> None: ...
    APP_INSTALLS_FIELD_NUMBER: _ClassVar[int]
    SCAN_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    SCAN_TIMESTAMP_MS_FIELD_NUMBER: _ClassVar[int]
    APP_DETAILS_FIELD_NUMBER: _ClassVar[int]
    app_installs: str
    scan_timestamp: str
    scan_timestamp_ms: int
    app_details: _containers.RepeatedCompositeFieldContainer[InstalledApps.AppDetail]
    def __init__(self, app_installs: _Optional[str] = ..., scan_timestamp: _Optional[str] = ..., scan_timestamp_ms: _Optional[int] = ..., app_details: _Optional[_Iterable[_Union[InstalledApps.AppDetail, _Mapping]]] = ...) -> None: ...
