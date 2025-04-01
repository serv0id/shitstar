from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class DownloadInfo(_message.Message):
    __slots__ = ("content_id", "widget_url", "content_provider", "is_premium", "studio_id", "studio_name", "title_name", "is_download_available", "user_language_preference_id", "content_type")
    CONTENT_ID_FIELD_NUMBER: _ClassVar[int]
    WIDGET_URL_FIELD_NUMBER: _ClassVar[int]
    CONTENT_PROVIDER_FIELD_NUMBER: _ClassVar[int]
    IS_PREMIUM_FIELD_NUMBER: _ClassVar[int]
    STUDIO_ID_FIELD_NUMBER: _ClassVar[int]
    STUDIO_NAME_FIELD_NUMBER: _ClassVar[int]
    TITLE_NAME_FIELD_NUMBER: _ClassVar[int]
    IS_DOWNLOAD_AVAILABLE_FIELD_NUMBER: _ClassVar[int]
    USER_LANGUAGE_PREFERENCE_ID_FIELD_NUMBER: _ClassVar[int]
    CONTENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    content_id: str
    widget_url: str
    content_provider: str
    is_premium: bool
    studio_id: str
    studio_name: str
    title_name: str
    is_download_available: bool
    user_language_preference_id: str
    content_type: str
    def __init__(self, content_id: _Optional[str] = ..., widget_url: _Optional[str] = ..., content_provider: _Optional[str] = ..., is_premium: bool = ..., studio_id: _Optional[str] = ..., studio_name: _Optional[str] = ..., title_name: _Optional[str] = ..., is_download_available: bool = ..., user_language_preference_id: _Optional[str] = ..., content_type: _Optional[str] = ...) -> None: ...
