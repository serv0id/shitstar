from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class DownloadInitRequest(_message.Message):
    __slots__ = ("content_id", "content_provider", "is_premium", "studio_id", "studio_name", "title_name", "client_capabilities", "drm_parameter", "advertising_id", "client_request_id", "user_lat", "device_brand", "device_model", "device_carrier", "device_os_version", "device_network_data", "device_platform", "device_app_version", "content_language", "custom_tags", "download_ids", "preferred_audio_languages", "content_type")
    CONTENT_ID_FIELD_NUMBER: _ClassVar[int]
    CONTENT_PROVIDER_FIELD_NUMBER: _ClassVar[int]
    IS_PREMIUM_FIELD_NUMBER: _ClassVar[int]
    STUDIO_ID_FIELD_NUMBER: _ClassVar[int]
    STUDIO_NAME_FIELD_NUMBER: _ClassVar[int]
    TITLE_NAME_FIELD_NUMBER: _ClassVar[int]
    CLIENT_CAPABILITIES_FIELD_NUMBER: _ClassVar[int]
    DRM_PARAMETER_FIELD_NUMBER: _ClassVar[int]
    ADVERTISING_ID_FIELD_NUMBER: _ClassVar[int]
    CLIENT_REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    USER_LAT_FIELD_NUMBER: _ClassVar[int]
    DEVICE_BRAND_FIELD_NUMBER: _ClassVar[int]
    DEVICE_MODEL_FIELD_NUMBER: _ClassVar[int]
    DEVICE_CARRIER_FIELD_NUMBER: _ClassVar[int]
    DEVICE_OS_VERSION_FIELD_NUMBER: _ClassVar[int]
    DEVICE_NETWORK_DATA_FIELD_NUMBER: _ClassVar[int]
    DEVICE_PLATFORM_FIELD_NUMBER: _ClassVar[int]
    DEVICE_APP_VERSION_FIELD_NUMBER: _ClassVar[int]
    CONTENT_LANGUAGE_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_TAGS_FIELD_NUMBER: _ClassVar[int]
    DOWNLOAD_IDS_FIELD_NUMBER: _ClassVar[int]
    PREFERRED_AUDIO_LANGUAGES_FIELD_NUMBER: _ClassVar[int]
    CONTENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    content_id: str
    content_provider: str
    is_premium: bool
    studio_id: str
    studio_name: str
    title_name: str
    client_capabilities: str
    drm_parameter: str
    advertising_id: str
    client_request_id: str
    user_lat: str
    device_brand: str
    device_model: str
    device_carrier: str
    device_os_version: str
    device_network_data: str
    device_platform: str
    device_app_version: str
    content_language: str
    custom_tags: str
    download_ids: _containers.RepeatedScalarFieldContainer[str]
    preferred_audio_languages: _containers.RepeatedScalarFieldContainer[str]
    content_type: str
    def __init__(self, content_id: _Optional[str] = ..., content_provider: _Optional[str] = ..., is_premium: bool = ..., studio_id: _Optional[str] = ..., studio_name: _Optional[str] = ..., title_name: _Optional[str] = ..., client_capabilities: _Optional[str] = ..., drm_parameter: _Optional[str] = ..., advertising_id: _Optional[str] = ..., client_request_id: _Optional[str] = ..., user_lat: _Optional[str] = ..., device_brand: _Optional[str] = ..., device_model: _Optional[str] = ..., device_carrier: _Optional[str] = ..., device_os_version: _Optional[str] = ..., device_network_data: _Optional[str] = ..., device_platform: _Optional[str] = ..., device_app_version: _Optional[str] = ..., content_language: _Optional[str] = ..., custom_tags: _Optional[str] = ..., download_ids: _Optional[_Iterable[str]] = ..., preferred_audio_languages: _Optional[_Iterable[str]] = ..., content_type: _Optional[str] = ...) -> None: ...
