from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Metadata(_message.Message):
    __slots__ = ("device_info", "network_info", "product_info", "user_info", "playback_info", "error_info", "cw_db_dump", "wl_db_dump")
    class ErrorInfoEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    DEVICE_INFO_FIELD_NUMBER: _ClassVar[int]
    NETWORK_INFO_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_INFO_FIELD_NUMBER: _ClassVar[int]
    USER_INFO_FIELD_NUMBER: _ClassVar[int]
    PLAYBACK_INFO_FIELD_NUMBER: _ClassVar[int]
    ERROR_INFO_FIELD_NUMBER: _ClassVar[int]
    CW_DB_DUMP_FIELD_NUMBER: _ClassVar[int]
    WL_DB_DUMP_FIELD_NUMBER: _ClassVar[int]
    device_info: DeviceInfo
    network_info: NetworkInfo
    product_info: ProductInfo
    user_info: UserInfo
    playback_info: PlaybackInfo
    error_info: _containers.ScalarMap[str, str]
    cw_db_dump: CWLocalDbDump
    wl_db_dump: WLLocalDbDump
    def __init__(self, device_info: _Optional[_Union[DeviceInfo, _Mapping]] = ..., network_info: _Optional[_Union[NetworkInfo, _Mapping]] = ..., product_info: _Optional[_Union[ProductInfo, _Mapping]] = ..., user_info: _Optional[_Union[UserInfo, _Mapping]] = ..., playback_info: _Optional[_Union[PlaybackInfo, _Mapping]] = ..., error_info: _Optional[_Mapping[str, str]] = ..., cw_db_dump: _Optional[_Union[CWLocalDbDump, _Mapping]] = ..., wl_db_dump: _Optional[_Union[WLLocalDbDump, _Mapping]] = ...) -> None: ...

class DeviceInfo(_message.Message):
    __slots__ = ("id", "platform", "device", "display", "manufacturer", "model", "board", "brand", "os_version", "os_sdk", "fingerprint", "security_path")
    ID_FIELD_NUMBER: _ClassVar[int]
    PLATFORM_FIELD_NUMBER: _ClassVar[int]
    DEVICE_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_FIELD_NUMBER: _ClassVar[int]
    MANUFACTURER_FIELD_NUMBER: _ClassVar[int]
    MODEL_FIELD_NUMBER: _ClassVar[int]
    BOARD_FIELD_NUMBER: _ClassVar[int]
    BRAND_FIELD_NUMBER: _ClassVar[int]
    OS_VERSION_FIELD_NUMBER: _ClassVar[int]
    OS_SDK_FIELD_NUMBER: _ClassVar[int]
    FINGERPRINT_FIELD_NUMBER: _ClassVar[int]
    SECURITY_PATH_FIELD_NUMBER: _ClassVar[int]
    id: str
    platform: str
    device: str
    display: str
    manufacturer: str
    model: str
    board: str
    brand: str
    os_version: str
    os_sdk: int
    fingerprint: str
    security_path: str
    def __init__(self, id: _Optional[str] = ..., platform: _Optional[str] = ..., device: _Optional[str] = ..., display: _Optional[str] = ..., manufacturer: _Optional[str] = ..., model: _Optional[str] = ..., board: _Optional[str] = ..., brand: _Optional[str] = ..., os_version: _Optional[str] = ..., os_sdk: _Optional[int] = ..., fingerprint: _Optional[str] = ..., security_path: _Optional[str] = ...) -> None: ...

class NetworkInfo(_message.Message):
    __slots__ = ("mcc", "type")
    MCC_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    mcc: str
    type: str
    def __init__(self, mcc: _Optional[str] = ..., type: _Optional[str] = ...) -> None: ...

class ProductInfo(_message.Message):
    __slots__ = ("build_type", "flavor", "locale", "version_name", "version_code", "installed_by")
    BUILD_TYPE_FIELD_NUMBER: _ClassVar[int]
    FLAVOR_FIELD_NUMBER: _ClassVar[int]
    LOCALE_FIELD_NUMBER: _ClassVar[int]
    VERSION_NAME_FIELD_NUMBER: _ClassVar[int]
    VERSION_CODE_FIELD_NUMBER: _ClassVar[int]
    INSTALLED_BY_FIELD_NUMBER: _ClassVar[int]
    build_type: str
    flavor: str
    locale: str
    version_name: str
    version_code: int
    installed_by: str
    def __init__(self, build_type: _Optional[str] = ..., flavor: _Optional[str] = ..., locale: _Optional[str] = ..., version_name: _Optional[str] = ..., version_code: _Optional[int] = ..., installed_by: _Optional[str] = ...) -> None: ...

class UserInfo(_message.Message):
    __slots__ = ("pid", "name", "phone", "email")
    PID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PHONE_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    pid: str
    name: str
    phone: str
    email: str
    def __init__(self, pid: _Optional[str] = ..., name: _Optional[str] = ..., phone: _Optional[str] = ..., email: _Optional[str] = ...) -> None: ...

class PlaybackInfo(_message.Message):
    __slots__ = ("content_id", "current_position", "selected_subtitle", "selected_language", "stats_for_nerds")
    CONTENT_ID_FIELD_NUMBER: _ClassVar[int]
    CURRENT_POSITION_FIELD_NUMBER: _ClassVar[int]
    SELECTED_SUBTITLE_FIELD_NUMBER: _ClassVar[int]
    SELECTED_LANGUAGE_FIELD_NUMBER: _ClassVar[int]
    STATS_FOR_NERDS_FIELD_NUMBER: _ClassVar[int]
    content_id: str
    current_position: str
    selected_subtitle: str
    selected_language: str
    stats_for_nerds: str
    def __init__(self, content_id: _Optional[str] = ..., current_position: _Optional[str] = ..., selected_subtitle: _Optional[str] = ..., selected_language: _Optional[str] = ..., stats_for_nerds: _Optional[str] = ...) -> None: ...

class CWLocalDbDump(_message.Message):
    __slots__ = ("content_id", "tag", "watch_ratio", "updated_at")
    CONTENT_ID_FIELD_NUMBER: _ClassVar[int]
    TAG_FIELD_NUMBER: _ClassVar[int]
    WATCH_RATIO_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    content_id: str
    tag: str
    watch_ratio: str
    updated_at: str
    def __init__(self, content_id: _Optional[str] = ..., tag: _Optional[str] = ..., watch_ratio: _Optional[str] = ..., updated_at: _Optional[str] = ...) -> None: ...

class WLLocalDbDump(_message.Message):
    __slots__ = ("content_id", "is_removed")
    CONTENT_ID_FIELD_NUMBER: _ClassVar[int]
    IS_REMOVED_FIELD_NUMBER: _ClassVar[int]
    content_id: str
    is_removed: bool
    def __init__(self, content_id: _Optional[str] = ..., is_removed: bool = ...) -> None: ...
